# create_database.py
import cv2, sys, numpy, os, time

count = 0
size = 4
fn_haar = 'haarcascade_frontalface_default.xml'
fn_dir = 'dataset'

#Entering USer's Unique ID
fn_name =input("Enter your unique ID")

#code snippet to save the images in the unique user's file directory
path = os.path.join(fn_dir, fn_name)

if not os.path.isdir(path):
    os.mkdir(path)
    
#Setting the size of our each image saved
(im_width, im_height) = (112, 92)

#=============initializing the haarcascade
haar_cascade = cv2.CascadeClassifier(fn_haar)

#initializing the webcam
webcam = cv2.VideoCapture(0)

#Setting total no. of Images to be stored in the database for each unique ID
TotImg=15;

while count < TotImg:            #Specifies the no. of Images to be taken
    #Capture frame-by-frame
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)
    
    #Converting the frame to be gray(Because the cascades used works with grayscale images)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))
    
    #To detect faces in our frame
    faces = haar_cascade.detectMultiScale(mini)
    faces = sorted(faces, key=lambda x: x[3])
    if faces:
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]
        
        #Finding the Region of Interest and Excluding everything else(resizing it)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))
        pin = sorted([int(n[:n.find('.')]) for n in os.listdir(path)
                      if n[0] != '.'] + [0])[-1] + 1
        cv2.imwrite('%s/%s.png' % (path, pin), face_resize)
        
        #Creation of a rectangle around the area of interest(Face)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(im, fn_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,
                    1, (0, 255, 0))
        time.sleep(0.38)
        count += 1

    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
print(str(count) + " images taken and saved to " + fn_name + " folder in database ")

#releasing the windows once done
webcam.release()
cv2.destroyAllWindows()
