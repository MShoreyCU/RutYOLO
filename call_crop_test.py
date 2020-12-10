import re
import cv2
import os

#import crop function to this file
#from cropfunction.py import crop

def crop(path_img, path_save, path_detection):
    # parse txt file
    
    myfile=open(path_detection,'r')
    
    lines=myfile.readlines()
    
    pattern= "Cat"
    
    for line in lines:
        if re.search(pattern,line):
            Cord_Raw=line
    Cord=Cord_Raw.split("(")[1].split(")")[0].split("  ")
    
    # calculate coordinates
    
    x_min=int(Cord[1])
    x_max=x_min + int(Cord[5])
    y_min=int(Cord[3])
    y_max=y_min+ int(Cord[7])
    
    #crop image
    
    img = cv2.imread(path_img)
    
    cv2.imshow('whatever the hell i want', img) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows()  
    
    
  #  crop_img = img[y_min:y_max, x_min:x_max]
    
   # img_name = 'whatever the hell I want.jpg'
    
   # os.chdir(path_save)
    
   # cv2.imwrite(img_name, crop_img)
    

#define variables to feed to function
pimg = r'C:\Users\shore\GitHub\RutYOLO\RutYOLO\image\cat'
psave = r'C:\Users\shore\GitHub\RutYOLO\RutYOLO\crop'
presult = r'C:\Users\shore\GitHub\RutYOLO\RutYOLO\result.txt'

crop(pimg,psave,presult)

