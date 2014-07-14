sklad
=====

Resource Inventory

Install mod_wsgi
- refer http://code.google.com/p/modwsgi/wiki/QuickInstallationGuide.
- httpd.conf can be found under /etc/apache2/httpd.conf on osx 10.6.8.
- The exact line added to httpd.conf was "LoadModule wsgi_module libexec/apache2/mod_wsgi.so". The path to mod_wsgi depends on where the mod_wsgi make places mod_wsgi.so. This should show up in the build output.

Setup sklad.conf
- For basic understanding refer to http://code.google.com/p/modwsgi/wiki/QuickConfigurationGuide
- %sklad%/etc/apache2/sklad.conf is the mod_wsgi configuration for sklad.
- Appropriately modify sklad.conf and place it under /etc/apache2/user/. Rename the conf file to the user you would like to run this as.

Install pecan
- Mostly following instructions from http://pecan.readthedocs.org/en/latest/installation.html
- created the virtual env while in the sklad folder. 'virtualenv sklad-env'.

Deploying the app with pecan
- More info can be found http://pecan.readthedocs.org/en/latest/deployment.html

To start the script drop into the sklad virtualenv and run start_uwsgi.sh.

TODO (manask) - Include sqlalchemy instructions

