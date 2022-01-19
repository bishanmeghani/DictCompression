# DictCompression

This assessment consists of three tasks.
Candidates should complete all tasks and provide evidence to meet all the marking criteria.

For the following scenario analyse the detailed requirements for each situation and, using suitable algorithms, design a solution to be coded in a suitable high-level programming language. Show the iterative development of the individual solutions with suitable testing throughout the process. Test the final products and evaluate your solutions against the detailed requirements you identified in the analysis.
The results for a task may be used without further testing in any subsequent task, or each of the tasks may be solved as a separate system.

Compressing text

**Task 1**
Develop a program that analyses a sentence that contains several words without punctuation. When a word in that sentence is input, the program identifies all of the positions where the word occurs in the sentence. The system should not be case sensitive: Ask. Ask, ASK should be treated as the same word.
For example, in the sentence
    ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY
The word ‘COUNTRY’ occurs in the 5th and 17th positions.
Analyse the requirements for this system and design, develop, test and evaluate a program to locate and return the position(s) of the word you have selected in a particular sentence or return an error message if the word is not in the sentence.

**Task 2**
Develop a program that identifies individual words in a sentence, stores these in a list and replaces each word in the original sentence with the position of that word in the list.
For example, the sentence
ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY
contains the words ASK, NOT, WHAT, YOUR, COUNTRY, CAN, DO, FOR, YOU
The sentence can be recreated from the positions of these words in this list using the sequence
    1,2,3,4,5,6,7,8,9,1,3,9,6,7,8,4,5
Save the list of words and the positions of these words in the sentence as separate files or as a single file.
Analyse the requirements for this system and design, develop, test and evaluate a program to:
  
  •	identify the individual words in a sentence and store them in a list   
  •	create a list of positions for words in that list  
  •	save these lists as a single file or as separate files.

**Task 3**
Develop a program that builds upon the technique from Task 2 to compress a text file with several sentences, including punctuation. The program should be able to compress a file into a list of words and list of positions to recreate the original file. It should also be able to take a compressed file and recreate the full text, including punctuation and capitalisation, of the original file.
Analyse the requirements for this system and design, develop, test and evaluate a program to compress a text file and reproduce the original text from a compressed file. You will need to create a text file with more than one sentence to test your system.
