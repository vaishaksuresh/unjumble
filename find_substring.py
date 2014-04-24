#! /usr/bin/python

__author__ = 'vaishaksuresh'
import sys


words = set([])
permuted_words = set([])

'''This builds the power set.
ex: {god} = {g}, {o}, {d}, {od}, {og}, {dg}, {god}
Since we start from index 1, {} is eliminated automatically
This results in 2^n-1 subsets

Algorithm:
1. Use binary representation to indicate which character to pick.
example: 001 = {d}, 010 = {o} and 111 = {god}

2. start from 001(1) all the way till 111(7, length of string)
3. bitwise AND with 1 and see if the current bit is 1, if it is,
pick the character at that index. else, continue
4. right shift by 1 bit to get the next letter

5. Finally, add all the sub sets to a master set.
'''


def find_power_set(given_string):
    bitset = 2 ** len(given_string)
    for bit_index in xrange(1, bitset):
        sub_set = []
        word_index = 0
        while bit_index > 0:
            if bit_index & 1 == 1:
                sub_set.append(given_string[word_index])
            bit_index >>= 1
            word_index += 1
        words.add("".join(sub_set))


''' This method computes the permutation of all characters the string.
A string of length n has n! permutations.
ex: {go} can be represented as {go} and {og}

Permutation is done using the recursive function.
Algorithm:
ex:
p{g} - > {g}
p{go} - > {go}, {og} => {g} * p{g}

this means for a string of length > 1, the permutation is calculated recursively
by appending the one character at all positions to the rest of the string.

'''


def permute_words(prefix, rest_of_string):
    if len(rest_of_string) == 0:
        permuted_words.add(prefix)
    else:
        for i in range(0, len(rest_of_string)):
            permute_words(prefix + rest_of_string[i], rest_of_string[0:i] + rest_of_string[i + 1:len(rest_of_string)])


''' Main Method.
Accepts a word as arguement and prints all dictionary words formed using the letters from the word
Word list used from http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt

1. The powerset of the word is calculated (2^n possible values)
2. For each of these, permutation is generated (n! possible values)
3. All these words are stored in a set (Eliminates duplicates, hash based, hence faster access)
4. Words from the word list are loaded into a set
5. Intersection of the two sets gives all the legal words.

'''


def main(argv):
    if len(argv) == 1:
        with open("wordsEn.txt") as word_file:
            legal_words = set(word.strip().lower() for word in word_file)
        find_power_set(argv[0])
        for word in words:
            permute_words("", word)
        final_words = set.intersection(permuted_words, legal_words)
        for index, word in enumerate(final_words):
            print "%d. %s" % (index+1, word)
    else:
        print "Please provide only one word."


if __name__ == "__main__":
    main(sys.argv[1:])
