import sqlalchemy

_ENGINE = None

def get_engine():
	"""Return a SQLAlchemy engine."""
	global _ENGINE
	if _ENGINE is None:
		dialect = 'mysql'
		creds = 'root:stack'
		server_address = '192.168.129.151:3306'
		novadb_connection_string = dialect +'://'+ creds +'@'+ server_address +'/nova'
		_ENGINE = sqlalchemy.create_engine(novadb_connection_string)
	return _ENGINE