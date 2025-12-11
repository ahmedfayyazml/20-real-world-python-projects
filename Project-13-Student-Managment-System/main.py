from PyQt6.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QWidget,
    QGridLayout, QLineEdit, QPushButton, QMainWindow, QTableWidget
)
from PyQt6.QtGui import  QAction
import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Managment System")

        file_menu_item = self.menuBar().addMenu("&file")
        help_menu_item = self.menuBar().addMenu("&help")

        add_student_action = QAction("Add Student",self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About",self)
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id","Name","Course","Mobile"))
        self.setCentralWidget(self.table)

    def load_data(self):
        pass

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())