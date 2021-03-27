import cv2
import os

source = cv2.VideoCapture(2) #BW Infrared
source_color = cv2.VideoCapture(3) #Color Image

save_path = os.getcwd() + '/captured/' 

#Read last image status
last_file = open(save_path + "LastStatus.txt","r")
k = last_file.read()
print("Last captured data is image " + k)
print("Shoot Image with Space-Bar! Exit with Esc!")
k = int(k)
last_file.close()

while(True):
    ret,img=source.read()
    ret2,img2=source_color.read()

    scale = 4 #Adjust Scaling for display
    
    resized = cv2.resize(img, (160*scale,120*scale))
    resized_color = cv2.resize(img2, (720,540))
    cv2.imshow("FLIR",resized)
    cv2.imshow("COLOR",resized_color)

    key = cv2.waitKey(1)
    
    #Exit
    if(key==27):
        break

    #Capture the image with space-bar
    if(key==32):
        cv2.imwrite(save_path+'IR/'+ 'IR-' + str(k) +'.png',img) #Capture raw
        cv2.imwrite(save_path+'/COLOR/'+ 'CI-' + str(k) +'.png',img2) #Captrure raw
        print("Capture " + str(k) + " Success!")
        k=k+1
        last_file = open(save_path + "LastStatus.txt","w")
        last_file.write(str(k))
        last_file.close()

cv2.destroyAllWindows()
source.release()