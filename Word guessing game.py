import random    #start

name = input("enter your name: ")
print(name)
#saved user input in name
print("        following are the rules of the game")
print("1> The word should be displayed  in encrypted form along with the hint then the user is asked whether he wants to guess the entire word or guess the letters in the word one by one.only fir the first time.")
print("2> The initial score of the player will be 10 points.")
print("3> If the user chooses to guess the entire word at once  then if he successfully makes the correct guess then display the word and 5 points will be awarded ,he wins the game so display the score and the game stops. But if he fails to make the correct guess then 3 points are deducted from the score and then he can make further guess for the entire word till the score greater than 0. The game gets over if the score becomes zero.")
print("4> If the user chooses to guess the letter one by one then If the correct letter is guessed ,display the letter(with correct placement) and 3 points will be awarded else 2 points will be deducted for each wrong guess.")
print("5> The user is allowed  to make further guesses only if the score is greater than 0.If the score is not greater than zero than the game is over and the player loses  the game.")
#described all the rules related to the game

print ("welcome " + name)

points = 10
#initial point is 10


def get_club():
    club=["EMOTICA","AVC","SOULS","VIBRANZ","PIXALS"]
    return random.choice(club).upper()


def check(club, guesses, guess):
    status = ''
    matches = 0
    global points
    for letter in club:
        if letter in guesses:
            status += letter
        else:
            status += '*'
        if letter == guess:
            matches += 1

    if matches >= 1:
        points = points + 3
	#here point variable point scored by the user
        print('your score',points)
        print('yes,the word you have to guess contains', matches, '"' + guess + '"' + 's')
	# if the user guessed the correct letter then the points will be increased by 3 points

    else:
        print('sorry,,the word doesn\'t contain the letter "' + guess + '"')
        points = points-2
        print('your score',points)
        # if points < 0:
        # print('your prediction is wrong!')
	# if the guessed letter is not present in the supposed club name then the point will be decresed by 2

    return status


def main():
    club= get_club()
    guesses=[] #this array stores guesses.
    guessed = False
    print('the word you have to guess contains', len(club), 'letters.')
    global points
    while points > 0:
        print('please enter one letter or {}-lettered word directly'.format(len(club)))
        guess = (input()).upper()
	#each letters in this guess variable are converted to capital letterl
	#this loop will be only executed when the points of the user is greater than 0

        if guess in guesses:
            print('you have already guessed the letter' + guess + '"')
            points = points - 2
            #if user repeats the same letter again it will deduct its 2 points
            print('your score is:' ,points)
        elif len(guess) == len(club):
            guesses.append(guess)
	    #append function is here used to add the letter at the end of guess variable
            if guess == club:
                guessed = True
            else:
                print('sorry,that is incorrect.')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(club, guesses, guess)
            if result == club:
                guessed = True
                break
            else:
                print(result)
        else:
            print('invalid entry.')
    if points>0:
        print('yes,the club name is', club + ' congratulations you have guessed the correct club name')
    else:
        print('NOO your input is wrong')

main()