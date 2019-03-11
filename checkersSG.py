from graphics import*

#Square Variable
sqSz = 60

#Create Window
window = GraphWin("Checkers",sqSz*10,sqSz*10)
window.setCoords(0,0,sqSz*10,sqSz*10)

#Create Square Function
def run_square(row,column):
    sQ = Rectangle (Point(sqSz*(row+1),sqSz*(column+1)),Point(sqSz*(row+1), sqSz*(column +2)))                    
    sQ.draw (window)

