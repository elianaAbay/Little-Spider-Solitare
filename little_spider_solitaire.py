'''
Name: Eliana Assefa
CSC 201
Programming Project 4

This program plays a version of Little Spider Solitaire. In this
version the foundation piles of two red aces and two black kings
are created when the game begins. The eight tableau piles are in
one horizontal line. At any time, cards can be moved from the
tableau to the foundation piles or to another tableau, as long as
it is a valid move. One point is earned for every valid move to
a foundation pile.

Document Assistance (who and what or declare no assistance): I recived help from Professor Mueller on organization and structure. 

'''

from board import *
from button import *
from deck import *
from card import *
import time
import math

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 500

def displayDirections():
    """
    Gives the directions for Skip 3 Solitaire. The "Click to begin" button
    must be clicked to continue to the game.

    """
    win = GraphWin("Directions", 700, 600)
    win.setBackground("white")
    string = ("Welcome to Little Spider Solitaire\n\n"
                "The objective is to get all cards\n"
                "into the foundation piles which are built\n"
                "sequentially from cards of the same suit.\n\n"
                "The top card in any tableau can be moved\n"
                "either to a foundation pile, to another\n"
                "tableau if its rank is one above or\n"
                "below the tableau's current top card, or\n"
                "moved to an empty tableau.\n\n"
                "No more moves? Click the stock pile to get\n"
                "eight more cards.\n\n"
                "Good luck!")
    directions = Text(Point(win.getWidth()/ 2, win.getHeight()/2), string)
    directions.setSize(16)
    directions.draw(win)
    startButton = Button(Point(350, 525), 120, 40, "Click to Begin")
    startButton.draw(win)
    startButton.activate()
    click = win.getMouse()
    while not startButton.isClicked(click):
        click = win.getMouse()
    win.close()

def setUpGame():
    '''
    Creates the window with a start button, the tableaus, the stock pile, the
    foundation, and the label for scoring an Aces Up solitaire game. When the
    start button is clicked one card is dealt to each tableau and the button
    is renamed Quit.
    
    Returns:
    the window where the game will be played, the board managing the cards,
    the button now labeled Quit, and the scoring label.
    '''
    window = GraphWin('Little Spider Solitaire', WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('lightgreen')
    
    board = LittleSpiderBoard(window)
    
    button = Button(Point(675, 50), 80, 40, "Start")
    button.draw(window)
    button.activate()
    
    scoreLabel = Text(Point(70, 450), "Score: 0")
    scoreLabel.setSize(16)
    scoreLabel.draw(window)
    
    click = window.getMouse()
    while not button.isClicked(click):
        click = window.getMouse()
    
    button.setLabel("Quit")
    
    board.dealFromStock(window)
    return window, board, button, scoreLabel

def playGame(window, board, button, scoreLabel):
    '''
    Plays the Spider solitaire game enforcing the rules
    
    Params:
    window (GraphWin): the window where the game is played
    board (LittleSpiderBoard): the board managing the cards
    button (Button): the button to click to end the game
    scoreLabel (Text): the label showing the game score as the game progresses
    '''
    #getting a click and then getting another clock to compare the cards to other card. how to get car(get card at point())
    #get the cardatpoint to get the card ("they have to be one apart in rank") take the sumbruct and then asbulute value of the differnce
    #same suit and black card one rank lower if its a red card one rank higher (*method called is red(to know if its a red foundation)* CLICK ON TABLEOU IF ITS ANYWHERE ELSE WE ONT DO ANYTHING
    # DONT DO ANYTHING IN THE FOUNDATUON CLICK OR STOCK PILE_ (IS POINT IN STOCK" THEN DEAL HAVE AN OBJECT OF THAT (DO BOARD.)
   
    
    score = 'Score: '
    count = 0
    click = window.getMouse()
    while not button.isClicked(click):
        
        if board.isPointInStockCard(click) and not board.isStockEmpty():
            board.dealFromStock(window)
        else:
            if board.isPointInTableauCard(click):
                card_FirstPoint = board.getCardAtPoint(click)
                card_rank = card_FirstPoint.getRank()
            
                another_click = window.getMouse()
                if board.isPointInTableauCard(another_click):
                    card_SecondPoint = board.getCardAtPoint(another_click)
                    card_two_rank = card_SecondPoint.getRank()
                    difference = abs(card_rank - card_two_rank)
               
                
                    if (difference == 1 ) or (difference == 12):
                        board.moveCardToAnotherTableauPile(card_FirstPoint, another_click, window)
                        
                elif board.isPointInEmptyTableau(another_click):
                    board.moveCardToAnotherTableauPile(card_FirstPoint, another_click, window)
                        
                        
                elif board.isPointInFoundationCard(another_click):
                    card_SecondPoint = board.getCardAtPoint(another_click)
                    card_two_rank = card_SecondPoint.getRank()
                    difference = abs(card_rank - card_two_rank)
                    
                    if  card_FirstPoint.getSuit() == card_SecondPoint.getSuit() and difference == 1:
                        count = count + 1
                        scoreLabel.setText(f'{score}{count}')
                        
                        board.moveCardToFoundationPile(card_FirstPoint, another_click, window)       
        

        click = window.getMouse()   
        
            
        
       
    
     
    
    
 
def flashingResultDisplay(window, result):
    '''
    Flashes text in the Graphics window
    
    Params:
    window (GraphWin): the window that will display the flashing text
    result (str): the String that will flash in the window
    '''
    resultText = Text(Point(300, 450), result)
    resultText.setSize(32)
    resultText.setTextColor('red')
    resultText.draw(window)
    for i in range(20):
        if i % 2 == 0:
            resultText.undraw()
        else:
            resultText.draw(window)
        time.sleep(.2)
    
def main():
    displayDirections()
    
    window, board, button, scoreLabel = setUpGame()
    
    playGame(window, board, button, scoreLabel)
    
    if board.isWin():
        result = 'Winner!'
    else:
        result = 'Loser :('
    flashingResultDisplay(window, result)
    
    time.sleep(2)    
    window.close()

if __name__ == '__main__':
    main()