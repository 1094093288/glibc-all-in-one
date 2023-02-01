import os, re

# execute command, and return the output
def execCmd(cmd):
	r = os.popen(cmd)
	text = r.read()
	r.close()
	return text

# write "data" to file-filename
def lg(s):
	print('\033[1;31;40m[+]  %s '%(s))

def download(LibcNameList):
    for item in LibcNameList:
        os.system("./download {}".format(item))
        
val = int(execCmd("ls libs/ | wc -l "))

if val == 0:
	os.system("python update_list")
	lg("update list finished!!")

	f=open("./list","r")
	content=f.read()
	print(content)
	
	LibcNameList=content.split("\n")
	download(LibcNameList)
	lg('download all libc to ./libs/')
else:
	lg('please clean the libs folder first!!')
