from matplotlib import pylab


def do_plot(x_vals, y_vals, year):
    """Plot x_vals vs. y_vals where each is a list of numbers of the same length."""
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in " + str(year))
    pylab.plot(x_vals, y_vals)
    pylab.show()


def open_file():
    """This function opens a file with the year w UI. It checks for error with year number and files available"""
    # loop that keeps asking for input until correct
    while True:
        year_str = input("Enter a year where 1990 <= year <= 2015: ")
        try:
            # makes sure ui is an integer
            year_str = int(year_str)
            if 1990 <= year_str <= 2015:
                # checks if year is valid and adds it to file name
                filename = "year" + str(year_str) + ".txt"
                try:
                    # opens file as a pointer and reads the first two lines
                    f = open(filename)
                    print('')
                    break
                # error check for file not found
                except FileNotFoundError:
                    print("Error in file name:", filename, " Please try again.")
            else:  # error check for year
                print("Error in year. Please try again.")
        except ValueError:
            print("Error in year. Please try again.")
    # return file pointer and year

    return f, year_str


def read_file(fp):
    """This function reads the file pointer and splits into a line of lines and returning it without any commas"""
    next(fp)
    next(fp)
    f = fp.readlines()
    ll = []
    # initialize line of lines and loop through fp and split each line then append
    for line in f:
        l = line.split()
        ll.append(l)
    # another loop that removes every comma in the numbers of a text file
    for line in ll:
        for i, v in enumerate(line):
            if ',' in v:
                line[i] = v.replace(',', '')
    # returns list of list with each as a list
    return ll


def find_average(ll):
    """This function finds the average of the year of the file inputted to the program"""

    # assign the total population number of all income ranges and starter values
    total = float(ll[-1][4])
    avg, summ = 0, 0

    # enumerate though the list of list and add column 6 which is the combined income in that range
    for i, v in enumerate(ll):
        try:
            summ += float(v[6])
        # error checks to make sure it is a float
        except ValueError:
            continue
    # divides the sum by the total pop and returns the avg as a float rounded to the second decimal spot
    avg = summ / total

    return round(avg, 2)


def find_median(ll):
    """This function finds what range of income is closest to 50% in column 5 that is
    the closest median we can approximate due to limitations"""
    # initialize needed list and value to approximate
    nl = []
    p = 50
    # loops through the list of list and creates new list of only column 5 values also error checks
    for i in ll:
        try:
            nl.append(float(i[5]))
        except ValueError:
            continue
    # this loops through column 5 values and approximates which value is the closest from the above and below
    h = min(enumerate(nl), key=lambda x: abs(x[1] - p))
    #   returns the value closest and its key
    key = h[0]
    # use the key to return the average of that range
    median = ll[key][7]
    # returns a float of the median
    return float(median)


def get_range(ll, p):
    """This function finds the income range that the percentage is equal to or greater than
        the one given and then returns the income range, cumulative %, also range average"""
    # initialize needed variables
    p = float(p)
    pay = []
    avg = 0
    percent = 0
    # loop though the list of lists checking column 5 for the first value greater than the percent given
    for i in ll:
        i[5] = float(i[5])
        # once found assign the percent and avg values and append the pay range into a list
        if i[5] >= p:
            percent = i[5]
            pay.append(float(i[0]))
            pay.append(float(i[2]))
            avg = i[7]
            break
    # create the tuple for pay range then return an entire tuple
    t = [tuple(pay), percent, float(avg)]

    return tuple(t)


def get_percent(ll, s):
    """This function takes the list of list and income given as UI and returns the cum % and income range
    that the income belongs too"""
    # initialize needed vars
    l = []
    # loop to find in what range the income given lies also error checks for last row
    for i in ll:
        try:
            # creates all range values into floats
            i[0] = float(i[0])
            i[2] = float(i[2])
            # checks ui per range once found assign the range into a tuple within a list that has cum %
            if i[0] <= s <= i[2]:
                l = [(i[0], i[2]), float(i[5])]
        except ValueError:
            i[0] = float(i[0])
            if s >= i[0]:
                l = [i[0], float(i[5])]
    # returns a tuple with another element within a tuple
    return tuple(l)


def main():
    """My main functions call upon all functions prior and displays all the values asked for by user"""
    # open file and read it into a list of list
    fp, year = open_file()
    l = read_file(fp)
    # find avg and median from list of list
    avg = find_average(l)
    median = find_median(l)
    x_vals = []
    y_vals = []
    # assign the first 40 values into plot list for graph and rounds them
    for i, v in enumerate(l):
        y = round(float(v[5]))
        x = round(float(v[0]))
        x_vals.append(x)
        y_vals.append(y)
        if i == 39:
            break
    # displays all the values in a formatted method then ask if the user wants to plot the values we collected
    print("{:<6s}{:<15s}{:<15s}".format('Year', 'Mean', 'Median'))
    print("{:<6d}${:<14,.2f}${:<14,.2f}".format(year, float(avg), float(median)))
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        do_plot(x_vals, y_vals, year)
    # determine x_vals, a list of floats -- use the lowest 40 income ranges
    # determine y_vales, a list of floats of the same length as x_vals
    choice = ' '
    # while loop that asks for ui and what specific data he wants to see from this year
    while choice != '':
        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
        # when the ui picks r then have to enter percent w error check
        if choice == 'r':
            while True:
                p = input('Enter a percent: ')
                try:
                    # makes ui a flaot and verifies that it is a valid percentage
                    p = float(p)
                    if 0 <= p <= 100:
                        # calls get_range function and pulls the first value within the first tuple
                        t = get_range(l, p)
                        pay = t[0][0]
                        print('')
                        # displays value and goes back
                        print("{:4.2f}% of incomes are below ${:<13,.2f}.".format(p, float(pay)))
                        break
                    else:
                        print("Error in percent. Please try again")
                        break
                except ValueError:
                    print("Error in percent. Please try again")
                    break
        # when ui picks p it will ask income if input is incorrect it will go back to the main menu
        elif choice == 'p':
            while True:
                # takes ui and makes it a float
                p = input('Enter an income: ')
                try:
                    p = float(p)
                    # verifies income is not negative and uses get_percent values
                    if p >= 0:
                        t = get_percent(l, p)
                        # displays values for the income given and cum %
                        print('')
                        print("An income of ${:<13,.2f} is in the top {:4.2f}% of incomes.".format(p, t[1]))
                        break
                    else:
                        print("Error: income must be positive")
                        break
                except ValueError:
                    print("Error: income must be positive")
                    break
        elif choice == '':
            # this ends the program if ui gives no input
            break
        else:
            print('Error in selection.')


if __name__ == "__main__":
    main()
