#! /usr/bin/python
import os

if os.name == 'nt':
	a = 'D:/images/boot_pictures'
if os.name == 'posix':

	a = '/media/gg/d_drive/images/boot_pictures' #the directory where the pictures reside

list_files = os.listdir(a) # gives the list of files in the above directory

#sort the list, to avoid confusion
list_files.sort()

#reverse the list to comply with below code
list_files.reverse()

len_list = len(list_files) # the length of the list "list_files"

#filename to be corrected

for i in list_files:
	# previous filename with path
	previous_filename_with_path = a+'/'+i
	# extension of the above filename
	previous_filename_ext = os.path.splitext(previous_filename_with_path)[1]
	# length of the above extension
	len_ext = len(previous_filename_ext)
	# find the interger from the filename
	previous_num = int(i[0:len(i)-len_ext])
	
	# generate new num as str
	present_num = str(previous_num + 1)
	# generate new filename with path
	present_filename_with_path =  a + '/' + present_num + previous_filename_ext
	
	# rename the files
	os.rename(previous_filename_with_path,present_filename_with_path)
	#os.rename(a+'/'+i,a+'/'+str(previous_num)+'.png')
	
#os.rename(a+'/'+str(len_list+1)+'.png',a+'/'+'1.png')
# final renaming

# list the files in the directory mentioned above again to find the file with the name starting with the largest integer
new_file_list = os.listdir(a)

# sort -> reverse -> choose the first file for manipulation
new_file_list.sort()
new_file_list.reverse()

first_filename_with_path = a + '/' + new_file_list[0]

first_filename_ext = os.path.splitext(first_filename_with_path)[1]

# renaming
os.rename(first_filename_with_path,os.path.normpath(a + '/' + str(1) + first_filename_ext))
