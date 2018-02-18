# DO NOT ADD tailing slash for location of files
# The first column of the csv file is the nam eof the file

import sys, os, multiprocessing, csv, urllib.request
from os.path import basename

#Reads the csv for the item number and creates the link supporting the web location
def readgetURLs(filename):
    urls = []
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            prefix = 'xxx'
            urls.append(prefix+row[0]+'.jpg')
    return urls

#Downloads the image
def download_image(url):
    print(location+'/'+basename(url))
    try:
        urllib.request.urlretrieve(url, location+'/'+basename(url))
    except:
        pass

# Main function to start everything
def loader():
    if len(sys.argv) != 3:
        print('Syntax: {} <inv_file.csv> <output_dir/>'.format(sys.argv[0]))
        sys.exit(0)
    (inv_file, out_dir) = sys.argv[1:]

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    global location
    location = out_dir

    url_list = readgetURLs(inv_file)
    pool = multiprocessing.Pool(processes=4)  # Num of CPUs
    print('Beginning file download...')
    pool.map(download_image, url_list)
    pool.close()
    pool.terminate()
    print('Reguested Files Downloaded...')


# arg1 : inv_file.csv
# arg2 : output_dir
if __name__ == '__main__':
    loader()
