'''
Name: Eliana Assefa 
CSC 201
Programming Project 2

This program draws a map to show presidential election results with subregions either colored
red/blue to show whether democrats/republicans won that subregion or colored a
shade of purple based on the proportion of deomocrat/republican/other votes. The
map can be chosen to display the USA subdivided by states or a state subdivided
by counties. The user will enter data to choose USA or a state, the election year,
and whether a red/blue or purple map will be drawn.

Document Assistance: (who and what  OR  declare that you gave or received no assistance):


'''

from graphics2 import *

RED_BLUE_MAP = 1  # code for red/blue map
PURPLE_MAP = 2    # code for purple map
MAX_COLOR_NUM = 255   # maximum number for a color
MAX_SIZE = 700  # maximum dimension of the graphics window

# list of valid state postal codes and 'USA' 
ABBREV_LIST = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN',
               'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MH', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT','NE',
               'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD',
               'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'USA']

# valid years for election data
YEAR_LIST  = ['1960', '1964', '1968', '1972', '1976', '1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012', '2016']

'''
Creates and returns a dictionary mapping the subregion
name to red or blue indictating whether republicans or
democrates had more votes in that subregion

Params:
fin_elect (file): file object connected to the data file with voting data

Returns:
a dictionary matching a subregion to either red (democrat) or blue (republican)
'''
def make_red_blue_dict(fin_elect):
    dict = {}
    first_line = fin_elect.readline()  # We're not using this line
    for line in fin_elect:
        line_data = line.split(',')
        subregion = line_data[0]
        democratic_vote = line_data[1]
        print(democratic_vote)
        republican_vote = line_data[2]
        other_vote = line_data[-1]
        
        
        # add code here to compare the election results
        if republican_vote > democratic_vote:
            color = 'red'
        else:
            color = 'blue'
        
        # and store 'red' or 'blue' in variable color
        

            
            
        dict[subregion] = color  # associates 'red' or 'blue' with the subregion name in a dictionary
    return dict
        
'''
Creates and returns a dictionary mapping the subregion
name to a color representing the proportion of republican
(red) votes, democratic (blue) votes, and independent
(green) votes for a particular presidential election.

Params:
fin_elect (file): file object connected to the data file with voting data

Returns:
a dictionary matching a subregion to a shade of purple
'''
def make_purple_dict(fin_elect):
    dict = {}
    first_line = fin_elect.readline()   # We're not using this line
    for line in fin_elect:
        line_data = line.split(',')
        subregion = int(line_data[0])
        democratic_vote = int(line_data[1])
        republican_vote = int(line_data[2])
        other_vote = int(line_data[-1])
        # add code here to compare the election results
        red = (republican_vote/(republican_vote + democratic_vote + other_vote)) * 255
        blue = (democratic_vote/(democratic_vote + republican_vote + other_vote)) * 255
        green = (other_vote/(other_vote + republican_vote + democratic_vote)) * 255
        
        color = color_rgb(red,green,blue)
        
        if subregion in dict:
            color = dict[subregion]
            polygon.setFill(color)
        else:
            polygon.setFill(color)
            color ='black'
            
            
        polygon.draw(window)
        # and store a shade of purple in variable color
        
       
       
       
        dict[subregion] = color # associates a shade of purple with the subregion name in a dictionary
        
    return dict


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

def user_input():
    file = input('Do you want a map of USA or a state? Enter USA or state postal code: ')
    file = file.upper()
    if file not in ABBREV_LIST:
        print('Not a valid abbreviation. Exiting program.'
)
        exit(-1)
    
    
    filename = f'purple/{file}.txt'
    return filename

def year_input(filename):
    file = input("Which year's election 1960-2012 do you want to see?")
    name = filename.split('/')[-1]
    name = filename.split('.')[0]
    print(name)
    if file not in YEAR_LIST:
        print('Not a valid year. Exiting program.')
        exit(-1)
    
    filename = f'{name}{file}.txt'
    print(filename)
    return filename

def map_type(fin_elect):
    print(fin_elect)
    number = int(input('Do you want a red/blue map(1) or purple map(2)? '))
    if number == RED_BLUE_MAP or number == PURPLE_MAP:
        if number == RED_BLUE_MAP:
            
            dict = make_red_blue_dict(fin_elect)
            
        else:
            
            dict = make_purple_dict(fin_elect)
    else:
        exit(-1)
        
    
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
    name = user_input()
    print(name)
    second_file = year_input(name)
    print(second_file)
    fin_elect = open(second_file, 'r')
    map_type(fin_elect)
    
    window = GraphWin('USA MAP', MAX_SIZE, MAX_SIZE)
    fin = open(name, 'r')    # change IL to another state or USA to draw its map
    window.setBackground("White")
    min_x, min_y =  min_values(fin)  
    max_x, max_y = max_values(fin) 
    
    num_subregions(fin, window, min_x, min_y, max_x, max_y)
    
    
  
main()



    




  



