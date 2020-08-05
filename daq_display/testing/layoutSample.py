from PyQt5 import QtWidgets 
import pyqtgraph as pg

'''
Name: Hamlin Liu
6/28/2020

Sample layout of the GUI

made according to 
https://docs.google.com/drawings/d/1nj8GllTTlC7pYvAv4aKbgEYh7g_emlMcZ6tk-5v_3Lg/edit
'''

def widgets() -> QtWidgets.QWidget:
    w = QtWidgets.QWidget()
    btn = QtWidgets.QPushButton('press me')
    text = QtWidgets.QLineEdit('enter text')
    listw = QtWidgets.QListWidget()
    plot = pg.PlotWidget()




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widgets()