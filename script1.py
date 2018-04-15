import os
import sys

f=open('Version.txt')  #All the Details are fetched from the Version.txt File. [No Complex Parsing Mechanism is Used!]
lines=f.readlines()    #For Ease of Use, all the details are read line by line and the required values are expected between "<" and ">".

username=lines[0][lines[0].find("<")+1:lines[0].find(">")]  
password=lines[1][lines[1].find("<")+1:lines[1].find(">")]
package_version=lines[3][lines[3].find("<")+1:lines[3].find(">")]
version=lines[4][lines[4].find("<")+1:lines[4].find(">")]
channel=lines[6][lines[6].find("<")+1:lines[6].find(">")]


str="--project=project#### --packageversion="+ package_version +" --version="+version+" --channel="+channel+" --server http://12.30.10.10/ --user="+ username + " --pass="+ password +""


os.system("start cmd /k octo create-release "+str+"")   #Passing the parameters to Octo.exe Client.[This steps starts a command prompt and launches the octo.exe client with the given parameters]

