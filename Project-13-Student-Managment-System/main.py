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

        file_menu_item = self.menuBar().addMenu("&file")
        help_menu_item = self.menuBar().addMenu("&help")

        add_student_action = QAction("Add Student")
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About")
        help_menu_item.addAction(about_action)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())