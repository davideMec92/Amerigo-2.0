import sock as inquiry_manager

"""from Bluetoothctl import Bluetoothctl

print("Initializing bluetooth..")
b = Bluetoothctl()
print("Start scan..")
b.start_scan()"""

"""import bluetooth

target_name = "Honor Play"
target_address = None

print('Start..')
nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    print( "Found devices: " + str( bdaddr ) )
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print("found target bluetooth device with address ", target_address)
else:
    print("could not find target bluetooth device nearby")"""

"""import bluetooth

bd_addr = "B4:86:55:59:A2:E9"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()"""

from bluetooth import *

addr = "B4:86:55:59:A2:E9"

# search for the SampleServer service
uuid = "977df3a1-93f2-4c19-91c5-d7d4ed8107e8"
service_matches = find_service( uuid = uuid, address = addr )

if len(service_matches) == 0:
    print("couldn't find the SampleServer service =(")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s port %s" % (name, host, port))

# Create the client socket
sock=BluetoothSocket( RFCOMM )
sock.connect((host, port))
print( 'CIAOOONEEEEEEEEE' )
print('RESULT: ' + str(inquiry_manager.device_inquiry_with_with_rssi(sock)))

print("connected.  type stuff")
while True:
    data = input()
    if len(data) == 0: break
    print("Try to send data: " + str(data))
    sock.send(data + "\n")

sock.close()
