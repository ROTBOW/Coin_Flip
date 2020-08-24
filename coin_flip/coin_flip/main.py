### flips numbers of coins as asked then returns the amount of each. ###
import random

def flip():
    amounts =[]
    print("Please enter the amount of coins to flip...")
    count = int(input("--> ")) - 1
    while count >= 0:
        coin = round(random.uniform(1, 2), 0)
        if coin == 1:
            amounts.append('heads')
        else:
            amounts.append('tails')
        count = count - 1
    print("%s Heads flipped" % amounts.count('heads'))
    print('%s Tails flipped' % amounts.count('tails'))  

flip()