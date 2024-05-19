import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Django + PyQt Application')
        
        self.browser = QWebEngineView()
        self.browser.setUrl('http://127.0.0.1:8000/')
        
        self.setCentralWidget(self.browser)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
