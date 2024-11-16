from PyQt6.QtWidgets import QApplication, QMainWindow
from MainWindowEx import MainWindow

app=QApplication([])
myWindow= MainWindow()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()