import os
import pandas as pd
from os.path import isfile,join,exists
import cv2
import argparse

##Declare arguments 
parser = argparse.ArgumentParser()
parser.add_argument("dataset", help="Location of dataset")
parser.add_argument("inputdir", help="Directory with input images")
parser.add_argument("outputdir", help="Directory with output images")
parser.add_argument("-s", "--size",type=int,help="Size of input images. ")

##Get arguments from command line
args = parser.parse_args()
dataSetPath =args.dataset
inputDir = args.inputdir
outputDir = args.outputdir
if args.size:
    size =args.size
else:
    size =224
##Validate inputs
if(isfile(dataSetPath)==False):
    raise "Wrong dataset location"
if not exists(inputDir):
    raise "Input directory not exists"
if not exists(outputDir):
    os.makedirs(outputDir)

##Get data from data set
data = pd.read_csv(dataSetPath)
productData = data[data['type']=="product"]
filtered_data = productData.filter(["decor_label","decor","file"]).values
x =filtered_data.shape[0]

##Make preprocessing
for i in range(x):
    decor= filtered_data[i,1]
    if not os.path.exists(join(outputDir,str(decor))):
        os.makedirs(join(outputDir,str(decor)))
    name = filtered_data[i,2][:-4]
    im = cv2.imread(join(inputDir,str(filtered_data[i,2])),1)
    im =cv2.resize(im,(size,size))
    finalDir = join(outputDir,str(decor))
    finalFile = join(finalDir,  str(name) + ".jpg")
    cv2.imwrite(finalFile,im)
