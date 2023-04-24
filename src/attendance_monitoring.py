import cv2, os
import csv
import datetime
import numpy as np

#Code snippet to get the system date
cd=datetime.datetime.now().date()
month=cd.month
day=cd.day
ct=datetime.datetime.now().time()
# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()
# Load the trained mode
recognizer.read('trainer.yml')
fn_dir = 'dataset'
# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"
(im_width, im_height) = (112, 92)
Total_stud=30
if((Total_stud/2)%1!=0):
    HalfStud=int(Total_stud/2)+1
else:
    HalfStud=int(Total_stud/2)
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
#Initialising the haarcascade classifier so that when the camera starts, it knows the area of interest
face_cascade = cv2.CascadeClassifier(cascadePath)
webcam = cv2.VideoCapture(0)
x=0
TotStud=[0]*Total_stud
for x in range(Total_stud):
    TotStud[x]=0
x=0
flag=[0]*Total_stud
for x in range(Total_stud):
    flag[x]=0
RecogCnt=0
while (1):
#Converting the current frame that will be used for recognition into grayscale, internally
#By internally we mean that we will see non-grayscale images    
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))
        prediction = recognizer.predict(face_resize)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if prediction[1] < 200:
            if (names[prediction[0]] == 'Nikhil'):
                cv2.putText(im, '%s - %.0f' % ('Nikhil', prediction[1]), (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1,
                            (0, 255, 0))
                TotStud[0] = TotStud[0] + 1
            elif (names[prediction[0]] == 'Obama'):
                cv2.putText(im, '%s - %.0f' % ('Obama', prediction[1]), (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1,
                            (0, 255, 0))
                TotStud[1] = TotStud[1] + 1               
            elif (names[prediction[0]] == 'Shripad sir'):
                cv2.putText(im, '%s - %.0f' % ('Shripad sir', prediction[1]), (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1,
                            (0, 255, 0))
                TotStud[2] = TotStud[2] + 1
        else:
            cv2.putText(im, 'not recognized', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
    if (TotStud[0]>35 and flag[0]==0):
        RecogCnt=RecogCnt+1
        flag[0]=1
        print('------Nikhil Marked-------')
        
    if (TotStud[1]>35 and flag[1]==0):
        RecogCnt=RecogCnt+1
        flag[1]=1
        print('------Obama Marked-------')
        
    if (TotStud[2]>35 and flag[2]==0):
        RecogCnt=RecogCnt+1
        flag[2]=1
    
    if (RecogCnt>=1):
        print("break state")
        break
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
webcam.release()
cv2.destroyAllWindows()
x=0
attend=[0]*Total_stud
for x in range(Total_stud):
    attend[x]=0
if(RecogCnt>=HalfStud):
    for i in range(Total_stud):      
        if(TotStud[i]>8):
            attend[i]=1

Subject=10
while(Subject<1 or Subject>9):
        Subject=int(input("Enter the Subject you want to load the attendance for\nSelect 1 for CVML"
            "\nSelect 2 for SIOT\nSelect 3 for AMT\nSelect 4 for DSP\nSelect 5 for OOPS\nSelect 6 for WC"
                "\nSelect 7 for DD\nSelect 8 for Robotics"))
def Mark_Attendance(Subject):
    
    AttRec=[day,month,ct,'',attend[0],attend[1],attend[2]]

 #-----------------------------------------------------------------------------------------------------------#
    
    if(Subject==1):
        
        if(month>=1 and month<=5):
            file = open('Subjects/MLCV/SEM1/MLCV_SEM1.csv', 'a',newline='')
        else:
            file = open('Subjects/MLCV/SEM2/MLCV_SEM2.csv', 'a',newline='')
            
#------------------------------------------------------------------------------------------------------------#
    
    if(Subject==2):
        
        if(month>=2 and month<=5):
            file = open('Subjects/SIOT/SEM1/SIOT_SEM1.csv', 'a',newline='')
        else:
            file = open('Subjects/SIOT/SEM2/SIOT_SEM2.csv', 'a',newline='')
            
#------------------------------------------------------------------------------------------------------------#            

    if(Subject==3):
        
        if(month>=1 and month<=5):
            file = open('Subjects/AMT/SEM1/AMT_SEM1.csv', 'a',newline='')
        else:
            file = open('Subjects/AMT/SEM2/AMT_SEM2.csv', 'a',newline='')
            
#------------------------------------------------------------------------------------------------------------#
            
    if(Subject==4):
        
        if(month>=1 and month<=5):
            file = open('Subjects/DSP/SEM1/DSP_SEM1.csv', 'a',newline='')
        else:
            file = open('Subjects/DSP/SEM2/DSP_SEM2.csv', 'a',newline='')
            
#------------------------------------------------------------------------------------------------------------#
    if(Subject==5):
        
        if(month>=1 and month<=5):
            file = open('Subjects/OOPS/SEM1/OOPS_SEM1.csv', 'a',newline='')
        else:
            file = open('Subjects/OOPS/SEM2/OOPS_SEM2.csv', 'a',newline='')

#------------------------------------------------------------------------------------------------------------#
           
    if(Subject==6):
        
        if(month>=1 and month<=5):
            file = open('Subjects/WC/SEM1/WC_SEM1.csv', 'a',newline='')
        else:
            file = open('Subjects/WC/SEM2/WC_SEM2.csv', 'a',newline='')

#------------------------------------------------------------------------------------------------------------#
   
    if(Subject==7):
        
        if(month>=1 and month<=5):
            file = open('Subjects/DD/SEM1/DD_SEM1.csv', 'a',newline='')
        else:
            file = open('Subjects/DD/SEM2/DD_SEM2.csv', 'a',newline='')

#------------------------------------------------------------------------------------------------------------#
    if(Subject==8):
       if(month>=1 and month<=5):
            file = open('Subjects/Robotics/SEM1/Robotics_SEM1.csv', 'a',newline='')
       else:
           file = open('Subjects/Robotics/SEM2/Robotics_SEM2.csv', 'a',newline='')


    wrt = csv.writer(file)
    wrt.writerow(AttRec) 
    file.close()




#Calling the mark attendance function
Mark_Attendance(Subject)



#--------------------------------------------Attendance Marking Done-----------------------------------------#



#Total no. of lecture conducted
Total_Lec=0

#Total Lectures attended
Lec_Attended=0

#Total Percentage Attended
Percent_Attended=0.0

#Creating the defaulters file

#accessing only the attendance(required) rows
LastRoll=3+Total_stud

#The Threshold Attendance for Defaulters Mark
Threshold_Attendance=75.0

#---------------------------------------Defaulters file creation-----------------------------------------------#
DefMonth=0

x=0
Stud=[0]*(Total_stud)
for x in range(Total_stud):
    Stud[x]=0

  
#------------------------------------------------------------------------------------------------------------#

def Defaulters_Entry(RollNo,DefMonth,TotLec,Attended,semester,subject):
    
        TotLec=TotLec
        DefMonth=DefMonth
      
        semester=semester
        subject=subject
        
        #Finding the percentage attended by that individual 
        #And making an entry if less than 75        
        Percent_Attended=(Attended/TotLec)*100
        if(Percent_Attended <= Threshold_Attendance):
            Stud[RollNo-1]=str(Percent_Attended)
        else:
            Stud[RollNo-1]="-"
        if(RollNo-1==Total_stud-1):
            Defaulters_File_Updation(DefMonth,TotLec,Stud,semester,subject)
            
#--------------------------------------------------------------------------------------------------------------#

def Defaulters_File_Updation(DefMonth,TotLec,Stud,semester,subject):
    
    DefRec=[DefMonth,TotLec,'',Stud[0],Stud[1],Stud[2]]
    
    file = open("Subjects/"+subject+"/"+semester+"/Defaulters_"+subject+"_"+semester+".csv","a",newline='')
    wrt = csv.writer(file)
    wrt.writerow(DefRec)

    file.close()

    
#-------------------------------------------------------------------------------------------------------------#       
           
                
        

        


DefCreated=0
#Creating the Defualters file at the end of the month

def Defaulers_Dates():
    
#-----------------------------------------------------------------------------------------------------------#    
        #Checking if its the month end (for 31 days' months)
        if((day==31) and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 )):
            
            file = open("DefCheck/DefCheck.csv","r")
            rdr = csv.reader(file,delimiter=",") 
           
            for row in rdr:
            
                if(row[0]==str(month)):
                    DefCreated=0
                    break
                else:
                    DefCreated=1
                
            file.close()
            
#-------------------------------------------------------------------------------------------------------------# 
               
        #Checking if its the month end (for 30 days' months)
        elif((day==30) and (month==4 or month==6 or month==9 or month==11 )):
            
            file = open("DefCheck/DefCheck.csv","r")
            rdr = csv.reader(file,delimiter=",") 
           
            for row in rdr:
            
                if(row[0]==str(month)):
                    DefCreated=0
                    break
                else:
                    DefCreated=1
                
            file.close()

#-------------------------------------------------------------------------------------------------------------#            
        
        #Checking if its the month end (for 28 days' months)
        elif((day==28) and (month==2)):
            
            file = open("DefCheck/DefCheck.csv","r")
            rdr = csv.reader(file,delimiter=",") 
           
            for row in rdr:
            
                if(row[0]==str(month)):
                    DefCreated=0
                    break
                else:
                    DefCreated=1
                
            file.close()
        
#--------------------------------------------------------------------------------------------------------------#       
        #If the month end was missed
        else:
            if((day==1 or day==2 or day==3) and ((month>=9 and month<=12) or (month>=2 and month<=5))):
                
                file = open("DefCheck/DefCheck.csv","r")
                rdr = csv.reader(file,delimiter=",") 
           
                for row in rdr:
            
                    if(row[0]==str(month-1)):
                        DefCreated=0
                        break
                    else:
                        DefCreated=2
                file.close()
  
        if(DefCreated==1 or DefCreated==2):
            x=0
            
            for x in range(8):
#--------------------------------------------CVML Defaulters------------------------------------------------#                
                if(x==0):
                    Subject="MLCV"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"
                        
                    
#---------------------------------------------SIOT Defaulters-----------------------------------------------#
                if(x==1):
                    Subject="SIOT"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"
                        
                    
#---------------------------------------------AMT Defaulters-----------------------------------------------#
                if(x==2):
                    Subject="AMT"
                    if(month>=1 and month<=5):
                        Semester="SEM1"                        
                    else:
                        Semester="SEM2"
                        
                    
#---------------------------------------------DSP Defaulters-----------------------------------------------#
                if(x==3):
                    Subject="DSP"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"
                        

#---------------------------------------------OOPS Defaulters-----------------------------------------------#
                if(x==4):
                    Subject="OOPS"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"
                    
#---------------------------------------------WC Defaulters-----------------------------------------------#
                if(x==5):
                    Subject="WC"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"


#---------------------------------------------DD Defaulters-----------------------------------------------#
                if(x==6):
                    Subject="DD"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"
                     
                    
#---------------------------------------------Robotics Defaulters-----------------------------------------------#
                if(x==7):
                    Subject="Robotics"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"
                
                        
                        
#------------------------------Finding Total Lectures conducted------------------------------------------------#                    
               
                
                Total_Lec=0
                print("In defaulters")
                #Code snippet to find out total no. of lectures conducted
                file = open("Subjects/"+Subject+"/"+Semester+"/"+Subject+"_"+Semester+".csv","r")
                rdr = csv.reader(file,delimiter=",")
                for row in rdr:
                    if(row[4]=='1' or row[4]=='0'):
                        Total_Lec=Total_Lec+1
                
                
#-------------------------find how many lecture individual student has attended-------------------------------#
                
                i=4
                while(i!=LastRoll+1):
                    Lec_Attended=0
                    file = open("Subjects/"+Subject+"/"+Semester+"/"+Subject+"_"+Semester+".csv","r")
                    rdr = csv.reader(file,delimiter=",") 
           
                    for row in rdr:
                        if(row[i]=='1'):
                           
                            Lec_Attended=Lec_Attended+1
                           # print("Lec attended="+str(Lec_Attended))
                            
                    #If Defaulters file created on month end
                    if(Total_Lec!=0):
                        
                        if(DefCreated==1):
                            Defaulters_Entry(i-3,month,Total_Lec,Lec_Attended,Semester,Subject)
                        
                    #If defaulters file is created for the prev month on dates 1 2 3 of next month
                        elif(DefCreated==2):
                            Defaulters_Entry(i-3,month-1,Total_Lec,Lec_Attended,Semester,Subject)
                        
                    
                    i=i+1
                    
                    file.close()
                    

#---------------------------------------Making an entry into Defaulters Check file-----------------------------#                    
         
        if(DefCreated==1):
            DefCheRec=[month]
            file = open("DefCheck/DefCheck.csv","a",newline='')
            
            wrt = csv.writer(file)
            wrt.writerow(DefCheRec)
            file.close()
            
        elif(DefCreated==2):
            DefCheRec=[month-1]
            file = open("DefCheck/DefCheck.csv","a",newline='')
            wrt = csv.writer(file)
            wrt.writerow(DefCheRec)
            file.close()
            
def Explicit_Def_Updt():
#Code Snippet if no teacher is able to initiate the defaulters update, in the above given days       
    if((day>=4 and day<=26) and ((month>=7 and month<=12) or (month>=1 and month<=5))):
        Update_Def=0
        x=0   
        #Remind the teacher to create a Defaulters file, if it hasnt been
        file = open("DefCheck/DefCheck.csv","r")
        rdr = csv.reader(file,delimiter=",") 
           
        for row in rdr:
            
            if(row[0]==str(month-1)):
                Update_Def=0
                
                break
            else:
                Update_Def=1
        
        if(Update_Def==1):
            Update_Def=int(input("Previous month's defaulter file hasn't been updated\n"
                                 "Do you want to update it?\nPress\n1->YES    0->NO  "))
        elif(Update_Def==0):
            print("Defaulters file already created for previous month")
            
      
        file.close()
    
        if(Update_Def==1):
            for x in range(8):

#--------------------------------------------CVML Defaulters------------------------------------------------#                
                if(x==0):
                    Subject="MLCV"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"
                        
                    
#---------------------------------------------SIOT Defaulters-----------------------------------------------#
                if(x==1):
                    Subject="SIOT"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"
                        
                    
#---------------------------------------------AMT Defaulters-----------------------------------------------#
                if(x==2):
                    Subject="AMT"
                    if(month>=1 and month<=5):
                        Semester="SEM1"                        
                    else:
                        Semester="SEM2"
                        
                    
#---------------------------------------------DSP Defaulters-----------------------------------------------#
                if(x==3):
                    Subject="DSP"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"
                        

#---------------------------------------------OOPS Defaulters-----------------------------------------------#
                if(x==4):
                    Subject="OOPS"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"
                    
#---------------------------------------------WC Defaulters-----------------------------------------------#
                if(x==5):
                    Subject="WC"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"


#---------------------------------------------DD Defaulters-----------------------------------------------#
                if(x==6):
                    Subject="DD"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"
                     
                    
#---------------------------------------------Robotics Defaulters------------------------------------------#
                if(x==7):
                    Subject="Robotics"
                    if(month>=1 and month<=5):
                        Semester="SEM1"
                    else:
                        Semester="SEM2"


#------------------------------------Total Lec conducted till last month-end--------------------------------#                 
                 #Code snippet to find out total no. of lectures conducted
                
                 #Counting the total no. of lectures conducted till the previous month
                LecTillLastMonth=0
                file = open("Subjects/"+Subject+"/"+Semester+"/"+Subject+"_"+Semester+".csv","r")
                rdr = csv.reader(file,delimiter=",") 
        
                for row in rdr:
                    if(row[1]<str(month)):
                        LecTillLastMonth=LecTillLastMonth+1
                
                file.close()
            

#----------------------------------Attendance of individual student till last month--------------------------#


            #Finding the attendance till last month and the passing the values 
                EmptyFile=0
                i=4
                count=0
                while(i!=LastRoll+1):
                    Lec_Attended=0
                    file = open("Subjects/"+Subject+"/"+Semester+"/"+Subject+"_"+Semester+".csv","r")
                    rdr = csv.reader(file,delimiter=",") 
                    for row in rdr:
                            if(row[i]=='1' and row[0]<=str(month-1)):
                    
                                print(row[i])
                                count=count+1
                    
                                Lec_Attended=Lec_Attended+1
                    if(LecTillLastMonth!=0):
                        Defaulters_Entry(i-3,month-1,LecTillLastMonth,Lec_Attended,Semester,Subject)
                    else:
                        EmptyFile=1
                        
                
                    print("\nLec attended="+str(Lec_Attended)+"\n")
                    file.close()
                    i=i+1
                    count=0
            
                    print("Sturdent "+str(i-4)+"'s attendance is="+str(Lec_Attended)+" out of="+str(LecTillLastMonth))
                if(EmptyFile==1):
                    print("No lectures happened in the month="+str(month-1)+"\nfor the subject="+str(Subject))
                    EmptyFile=0
        if(Update_Def==1):
            DefCheRec=[month-1]
            file = open("DefCheck/DefCheck.csv","a",newline='')
            wrt = csv.writer(file)
            wrt.writerow(DefCheRec)
            file.close()
#----------------------------Checking the date and updating Defaulters file---------------------------------#           
if((day==30 and (month==4 or month==6 or month==9 or month==11 )) or 
   ((day==31) and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 )) or 
   (day==1 or day==2 or day==3) and ((month>=9 and month<=12) or ((month>=2 and month<=5)) or (day==28) and (month==2))):
    
    Defaulers_Dates()
        
elif((day>=4 and day<=26) and ((month>=7 and month<=12) or (month>=1 and month<=5))):
    Explicit_Def_Updt()
  
