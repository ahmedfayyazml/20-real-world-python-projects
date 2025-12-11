from PyQt6.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QWidget,
    QGridLayout, QLineEdit, QPushButton, QMainWindow
)
from PyQt6.QtGui import  QAction
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Managment System")


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())