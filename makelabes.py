import os
import shutil

with open('example.xml', 'r') as file :
  example = file.read()

basepath = 'RAW/'

entries = os.listdir(basepath)
print(entries)

if not os.path.exists("Data/train/images"):
    os.makedirs("Data/train/images")

if not os.path.exists("Data/train/annotations"):
    os.makedirs("Data/train/annotations")

if not os.path.exists("Data/validation/images"):
    os.makedirs("Data/validation/images")

if not os.path.exists("Data/validation/annotations"):
    os.makedirs("Data/validation/annotations")      

for entry in entries:
    if not entry.startswith('.'):

        i=0
        for imageFile in os.listdir(basepath+entry):
            if not imageFile.startswith('.'):
                if imageFile.endswith('.jpg'):
                    destImage = "Data/train/images/" + entry+ str(i) +'.jpg'
                    destxml = "Data/train/annotations/" + entry+ str(i) + '.xml'
                    if( i %7 == 0 or i %8 == 0 ):
                        destImage = "Data/validation/images/" + entry+ str(i) +'.jpg'
                        destxml = "Data/validation/annotations/" + entry+ str(i) + '.xml'
                    shutil.copy(basepath+entry+'/'+imageFile,destImage ) 
                    filedata = example.replace('LABEL', entry)
                    with open(destxml, 'w') as file:
                        file.write(filedata)

                    print("Data/" + entry+ str(i)+ '.jpg')
                    i+=1
                print(imageFile)

