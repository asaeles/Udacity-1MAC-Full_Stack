import os
import re

def listImagesStartingWithNumbers(folder):
	filtered_files = []
	for fn in os.listdir(folder):
		if re.search('^\d+.+\.jpg$', fn) != None:
			filtered_files.append(fn)
	return filtered_files

def removePrefixNumbers(text):
	return re.sub('^\d+', '', text)

def revealSecretMessage(folder):
	curr_folder = os.getcwd()
	os.chdir(folder)
	for fn in listImagesStartingWithNumbers(folder):
		os.rename(fn, removePrefixNumbers(fn))
		print "File: " + fn + " renamed to: " + removePrefixNumbers(fn)
	os.chdir(curr_folder)

#print listImagesStartingWithNumbers(r"C:\secret_message\images")
#print removePrefixNumbers("123 file 123 name.jpeg")
revealSecretMessage(r"C:\secret_message\images")
