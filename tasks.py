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

print(task1(sentence, word))