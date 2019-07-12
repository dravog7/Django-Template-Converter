from bs4 import BeautifulSoup
import sys
def update_link_static(i,tagname):
    link=i.get(tagname)
    if(link.startswith("/")):
        i[tagname]="{% static '"+link+"' %}"

def relative_static(soup):
    try:
        soup.html.insert_before("{% load static %}")
    except:
        print("couldnt find html tag")
        sys.exit(2)
    for i in soup.findAll(href=True):
        update_link_static(i,"href")
    for i in soup.findAll(src=True):
        update_link_static(i,"src")

def minify(soup):
    mini=str(soup).replace("\n","")
    return mini

def helpopt():
    st="""
    Syntax:
    python Tparse.py -h [-o outputfile] [-m|-p] [inputfile]

    What Am I?

    I am a python script made to replace relative paths to django static template tags easily. 
    I only replace / relative paths. I can minify to an extend as well. Use me if reading to avoid manually
    replacing these paths.

    Options:
    -h            displays this help dialog
    -o outputfile redirect output to outputfile, if not specified outputs to stdout
    -m            minify the html
    -p            pretty print html
    inputfile     the input taken from inputfile, if not specified inputs taken from stdin
    """
    print(st)

def multilineinput():
    st=[]
    while True:
        try:
            i=input()
            st.append(i)
        except:
            return "/n".join(st)