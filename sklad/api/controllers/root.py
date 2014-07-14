from pecan import expose, rest
from sklad.datasource import session
import json
from sklad.api.resourcedescriptors import *

class HostController(rest.RestController):
    """
    All host specific data is returned by this controller.
    supports the url -
    1. http://localhost:9090/hosts/
    2. http://localhost:9090/hosts/1
    3. http://localhost:9090/hosts/describe
    """
    __descriptor = HostResourceDescriptor()

    _custom_actions = {
        'describe': ['GET']
    }

    @expose('json')
    def get_all(self):
        engine = session.get_engine()
        result = engine.execute("select id, hypervisor_hostname from compute_nodes")
        rows = [{'id':row['id'], 'hypervisor_hostname':row['hypervisor_hostname']} for row in result]
        return json.dumps(rows)

    @expose('json')
    def get_one(self, host):
        engine = session.get_engine()
        result = engine.execute("select id, hypervisor_hostname from compute_nodes where id = '"+host+"'")
        rows = [{'id':row['id'], 'hypervisor_hostname':row['hypervisor_hostname']} for row in result]
        result_vm = result = engine.execute("select id, display_name from instances where host='"+rows[0]['hypervisor_hostname']+"'")
        rows_vm = [{'id':row['id'],'display_name':row['display_name']} for row in result]
        rows[0]['vms'] = rows_vm
        return json.dumps(rows)

    @expose('json')
    def describe(self):
        return json.dumps(HostController.__descriptor, cls=ResourceDescriptorEncoder)

class VmController(rest.RestController):
    """
    All vm specific data is returned by this controller.
    supports the url -
    1. http://localhost:9090/vms/
    2. http://localhost:9090/vms/1
    3. http://localhost:9090/vms/describe
    """
    __descriptor = VmResourceDescriptor()

    _custom_actions = {
        'describe': ['GET']
    }

    @expose('json')
    def get_all(self):
        engine = session.get_engine()
        result = engine.execute("select id, display_name from instances")
        rows = [{'id':row['id'],'display_name':row['display_name']} for row in result]
        return json.dumps(rows)

    @expose('json')
    def get_one(self, vm):
        engine = session.get_engine()
        result = engine.execute("select id, display_name from instances where id = '"+vm+"'")
        rows = [{'id':row['id'],'display_name':row['display_name']} for row in result]
        return json.dumps(rows)

    @expose('json')
    def describe(self):
        return json.dumps(VmController.__descriptor, cls=ResourceDescriptorEncoder)

class RootController(object):
    """sets up the host and vm controllers"""
    @expose(
        template        = None,
        content_type    = 'text/html',
        generic         = False
    )
    def index(self):
        return "Welcome to Sklad."

    hosts = HostController()
    vms = VmController()