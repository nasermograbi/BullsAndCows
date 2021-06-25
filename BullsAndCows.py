import random
from random import choice

all_numbers = []

guessNumber = 1234  # guess
remaining_count = 0  # remaining possible numbers
old_count = 0  # temp value for the remaining possible numbers

outputString = ""


def check_for_zero(num):
    if get_first(num) == 0 or get_second(num) == 0 or get_third(num) == 0 or get_fourth(num) == 0:
        return True
    else:
        return False


def check_for_duplicates(num):
    output = False

    if get_first(num) == get_second(num):
        output = True

    if get_first(num) == get_third(num):
        output = True

    if get_second(num) == get_third(num):
        output = True

    if get_second(num) == get_fourth(num):
        output = True

    if get_third(num) == get_fourth(num):
        output = True

    if get_first(num) == get_fourth(num):
        output = True

    return output


def check_bulls(bull):
    output = 0

    if get_first(guessNumber) == get_first(bull):
        output += 1

    if get_second(guessNumber) == get_second(bull):
        output += 1

    if get_third(guessNumber) == get_third(bull):
        output += 1

    if get_fourth(guessNumber) == get_fourth(bull):
        output += 1

    return output


def check_cows(cow):
    output = 0

    # all digits from the guessed number
    guess_array = [get_first(guessNumber), get_second(guessNumber), get_third(guessNumber), get_fourth(guessNumber)]

    # add all digits from each of the numbers in the list
    all_array = [get_first(cow), get_second(cow), get_third(cow), get_fourth(cow)]

    for x in range(len(guess_array)):
        if guess_array[x] == all_array[x]:
            output += output

    return output


def get_first(num):
    return int(num / 1000)


def get_second(num):
    return int((num / 100) % 10)


def get_third(num):
    return int((num % 100) / 10)


def get_fourth(num):
    return int(num % 10)


def generate_number():
    generate_first = random.randint(1, 9)
    generate_second = choice([i for i in range(1, 9) if i not in [generate_first]])
    generate_third = choice([i for i in range(1, 9) if i not in [generate_first, generate_second]])
    generate_fourth = choice([i for i in range(1, 9) if i not in [generate_first, generate_second, generate_third]])

    a = [generate_first, generate_second, generate_third, generate_fourth]

    return a


def check_number(generated_num, check_num):
    bulls = 0
    cows = 0

    # bulls
    if check_num[0] == generated_num[0]:
        bulls += 1
    elif check_num[0] in generated_num:
        cows += 1

    if check_num[1] == generated_num[1]:
        bulls += 1
    elif check_num[1] in generated_num:
        cows += 1

    if check_num[2] == generated_num[2]:
        bulls += 1
    elif check_num[2] in generated_num:
        cows += 1

    if check_num[3] == generated_num[3]:
        bulls += 1
    elif check_num[3] in generated_num:
        cows += 1


    print("bulls: " + str(bulls) + "\n" + "cows: " + str(cows))

    if bulls == 4:
        return False


if __name__ == "__main__":
    end = True
    print("If you want me to guess your number press[1].\nIf you want to guess my number press [2]")
    press = input()
    if int(press) == int(1):
        new_gen_num = generate_number()
        while end:
            for i in range(0,9):
                print("What is your guess?")
                new_guess = input()
                res = [int(x) for x in str(new_guess)]
                if check_number(new_gen_num, res) == False:
                    print("You win! The number is: " + new_guess)
                    end = False
            print("You got no more guesses left! You lose.")
            end = False

    if int(press) == int(2):
        for i in range(1234, 9876):
            if not check_for_zero(i) and not check_for_duplicates(i):
                all_numbers.append(i)

        remaining_count = len(all_numbers)
        old_count = remaining_count
        print("Remaining possibilities: " + str(remaining_count) + "\n")
        print("My guess is:" + str(guessNumber) + "\n")
        while end:
            for i in range(0, 10):
                print("bulls:")
                bulls = input()
                print("cows:")
                cows = input()

                if bulls != "" and cows != "":
                    bulls_int = int(bulls)

                    if bulls_int != 4:
                        bulls_temp = []

                        for i in all_numbers:
                            if check_bulls(i) == bulls_int:
                                bulls_temp.append(i)

                        all_numbers.clear()
                        all_numbers.extend(bulls_temp)

                        # cows
                        cows_int = int(cows)
                        cows_int = cows_int + bulls_int
                        cows_temp = []

                        for i in all_numbers:
                            if check_cows(i) == cows_int:
                                cows_temp.append(i)
                        # remove all wrong possibilities and keep only the right ones base on cows
                        if len(cows_temp) > 0:
                            all_numbers.clear()
                            all_numbers.extend(cows_temp)

                        # remaining possibilities
                        remaining_count = len(all_numbers)
                        # 8519
                        # check how many possibilities are left
                        if remaining_count > old_count or remaining_count == 0:
                            print("You're lying\n")
                        elif remaining_count == 1:
                            guessNumber = all_numbers[0]
                            print("Your number is: " + str(guessNumber) + "\n")
                        else:
                            old_count = remaining_count
                            print("Remaining possibilities: " + str(remaining_count) + "\n")

                            # guess the next available number
                            guessNumber = all_numbers[0]
                            print("My guess is:" + str(guessNumber) + "\n")

                        all_numbers.clear()
                        all_numbers.extend(bulls_temp)

                    else:
                        print("Your number is:" + str(guessNumber))
                        end = False
                else:
                    print("Wrong input\n")
            print("You win i could not guess your number!")
            end = False

    elif int(press) != int(1) and int(press) != int(2):
        print("Wrong Input! Start the game again!")
