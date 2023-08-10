# Import the ConnectHandler() function from the netmiko module.
from netmiko import ConnectHandler

# Setup a sshCli connection object using the ConnectHandler() function
# to the IOS XE device.
sshCli = ConnectHandler(
    device_type='cisco_ios',
    host='sandbox-iosxe-recomm-1.cisco.com',
    port=22,
    username='developer',
    password='lastorangerestoreball8876'
    )

# Send a show command and print the output. The send_command() function of the
# sshCli object is used to send a string including a command you wish to execute
# in the exec mode.
output = sshCli.send_command("show ip int brief")
print("show ip int brief:\n{}\n".format(output))

# Set the commands you want to send to a list.
config_commands = [
    'int loopback 1',
    'ip address 2.2.2.2 255.255.255.0',
    'description WHATEVER'
    ]

# The send_config_set() function will be used on the sshCli object to send
# configuration commands that you wish to execute in exec mode.
output = sshCli.send_config_set(config_commands)

# Add code to create a new loopback interface (loopback2).
config_commands = [
    'int loopback 2',
    'ip address 2.2.2.2 255.255.255.0',
    'description DIFFERENT'
    ]

output = sshCli.send_config_set(config_commands)

# The instructions were unclear, however I would definitely put a "show ip int
# brief" command here in order to verify the results, if I wasn't getting the
# netmiko errors. I will add it here now, even though the instructions didn't
# explicitly state to.
output = sshCli.send_command("show ip int brief")
print("show ip int brief:\n{}\n".format(output))
