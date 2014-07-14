import json

class ResourceDescriptor(object):
	"Base type for descriptor of resources."
	def __init__(self, typename=None, relations=None, properties=None, default=None):
		self.typename = typename
		self.relations = relations
		self.properties = properties
		self.default = default

class HostResourceDescriptor(ResourceDescriptor):
	"Descriptor for a host/hypervisor."

	def __get_property_descriptors():
		return {'id':'string', 'hypervisor_hostname':'string'}

	def __get_default_properties():
		return ["id","hypervisor_hostname"]

	__typename = "host"
	__relations = ["vm"]
	__properties = __get_property_descriptors()
	__default = __get_default_properties()
	
	def __init__(self):
		global __typename
		ResourceDescriptor.__init__(self, 
			HostResourceDescriptor.__typename, 
			HostResourceDescriptor.__relations, 
			HostResourceDescriptor.__properties, 
			HostResourceDescriptor.__default)

class VmResourceDescriptor(ResourceDescriptor):
	"Descriptor for a vm/instance."

	def __get_property_descriptors():
		return {'id':'string', 'display_name':'string'}

	def __get_default_properties():
		return ["id","display_name"]

	__typename = "vm"
	__relations = None
	__properties = __get_property_descriptors()
	__default = __get_default_properties()

	def __init__(self):
		ResourceDescriptor.__init__(self, 
			VmResourceDescriptor.__typename, 
			VmResourceDescriptor.__relations, 
			VmResourceDescriptor.__properties, 
			VmResourceDescriptor.__default)

class ResourceDescriptorEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, ResourceDescriptor):
			return {'typename' : obj.typename, 'relations' : obj.relations, 'properties' : obj.properties, 'default': obj.properties}
		return json.JSONEncoder.default(self, obj)
