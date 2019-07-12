import sys,getopt
from bs4 import BeautifulSoup
from utility import *
# -o output file
# -h help
# -m minify

argopt={'-o':False,'-h':False,'-i':False,'-m':False,"-p":False}
#process arguments
try:
    i=sys.argv.index("Tparse.py")
except:
    i=0
try:
    opts,args=getopt.getopt(sys.argv[i+1:],"hmpo:")
except:
    helpopt()
    sys.exit(2)
for opt,argu in opts:
    argopt[opt]=True if argu=="" else argu
try:
    argopt['-i']=args[0]
except:
    pass

#handling arguments
if(argopt['-h']):#help
    helpopt()
    sys.exit(0)

if(argopt['-i']): #input file
    f=open(argopt['-i'],'r')
    soup=BeautifulSoup(f.read(),"html.parser")
    f.close()
else: #get input from stdin
    html=multilineinput()
    soup=BeautifulSoup(html,"html.parser")


relative_static(soup)

if(argopt['-m']): #minify
    output=minify(soup)
elif(argopt['-p']): #pretty print
    output=soup.prettify()
else: #if nothing specified
    output=str(soup)

if(argopt['-o']): #output file
    f=open(argopt['-o'],"w")
    f.write(output)
    f.close()
else: #output to stdout
    print(output)