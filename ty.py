from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os
import sys
import time
app = QtWidgets.QApplication(sys.argv)
ex = uic.loadUi("window1.ui")
ex2 = uic.loadUi("recovery1.ui")
ex3= uic.loadUi("syst.ui")
ex1= uic.loadUi("dilog1.ui")
ex4= uic.loadUi("killproc.ui")
def Check_the_right():
    vlue=ex.code_line.toPlainText()
    if vlue == "qwerty":
        ex.close()
        ex2.show()
    else:
        print(vlue)
        ex1.show()
def recovery_process():
    if ex2.checd.isChecked():
        print("suk")
        completed = 0
        l=[i for i in range(101)]
        time.sleep(10)
        ex2.label_7.setText("Подготовка системного диска...")
        ex2.label_8.setText("Восстановление...")
        ex2.label_9.setText("Удаление барьеров...")
        ex2.label_10.setText("Починка загрузочного сектора...")
        ex2.Recovery_button.setEnabled(False)
        ex2.recbutt.setEnabled(True)
        while completed < 100:
            completed += 1
            if completed in l:
                int(completed)
                ex2.progress.setValue(completed)
            else:
                print(completed)
    else:
        ex3.show()
def kill_pc():
    ex4.show()
imer=QtCore.QTimer()
imer.setInterval(5000)
imer.timeout.connect(kill_pc)
imer.start()
ex.Butt.clicked.connect(Check_the_right)
ex1.exit_but.clicked.connect(ex1.close)
ex2.Recovery_button.clicked.connect(recovery_process)
ex2.recbutt.clicked.connect(app.quit)
ex3.ok.clicked.connect(ex3.close)
ex.show()
sys.exit(app.exec_())
