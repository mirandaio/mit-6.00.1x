def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
    It takes as a parameter one number and returns:
    *  -1 if the number is less than the secret number
    *  0 if the number is equal to the secret number
    *  1 if the number is greater than the secret number
    
    returns: integer, the secret number
    ''' 
    guess = 1
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == 0:
            foundNumber = True
        elif sign == -1:
            guess *= 2
        else:
            guess -= 1
    return guess
