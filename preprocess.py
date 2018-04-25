import pandas as pd
import os
from PIL import Image
import argparse
import sys
if(len(sys.argv)!=4):
    raise "Wrong params number"
else:
    dataSetPath =sys.argv[1]
    inputDir = sys.argv[2]
    outputDir = sys.argv[3]
if not os.path.exists(outputDir):
    os.makedirs(outputDir)
data = pd.read_csv(dataSetPath)
productData = data[data['type']=="product"]
filtered_data = productData.filter(["decor_label","decor","file"]).values
x =filtered_data.shape[0]
for i in range(x):
    decor= filtered_data[i,1]
    if not os.path.exists(outputDir+"/"+str(decor)):
        os.makedirs(outputDir+"/"+str(decor))
    name = filtered_data[i,2][:-4]
    im = Image.open(inputDir+"/"+str(filtered_data[i,2]))
    im =im.resize((224,224))
    rgb_im = im.convert('RGB')
    finalFile = outputDir+"/"+ str(decor) + "/" + str(name) + ".jpg"
    rgb_im.save(finalFile)
