from ncclient import manager
import xml.dom.minidom

# Using the manager.connect() function, set up an m connection object
# to the IOS XE device.
m = manager.connect(
    host="sandbox-iosxe-latest-1.cisco.com",
    port=830,
    username="admin",
    password="C1sco12345",
    hostkey_verify=False
    )

# After a successful NETCONF connection, use the “get_config()” function
# of the “m” NETCONF session object to retrieve and print the device’s running
# configuration. The get_config() function expects a “source” string parameter
# that defines the source NETCONF data-store.
netconf_reply = m.get_config(source="running", filter= netconf_filter)
print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )

# Create the following netconf_filter variable containing an XML NETCONF filter
# element that is designed to retrieve only data that is defined by the
# Cisco IOS XE Native YANG model:
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
