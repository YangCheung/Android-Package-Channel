#!/usr/bin/python
# encoding: utf-8
import zipfile,sys,shutil,os

if len(sys.argv)< 3 :
	print "parameter error"
	sys.exit()

if sys.argv[1].endswith('.apk') != True:
	print "First parameter must be apk file !"
	sys.exit()

if os.path.isfile(sys.argv[1]) != True:
	print sys.argv[1] + " not exist !"
	sys.exit()

tempFile = sys.argv[1]+"___tem"
shutil.copy(sys.argv[1], tempFile)
your_channel = sys.argv[2]

zipped = zipfile.ZipFile(tempFile, 'a', zipfile.ZIP_DEFLATED) 

empty_channel_file = "META-INF/channel_info"

file_object = open("empty_file", 'w')
try:
	file_object.write(your_channel)
finally:
     file_object.close( )


zipped.write("empty_file", empty_channel_file)

zipped.close()

targetFile = sys.argv[1].replace(".apk", "-" + sys.argv[2]) + ".apk"
shutil.move(tempFile, targetFile)
print "渠道包为：" + your_channel
print "生成文件：" + targetFile



