import pandas as pd

"""File is open given the correct input and will loop until file is found in  directory"""


def openfile():
    #While loop to keep asking for inut until file is found
    while True:
        filename = input("Enter a file: ")
        try:
        #We open the csv using pandas making it a dataframe and using the headers
            fp = pd.read_csv(filename, header=0)
            return fp
        except IOError:
            print('Wrong File Name')


"""This Function searches through the nested dictionaries and finds the min and max values along with the year for each state and assigns it to new dict""" 
def search(d):
#declare variables
    min = 100
    max = 0
    maxy = 0
    miny = 0
    new = {}
#Searches through the first level of dict items which are the crops
    for crop, state in d.items():
    #adds every crop into dict
        if crop not in new:
            new[crop] = []
        #loops through state and year 
        for state, year in state.items():
        #reset min and max values
            min = 100
            max = 0
            maxy = 0
            miny = 0
            #loops through year and values for every state
            for i, value in year.items():
            #finds the min
                if int(value) < min:
                    min = int(value)
                    miny = i
            #finds the max
                if int(value) > max:
                    max = int(value)
                    maxy = i
            #assigns the values as a list per state per crop
            l = [state, maxy, max, miny, min]
            #assigns the list to the dict value and makes a list of list per crop
            new[crop].append(l)
    #Retruns new dict
    return new




"""This function reads the df and takes out all the information we do not want and cleans all the columns and rows and returns nested dicts"""

def readfile(df):

    #reassings values for incorrect spelling fo certain states
    for index in df.index:
        if df.loc[index, 'State'] == 'Missouri 2/':
            df.loc[index, 'State'] = 'Missouri'
    #drops rows and columns we do not want
    df = df.loc[df["Value"] != '.']
    df = df.loc[df["Value"] != '*']
    df = df.loc[df['State'] != 'U.S.']
    df = df.loc[df['State'] != 'Other States ']
    df = df.drop(["Crop title", "Variety", "Unit"], axis=1)


    #Groups values by crop and then groups by states with a nested dictionary with one more dict assigning yeaer and value
    d = df.groupby('Crop').apply(lambda a: dict(a.groupby('State').apply(lambda x: dict(zip(x['Year'], x['Value'])))))
    d = d.to_dict()
    #returns nested dict
    return d

"""This Function displays the formatted information that we need for the lab"""


def display(new):
#loops through the dict 
    for i, k in new.items():
    #prints crop
        print('Crop:',i)
        #prints headers
        print("{:<20s}{:<8s}{:<6s}{:<8s}{:<6s}".format('State', 'Max Yr', 'Max', 'Min Yr', 'Min'))
        #loops through the list and prints all the storted information
        for l in k:
            print("{:<20s}{:<8d}{:<6d}{:<8d}{:<6d}".format(l[0], l[1], l[2], l[3], l[4]))
        #space
        print()


"""main function that calls all the other functions"""
def main():
#openfile as a pointer(DF)
    fp = openfile()
    #create nested dicts
    datamap = readfile(fp)
    #make new dict with max and min vals
    new = search(datamap)
    #displays values
    display(new)

#calls main function
if __name__ == "__main__":
    main()
