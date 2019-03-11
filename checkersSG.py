from graphics import*

#Square Variable
sqSz = 60

#Create Window
window = GraphWin("Checkers",sqSz*10,sqSz*10)
window.setCoords(0,0,sqSz*10,sqSz*10)

#Create Square
sQ = Rectangle (Point(sqSz, sqSz),Point(sqSz*2, sqSz*2))
sQ.draw (window)
