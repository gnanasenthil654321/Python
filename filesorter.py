# sorts files in a folder according to date and puts them in a destination folder with the same date as its name

import os
import datetime
import Tkinter
import tkFileDialog
import shutil

def modification_date(filename):
	t = os.path.getmtime(filename)
	return datetime.date.fromtimestamp(t)

def askFolder():
	root = Tkinter.Tk()
	
	folder_name = tkFileDialog.askdirectory(parent = root, initialdir = '/', title = "Choose a  sourcefolder")
	root.destroy()
	return str(folder_name)
	
folder_chosen = askFolder()



for i in os.walk(folder_chosen):
	for files in i[2]:
		file_path = os.path.abspath(os.path.join(i[0],files))
		newpath = os.path.abspath('F:/Test3/Kavin photos'+'/'+str(modification_date(file_path)))
		print newpath
		if not os.path.exists(newpath):
			os.makedirs(newpath)
			
		shutil.copy2(file_path,newpath)	
		


print "End of Process"
