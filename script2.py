import os
import sys

f=open('Version.txt')
lines=f.readlines()

username=lines[0][lines[0].find("<")+1:lines[0].find(">")]
password=lines[1][lines[1].find("<")+1:lines[1].find(">")]
version=lines[4][lines[4].find("<")+1:lines[4].find(">")]
deploy_to=lines[8][lines[8].find("<")+1:lines[8].find(">")]
bdl=lines[10][lines[10].find("<")+1:lines[10].find(">")]       #These are some Variable Names defined in my deployment steps. You can skip/remove these if no prompt variables are there in your case.
dsu=lines[11][lines[11].find("<")+1:lines[11].find(">")]
dbr=lines[12][lines[12].find("<")+1:lines[12].find(">")]
gfm=lines[13][lines[13].find("<")+1:lines[13].find(">")]
str="--project=KORE.Telematics --version="+version+" --deployto="+deploy_to+""
var1='"'"Block on Dataloss (true or false):"+bdl+""'"'
var2='"'"Deploy Schema Update to target DB (true or false)?:"+dsu+""'"'
var3='"'"DBRestoreSource:"+dbr+""'"'
os.system("start cmd /k octo deploy-release --progress "+str+" --variable="+var1+" --variable="+var2+" --variable="+var3+" --guidedfailure="+gfm+" --server http://12.30.10.10/ --user="+ username + " --pass="+ password +"")