sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
word = "country"

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
    
    try:
        with open("positions.txt", "w") as f:
            f.write(str(positions) + "\n" + str(unique_words))
    except:
        print("Error with file")

    return unique_words, positions


print(task2(sentence))