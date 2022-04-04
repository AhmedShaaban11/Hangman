import random

words = ["apple", "banana", "orange", "lemon", "mango", "coconut", "pineapple"]


def get_word(dic):
    return words[random.randint(0, dic.__len__() - 1)]


def hinter(n, length):
    hints = []
    for i in range(0, n):
        hints.append(random.randint(0, length - 1))
    return hints


def filler(li1, word, li2):
    for val in li2:
        li1[val] = word[val]


def generate_word(word):
    length = word.__len__()
    game_word = ['-'] * length
    if length > 7:
        hints = hinter(3, length)
    elif length > 4:
        hints = hinter(2, length)
    else:
        hints = hinter(1, length)
    filler(game_word, word, hints)
    return game_word


def start_game():
    print("Salam")
    print("You have three chances to win")
    print("Good luck")


def win_message(word):
    print('=' * 20)
    print("You won the game")
    print("The word is: " + word)


def lose_message(word):
    print('=' * 20)
    print("You lost the game!")
    print("The word is: " + word)


def state_message(li):
    word = ''.join(li)
    print('=' * 20)
    print("Guess this word: " + word)


def update_state(word, li, chances):
    if "".join(li) == word:
        win_message(word)
    elif chances == 0:
        lose_message(word)
    else:
        game_round(word, li, chances)


def game_round(word, li, chances=3):
    state_message(li)
    i = li.index('-')
    letter = input("Enter letter: ")
    if letter == word[i]:
        li[i] = letter
        print("Correct!")
    else:
        chances -= 1
        print("Wrong!")
        print("You have", chances, "chances")
    update_state(word, li, chances)


def end_game():
    print('=' * 20)
    print("Thank you for playing")
    replay = input("Play again? (y/n) ")
    if replay == 'y':
        main()


def main():
    aim = get_word(words)
    game_word = generate_word(aim)
    start_game()
    game_round(aim, game_word)
    end_game()


main()
