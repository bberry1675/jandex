srcpath = ""
for srcpath in open("test.txt","r"):
	srcpath = srcpath.strip()
	if(srcpath == ""):
		continue
	src = open("./"+srcpath,"r")
	des = open("/Users/brandonberry/Documents/libertyGit/workspaces/open/open-liberty/dev/com.ibm.ws.anno/src/com/ibm/ws/anno/jandex/internal/"+srcpath,"w+")
	temp = ""
	for temp in src:
		if "package org.jboss.jandex;" in temp:
			des.write("package com.ibm.ws.anno.jandex.internal;\n")
		else:
			des.write(temp)

	src.close()
	des.close()

	


