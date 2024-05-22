# love_score

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
2. Then check for the number of times the letters in the word LOVE occurs.
3. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is *z*."

e.g.
1. name1 = "Angela Yu"
2. name2 = "Jack Bauer"
Result : 
1) T occurs 0 times
2) R occurs 1 time
3) U occurs 2 times
4) E occurs 2 times

Total = 5

1) L occurs 1 time
2) O occurs 0 times
3) V occurs 0 times
4) E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

These functions will help you:
lower() count()

Example Input 1
Kanye West
Kim Kardashian

Example Output 1
The Love Calculator is calculating your score...
Your score is 42, you are alright together.

Example Input 2
Brad Pitt
Jennifer Aniston

Example Output 2
The Love Calculator is calculating your score...
Your score is 73.


Hint
You can check your values against mine using this table:

      Name 1	      Name 2	         Score
1) Brad Pitt           Jennifer Aniston       73
2) Prince William      Kate Middleton         67
3) Ashton Kutcher      Mila Kunis             63
4) Angela Yu           Jack Bauer             53
5) David Beckham       Victoria Beckham       45
6) Mario Princess      Peach                  43
7) Kanye West          Kim Kardashian	    42
