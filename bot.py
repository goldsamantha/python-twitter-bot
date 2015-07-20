from twython import Twython
import sys
#import json
#from datetime import datetime, timedelta
import random
from markov_aparrish import *
#from markov_aparrish import char_level_generate
#from markov_aparrish import word_level_generate
import os

def main():
    #api_key, api_secret, access_token, token_secret = sys.argv[1:]
    #twitter = Twython(api_key, api_secret, access_token, token_secret)
    #twitter.update_status(status="Hey!")

    return 0

def generateTweet():

    fl = open('data/bspears_sample.txt', 'r')
    lines = fl.readlines()
    gen = word_level_generate(lines, 2, 10);
    # model = build_model(lines,2)
    #gen = generate(model, 2)
    # gen = generate_from_token_lists(model, 2)



    return gen #'hello world'

if __name__ == '__main__':
    print generateTweet()
