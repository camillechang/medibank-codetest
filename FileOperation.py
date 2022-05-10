import sys
import re
import os

# find all the txt files and file path under a folder
def getTextFileList(folderPath):
	fileList = []
	for root, dirs, files in os.walk(folderPath):
		for file in files:
			if os.path.splitext(file)[1] == '.txt':
					fileList.append(os.path.join(root,file))
	return fileList

#search keyword from  single file
def searchTextFile(filePath, keyword):
    count = 0
    file = open(filePath,'r')
		#Loop through the file line by line:
    for line in file:
       count += line.lower().count(keyword) #case insensitive
    return count

#search keyword  from  one folder
def getKeywordTimes(fileList, keyword):
	sum = 0
	for file in fileList:
		num = searchTextFile(file, keyword.lower()) #case insensitive
		sum += num
	return sum

def test(testStr,dirPath):
	keywords=testStr.split(' ')
	dirlist= getTextFileList(dirPath)
	for keyword in keywords:
		time = getKeywordTimes(dirlist, keyword)
		print('{} {}'.format(keyword, time)) #format output