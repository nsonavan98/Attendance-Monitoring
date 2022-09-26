# facerec.py
import cv2, sys, numpy, os,time

size = 4
fn_haar = 'haarcascade_frontalface_default.xml'
fn_dir = 'dataset'

#Initializing the Feature Detector- LOCAL BINARY PATTERN
recognizer=cv2.face.LBPHFaceRecognizer_create()

# Part 1: Create fisherRecognizer
print('Training...')
# Create a list of images and a list of corresponding names

#This is the code snippet for setting up the nomenclature for training of the images
#For example, the machine wants to train the faces corresponiding to the id of the user
#Then each image is given a tag or the label and the recognizer extracts features of the user
#And maps it to that particular id
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(fn_dir):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(fn_dir, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1
(im_width, im_height) = (112, 92)

# Create a Numpy array from the two lists above
(images, lables) = [numpy.array(lis) for lis in [images, lables]]


# model = cv2.reateFisherFaceRecognizer()
#This snippet is the recognizer class of the cv2 library and we are using LBPH recognizer
recognizer.train(images, lables)
recognizer.save('trainer.yml')