#image cropping algorithm based on answer at https://stackoverflow.com/questions/61643523/how-to-crop-the-detected-object-after-training-using-yolo

import re
import cv2
import os

#path_img = path to image to be cropped
#path_save = path to where cropped image will be saved
#path_detection = path ro results file

#def crop(path_img, path_save, path_detection):
    # parse txt file
    
    path_img = r'C:\Users\shore\GitHub\RutYOLO\RutYOLO\image'
    path_save = r'C:\Users\shore\GitHub\RutYOLO\RutYOLO\crop'
    path_detection = r'C:\Users\shore\GitHub\RutYOLO\RutYOLO\results.txt'
    
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
    
  #  img_name = 'whatever the hell I want.jpg'
    
 #   os.chdir(path_save)
    
  #  cv2.imwrite(img_name, crop_img)
    
    