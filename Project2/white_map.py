"""
Name:
CSC 201
Programming Project 2-Checkpoint

This program reads a file in a specific format and draws
a map of a region using the latitude and longitude values
delineating the outline of subregions on the map. It is
either a map of the USA with subregions as states OR
a map of a state with subregions as counties.

Document Assistance: (who and what  OR  declare that you gave or received no assistance):


"""
MAX_SIZE = 700

from graphics2 import *

def min_values(fin):
    first_line = fin.readline()
    first_List = first_line.strip().split()
    min_x = float(first_List[0])
    min_y = float(first_List[-1])
    
    return min_x, min_y
def max_values(fin):
    second_line = fin.readline()
   
    
    second_list = second_line.strip().split()
    max_x = float(second_list[0])
    max_y = float(second_list[-1])
    
    return max_x, max_y

def num_subregions(fin,window,min_x, min_y, max_x, max_y):
    window.setCoords(min_x, min_y, max_x, max_y)
    num = fin.readline()
    
    
    for line in fin:
        subregion_name = fin.readline()
        region_name = fin.readline()
        num_lines_for_subregion = fin.readline()
       
        list = []
        for i in range(int(num_lines_for_subregion)):
            
            line = fin.readline()
            line_list = line.strip().split()
            x = line_list[0]
            y = line_list[-1]
            list.append(Point(x,y))
            
            
        polygon = Polygon(list)
        polygon.draw(window)


        
        
        
def main():
    window = GraphWin('USA MAP', MAX_SIZE, MAX_SIZE)
    fin = open('purple/IL.txt', 'r')    # change IL to another state or USA to draw its map
    window.setBackground("White")
    min_x, min_y =  min_values(fin)  
    max_x, max_y = max_values(fin) 
    
    num_subregions(fin, window, min_x, min_y, max_x, max_y)
    
 

    
  
main()