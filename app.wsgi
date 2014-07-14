import os
import sys
import site

# Add curerntFilePath to the search path so that everything under sklad is found.
currentFilePath = os.path.dirname(os.path.abspath(__file__))
print 'currentFilePath : ' + currentFilePath
sys.path.append(currentFilePath)

# Setup sklad-env virtual env as the configuration environment
skladVirtualEnv = currentFilePath + '/sklad-env/lib/python2.7/site-packages'
print 'skladVirtualEnv : ' + skladVirtualEnv
site.addsitedir(skladVirtualEnv)

from sklad.api import app

application = app.VersionSelectorApplication()