import serial

class com_ard():
    def __init__(self, parent):
        self.parent = parent
        print("ard created")


    def connect(self, port):
        try:
            self.ser = serial.Serial('/dev/cu.usbmodem141011', 115200)
            self.parent.connected = True
            print("connected to arduino on port : ", port)
            return True
        except Exception as e:
            print("Error connecting to Arduino: ", e)
            return False

    def send_message(self, message):
        self.ser.write(message)
        print(message)
