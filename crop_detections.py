#image cropping algorithm based on answer at https://stackoverflow.com/questions/61643523/how-to-crop-the-detected-object-after-training-using-yolo

import re
import cv2
import os

# parse txt file
path_results = r'C:\Users\shore\PythonProjects\FNCrop\result.txt'
path_img = r'C:\Users\shore\PythonProjects\FNCrop\image\cat.jpg'

myfile=open(path_results,'r')

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

crop_img = img[y_min:y_max, x_min:x_max]

#show image

#window_name = 'cropped image'

#cv2.imshow(window_name, crop_img) 
  
#cv2.waitKey(0)  
#cv2.destroyAllWindows()  


# save cropped image
save_directory = r'C:\Users\shore\PythonProjects\FNCrop\crop'

os.chdir(save_directory)

cv2.imwrite('crop.jpg', crop_img)