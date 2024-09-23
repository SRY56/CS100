# Shailesh Yannam
# cs 100 2023S section 012
# HW 07, March 28, 2023

# Problem 1
def file_copy(in_file, out_file):
    iF = open(in_file, 'r')
    oF = open(out_file,'w')
    for line in iF:
        oF.write(line)
    iF.close
    oF.close

file_copy('created_equal.txt', 'copy.txt')

# Problem 2
def file_stats(in_file):
    inFile = open(in_file, 'r')
    linesinList = inFile.readlines()
    lines = len(linesinList)
    inFile.close()
    inFile = open(in_file, 'r')
    data = inFile.read()
    inFile.close()
    words = data.split()
    wordnum = len(words)
    characters = len(data)
    print('lines: ', lines)
    print('words: ', wordnum)
    print('characters: ', characters)
    file_stats('created_equal.txt')

# Problem 3
def repeat_words(in_file, out_file):
    iF1 = open(in_file)
    oF1 = open(out_file, 'w')
    repeat = []
    for line in iF1:
        lineLowercase = line.lower().split()
        for letter in lineLowercase:
            if lineLowercase.count(letter) > 1:
                if letter not in repeat:
                    repeat.append(letter)
                    oF1.write(letter + ' ')
        oF1.write('\n')
    iF1.close()
    iF1.close()
inF = 'catInTheHat.txt'
outF = 'catRepWords.txt'
repeat_words(inF, outF)
