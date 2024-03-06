import sys
from PyQt6 import QtWidgets

from ui.converted import sensorics_logger_ui


class sensorics_logic(QtWidgets.QFrame, sensorics_logger_ui.Ui_Form):
    def __init__(self, parent, **kw):

        super().__init__(parent)
        self.setupUi(self)  


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