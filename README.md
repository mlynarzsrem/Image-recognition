# Image-recognition

## Notes

Part of the training set containing images which have label named "Neglyubka" has been artificially enlarged 
by making copy of rotated and blured orginal images. I did this because orginal set was too small to just use it to training.

## Preprocessing

I create script named "preprocess.py" to extend images with type named "product" from the data set.
This script also convert images to jpg format, resize them and divide them into subfolders which has the same name as labels.

Extra librraries required to run this script: pandas and Pillow.

Execution:

python preprocess.py dataSetLocation inputImagesDirectory outputImagesDirectory

