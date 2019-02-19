from itertools import permutations
import pandas as pd





# Create list of words in the vertical
def create_vertical(wordlist):

    wl = wordlist
    verticals = []
    for x in range(len(wordlist[0])):
        add = ""
        for y in range(len(wordlist[0])):
            add += wl[y][x]
        verticals.append(add)
    return verticals




f = open("scrabble_words.txt",'r')

# Create a list of all words of desired length, this is for 3 letter words
words = []


for line in f:
    if len(line) == 4:
        words.append(line[0:3])

count = 0
mx = [0,0,0]
testlength = 100

# Get unique word combination
perms = list(permutations(words,3))
for p in perms:

    if (perms.index(p) % 100) == 0:
        print ("%s permutations checked out of %s" % (perms.index(w1), len(perms)))

        verticals = create_vertical(p)
        if (verticals[0] in words) and (verticals[1] in words) and (verticals[2] in words):
            count += 1
print(count)



# Returns a dataframe with counts per wordlength
def len_count():
    f = open("scrabble_words.txt",'r')
    words = []
    for line in f:
        x = line[:len(line)-1]

        words.append(x)

    # Create a list of all words of desired length, this is for 3 letter words
    wordcount = []

    for x in range(2,20):

        count = 0
        for w in words:

            if len(w) == x:
                count += 1

        wordcount.append([x,count])

    df = pd.DataFrame.from_records(wordcount, columns=["Length of Word", "Count"])
    print(df)
