import os, sys, site, time, uwsgi

# Add curerntFilePath to the search path so that everything under sklad is found.
currentFilePath = os.path.dirname(os.path.abspath(__file__))
print 'currentFilePath : ' + currentFilePath
# sys.path.append(currentFilePath)

# Setup sklad-env virtual env as the configuration environment
# TODO(manasK) - path config should not have to be this way.
skladVirtualEnv = currentFilePath + '/sklad-env/lib/python2.7/site-packages'
print 'skladVirtualEnv : ' + skladVirtualEnv
site.addsitedir(skladVirtualEnv)

from sklad.api import app

# setup the wsgi application
application = app.VersionSelectorApplication()

# uwsgi specific stuff

_mtimes = {}
_win = (sys.platform == "win32")

def get_free_signal():
    for signum in xrange(0, 256):
        if not uwsgi.signal_registered(signum):
            return signum

    raise Exception("No free uwsgi signal available")

class timer(object):

    def __init__(self, secs, **kwargs):
        self.num = kwargs.get('signum', get_free_signal())
        self.secs = secs
        self.target = kwargs.get('target', '')

    def __call__(self, f):
        uwsgi.register_signal(self.num, self.target, f)
        uwsgi.add_timer(self.num, self.secs)
        return f

def code_changed():
    global _mtimes, _win
    filenames = []
    for m in sys.modules.values():
        try:
            filenames.append(m.__file__)
        except AttributeError:
            pass
    for filename in filenames:
        if not filename:
            continue
        if filename.endswith(".pyc") or filename.endswith(".pyo"):
            filename = filename[:-1]
        if filename.endswith("$py.class"):
            filename = filename[:-9] + ".py"
        if not os.path.exists(filename):
            continue # File might be in an egg, so it can't be reloaded.
        stat = os.stat(filename)
        mtime = stat.st_mtime
        if _win:
            mtime -= stat.st_ctime
        if filename not in _mtimes:
            _mtimes[filename] = mtime
            continue
        if mtime != _mtimes[filename]:
            _mtimes = {}
            return True
    return False

#@timer(3)
def change_code_gracefull_reload(sig):
	if code_changed():
		uwsgi.reload()

