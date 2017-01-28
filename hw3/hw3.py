#---------------------------------------------------------
# Anna Cho
# anna.cho@ischool.berkeley.edu
# Homework #3
# September 20, 2016
# hw3.py
# Main
#---------------------------------------------------------

from BST import *

def read_file(filename):
    with open(filename, 'rU') as document:
        text = document.read()
    filter_punc = lambda t: ''.join([x.lower() for x in t if x.isalpha()])
    words = [x for x in map(filter_punc, text.split()) if x]
    return words

def user_input(tree):
    query = input('Query? ')
    while query != 'terminate':
        if query == 'terminate':
            break
        elif query == 'stats':
            print('Number of entries: {}'.format(tree.size()))
            print('Depth: {}'.format(tree.height()))
            query = input('Query? ')
        else:
            print('The word "{}" appears {} times in the tree.'.format(query, tree.find(query)))
            query = input('Query? ')

def main():
    while(True):
        print("Enter the file name to read:")
        filename = input('> ')
        try:
            words = read_file(filename)
        except IOError:
            print("Unable to find the file {}".format(filename))
        else:
            tree = BSTree()
            for word in words:
                tree.add(word)
            break
    user_input(tree)

    ######################
    # Begin Student Code #
    ######################
    #Functions for use
    # tree.add(word)
    # tree.find(word)
    # tree.size()
    # tree.height()
    # tree.inOrderPrint()


if __name__ == "__main__":
    main()