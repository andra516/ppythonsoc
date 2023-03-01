# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:15:56 2021

@author: henry

Poynting's Python Society: Workshop on GUIs 24-03-2022

Here you'll be creating a DVD bounce animation by periodically updating the position 
of a DVD marker and refreshing the graph.


"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class Logo():
    
    '''
    Logo class stores the position and velocity of the moving logo, and calculates the position 
    of the Logo at the next time step :)    
    '''
    
    def __init__(self):
        self.pos = np.random.rand(1, 2) # randomly initialise the position of the Logo inside the frame
        self.vel = np.random.randn(1, 2)*0.2 # same for velocities
        
    def update_position(self, dt):
        '''
        Calculates the position of the centre of the DVD logo after a time step - checking 
        whether the marker has exceeded the frame boundary.
        '''
        self.pos  = self.pos + self.vel * dt # this calculates the updated position of the logo 
        
        if self.pos[0,0] < 0 or self.pos[0, 0] > 1: # CHECK IF OUTSIDE SIDE WALLS
            self.vel[0, 0] = -self.vel[0,0] # if so - reverse x component of velocity
        if self.pos[0, 1] < 0 or self.pos[0,1] > 1: # CHECK IF OUTSIDE TOP/BOTTOM WALLS
            self.vel[0, 1] =-self.vel[0,1] # if outside - reverse y component of velocity 

class MyMainWindow(QtWidgets.QMainWindow):
    '''
    Class defining the main window that our widget will sit within
    '''
    
    def __init__(self):
        super().__init__() # calls initialiser of parent class QMainWindow - this makes sure MyMainWindow has all the functionalities we need
        self.resize(900, 900) # resize the main window
        self.move(400, 50) # move it slightly
        central_widget = MyCentralWidget(self) # create instance of MyCentralWidget - the widget that will hold the matplotlib figure
        self.setCentralWidget(central_widget) # set the central widget of the window to be to MyCentralWidget
        self.setWindowTitle('DVD Logo Bounce')
        
class MyCentralWidget(QtWidgets.QWidget):
    '''
    Class defining the central widget that will hold the layout and matplotlib figure.
    '''
    
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.mpl_widget = MyMplWidget(self.main_window) # creates instance of MyMplWidget class (below)
        vbox = QtWidgets.QVBoxLayout() # setting up the layout
        vbox.addWidget(self.mpl_widget) # of the gui
        self.setLayout(vbox) 
 
class MyMplWidget(FigureCanvas):
    '''
    Class for our matplotlib figure which will be the frame the DVD logo bounces around in.
    
    Inherits FigureCanvas - a class for displaying matplotlib figures to GUIs. Therefore, MyMplWidget 
    has all the functionalities of the 'FigureCanvas' class (whatever that might be). (come and talk to me
                                                                                       about inheritance if you
                                                                                       want to know more :))
    '''

    def __init__(self, main_window, figsize=(4,4), dpi=100):
        self.main_window = main_window
        # create the figure
        self.fig = plt.figure(figsize=figsize, dpi=dpi)
        
        # you can safely ignore these next 3 lines if you like, they just make sure the figure will stretch/compress in the right way
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        # the next three lines ensure we can handle mouse press, mouse release and mouse move 'events'
        self.cid_press = self.fig.canvas.mpl_connect('button_press_event', self.on_mouse_press)
        self.cid_release = self.fig.canvas.mpl_connect('button_release_event', self.on_mouse_release)
        self.cid_move = self.fig.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
            
        self.initial_plot()
        
        
    def initial_plot(self):
        ''' 
        Plots the first iteration in the animation - should just be DVD logo on a black background :)        
        '''
        self.ax = self.fig.add_subplot(1, 1, 1)
        
        # self.ax.set_xlim([0, 1])
        # self.ax.set_ylim([0, 1])
        # self.ax.set_facecolor('black')
    
        # self.line, = self.ax.plot(0.5, 0.5, color='c', marker='$DVD$', markersize=60)
        

    def on_mouse_press(self, event):
        pass

    def on_mouse_release(self, event):
        pass
    
    def on_mouse_move(self, event):
        pass
    
app = None

def main():
    global app
    app = QtWidgets.QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()