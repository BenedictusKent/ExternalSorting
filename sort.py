import os
import shutil

def split_file(inputfile, file_size):
    count = 0                                                           # counter
    name = 0                                                            # file namer
    temp_data = []                                                      # hold data temporarily

    if(os.path.isdir('text_files')):                                    # if directory exist, delete it
        shutil.rmtree('text_files')

    os.mkdir('text_files/')                                             # make directory for the sake of tidiness
    
    # split files
    for i in inputfile:
        temp_data.append(int(i))
        count += 1
        if(count == int(file_size / 100)):
            outfile = open('file0' + str(name) + '.txt', 'w')           
            for j in range(len(temp_data)):
                outfile.write(str(temp_data[j]))
                if(j < len(temp_data)-1):
                    outfile.write("\n")
            temp_data.clear()
            outfile.close()
            shutil.move('file0' + str(name) + '.txt', 'text_files/')    # move text file to the directory
            count = 0
            name += 1

def sortarray(array):
    if(len(array) > 1):
        # divide array to 2
        mid = int(len(array) / 2)
        left = array[:mid]
        right = array[mid:]

        # sort by position
        sortarray(left)
        sortarray(right)

        i = j = k = 0
        while i<len(left) and j<len(right):
            if(left[i] < right[j]):
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i<len(left):
            array[k] = left[i]
            i += 1
            k += 1
        
        while j<len(right):
            array[k] = right[j]
            j += 1
            k += 1

def sort_allfiles(file_size):
    hold = []
    for i in range(int(file_size/100)):
        infile = open('text_files/file0' + str(i) + '.txt', 'r')
        for j in infile:
            hold.append(int(j))
        infile.close()

        os.remove('text_files/file0' + str(i) + '.txt')

        outfile = open('text_files/file0' + str(i) + '.txt', 'w')
        sortarray(hold)
        for j in range(len(hold)):
            outfile.write(str(hold[j]))
            if(j < len(hold)-1):
                outfile.write("\n")
        hold.clear()
        outfile.close()

def merge(file1, file2, name):
    text1 = file1.readline()
    text2 = file2.readline()

    outfile = open('text_files/file' + str(name) + '.txt', 'w')

    while True:
        if(text1 != '' and text2 != ''):
            if(int(text1) <= int(text2)):
                outfile.write(text1)
                text1 = file1.readline()
            elif(int(text1) > int(text2)):
                outfile.write(text2)
                text2 = file2.readline()
        else:
            outfile.write('\n')
            while(text1 != ''):
                outfile.write(text1)
                text1 = file1.readline()
            while(text2 != ''):
                outfile.write(text2)
                text2 = file2.readline()
            break

    outfile.close()

infile = open("test.txt", 'r')
file_size = os.stat("test.txt").st_size                                 # file size

split_file(infile, file_size)
sort_allfiles(file_size)

# first merge
name = 10
for i in range(9):
    if(i%2 == 0):
        file1 = open('text_files/file0' + str(i) + '.txt', 'r')
        file2 = open('text_files/file0' + str(i+1) + '.txt', 'r')
        merge(file1, file2, name)
        name += 1
        file1.close()
        file2.close()
        os.remove('text_files/file0' + str(i) + '.txt')
        os.remove('text_files/file0' + str(i+1) + '.txt')

# second merge
name = 15
for i in range(4):
    if(i%2 == 0):
        if(os.path.isfile('text_files/file1' + str(i) + '.txt') and os.path.isfile('text_files/file1' + str(i+1) + '.txt')):
            file1 = open('text_files/file1' + str(i) + '.txt', 'r')
            file2 = open('text_files/file1' + str(i+1) + '.txt', 'r')
            merge(file1, file2, name)
            name += 1
            file1.close()
            file2.close()
            os.remove('text_files/file1' + str(i) + '.txt')
            os.remove('text_files/file1' + str(i+1) + '.txt')

# third merge
name = 17
file1 = open('text_files/file14.txt', 'r')
file2 = open('text_files/file15.txt', 'r')
merge(file1, file2, name)
name += 1
file1.close()
file2.close()
os.remove('text_files/file14.txt')
os.remove('text_files/file15.txt')

# last merge
name = 18
file1 = open('text_files/file16.txt', 'r')
file2 = open('text_files/file17.txt', 'r')
merge(file1, file2, name)
name += 1
file1.close()
file2.close()
os.remove('text_files/file16.txt')
os.remove('text_files/file17.txt')

'''
testing = open('text_files/file18.txt', 'r')
count = 0
for i in testing:
    if(int(i) == hold[i]):
        count += 1
print(count)
testing.close()
'''
infile.close()