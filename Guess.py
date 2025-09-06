

guess=7
while(True):
    maind = int(input('enter your choice between 1 and 10 : '))
    if guess== maind:
        print('correct')
        break
    elif guess > maind:
        print('your guess is too large')
    elif guess < maind:
        print('your guess is too small')