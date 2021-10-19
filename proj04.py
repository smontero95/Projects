import pylab

def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
    
def open_file():
    '''You fill in the doc string'''
    year_str = input("Enter a year where 1990 <= year <= 2015: ")
    pass  # replace this line with your code
        
def read_file(fp):
    '''You fill in the doc string'''
    pass  # replace this line with your code
        
def find_average(data_lst):
    '''You fill in the doc string'''
    pass  # replace this line with your code
    
def find_median(data_lst):
    '''You fill in the doc string'''
    pass  # replace this line with your code
        
def get_range(data_lst, percent):
    '''You fill in the doc string'''
    pass  # replace this line with your code

def get_percent(data_lst,salary):
    '''You fill in the doc string'''
    pass  # replace this line with your code
    

def main():
    # Insert code here to determine year, average, and median
    print("For the year {:4d}:".format(year))
    print("The average income was ${:<13,.2f}".format(avg))
    print("The median income was ${:<13,.2f}".format(median))
    
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        pass  # replace this line
        # determine x_vals, a list of floats -- use the lowest 40 income ranges
        # determine y_vales, a list of floats of the same length as x_vals
        # do_plot(x_vals,y_vals,year)
    
    choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
    
    while choice:
        # Insert code here to handle choice
        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")

if __name__ == "__main__":
    main()