from twython import Twython
import sys
import random
import os
from pseudo_markov import *

def main():
    #api_key, api_secret, access_token, token_secret = sys.argv[1:]
    #twitter = Twython(api_key, api_secret, access_token, token_secret)
    #twitter.update_status(status="Hey!")

    return 0

def generateTweet():

    # fl = open('data/bspears_sample.txt', 'r')

    fl = open('data/small_sample.txt', 'r')
    lines = fl.readlines()

    ###TODO: string parsing here!!!!!

    
    # print lines[0:4];
    # print " ".join(lines)
    gen  = generateModel(" ".join(lines[:len(lines)/2]), " ".join(lines[len(lines)/2:-1]), 2)

    return gen

if __name__ == '__main__':
    print generateTweet()
