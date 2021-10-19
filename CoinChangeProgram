quarters = 10
dimes = 10
nickels = 10
pennies = 10

print("Welcome to change-making program.")

print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(quarters, dimes, nickels, pennies))
in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

while in_str != 'q':

    if in_str == 'q':
        break
    else:
        in_str = float(in_str)

    qc = 0
    dc = 0
    nc = 0
    pc = 0
    amount = -1
    while amount < 0:
        amount = int(input("Input dollars paid (int): "))

        d = (amount * 100) - (in_str * 100)
        if d == 0:
            print('No change.')
            break
        else:
            print("Collect change below: ")
        while quarters != 0 and d >= 25:
            d = d - 25
            quarters -= 1
            qc += 1
            if d == 0:
                break
        if qc != 0:
            print("Quarters: {:d}".format(int(qc)))

        while dimes != 0 and d >= 10:
            d = d - 10
            dimes -= 1
            dc += 1
            if d == 0:
                break
        if dc != 0:
            print("Dimes: {:d}".format(int(dc)))

        while nickels != 0 and d >= 5:
            d = d - 5
            nickels -= 1
            nc += 1
            if d == 0:
                break
        if nc != 0:
            print("Nickles: {:d}".format(int(nc)))

        while pennies != 0 and d > 0:
            d -= 1
            pennies -= 1
            pc += 1
            if d == 0:
                break
        if pc != 0:
            print("Pennies: {}".format(int(pc)))

        # Fill in the good stuff here instead of the following print



    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
        quarters, dimes, nickels, pennies))
    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    print('')
