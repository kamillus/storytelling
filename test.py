#!/home2/kamillus/storytelling/venv/bin/python
import os,sys

sys.path.append("/home2/kamillus/storytelling/storytelling")
sys.path.insert(0, "/home2/kamillus/storytelling/venv/lib/python2.7/site-packages")
#sys.path.insert(0, "/home2/kamillus/storytelling/venv/lib/python2.7/site-packages/Django-1.7.dist-info")

#os.chdir("/home2/kamillus/storytelling/storytelling")

os.environ['DJANGO_SETTINGS_MODULE'] = "storytelling.settings"
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
