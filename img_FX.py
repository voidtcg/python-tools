import numpy as np
import cv2, os, sys, multiprocessing , time


def image_fix(img):
    image = cv2.imread(img)
    # resize images
    image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
    #template = cv2.resize(template, (0,0), fx=0.5, fy=0.5)

    # Convert to grayscale
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Find template
    result = cv2.matchTemplate(imageGray,templateGray, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    h,w = templateGray.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image,top_left, bottom_right,(255,255,255),-2)

    cv2.imwrite(img,image)

    ##Show result for spot checking
    # cv2.imshow("Result", image)
    # cv2.moveWindow("Result", 150, 50);
    # cv2.waitKey(0)

def loader():
    if len(sys.argv) != 3:
        print('Syntax: {} <template_file.jpg> <input_dir/>'.format(sys.argv[0]))
        sys.exit(0)
    (template_file, input_dir) = sys.argv[1:]

    global template
    template = cv2.imread(template_file)
    template = cv2.resize(template, (0,0), fx=0.5, fy=0.5)
    print('Beginning picture cleaning... prayers please!!!')
    print('RUN THIS ONCE OR YOU WILL HAVE TO REDOWNLOAD ALL THE PICTURES AGAIN')
    os.chdir(input_dir)
    for file in os.listdir('.'):
        #print(file)
        image_fix(file)
    print('Hopefully our prayers have been answered, if not ... well :D')
if __name__ == '__main__':
    loader()
