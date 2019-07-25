#Question 1
#Using os.walk, write a script that will print the filenames of zero length files.
## It should also print the count of zero length files.

import os

for root, dirs, files in os.walk('.'):
    print(files)
    for file in files:
        size=os.path.getsize(os.path.join('.',file))
        if size==0:
            print("Size:", size, "\nFile:", file)





#Question 2
#Write a script that will list and count all of the images in a given HTML web page/file.
# You can assume that:
##Each image file is enclosed with the tag <img and ends with >
##The HTML page/file is syntactically correct
#(<img)(.)+(>)


import re

def countimages(file):
    file = open(file,'r')
    numberimages=0
    for line in file:
        imgcode= re.findall(r'<img', line)
        numberimages=numberimages+len(imgcode)
    file.close()
    print("The number of images is:", numberimages)


simpletest=countimages("simplehtml.txt")
amazontest=countimages("amazonsite.txt")