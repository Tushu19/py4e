'''
fhand = open('../data/mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    if len(words) >= 3:
        print(words[2])

Exercise 3: Rewrite the guardian code in the above example without two if statements. 
Instead, use a compound logical expression using the "and" logical operator with a single if statement.
'''

fhand = open('../data/mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) >= 3 and words[0] == 'From':
        print(words[2])