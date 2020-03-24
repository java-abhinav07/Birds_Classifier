# Birds_Classifier

Dataset
----------
Data set of 150 bird species. 19744 training images, 750 test images(5 per species) and 750 validation images(5 per species.All images are 224 X 224 X 3 color images in jpg format. Also includes a "consolidated" image set that combines the training, test and validation images into a single data set.
source: https://www.kaggle.com/gpiosenka/100-bird-species

Model Architecture
-------------------
Inspired by GoogLeNet/Inception v1, has a total of 10 million trainable parameters and was trained for only 30 epochs. Refer the uploaded jupyter notebook for details about the modle architectue.

Model file
-----------
Model has been converted json format for ease of use, File name: "model.json"

Trained Weights
-----------------
Training achieved an accuracy of 82 percent on the validation set. File name: "model_weights_v3.h5"
