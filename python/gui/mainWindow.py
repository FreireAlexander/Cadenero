from PySide6.QtCore import Qt
from PySide6.QtWidgets import  QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
import sys


class MainWindow(QMainWindow):
    """
    Main Window for the app
    """

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Cadenero")
        self.setGeometry(0,0,600,800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("Cadenero version 0.0.0-dev")
        self.layout.addWidget(self.label)

        self.central_widget.setLayout(self.layout)


    def run():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())