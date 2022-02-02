import re

sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU, ASK WHAT YOU CAN DO FOR YOUR COUNTRY." # task 1 and 2
word = "country," # task 2


def readFromFile(fileName):
    try:
        with open(fileName, "r") as f:
            text = f.read()
    except:
        print("Error with file")
    return text

sentences = readFromFile("sentences.txt") # original

def writeToFile(fileName, positions, words):
    try:
        with open(fileName, "w") as f:
            f.write(str(positions) + "\n" + str(words))
    except:
        print("Error with file")

def task1(sentence, word):
    s = sentence.lower().split()
    positions = []
    found = False
    for i in range(0, len(s)):
        if word.lower() == s[i]:
            found = True
            positions.append(i+1)
    return positions if found else "Word not found"

def task2(sentence):
    unique_words = []
    positions = []

    for word in sentence.split():
        if word not in unique_words:
            unique_words.append(word)
    
    for word in sentence.split():
        for u in range(len(unique_words)):
            if unique_words[u] == word:
                positions.append(u+1)
 
    writeToFile("positions.txt", positions, unique_words)

    return unique_words, positions


def task3(sentences):
    unique_words = []
    positions = []
    pattern = "[\w]+|[.,;:?/\']"
    list_sentence = re.findall(pattern, sentences)
    for word in list_sentence:
        if word not in unique_words:
            unique_words.append(word)
    for word in list_sentence:
        for u in range(len(unique_words)):
            if unique_words[u] == word:
                positions.append(u+1)
    writeToFile("task3.txt", positions, unique_words)
    return unique_words, positions

def decompress(fileName):
    text = readFromFile(fileName)
    positions_str = (text[:text.index("\n")][1:-1]).split(",")
    positions = []
    for p in positions_str:
        positions.append(int(p))
    unique_words = (text[text.index("\n"):][2:-1]).split(", ")
       
    recreated = ""
    for p in positions:
        if unique_words[p-1] not in ".,;:?/'":
            recreated += (unique_words[p-1].strip("'")) + ' '
        else:
            recreated += unique_words[p-1].strip("'")

    count = 0
    lst = []
    finalstr = ""
 
    for i in recreated:
        lst.append(i)
        
    for i in lst:
        count += 1
        if i.isalpha():
            if lst[count+1] == " ":
                if lst[count+2] in "'.,;:?/'\"":
                    lst[count+1] = ""
    for i in lst:
        finalstr = finalstr + i
        
    final = finalstr.strip()
    try: 
        f = open("recreated.txt", "w")
        f.write(final)
        f.close()
    except:
        print("Error in decompress")

decompress("task3.txt")