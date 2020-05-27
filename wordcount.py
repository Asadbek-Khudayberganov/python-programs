# For sys.argv gloval command line arguments list
import sys

def main():
    """ Counts the words in a text file. """
    if len(sys.argv) < 2:
           # Did the user not supply a file name?
           print('Usage: python wordcount <filename>')
           print('      where <filename> is the name of text file. ')
    else:
        # User provided fle name
        filename = sys.argv[1]
        counters = {}
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            for word in words:
                word = word.upper()
                if word not in counters:
                    counters[word] = 1
                else:
                    counters[word] +=1
            # Report the counts for each word
            for word,count in counters.items():
                print(word, count)

if __name__ == '__main__':
    main()
