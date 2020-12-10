import cv2

path = r'C:\Users\shore\PythonProjects\FNCrop\image\cat.jpg'

img = cv2.imread(path)

crop_img = img[26:504, 311:646]

window_name = 'crop'

# Using cv2.imshow() method  
# Displaying the image  
cv2.imshow(window_name, crop_img) 
  
#waits for user to press any key  
#(this is necessary to avoid Python kernel form crashing) 
cv2.waitKey(0)  
  
#closing all open windows  
cv2.destroyAllWindows()  