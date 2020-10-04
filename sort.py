import os
import time
import shutil

def split_file(inputfile, filesize):
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
        if(count == filesize):
            outfile = open('file' + str(name) + '.txt', 'w')           
            for j in range(len(temp_data)):
                outfile.write(str(temp_data[j]))
                if(j < len(temp_data)-1):
                    outfile.write("\n")
            temp_data.clear()
            outfile.close()
            shutil.move('file' + str(name) + '.txt', 'text_files/')    # move text file to the directory
            print("file" + str(name) + ".txt splitting complete")
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

def sort_allfiles(number_of_files):
    hold = []
    for i in range(number_of_files):
        infile = open('text_files/file' + str(i) + '.txt', 'r')
        for j in infile:
            hold.append(int(j))
        infile.close()

        os.remove('text_files/file' + str(i) + '.txt')

        outfile = open('text_files/file' + str(i) + '.txt', 'w')
        sortarray(hold)
        for j in range(len(hold)):
            outfile.write(str(hold[j]))
            if(j < len(hold)-1):
                outfile.write("\n")
        hold.clear()
        outfile.close()
        print("file" + str(i) + ".txt done sorting")

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

def iteration(start, end, name):
    for i in range(start, end):
        if(i%2 == 0):
            file1 = open('text_files/file' + str(i) + '.txt', 'r')
            file2 = open('text_files/file' + str(i+1) + '.txt', 'r')
            merge(file1, file2, name)
            print("file" + str(i) + ".txt and file" + str(i+1) + ".txt merge complete")
            name += 1
            file1.close()
            file2.close()
            os.remove('text_files/file' + str(i) + '.txt')
            os.remove('text_files/file' + str(i+1) + '.txt')


TOTAL_NUM = int(input("How many numbers in the file? "))

while True:
    FILE_LIMIT = int(input("How big should each file be when splitted? "))
    if(TOTAL_NUM/FILE_LIMIT >= 230000000):
        print("Separated files are still too big.")
    if(FILE_LIMIT >= TOTAL_NUM/4):
        print("File limit may still be too big to sort right away.")
    else:
        break

while True:
    FILE_NAME = input("Which file to sort? ")
    if(os.path.isfile(FILE_NAME)):
        break
    else:
        print("The file", str(FILE_NAME), "is not found.")

infile = open(FILE_NAME, 'r')                                               # open file

# file should exceed 2.3 GB to use external sort 
if(TOTAL_NUM >= 230000000):
    number_of_files = int(TOTAL_NUM/FILE_LIMIT)

    # split and sort
    start_timer = time.time()                                               # start time
    split_file(infile, FILE_LIMIT)                                          # split files
    sort_allfiles(number_of_files)                                          # sort splitted files
    end_timer = time.time()                                                 # end time

    print("time to split and sort: " + str(end_timer-start_timer) + " seconds / " 
            + str((end_timer-start_timer)/60) + " minutes")

    # merging automated
    start = 0
    end = number_of_files
    temp = end
    name = number_of_files
    start_timer = time.time()
    while temp >= 1:
        iteration(start, end-1, name)
        if(end%2 == 0):
            start = end
        else:
            start = end-1
        temp = int(temp/2)
        end += temp
        name = end
    if(len(os.listdir('text_files/')) == 2):
        iteration(start, end, name+1)
    end_timer = time.time()

    print("time to merge: " + str(end_timer-start_timer) + " seconds / " 
            + str((end_timer-start_timer)/60) + " minutes")

    old_file = os.listdir("text_files/")
    os.rename("text_files/" + old_file[0], "text_files/output.txt")         # rename file to output.txt

# any files less than 2.3 GB
else:
    hold = []
    start_timer = time.time()
    for i in infile:
        hold.append(int(i))
    end_timer = time.time()
    print("time to put in array: " + str(end_timer-start_timer) + " seconds / " 
            + str((end_timer-start_timer)/60) + " minutes")
    
    start_timer = time.time()
    sortarray(hold)
    end_timer = time.time()
    print("time to sort: " + str(end_timer-start_timer) + " seconds / " 
            + str((end_timer-start_timer)/60) + " minutes")

infile.close()