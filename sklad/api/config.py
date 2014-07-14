# Server Specific Configurations
server = {
    'port': '8777',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'sklad.api.controllers.root.RootController',
    'modules': ['sklad.api'],
    'static_root': '',
    'template_path':'',
    'debug': False,
}

logging = {
    'loggers': {
        'root': {'level': 'INFO', 'handlers': ['console']},
        'sklad': {'level': 'DEBUG', 'handlers': ['console']}
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        }
    },
}