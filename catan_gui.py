#!/usr/bin/env python3
###############################################################################
#
#   Title   : catan.py
#   Author  : Carolyn Mason 
#   Date    : 7/6/15
#   Synopsis: Settlers of Catan
#
#   Usage   : python3 catan.py
#   Output  : 
#   example : 
# 
###############################################################################

import sys
import os
from PyQt4 import QtGui, QtCore
# import cherrypy
import numpy as np
import random
import math
from PIL import Image, ImageDraw

class TheGame(QtGui.QApplication):
   """This is a main application."""
   def __init__(self):
      QtGui.QApplication.__init__(self, sys.argv)
                         
      self.mainWindow = MainWindow()                                                                  
      #  Show this window
      self.mainWindow.show()
   
class MainWindow(QtGui.QMainWindow):
   def __init__(self):
      QtGui.QMainWindow.__init__(self)
      
      # Initialize this main window
      self.setWindowTitle('Settlers of Catan')
      self.setMinimumSize(1100,650)
      
      # self.mainLayout = Dashboard.defineLayout(self)
      self.mainLayout = QtGui.QVBoxLayout()
      self.mainWidget = QtGui.QWidget()
      self.mainWidget.setLayout(self.mainLayout)
      self.setCentralWidget(self.mainWidget)
      
      # Create the main layouts
      hexLayout = QtGui.QVBoxLayout()
      r1Layout = QtGui.QHBoxLayout()
      r2Layout = QtGui.QHBoxLayout()
      r3Layout = QtGui.QHBoxLayout()
      r4Layout = QtGui.QHBoxLayout()
      r5Layout = QtGui.QHBoxLayout()
      allRows = [r1Layout,r2Layout,r3Layout,r4Layout,r5Layout]
      
      # Create the board    
      # Set arrays for game play
      self.numTiles = 19 
      numbers = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
      rowOrg = [3,4,5,4,3]
      
      # Create the resources: wheat,wood,sheep,rock,brick
      allColors = ['#DDFF22','#004400','#00FF00','#808074','#E73204']
      desert = '#F3F4A7'
      
      # Randomize the tiles and numbers
      [resources,spot] = self.generateResources(allColors,desert)
      numbers = self.generateNumbers(numbers,spot)
      
      # Create the tiles and their attributes  
      spot = 0
      for row,numInRow in enumerate(rowOrg):
         allRows[row].addStretch(4)
         for col in range(0,numInRow):
            tileButton = HexButton()
            tileButton.setText(str(numbers[spot]))
            tileButton.setColor(str(resources[spot]))
            allRows[row].addWidget(tileButton)
            spot += 1
         
         # Add the tiles to the board
         allRows[row].addStretch(4)
         hexLayout.addLayout(allRows[row])
      
      
      # add stuff to the main layout
      self.mainLayout.addLayout(hexLayout)
   
   def choosePlayers(self):
      pass
   
   def hexagonGenerator(self, edge_length, offset):
      # Generator for coordinates in a hexagon
      x, y = offset
      for angle in range(0, 360, 60):
         x += math.cos(math.radians(angle)) * edge_length
         y += math.sin(math.radians(angle)) * edge_length
         yield x, y
   
   def generateNumbers(self,numbers,desert_spot):
      # Generate numbers 2->12
      random.shuffle(numbers)
      numbers = numbers[0:desert_spot] + [' '] + numbers[desert_spot::]
      return(numbers)
   
   def generatePositions(self):
      # Generate Hex positions
      xpos = [50,0,0,86.6666667,0,0,0,86.6666667,0,0,0,0,86.6666667,0,0,0,86.6666667,0,0]-59*np.ones(19)
      ypos = [200,100,100,-250,100,100,100,-350,100,100,100,100,-350,100,100,100,-250,100,100]
      return(xpos,ypos)
   
   def generateResources(self,allColors,desert):
      # Create the resources: wheat,wood,sheep,rock,brick
      array = []
      for i in range(0,self.numTiles-1):
         array.append(allColors[i%5])
      
      # Add in the desert
      array.append(desert)
      
      # Shuffle the array
      random.shuffle(array)
      
      # Find the desert spot
      spot = array.index(desert)
      
      return(array,spot)

class HexButton(QtGui.QPushButton):
   size = 120
   x = (3**0.5 / 1.7)
   font = QtGui.QFont('Arial', size*0.15)
   font.setWeight(500)
   hexaPointsF = [QtCore.QPointF(size*0.5*x     , 0              ),
                  QtCore.QPointF(size*x         , size/4         ),
                  QtCore.QPointF(size*x         , size/2 + size/4),
                  QtCore.QPointF(size*0.5*x     , size           ),
                  QtCore.QPointF(0              , size/2 + size/4),
                  QtCore.QPointF(0              , size/4         )]
#    hexaPointsF = [QtCore.QPointF(size/4,0),
#                   QtCore.QPointF(size/4 + size/2,0),
#                   QtCore.QPointF(size,size*0.5*x),
#                   QtCore.QPointF(size/4 + size/2,size*x),
#                   QtCore.QPointF(size/4,size*x),
#                   QtCore.QPointF(0,size*0.5*x)]
   hexaF = QtGui.QPolygonF(hexaPointsF)

   def __init__(self, parent=None):
      QtGui.QPushButton.__init__(self)
      self.setStyleSheet("border: none;")
      
      self.setMinimumSize(HexButton.size, HexButton.size)
      self.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
      self.setFlat(True)
      
   def setText(self, text):
      self.text = text
      self.update()

   def setColor(self,hex):
      self.color = QtGui.QColor(hex)
      self.update()
      
   def paintEvent(self, event):
      qp = QtGui.QPainter()
      qp.begin(self)
      opt = QtGui.QStyleOptionButton()
      self.initStyleOption(opt)
      self.style().drawControl(QtGui.QStyle.CE_PushButton, opt, qp, self)
      qp.end()
      painter = QtGui.QPainter()
      painter.begin(self)
      painter.setRenderHint(QtGui.QPainter.Antialiasing)
      painter.setPen(QtCore.Qt.NoPen)
      painter.setBrush(self.color)
      basePoly = QtGui.QPolygonF(HexButton.hexaF)
      painter.drawPolygon(basePoly)
      
      if self.text:
         pen_text = QtGui.QPen()
         painter.setPen(pen_text)
         painter.setFont(HexButton.font)
         painter.drawText(0, 0, HexButton.size, HexButton.size*HexButton.x, QtCore.Qt.AlignCenter, self.text)
         painter.end()
         
         
if __name__ == '__main__':
   # Launch the game
   DataMapApp = TheGame()
   DataMapApp.setApplicationName("Catan")
   returnCode = DataMapApp.exec_()
   DataMapApp.deleteLater()
   
   #  Start the application
   sys.exit(returnCode)
        
   # Finished
   print('done')
 
   
   
   
   
   
   
   
   
   
   
