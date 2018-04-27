# Image-recognition

## Notes

Part of the training set containing images which have label named "Neglyubka" has been artificially enlarged 
by making copy of blurry and rotated orginal images. I did this because orginal set was too small to just use it to training.

## Preprocessing

I create script named "preprocess.py" to extend images with type named "product" from the data set.
This script also convert images to jpg format, resize them and divide them into subfolders which has the same name as labels.

Extra librraries required to run this script: pandas and opencv.

*Execution:*
python preprocess.py dataSetLocation inputImagesDirectory outputImagesDirectory --size=imageSize

--size is optional (default 224)

---

I blurred and rotaded left images using my scritp blur.py which take as argument folder with images and create in the same folder blurred and rotated copy of all images from thast folder.

Extra librraries required to run this script: opencv

*Execution:*
python blur.py inputImagesDirectory

## Running

1.  git clone https://github.com/mlynarzsrem/Image-recognition.git

2. cd Image-recognition

3. Use preprocess.py to extract all necessary images to proper folder in tf_files (instruction above)

4.  If you want you can use blur.py to enlarge your training set (instruction above)

5. To train the classifier use command below:

    python -m scripts.retrain \\ <br />
      --bottleneck_dir=tf_files/bottlenecks \\ <br />
      --how_many_training_steps=4000 \\ <br />
      --model_dir=tf_files/models/ \\ <br />
      --summaries_dir=tf_files/training_summaries/"mobilenet_0.75_128" \\<br />
      --output_graph=tf_files/retrained_graph.pb \\<br />
      --output_labels=tf_files/retrained_labels.txt \\<br />
      --architecture="mobilenet_0.75_128" \\<br />
      --image_dir=tf_files/photos


     Set the appropriate value of "how_many_training_steps". I choosed 4000 because it gave quite good results and it did not last too long.
    Insert path with your training set to --image_dir.

    Architecture name "mobilenet_0.75_128" containts two important parameters. First one, relative size of model can accept values "1.0, 0.75, 0.50, or 0.25". In this case I've been choosen 0.75. Second one, image size can accept values "128,160,192, or 224px". In this case I've been choosen 128 px, becuse it is size of photos after resizing.

6. To run classifier use command below:

    python -m scripts.label_image --graph=tf_files/retrained_graph.pb \\ <br />
    --input_height=128 \\ <br />
    --input_width=128 \\ <br />
    --image=tf_files/photos/Iznik/03_05_2_001.jpg

    Insert into --image location of image which you want to classify.

    Set image height and width into proper variables.

## Accuracy

After enlarging all data set by copy of rotated and blurry images I achieved 87 % accuracy.      