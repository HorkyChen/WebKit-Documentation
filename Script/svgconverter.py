#!/usr/bin/python
# coding: utf-8
#/*!
#@brief Description
#  A simple utility to remove watermark for SVG files exported by VP 9.0
#*/
import os,sys,string,datetime,copy,re

srcSVGString = ["Visual Paradigm for UML Enterprise Edition [evaluation copy]",
	"Visual Paradigm for UML Community Edition [not for commercial use]"]
pathInkSpace = "/Applications/Inkscape.app/Contents/Resources/bin/inkscape"
	
def replaceStringInNewFile(srcFile):
	file=open(srcFile, "r") 
	if None==file:
		print "Could not open for %s updating" %srcFile
		return -1
	
	allLines=file.readlines()
	file.close()
	index = 0
	
	
	for eachLine in allLines:
		
		for srcString in srcSVGString:
			if 0<=string.find(eachLine,srcString):
				allLines[index] = eachLine.replace(srcString,' ')
				break
		
		index = index+1
		
		
	file = open(srcFile,"w")
	file.writelines(allLines)
	file.close()
	
	return 0

def convertSVGToPNG(filename):
		fileStr, extStr = os.path.splitext(filename)
		if 0 == replaceStringInNewFile(filename):
			convertCmd=pathInkSpace+" -f\""+filename+"\" -e \""+fileStr+".png\" -d 150";
			return os.system(convertCmd)	
		else:
			return -1
			
			
def convertAllSVNInFolder(srcFolder):
	if not os.path.isdir( srcFolder ):
		return -1
	
	paths = os.listdir( srcFolder )
	for path in paths:
		filePath = os.path.join( srcFolder, path )
		if filePath[-4:].lower() == ".svg":
			convertSVGToPNG(filePath)
	
	return 0
	
# Main entry		
if __name__ =="__main__":
	print 'Please ensure the Inkscape has been installed,'
	print ' and put the installed folder in the PATH!' 
	
	if len(sys.argv) < 2:
		print '\tUsage: '
		print '\t python svgconvert.py sourceSVGFile or'
		print '\t python svgconvert.py svnFolder'
		print ' '
	elif os.path.isdir(sys.argv[1]):
		convertAllSVNInFolder(sys.argv[1])
	else:
		convertSVGToPNG(sys.argv[1])
	
	print '\nFinished! Enjoy the conversation result! '
	print 'If you have any comment, pls mail to'
	print '\t horky.chen@gmail.com'
	print ''