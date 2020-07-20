#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QToolTip,QPushButton,
                             QApplication,QMessageBox,
                             QDesktopWidget,QMainWindow,
                             QAction, qApp,QTextEdit, QFileDialog)
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication



class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        QToolTip.setFont(QFont('SansSerif', 10))#размер подсказки
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)
        self.textEdit.setToolTip('Введите свой <b>текст</b> ')#подсказка на рабочей области

        btn = QPushButton('Очистить', self)
        #btn.clicked.connect(QCoreApplication.instance().quit) #закрытие приложение при нажатии кнопки
        btn.setToolTip('This is a <b>QPushButton</b> widget')#подсказка на кнопке
        btn.resize(btn.sizeHint())#рекомендуемый размер кнопки
        #btn.resize(200,50)#размер кнопки
        btn.move(0,350)#расположение кнопки
        btn.clicked.connect(self.textEdit.clear)
        #self.setGeometry(300, 300, 300, 220)#расположение и размер окна
        self.resize(300,400)#при центрировании
        self.center()#применение метода прописанного дальше
        self.setWindowTitle('Название')
        self.setWindowIcon(QIcon('image.png'))
        #self.statusBar().showMessage('Ready')#статусбар не работает при Example(Qwidget) 
        exitAction = QAction(QIcon('image.png'), '&Exit', self)#строка меню
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
 
        self.statusBar()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(exitAction)
        #toolbar = self.addToolBar('Exit')
        #toolbar.addAction(exitAction)
        self.show()
    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):#сообщение при закрытии окна

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
