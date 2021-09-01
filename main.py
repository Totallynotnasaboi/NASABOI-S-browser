import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.browser = QWebEngineView()
    self.browser.setUrl(QUrl('https://nasa-boi.ga'))
    self.setCentralWidget(self.browser)
    self.showMaximized()

    #navbar
    navbar = QToolBar()
    self.addToolBar(navbar)

    back_btn = QAction('Back', self)
    back_btn.triggered.connect(self.browser.back)
    navbar.addAction(back_btn)

    forward_btn = QAction('Forward', self)
    forward_btn.triggered.connect(self.browser.forward)
    navbar.addAction(forward_btn)

    reload_btn = QAction('Reload', self)
    reload_btn.triggered.connect(self.browser.reload)
    navbar.addAction(reload_btn)


app = QApplication(sys.argv)
QApplication.setApplicationName('Nasa Boi Browser')
QApplication.setApplicationVersion('1.0.0')
window = MainWindow()
app.exec_()