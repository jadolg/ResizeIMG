from PyQt4 import QtGui
from Ui_MainWindow import Ui_MainWindow
from PyQt4.QtCore import pyqtSignature
from PIL import Image
from threading import Thread
import os

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    class resizeIMG(Thread):
        def __init__(self,fin,fout,x,y,opt):
            Thread.__init__(self)
            self.fin= fin
            self.fout= fout
            self.x= x
            self.y= y
            self.opt= opt

        def setLog(self,log):
            self.log= log

        def run(self):
            if self.opt == 'f':
                self.resizei(self.fin,self.fout,self.x,self.y)
            elif self.opt == 'd':
                self.resizedir(self.fin,self.fout,self.x,self.y)
            elif self.opt == 'dr':
                self.resizedirr(self.fin,self.fout,self.x,self.y)
            else:
                self.log.append('<font color=#FF0000>-> Seleccione correctamente la opcion de redimensionado</font>')
            self.log.append('***Proceso Terminado')


        def resizei(self,imageIN, imageOUT, x, y):
            """
            Cambia el tamano de una imagen
            """
            try:
                if os.path.isfile(imageIN):
                    im = Image.open(imageIN) # abre el archivo imagen
                    width, height = im.size
                    if width > height:
                        im = im.resize((x, y), Image.ANTIALIAS)
                    else:
                        im = im.resize((y, x), Image.ANTIALIAS)

                    im.save(imageOUT, 'jpeg', quality=80) # guarda la imagen
                    self.log.append('<font color=#0066FF>-> redimensionado '+ imageIN + '>' + imageOUT+'</font>')
                else:
                    self.log.append('<font color=#FF0000>-> error la ruta seleccionada ' + imageIN + ' no corresponde a un archivo</font>')
            except:
                self.log.append('<font color=#FF0000>-> error redimensionando ' + imageIN + '>' + imageOUT+'</font>')


        def resizedir(self,dirIN, dirOUT, x, y):
            """
            Redimensiona un directorio
            """
            try:
                os.mkdir(dirOUT)
            except:
                pass
            if os.path.isdir(dirIN):
                ficheros = os.listdir(dirIN)
                for i in ficheros:
                    if os.path.isfile(dirIN + "/" + i):
                        self.resizei(dirIN + "/" + i, dirOUT + "/" + i, x, y)
            else:
                self.log.append('<font color=#FF0000>-> error la ruta seleccionada ' + dirIN + ' no corresponde a un directorio</font>')

        def resizedirr(self,dirIN, dirOUT, x, y):
            """
            Redimensiona un directorio recursivamente
            """
            try:
                os.mkdir(dirOUT)
            except:
                pass

            if os.path.isdir(dirIN):
                ficheros = os.listdir(dirIN)
                for i in ficheros:
                    if os.path.isfile(dirIN + "/" + i):
                        try:
                            self.resizei(dirIN + "/" + i, dirOUT + "/" + i, x, y)
                        except:
                            pass
                    elif os.path.isdir(dirIN + "/" + i):
                        self.resizedirr(dirIN + "/" + i,dirOUT + "/" + i, x, y)
            else:
                self.log.append('<font color=#FF0000>-> error la ruta seleccionada ' + dirIN + ' no corresponde a un directorio</font>')



    def __init__(self):
        """Creates a MainWindows"""
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def on_checkBox_stateChanged(self):
        if self.checkBox.isChecked():
            self.lineEdit_2.setText(self.lineEdit.text())
            self.lineEdit_2.setReadOnly(True)
        else:
            self.lineEdit_2.setReadOnly(False)

    def on_lineEdit_textChanged(self):
        if self.checkBox.isChecked():
            self.lineEdit_2.setText(self.lineEdit.text())

    def on_xval_textChanged(self):
        self.yval.setText(str(int(int(self.xval.text())/1.33333333333333)))

    def on_pushButton_released(self):
        if self.lineEdit.text() and self.lineEdit_2.text() and self.xval.text() and self.yval.text():
            if self.archivo.isChecked():
                tt = self.resizeIMG(str(self.lineEdit.text()),str(self.lineEdit_2.text()),int(self.xval.text()),int(self.yval.text()),'f')
                tt.setLog(self.log)
                tt.start()
            elif self.directorio.isChecked():
                tt = self.resizeIMG(str(self.lineEdit.text()),str(self.lineEdit_2.text()),int(self.xval.text()),int(self.yval.text()),'d')
                tt.setLog(self.log)
                tt.start()
            else:
                tt = self.resizeIMG(str(self.lineEdit.text()),str(self.lineEdit_2.text()),int(self.xval.text()),int(self.yval.text()),'dr')
                tt.setLog(self.log)
                tt.start()
        else:
            self.log.append('<font color=#FF0000>-> error Faltan parametros necesarios</font>')
