# David Cabrera
# CS 021
# Assignment 10, exercise #6

# The program prompts the user to enter two file names. The program then makes
# both files lower case, takes away allpunctuation, and creates two sets with the
# words from each file. Then the program displays all the words in both files. the
# words that are in both files, the words unique to each file, and the words in
# either file but not both.


def main():

    # Ask for two file names
    file_name1 = input('Enter the name of the first file: ')

    file_name2 = input('Enter the name of the second file: ')

    # Open the files and except errors
    try:
        infile1 = open(file_name1, 'r')
    except FileNotFoundError:
        print('File not found')
    except IOError:
        print('Error opening file')

    try:
        infile2 = open(file_name2, 'r')
    except FileNotFoundError:
        print('File not found')
    except IOError:
        print('Error opening file')

    # Read contents of both files
    contents1 = infile1.read()

    contents2 = infile2.read()

    # Make text case-insensitive
    contents1 = contents1.lower()

    contents2 = contents2.lower()

    # Replace punctuation with whitespace
    punctuation = '~!@#$%^&*()_+-={}|[]\:";<>?,./'

    for ch in contents1:
        if ch in punctuation:
            contents1 = contents1.replace(ch, "")

    for ch in contents2:
        if ch in punctuation:
            contents2 = contents2.replace(ch, "")

    # Split by word
    contents1 = contents1.split()

    contents2 = contents2.split()

    # Create empty sets
    set1 = set([])

    set2 = set([])

    # Fill sets with words from files
    for word in contents1:
        set1.add(word)

    for word in contents2:
        set2.add(word)

    # Unique words from both files
    print("List of unique words in each file: ", set1 | set2)

    # Words both files have in common
    print("Words contained in both files: ", set1 & set2)

    # Words in the first file but not the second
    print("Words only in", file_name1 + ':', set1 - set2)

    # Words in second file but not first
    print("Words only in", file_name2 + ':', set2 - set1)

    # Words that are in either file but not both
    print("Words in either file,but not both: ", set1 ^ set2)

    # Close files
    infile1.close

    infile2.close
    
    
    
main()
