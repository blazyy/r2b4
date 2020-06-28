import string
import random

sentence = 'methinks it is like a weasel'
sentence_length = len(sentence)

def generate_sentence():
    rand_sent = ''
    for i in range(sentence_length):
        rand_sent += random.choice(string.ascii_lowercase + " ")
    return rand_sent

def generate_character():
    return random.choice(string.ascii_lowercase + " ")

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
    old_sentence = generate_sentence()
    best_score = score(old_sentence, sentence)

    while best_score != sentence_length:
        iteration += 1
        new_sentence = old_sentence[:best_score] + generate_character() + old_sentence[(best_score+1):]
        new_score = score(new_sentence, sentence)
        if new_score > best_score:
            best_score = new_score
            old_sentence = new_sentence
        if iteration % 1 == 0:
            print("Iteration {}, Guess: {}, Score = {}".format(iteration, new_sentence, best_score))
    print("Done!")
gen_and_score()
