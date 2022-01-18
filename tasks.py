from re import I, L

sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
word = "Country"

def task1(sentence, word):
    s = sentence.lower().split()
    positions = []
    for i in range(0, len(s)):
        if word.lower() == s[i]:
            positions.append(i)
    return positions

print(task1(sentence, word))