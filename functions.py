#author:RED 2/6/23
import random


def add_two_numbers(one, two):  # add two numbers
    return one + two


def print_all_keys(dictionary):  # print all the keys in a dictionary
    return [k for k in dictionary]


def add_indexes_to_list(list):  # add index numbers to a list
    for i, v in enumerate(list):
        list[i] = f'{i}: {v}'
    return list


def input_until_password(password):  # put user in an infinite loop until they put in the password
    n = ''
    while n != password:
        n = input('please enter your password: ')
    return 'access granted'


def nickname_maker():  # Nickname creator
    name = input('What is your name?: ')
    prefixes = ['Lil', 'Big', 'The', 'Champ', 'Mr.', 'King', 'MVP']
    suffixes = ['III', 'Jr.', 'Sr.', 'the one and only']
    return f'Your nickname is: {random.choice(prefixes)} {name} {random.choice(suffixes)}!'


def guess_the_number():  # Guess the number game
    number = random.randint(1, 10)
    print('Guess the number from 0-10!')
    attempts = 0
    while int(input(f'Guess {attempts}: ')) != number:
        attempts += 1
    if attempts == 1:
        return 'Wow you got it on the first try!'
    elif attempts < 5:
        return 'hey thats pretty good!'
    elif attempts < 10:
        return "there's always next time!"
    elif attempts < 20:
        return 'how is this possible'
    else:
        return 'never play again'


def quiz_game():  # Quiz game
    print('Welcome to my quiz game!')
    print('There will be 4 questions. Your score will be returned when the game has concluded.')
    score = 0
    trivia_questions = {"What's the fastest land animal?": 'Cheetah',  # very tough questions
                        "Who is the patron saint of Ireland?": 'St. Patrick',
                        'What color is a Ruby?': 'Red',
                        "Who was the 13th President of the United States?": 'Millard Fillmore'}
    for question in trivia_questions:
        print(question)
        answer = input()
        if answer.lower() != trivia_questions[question].lower():
            print('Incorrect')
        else:
            score += 1
            print('Correct!')
    print('Thanks for playing!')
    if score == 4:  # Return the score
        return f'You had a perfect score of {score} points!'
    elif score == 0:
        return 'You got none correct.'
    else:
        return f'You got a score of {score} points!'


def two_number_calculator(function, one, two):  # calculator for working with two numbers
    if function == 'add':
        return one + two
    elif function == 'subtract':
        return one - two
    elif function == 'subtract two':
        return two - one
    elif function == 'divide':
        return one / two
    elif function == 'divide two':
        return two / one
    elif function == 'multiply':
        return one * two
    elif function == 'power':
        return one ** two
    elif function == 'inverse the sum':  # very handy
        return (one + two) ** -1
    else:
        return f"unknown function: {function}"


def blackjack():  # very simple blackjack
    dealer = [random.randint(1, 10), random.randint(1, 10)]  # generate hands
    your_hand = [random.randint(1, 10), random.randint(1, 10)]
    print('Welcome to Blackjack!')
    print(f'Your hand has a {your_hand[0]} and a {your_hand[1]} (Total = {sum(your_hand)})')
    print(f'The dealer shows a {dealer[0]}.')
    while True:  # main game loop
        move = input('(H)it, (S)tand, or (F)old: ')
        if move.lower() == 'h':  # add card to hand
            your_hand.append(random.randint(1, 10))
            print(f'The dealer gives you a {your_hand[-1]} (Total = {sum(your_hand)})')
        if sum(your_hand) == 21:  # if you get lucky
            print('You have a blackjack!')
            break
        if sum(your_hand) > 21:  # if you are not lucky
            return 'You lose!'
        elif move.lower() == 's':  # if you want to keep playing
            break
        elif move.lower() == 'f':  # if you give up
            return 'You lose!'
    print(f'The dealers second card is a {dealer[1]} (Total = {sum(dealer)})')

    while sum(dealer) < 17:  # give more cards to the dealer (dealer stands on 17)
        dealer.append(random.randint(1, 10))
        print(f'The dealers draws a {dealer[-1]} (Total = {sum(dealer)})')

    if sum(dealer) > 21:
        return 'You lose!'
    elif sum(your_hand) < sum(dealer):  # lose
        return 'You lose!'
    elif sum(your_hand) > sum(dealer):  # win
        return 'You win!'
    elif sum(your_hand) == sum(dealer):  # tie
        return 'Push'


def create_computer_lab_seating_chart(students, num_seats, randomize):  # Create a seating chart for B202
    print('Creating seating chart...')
    seats = {}
    try:  # error handling
        for i, v in enumerate(students):
            if randomize:  # if you don't want the inputted order
                seats[f'B202_{random.randint(1, num_seats) + 1}'] = v
            else:
                seats[f'B202_{i+1}'] = v
    except Exception:
        return 'Input error'

    print('Here is your seating chart: ')
    for v in seats:  # print out the entire seating chart
        print(f'{v}: {seats[v]}')
    return seats  # returns the dictionary
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
cycle-11-labs-p23jmarotta/lab_11-3_functions.py at main · fp-computer-programming/cycle-11-labs-p23jmarotta