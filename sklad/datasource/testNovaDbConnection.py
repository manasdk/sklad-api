# Connects directly to mysql server on controller node.
# - requires MySQL-python
# - requires sqlalchemy
# To install MySQL-python follow instruction from http://mysql-python.blogspot.com/. Summary below ...
# - brew install mysql (reqired to install various driver)
# - pip install MySQL-python
# - pip install SQLAlchemy
import sqlalchemy
import json

def instancesOnComputeNode(connection, host):
	result = connection.execute("select display_name from instances where host='" + host + "'")
	for row in result:
		print '\t' + row['display_name']

# sqlalchemy url dialect+driver://username:password@host:port/database
# see http://docs.sqlalchemy.org/en/rel_0_8/core/engines.html#sqlalchemy.create_engine
dialect = 'mysql'
creds = 'root:stack'
serverAddr = '192.168.129.151:3306'
novaConnStr = dialect+'://'+creds+'@'+serverAddr+'/nova'

print 'Connecting to : ' + novaConnStr
engine = sqlalchemy.create_engine(novaConnStr)
connection = engine.connect()

try :
	result = connection.execute("select id, hypervisor_hostname from compute_nodes")
	rows = [json.dumps({'id' : row['id'], 'hypervisor_hostname' : row['hypervisor_hostname']}) for row in result]
	print json.dumps(rows)
	#print 'host-vm relation'
	#for row in result:
	#	print row['hypervisor_hostname']
	#	instancesOnComputeNode(connection, row['hypervisor_hostname'])
finally :
	connection.close()