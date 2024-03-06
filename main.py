import sys
from PyQt6 import QtWidgets

from ui.converted import ADCS_connector_main_wind_ui
from sensorics_logic import sensorics_logic


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем

    class MainWindow(QtWidgets.QMainWindow, ADCS_connector_main_wind_ui.Ui_MainWindow):
        def __init__(self):
            # Это здесь нужно для доступа к переменным, методам
            # и т.д. в файле design.py
            #
            super().__init__()
            self.setupUi(self)  # Это нужно для инициализации нашего дизайна
            #
            self.sensorics_widget = sensorics_logic(self)
            self.sensorics_layout.addWidget(self.sensorics_widget, 0, 0, 1, 1)

        def closeEvent(self, event):
            pass

    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # os.environ["QT_SCALE_FACTOR"] = "1.0"
    #
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()
    app.exec()