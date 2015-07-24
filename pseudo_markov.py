"""
This function takes in text1, text2, and n
    text1: base text to generate the leading phrases
    text2: corrolary text to append to end of t1 phrases
    n: the size of the tokens generated
"""


from random import *

def generatePhrase(t1, n):
    # print T1[:5], "more: ", len(T2)
    ls1 = t1.split()

    # Find a location that is between zero and
    # n places from the end of the list
    location = randrange(0, len(ls1)-n)

    phrase = ' '.join(ls1[location:location+n])
    return phrase


def findPhrase(startWord, corpus, n):
    st = corpus.lower() #.split()

    #TODO: don't just use the fist one you see! Set up a more glamorous
    # algo that randomly chooses an instance of this word
    location = st.find(startWord.lower())

    if (location>=0 and location+ 50 <= len(st)  ):
        return st[location: location+50]

    else:
        return "BAH HUMBUG"



if __name__ == '__main__':
    b_fl = open('data/bspears_sample.txt','r')
    brit = b_fl.read()
    s_fl = open('data/shakes_sample.txt', 'r').read()
    n=8
    phrase = generatePhrase(brit, n)
    print "FIRST PHRASE: " ,phrase
    print "SECOND PHRASE: ", findPhrase(phrase.split()[-1].lower(), s_fl, n)


    # main()
