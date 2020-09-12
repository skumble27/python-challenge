## Importing the necessary modules
import re
import os

## Creating a file path to the source text
pyparagraphfile = os.path.join("Resources","paragraph_2.txt")

## Creating an outputfile
pyparagraphfile_output = os.path.join("Analysis","parapgraph_analysis.txt")

## Changing the terminal directory to the location to the location of the main python script
os.chdir(os.path.dirname(__file__))

total_letter_count = [] 

## Opening and reading the textfile
with open(pyparagraphfile) as textfile:
    paragraph2 = textfile.read().replace("\n", " ")
    
    
    ## First we split all the words into seperate elements
    wordsplit = re.findall("(\S+)", paragraph2)
    
    ## Then implement the len function to count the words in the new list
    wordcount = len(wordsplit)

    ## Counting the number of sentences
    sentencesplit = re.findall("(\.\W)", paragraph2)
    
    ## There are sentences that end with a ." which need to be counted as well
    sentencesplit2 = re.findall("(.*)", paragraph2)

    ## We then add up the two seperate counts to determine the total number of sentences
    sentencecount = len(sentencesplit) + len(sentencesplit2)

    ## Counting the number of letters in a word
    for letter in wordsplit:
        total_letter_count.append(len(letter))


## The sum of letters in each word is divided by the total number of words in the paragraph
average_letter_per_word = format(sum(total_letter_count)/(len(wordsplit)),".3f")

## Calculating the average word length of a sentence
average_word_in_sentence = format(len(wordsplit)/sentencecount, ".0f")


## Printing the results into the terminal
print(f'Paragraph Analysis')
print(f'--------------------------------')
print(f'Approximate word count: {wordcount}')
print(f'Approximate sentence count: {sentencecount}')
print(f'Average Letter Count: {average_letter_per_word}')
print(f'Average Sentence Count: {average_word_in_sentence}')

## Exporting analysis to a text file
with open(pyparagraphfile_output, 'w') as textoutfile:
    textoutfile.write(f'Paragraph Analysis\n')
    textoutfile.write(f'--------------------------------\n')
    textoutfile.write(f'Approximate word count: {wordcount}\n')
    textoutfile.write(f'Approximate sentence count: {sentencecount}\n')
    textoutfile.write(f'Average Letter Count: {average_letter_per_word}\n')
    textoutfile.write(f'Average Sentence Count: {average_word_in_sentence}\n')
    textoutfile.close()
