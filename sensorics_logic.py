import sys
import datetime
from PyQt6 import QtWidgets, QtCore

from ui.converted import sensorics_logger_ui


class sensorics_logic(QtWidgets.QFrame, sensorics_logger_ui.Ui_Form):
    def __init__(self, parent, **kw):

        super().__init__(parent)
        self.setupUi(self)  

        self.running = False
        self.StartStopBtn.clicked.connect(self.on_StartStop_clk)
        self.update_SSBtn_style()

        self.poll_time = 100
        self.poll_timer = QtCore.QTimer()
        self.poll_timer.timeout.connect(self.poll_func)

    def poll_func(self):        
        print(self.get_time() + "Polled!")
        self.logTE.append(self.str_to_colored(self.get_time()) + "Logged!")
        pass

    def on_StartStop_clk(self):
        if self.running:
            self.poll_timer.stop()
        else:
            self.poll_timer.start(self.poll_time)

        self.running = not self.running
        self.update_SSBtn_style()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Space:
            self.on_StartStop_clk()


    def update_SSBtn_style(self):
        if self.running:
            self.StartStopBtn.setText("Стоп")
            self.StartStopBtn.setStyleSheet("background-color:red")
        else:
            self.StartStopBtn.setText("Старт")
            self.StartStopBtn.setStyleSheet("background-color:green")        


    def str_to_colored(self, userInput, color="red"):
        return f"<span  style='color:{color}'>{userInput}</span >"

    def get_time(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]+" "

if __name__ == "__main__":
    class MainWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            
            self.setWindowTitle("Sensorics widget")
            self.sensorics_widget = sensorics_logic(self)
            self.setCentralWidget(self.sensorics_widget)

        def closeEvent(self, event):
            pass


    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()