import re
import cv2
import os
import csv

field_names = ['file name', 'x min', 'x max', 'y min', 'y max']

dict = [
    {'file name': 'Mark', 'x min': 69, 'x max': 420, 'y min': 210, 'y max': 999},
    {'file name': 'Bashar', 'x min': 2, 'x max': 4, 'y min': 12, 'y max': 10000000000}
]

with open('dict.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(dict)