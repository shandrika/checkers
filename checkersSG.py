from graphics import*

#Square Variable
sqSz = 50

#Create Window
window = GraphWin("Checkers",sqSz*10,sqSz*10)
window.setCoords(0,0,sqSz*10,sqSz*10)


#Create Square Function
def run_square(row,column,color):
    sQ = Rectangle (Point(sqSz*(row+1),sqSz*(column+1)),Point(sqSz*(row+2), sqSz*(column+2)))
    sQ.setFill(color)
    sQ.draw (window)

userC = input ("what colour you want bro?")
sqC = userC

for c in range (8):
    for i in range (8):
        if (c+1 * i) % 2 == 0:
            sqC = userC
        else :
            sqC = "black"
        
        run_square(i,c,sqC)


