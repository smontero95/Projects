def open_file():
    #This Function opens and points to file
    fp = open("GDP.txt")
    return fp

def find_min_percent(line):

    #Function finds the min and index after shaving the str down
    min = 10000
    mini = 0
    line = line[76:]
    #we assign enum to a variable so we can skip iterations
    #My loop searches for all the parts of the string that is not a space
    count = enumerate(line)
    for i, value in count:
        if value != " " :
            sub = line[i:i+5] #splice substring 5 indexes over and use try statement as a fail safe
            try:
                sub = float(sub)
            except ValueError:
                break
            if sub < min : #Assign the min value and first index
                min = sub
                mini = i
            for _ in range(6): #this loop allows me to skip iterations in increments of 6 using enumerate
                next(count, None)
    return min, mini +73


def find_max_percent(line):
    #same methods min function
    max = 0
    maxi = 0
    line = line[76:]
    count = enumerate(line)
    for i, value in count:
        if value != " ":
            sub = line[i:i + 5]
            try:
                sub = float(sub)
            except ValueError:
                break
            if sub > max:
                max = sub
                maxi = i
            for _ in range(6):
                next(count, None)
    return max, maxi+72

def find_gdp(line, index):
    #function allows me to find the GDP value given an index from the 44th line. I splice the index 3 values behind and 4 ahead and return a float
    value = line[index-3:index+7]
    return float(value)


def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    #convert billions into trillions
    min_val_gdp /= 1000
    max_val_gdp /= 1000
    
    #prints out all values formatted exactly how the instructions asked
    print("Gross Domestic Product")
    print("{:<10s}{:>8s}{:>6s}{:>18s}".format("min/max","change","year","GDP (trillions)"))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("min", min_val, min_year, min_val_gdp))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("max", max_val, max_year, max_val_gdp))



def main():
    #Allows userinput to continue input until correct file name is entered and calls the open fuction
    ui = ""
    while ui != "GDP.txt":
        ui = input("Enter a file name: ")
        if ui == "GDP.txt":
            fp = open_file()
            break
        else:
            print("Error. Please try again")
    
    #create var before str assignment
    str1 = ""
    str2 = ""
    stry1 = ""

    #counts through the lines and assigns rows 8, 9, and 44 so i can search for values
    for i, line in enumerate(fp):
        if i == 8:
            str1 = line
        elif i == 43:
            str2 = line
        elif i == 7:
            stry1 = line


    min, mini = find_min_percent(str1)
    max, maxi = find_max_percent(str1)
    min_gdp = find_gdp(str2, mini)
    max_gdp = find_gdp(str2, maxi)
    min_year = int(stry1[mini+1:mini+7])
    max_year = int(stry1[maxi+1:maxi+7])


    display(min, min_year, min_gdp, max, max_year, max_gdp)




if __name__ == "__main__":
    main()
