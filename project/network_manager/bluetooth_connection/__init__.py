import bluetooth

class BluetoothConnection():

    appName = 'Bluetooth_server_app'
    appUUID = '94f39d29-7d6d-437d-973b-fba39e49d4ee'

    @staticmethod
    def initBluetoothConnection():
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.bind(("", bluetooth.PORT_ANY))
        server_sock.listen(1)
        port = server_sock.getsockname()[1]

        bluetooth.advertise_service(server_sock, BluetoothConnection.appName, service_id=BluetoothConnection.appUUID,
                                    service_classes=[BluetoothConnection.appUUID, bluetooth.SERIAL_PORT_CLASS],
                                    profiles=[bluetooth.SERIAL_PORT_PROFILE],
                                    # protocols=[bluetooth.OBEX_UUID]
                                    )

        print("Waiting for connection on RFCOMM channel", port)
        return server_sock