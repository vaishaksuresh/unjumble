unjumble
========
Can you create a program to solve a word jumble? The program should accept a string as input, and then return a list of words that can be created using the submitted letters. For example, on the input "dog", the program should return a set of words including "god", "do", and "go".
 
Please implement the program in a language of your choice, but refrain from using any combinatorics helper modules or imports (e.g. itertools in Python). In order to verify your words, just download an English word list.

Algorithm
=========
1. Find the powerset of the word
2. For each subset, find all the permutations of characters (Anagram)
3. Add all these into a set to remove duplicates and easy access
4. create a set of dictionary word
5. Required output is the intersection of the two sets.


Running
==========

`./find_substring.py god`

Output:

  1. go
  2. do
  3. od
  4. dog
  5. god
