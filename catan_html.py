#!/usr/bin/env python3
###############################################################################
#
#   Title   : catan.py
#   Author  : Carolyn Mason and Scott Mende
#   Date    : 7/6/15
#   Synopsis: Settlers of Catan
#
#   Usage   : python3 catan.py
#   Output  : 
#   example : 
# 
###############################################################################

import os,sys
# import cherrypy
import numpy as np
import random

class TheGame(object):
   def index(self):
      # Set up the main html string
      self.html = ""
      self.html += "<h1>This is Catan</h1>"
      self.html += "<b>7/6/15</b>"
      
      # Set up the js
#       self.html += "<script>type='text/javascript' src='jsFile.js'</script>"
#       self.html += '<input type="button" onclick="popup()" value="Click Me!">'

#       self.html += "<script>$('.tile1').click(function()) {"
#       self.html += "alert('hmmmmmm');"
#       self.html += "});</script>"
      
      # Create the board
      self.html += '<span id="hex"></span>'
      self.html += self.createBoard()
      
      # Create the pieces
      
      
      # Return html
      return self.html
      
   def createBoard(self):
      # Initiallize
      board = '' 
      self.numTiles = 19
      
      # Randomize the tiles and numbers
      [resources,spot] = self.generateResources()
      numbers = self.generateNumbers(spot)
      [xpos,ypos] = self.generatePositions()
      
      # Create the tiles and their attributes    
      board += "<style>"
      for tile in range(0,self.numTiles):
         board += self.createHex('tile'+str(tile),resources[tile],xpos[tile],ypos[tile])
         board += self.createNumber('num'+str(tile),xpos[tile],ypos[tile])
      board += "</style>"
      
      # Add the tiles to the board
      for tile in range(0,self.numTiles):
         board += '<div class="tile'+str(tile)+' onetile'+str(tile)+'">'
         board += '<div class="num'+str(tile)+' onenum'+str(tile)+'">'
         board += str(numbers[tile])+'</div>'
      
      return board
   
   def createHex(self,name,resource,xpos,ypos):
      # The hex
      hex = '.'+name+'{'
      hex += '  position: relative;'
      hex += '  width: 100px; '
      hex += '  height: 57.7366666667px;'
      hex += '  background-color: '+resource+';'
      hex += '  margin: 28.8666666667px 0;'
      hex += '}'
      hex += '.'+name+':before,'
      hex += '.'+name+':after {'
      hex += '  content: "";'
      hex += '  position: absolute;'
      hex += '  width: 0;'
      hex += '  border-left: 50px solid transparent;'
      hex += '  border-right: 50px solid transparent;'
      hex += '}'
      hex += '.'+name+':before {'
      hex += '  bottom: 100%;'
      hex += '  border-bottom: 28.8666666667px solid '+resource+';'
      hex += '}'
      hex += '.'+name+':after {'
      hex += '  top: 100%;'
      hex += '  border-top: 28.8666666667px solid '+resource+';'
      hex += '}'
      
      # Position the hex
      hex += '.one'+name+' {'
      hex += '  top: '+str(xpos)+'px;'
      hex += '  left: '+str(ypos)+'px;'
      hex += '}'

      # Return the tile
      return(hex)
   
   def createNumber(self,name,xpos,ypos):
      # Add the circle
      num = ''
      num += '.'+name+'{ width: 30px;'
      num += '  height: 30px;' 
      num += '  background: white;' 
      num += '  -moz-border-radius: 15px;'
      num += '  -webkit-border-radius: 15px;'
      num += '  border-radius: 15px;'
      num += '}'
      
      # Position the circle
      num += '.one'+name+' {'
      num += '  top: '+str(xpos)+'px;'
      num += '  left: '+str(ypos)+'px;'
      num += '}'
      
      return(num)
   
   def choosePlayers(self):
      pass
   
   def generateNumbers(self,desert_spot):
      # Generate numbers 2->12
      numbers = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
      random.shuffle(numbers)
      numbers = numbers[0:desert_spot] + [-1] + numbers[desert_spot::]
      return(numbers)
   
   def generatePositions(self):
      # Generate Hex positions
      xpos = [50,0,0,86.6666667,0,0,0,86.6666667,0,0,0,0,86.6666667,0,0,0,86.6666667,0,0]-59*np.ones(19)
      ypos = [200,100,100,-250,100,100,100,-350,100,100,100,100,-350,100,100,100,-250,100,100]
      return(xpos,ypos)
   
   def generateResources(self):
      # Create the resources: wheat,wood,sheep,rock,brick
      allColors = ['#DDFF22','#004400','#00FF00','#808074','#E73204']
      desert = '#F3F4A7'
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

if __name__ == '__main__':
   #    cherrypy.quickstart(TheGame())
   output = TheGame()
   html_board = output.index()
   
   # Create an output text file
   text_file = open("board.html", "w")
   text_file.write(html_board)
   text_file.close()
   
   # Finished
   print('done')
 
   
   
   
   
   
   
   
   
   
   
