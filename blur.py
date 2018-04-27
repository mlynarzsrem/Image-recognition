from os import listdir
import cv2
from os.path import isfile,join,exists
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("inputdir", help="Directory containing images")
args = parser.parse_args()
inputDir =args.inputdir
if not exists(inputDir):
    raise "Wrong directory"

for f in listdir(inputDir):
    if(isfile(join(inputDir,f))==True):
        finalPath=join(inputDir,f)
        img = cv2.imread(finalPath,1)
        (h, w) = img.shape[:2]
        center = (w / 2, h / 2)
        blur = cv2.GaussianBlur(img,(5,5),0)
        M = cv2.getRotationMatrix2D(center, 90, 1)
        rotated =  cv2.warpAffine(blur, M, (h, w))
        cv2.imwrite(join(inputDir,"edited"+f),rotated)
               
        