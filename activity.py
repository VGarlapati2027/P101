import random
request = input('Do you want to roll the dice? Y for yes and N for no')
if(request == 'Y'):
    yes = random.randint(1,6)
    print(yes)
    again = input('Y to roll again, N to exit')
else:
    print('Exit program')

