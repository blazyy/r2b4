# coding: utf-8

'''
Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

You’re not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we’ll simulate this is to write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.

Extra: See if you can improve upon the program in the self check by keeping letters that are correct and only modifying one character in the best string so far. This is a type of algorithm in the class of ‘hill climbing’ algorithms, that is we only keep the result if it is better than the previous one.
'''

import string
import random

sentence = 'methinks it is like a weasel'
sentence_length = len(sentence)

def generate_sentence():
    rand_sent = ''
    for i in range(sentence_length):
        rand_sent += random.choice(string.ascii_lowercase + " ")
    return rand_sent

def score(str1, str2):
    score = 0
    for i in range(sentence_length):
        if str1[i] == str2[i]:
            score += 1
        else:
            return score
    return score

def gen_and_score():
    iteration = 0
    best_score = 0
    best_sentence = ''
    while(True):
        new_sentence = generate_sentence()
        new_score = score(new_sentence, sentence)
        if new_score > best_score:
            best_score = new_score
            best_sentence = new_sentence
        if iteration % 1000000 == 0:
            print("Iteration {}, Best Sentence: {}, Score = {}".format(iteration, best_sentence, best_score))
        iteration += 1
        if new_sentence == sentence:
            break

gen_and_score()
