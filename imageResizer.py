import datetime
import time
import os
from PIL import Image

def getFolder():
	print ("Please input the source Folder's name")
	folder_name = input()
	return str(folder_name)

def getAllFiles():
# gets all the files with the absolute path in a folder
	a = getFolder()
	file_names = []
	for i in os.walk(a):
		for files in i[2]:
			file_path = os.path.abspath(os.path.join(i[0],files))
			file_names.append(file_path)
	file_names.sort()
	return file_names	

def resizePicture(filename,width,height,outfilename):
	size = width,height
#outfilename is the name of the saved file
	img = Image.open(filename)
	img = img.resize(size)
	t = time.time()
	timestring = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
	
	# users may which to change the destination folder as required.
	filename_save = "/home/physiology/resized/" + timestring +str(outfilename)+".jpg"
	img.save(filename_save,"JPEG")

files = getAllFiles()
print(files)
print(len(files))
j = 1
print("please input width of intended picture")
width = int(input())
print("please input height of intended picture")
height =int(input())


for i in files:
	resizePicture(i,width,height,j)
	print(j)
	j = j+1
