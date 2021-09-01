import os
def get_inputs():
    #get the total weight and bar type from user,
    #prompting them to re-enter an input if it
    #is not an integer.
    bar = input('How much does your bar weigh?\n')
    if bar == 'exit':
            os._exit(0)
    while bar.isnumeric() != True:
        print('Please enter a valid weight!')
        bar = input('How much does your bar weigh?\n')
        if bar == 'exit':
            os._exit(0)
    bar = int(bar)
    weight = input('Enter the desired weight:\n')
    if weight == 'exit':
            os._exit(0)
    while weight.isnumeric() != True:
        print('Please enter a valid weight!')
        weight = input('Enter the desired weight:\n')
        if weight == 'exit':
            os._exit(0)
    weight = int(weight)
    one_side = float(((weight-bar)/2))
    return bar, weight, one_side

def calculator(one_side, weight_lst):
    #create variables with initial values
    remaining_weight = one_side
    forty_five = 0
    thirty_five = 0
    twenty_five = 0
    ten = 0
    five = 0
    two = 0
    #use while loop to keep iterating through plate options
    #as long as the remaining weight is not zero
    while remaining_weight != 0:
        #use for loops to iterate through the
        #weight list and keep subtracting the largest
        #plate possible from the remaining weight.
        for weight in weight_lst:
            if weight == 45:
                if remaining_weight - 45 >= 0:
                    remaining_weight -= 45
                    forty_five += 1
                    if remaining_weight - 45 >= 0:
                        break
            elif weight == 35:
                if remaining_weight - 35 >= 0:
                    remaining_weight -= 35
                    thirty_five += 1
                    if remaining_weight - 35 >= 0:
                        break
            elif weight == 25:
                if remaining_weight - 25 >= 0:
                    remaining_weight -= 25
                    twenty_five += 1
                    if remaining_weight - 25 >= 0:
                        break
            elif weight == 10:
                if remaining_weight - 10 >= 0:
                    remaining_weight -= 10
                    ten += 1
                    if remaining_weight - 10 >= 0:
                        break
            elif weight == 5:
                if remaining_weight - 5 >= 0:
                    remaining_weight -= 5
                    five += 1
                    if remaining_weight - 5 >= 0:
                        break
            elif weight == 2.5:
                if remaining_weight - 2.5 >= 0:
                    remaining_weight -= 2.5
                    two += 1
                    if remaining_weight - 2.5 >= 0:
                        break
    return forty_five, thirty_five, twenty_five, ten, five, two

def main():
    #print welcome message
    print('---Welcome to the weight calulator---')
    #create varibles from get_inputs function
    bar, weight, one_side = get_inputs()
    #create a list of plate options
    weight_lst= [45, 35, 25, 10, 5, 2.5]
    #call calculator function
    forty_five, thirty_five, twenty_five, ten,\
    five, two = calculator(one_side, weight_lst)
    #print final results
    print(('\\' * 15))
    if forty_five > 0:
        print('\n45lb Plates: ' + str(forty_five*2))
    if thirty_five > 0:
        print('\n35lb Plates: ' + str(thirty_five*2))
    if twenty_five > 0:
        print('\n25lb Plates: ' + str(twenty_five*2))
    if ten > 0:
        print('\n10lb Plates: ' + str(ten*2))
    if five > 0:
        print('\n5lb Plates: ' + str(five*2))
    if two > 0:
        print('\n2.5lb Plates: ' + str(two*2))


main()
