import bluetooth
import os

from dotenv import load_dotenv

load_dotenv()

class BluetoothConnection():

    appName = os.getenv('BLUETOOTH_SERVER_APP_NAME');
    appUUID = os.getenv('DEVICE_ID');

    @staticmethod
    def initBluetoothConnection():

        if os.getenv('DEVICE_ID') is None:
            raise Exception('DEVICE_ID not found')

        if os.getenv('BLUETOOTH_SERVER_APP_NAME') is None:
            raise Exception('BLUETOOTH_SERVER_APP_NAME not found')

        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.bind(("", bluetooth.PORT_ANY))
        server_sock.listen(1)
        port = server_sock.getsockname()[1]

        bluetooth.advertise_service(server_sock, BluetoothConnection.appName, service_id=BluetoothConnection.appUUID,
                                    service_classes=[BluetoothConnection.appUUID, bluetooth.SERIAL_PORT_CLASS],
                                    profiles=[bluetooth.SERIAL_PORT_PROFILE],
                                    # protocols=[bluetooth.OBEX_UUID]
                                    )

        print(("Waiting for connection on RFCOMM channel", port))
        return server_sock