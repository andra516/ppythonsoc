# -*- coding: utf-8 -*-
# pylint: disable=E0012, fixme, invalid-name, no-member, R0913, W0613, W0622, E0611, W0603, R0902, R0903, C0301

import sys
import numpy as np
from scipy.integrate import odeint
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MyMainWindow(QMainWindow):
    ''' the main window potentially with menus, statusbar, ... '''

    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.move(400, 300)
        central_widget = MyCentralWidget(self)
        self.setCentralWidget(central_widget)
        self.setWindowTitle('WHACK-A-MOLE')

class MyCentralWidget(QWidget):
    ''' everything in the main area of the main window '''

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        # define figure canvas
        self.mpl_widget = MyMplWidget(self.main_window)
        # place MplWidget into a vertical box layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.mpl_widget)  # add the figure
        # use the box layout to fill the window
        self.setLayout(vbox)


class MyMplWidget(FigureCanvas):
    ''' both a QWidget and a matplotlib figure '''

    def __init__(self, main_window, parent=None, figsize=(4, 4), dpi=100):
        self.main_window = main_window
        self.fig = plt.figure(figsize=figsize, dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        
        self.plot_background()

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        self.cid_press = self.fig.canvas.mpl_connect('button_press_event', self.on_mouse_press)
        self.cid_release = self.fig.canvas.mpl_connect('button_release_event', self.on_mouse_release)
        self.cid_move = self.fig.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        
        self.mole_timer = QTimer()
        self.mole_timer.setInterval(1000)
        self.mole_timer.timeout.connect(self.move_mole)
        self.mole_timer.start()      
        

    def plot_background(self):
        '''
        Plots the background (and mole)
        background array of 9 holes
        '''
        self.fig.clf()
        self.ax = self.fig.add_subplot(1, 1, 1)
        
        self.holes = []
        
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                hole, = self.ax.plot(x, y, color='k', markersize=80, marker='o', markeredgecolor='grey', markeredgewidth=2)
                self.holes.append(hole)

        self.mole, = self.ax.plot(np.random.randint(-1, 2), np.random.randint(-1, 2), marker='$mole$', color='brown', markersize=40)
        self.mole.set_pickradius(40)
        
        self.ax.set_xlabel('$x$')
        self.ax.set_ylabel('$y$')
        self.ax.set_xlim(-1.5, 1.5)
        self.ax.set_ylim(-1.5, 1.5)
        self.ax.set_aspect('equal')
        self.draw()

    def move_mole(self):
        '''
        moves the mole and replots the axes
        '''
        self.ax.draw_artist(self.ax.patch)                              # <-- redraw the plotting area of the axis
        self.mole.set(xdata=np.random.randint(-1,2), ydata=np.random.randint(-1, 2), marker='$mole$')
                
        for hole in self.holes:
            
            self.ax.draw_artist(hole)
            
        self.ax.draw_artist(self.mole)     
        
        self.fig.canvas.update()                                        # <-- update the figure
        self.fig.canvas.flush_events()                                  # <-- ensure all draw requests are sent out

    def on_mouse_move(self, event):
        # print('mouse moving')
        # print(event.xdata, event.ydata)
        pass

    def on_mouse_press(self, event):
        # print('mouse press event')
        # print(event.xdata, event.ydata)
        
        
        #### check whether the mouse is over the mole, if so, splat :)
        if self.mole.contains(event)[0]:
            self.mole.set(marker='$splat$')
            
            for hole in self.holes:
                self.ax.draw_artist(hole)
            
            self.ax.draw_artist(self.mole)
            self.fig.canvas.update()
            self.fig.canvas.flush_events()
        
        
        else:
            pass
        
    def on_mouse_release(self, event):
        pass


app = None


# pylint: disable=C0111
def main():
    global app
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec()


if __name__ == '__main__':
    main()
