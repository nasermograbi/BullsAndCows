<h1>Bulls And Cows</h1>

This repository holds implementation of the Bulls And Cows game with two mods.

<h3>About the game</h3>

-Bulls and Cows is a usually a 2 player game(int this case - you and the computer). One player thinks of a number, while the other player tries to guess it.

-The number to be guessed must be a 4 digit number, using only digits from 1 - 9, each digit atmost once. e.g. 1234 is valid, 0123 is not valid, 9877 is not valid, 9876 is valid.
For every guess that the player makes, he gets 2 values - the number of bulls and the number of cows. 1 bull means the guess contains and the target number have 1 digit in common, and in the correct position. 1 cow means the guess and the target have 1 digit in common, but not in correct position. e.g. Let the target be 1234. Guessing 4321 will give 0 bulls and 4 cows. 3241 will give 1 bull and 3 cows. 4 bulls means you have won the game!

-The player gets 7 chances to correctly guess the entire number.

<h3>Logic behind the game</h3>
-If you want the computer to guess your number: We assign the numbers from the input for bulls and cows, and check if they are entered. At each end of the cycle, check how many bulls there are. The bulls are counted by checking each number in the list and we see if the number of bulls changes. If the number on the list has not been reduced, reduce the probability.Similar way we check the cows. When every time a sequential number is being guessed in the range from 1234 to 9876 minus all the probabilities that we have rejected. And so on until the bulls become 4.


-If you want to guess the computers number: A random number is being generated. After you input a number it checks its numbers one by one if the element is in the same position with the one generated one for the bulls.If its in the list but not in the same spot its a cow.


<h3>How to get to play it?</h3>
The easiest way is to copy the code and run it on your local or online python ide like https://www.programiz.com/python-programming/online-compiler/

