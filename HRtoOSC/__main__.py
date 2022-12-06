import threading
import time
import sendmessage
import server
from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtCore import QTimer, pyqtSignal, pyqtSlot


class Ui(QtWidgets.QMainWindow):
    # Declare the signal that will be emitted when the timer times out
    timeout = pyqtSignal()

    def __init__(self):
        super(Ui, self).__init__()

        # Load the UI file
        uic.loadUi('MainWindow.ui', self)

        # Create a timer object
        self.timer = QTimer(self)
        # Connect the timer's timeout signal to the update_buttons method
        self.timeout.connect(self.update_buttons)
        # Set the timer to run every 100 ms
        self.timer.start(100)

        self.startButton.clicked.connect(self.startButtonPressed)
        # Emit the timeout signal every 100 ms to call the update_buttons method
        self.timer.timeout.connect(self.timeout)
        self.timer.timeout.connect(self.checkPort)

    @pyqtSlot()
    def update_buttons(self):
        # Check the value of serverRunning and enable or disable the buttons accordingly
        if not serverRunning:
            self.startButton.setEnabled(True)
            self.stopButton.setEnabled(False)
        else:
            self.startButton.setEnabled(False)
            self.stopButton.setEnabled(True)

    @pyqtSlot()
    def startButtonPressed(self):
        global serverRunning
        global portInput
        if 1000 < portInput < 9999 and not portInput == 9000 and not portInput == 9001:
            print("Debug: Valid Port")
        serverRunning = True
        print("startButtonPressed called, serverRunning is now {}".format(serverRunning))

    def checkPort(self):
        # Get the inputted port number from the portInput text box
        port_input = 0000

        # Check if the port number is valid (i.e. in the range 1000-9999)
        if 1000 <= port_input <= 9999:
            # If the port number is valid, set the text of the console label to indicate that the server is running
            # on that port
            self.console.setText("Server is now running on port {}".format(port_input))
        else:
            # If the port number is not valid, set the text of the console label to indicate that an invalid port was
            # entered
            self.console.setText("Please enter a valid port number in the range 1000-9999")


def bufferHold():
    while True:
        if serverRunning:
            pass


# Define and initialize the GUI for the program
def loadGUI():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    # Call the show() method to make the window visible
    window.show()
    app.exec()


def sendHeartRate():
    while serverRunning:
        time.sleep(1)
        sendmessage.sendHeartRate(server.write_hr)


if __name__ == "__main__":
    serverRunning = False
    portInput = 0000

    runGUI = threading.Thread(target=loadGUI, daemon=True)  # GUI Thread
    runGUI.start()

    sendHeart = threading.Thread(target=sendHeartRate, daemon=True)  # TEMP
    sendHeart.start()

    while True:
        time.sleep(1)
