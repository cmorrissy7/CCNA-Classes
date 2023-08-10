# Import the “manager” class from the ncclient module.
from ncclient import manager

# Setup an m connection object using the manager.connect() function to
# the IOS XE device.
m = manager.connect(
    host="sandbox-iosxe-latest-1.cisco.com",
    port=830,
    username="admin",
    password="C1sco12345",
    hostkey_verify=False
    )

# In every NETCONF session, the server first sends its list of
# capabilities – supported YANG models. With the ncclient module,
# the received list of capabilities is stored in the m.server_capabilities list.

# Use a for loop and a print function to print the device capabilities:
print("#Supported Capabilities (YANG models): ")
for capability in m.server_capabilities:
    print(capability)
