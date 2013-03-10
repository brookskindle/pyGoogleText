import os
from distutils.sysconfig import get_python_lib
libdir = get_python_lib() #give site packages directory #solution found at http://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory
#pythonpath = os.getcwd() #we assume this is the python directory
os.chdir(libdir)
#os.chdir('site-packages')
os.chdir('googlevoice')
#gvdir = "C:\python27\Lib\site-packages\googlevoice\settings.py"
gvdir = os.getcwd()
gvdir += "\\settings.py"
f = open(gvdir,'r')
fread = f.read()
fread.replace("LOGIN = 'https://www.google.com/accounts/ServiceLoginAuth?service=grandcentral'","LOGIN = 'https://accounts.google.com/ServiceLogin?service=grandcentral&passive=1209600&continue=https://www.google.com/voice&followup=https://www.google.com/voice&ltmpl=open'")
f.close()
f = open(gvdir,'w')

f.write(fread)

f.close()
