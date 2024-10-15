'''
Name: Eliana Assefa
CSC 201
Programming Project 4--Card Class

The Card class represents one standard poker card for a card game. Cards have a rank,
a suit, and an image. The card stores its position in a graphics window. It can be drawn and
undrawn in the graphics window.

Document Assistance (who and what or declare no assistance):



'''
from graphics2 import *
import time

class Card:
    # Add your methods above __eq__
    def __init__(self,filename):
        '''
        Initializes the suit, rank and image
        
        Params:
        fileName (string): name of the file which contains suit and rank of the card
        
        '''
         
        self.image = Image(Point(0, 0), filename)
         
        first = filename.split('/')
        first = first[-1]
        first = first.split('.')
        first = first[0]
        suit = first[-1]
        rank = first[:-1]
        
        self.rank = int(rank)
        self.suit = suit
         
    def getRank(self):
        '''
        Returns  the rank of the card.
        
        '''
        
        return self.rank
    
    def getSuit(self):
        '''
        Returns The suit of the card
        
        '''
        return self.suit
    
    def getImage(self):
        '''
        Returns The image of the card
        
        '''
        
        return self.image
    
    def draw(self, window):
        '''
        Draws the image on the window
        
        Params: window(GraphWin): window where the card will be drawn.
        '''
        
        self.image.draw(window)
        
    def undraw(self):
        '''
        undraws the card from the window
        
        '''
        self.image.undraw()
    
    def isRed(self):
        '''
        Checks if the card is red(hearts or diamonds).
        
        returns: bool :
            True if the card is red, False if not
        
        '''
        
        if self.suit == 'h' or self.suit == 'd':
            return True
        else:
            return False
   
    def move(self, dx, dy):
        '''
        Moves the card by the specified amount.
        
        Params:
            dx (int): The change in x coordinate
            dy (int): the change in y coordinate
        
        '''
        self.image.move(dx, dy)
        
    def containsPoint(self, point):
        
        '''
        Checks if the give point is within the bound of the card.
        
        Params: point(point) (the point to check:.
        
        Returns:
            bool: True if the point is within a card bound, false is not.
        '''
        leftPoint = self.image.getCenter().getX() - 1/2 * self.image.getWidth()
        RightPoint = self.image.getCenter().getX() + 1/2 * self.image.getWidth()
        topPoint = self.image.getCenter().getY() - 1/2 * self.image.getHeight()
        bottomPoint = self.image.getCenter().getY() + 1/2 * self.image.getHeight()
        
        if (point.getX() > leftPoint) and (point.getX() < RightPoint) and (point.getY() > topPoint) and (point.getY() < bottomPoint):
            return True
        else:
            return False
    
    def __eq__(self, cardToCompare):
        '''
        Allows users of the Card class to compare two cards using ==
        
        Params:
        cardToCompare (Card): the Card to check for equality with this Card
        
        Returns:
        True if the two cards have the same rank and suit. Otherwise, False
        '''
        
        return self.suit == cardToCompare.suit and self.rank == cardToCompare.rank
    
    def __str__(self):
        return f'suit = {self.suit}, rank = {self.rank}, center = {self.image.getCenter()} '
   
        
        
        


def main():  
    window = GraphWin("Testing Card", 500, 500)
    
    # create King of Hearts card
    fileName = 'cards/13h.gif'
    card = Card(fileName)

    # print card using __str__ and test getRank, getSuit, getImage
    print(card)
    print(card.getRank())
    print(card.getSuit())
    print(card.getImage())
    print(card.isRed())
    
    
    
    # move card to center of window and display it
    card.move(250, 250)
    card.draw(window)
    
    # click only on the card should move it 100 pixels left
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(-100, 0)
    
    # click only on the card should move it 200 pixels right and 100 pixels down
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(200, 100)
    
    # print the card using __str__
    print(card)
    
    # stall 2 seconds
    time.sleep(2)
    
    # create 2 of Spades card
    fileName = 'cards/2s.gif'
    card2 = Card(fileName)

    # print card2 using __str__ and test getRank, getSuit
    print(card2)
    print(card2.getRank())
    print(card2.getSuit())
    print(card2.isRed())
    
    # move card2 to center of window and display it
    card2.move(250, 250)
    card2.draw(window)
    
    # stall 2 seconds then remove both cards from the window
    time.sleep(2)
    card.undraw()
    card2.undraw()
    
    # stall 2 seconds then close the window
    time.sleep(2)
    window.close()
    

    
if __name__ == '__main__':
    main()
        
        