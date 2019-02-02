## Dependencies
- Python 3.6.5
- conda 4.5.4
- pip 9.0.1
- Tensorflow v.1.8.0
- Numpy v.1.14.3
- Pandas v.0.23.3
- OpenCV v.3.4.1
- Sci-kit Learn v.0.19.1
- Matplotlib v.2.2.2
- libopencv v.3.4.1
- h5py

## Directory
- Dataset: Contain training set and validation set for training ktp classification model, contain positive sample and negative sample to train cascade feature
- Data: Contain all stages obtained by training cascade feature and trained ktp cascade feature
- Haar Features: Contain all trained haar like feature cascade to classify face and ktp
- Info: Contain all samples to train ktp cascade feature
- Test Images: Contain images to define ktp position and make border to ktp

## Text
- bg.txt: All path to negatives sample
- positives.txt: All path to positives sample
- traincascade_command.txt: All command needed to create sample and train cascade

## Other
- KoinWorks.ipynb: Script to all sample test
- positives.vec: A vector of positives sample use for train cascade feature

Answer for 1st number:
The answer for number one use 3 different algorithm, neural network, convolutional neural network, and support vector machine. Each model was trained using 31 ktp image and 31 other image.

Answer for 2nd number:
The answer for number two use Haar Like Cascade Feature by Viola Jones (Cascade Classifier) due to small amount of collected data so it's hard to train using R-CNN, YOLO, SSD with minimum amount of data. ktpcascade feature is trained using opencv_trainedcascade. To define the position of KTP wheter it's on top, bottom, right or left, a face detection is needed and measure the distance between KTP region of interest and face region of interest. 

## Instruction 

### 1. Clone the project
```bash
$ git clone 
```
### 2. Dependecies
- Install all dependencies to run all the script in ipynb file using pip3. Ensure pip3 is up to date. You can also use conda package manager to install all the package

```bash
$ pip3 install opencv-python
$ pip3 install numpy
$ pip3 install Pandas
$ pip3 install --upgrade tensorflow
$ pip3 install matplotlib
$ pip3 install -U scikit-learn
$ pip3 install h5py
```

### 3. Run notebook
- You can run the notebook using virtual environment created using anaconda and don't forget all the dependencies requires to run all script in the notebook.
```bash
$ jupyter notebook
```

### 4. Testing Field
- At the bottom of the notebook, I have prepared a testing field to test all the classifier model and ktp detector (#2). Please don't forget to run all required function and variable above.

## Extras
- You can try to train 3 classifier model with your own dataset, be careful of directory path will affect every script. Or simply add more data to current directory used for train the models.
- If you want to train your own cascade feature make sure you install libopencv-dev, create the samples, positive vector, and train the cascade.
- h5py use to save deep learning model (required). if you want to train the new model please check the filename so it won't overwrite the old one.
- If there's any issue regarding this sample test project, don't hesitate to contact: adiguna.richard@gmail.com
