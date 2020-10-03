import os

def split_file(inputfile, file_size):
    count = 0                                       # counter
    name = 1                                        # file namer
    temp_data = []                                  # hold data temporarily

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
            count = 0
            name += 1
            outfile.close()

def mergearray(array):
    if(len(array) > 1):
        # divide array to 2
        mid = int(len(array) / 2)
        left = array[:mid]
        right = array[mid:]

        # sort by position
        mergearray(left)
        mergearray(right)

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
        infile = open("file0" + str(i+1) + ".txt", "r")
        for j in infile:
            hold.append(int(j))
        infile.close()

        os.remove("file0" + str(i+1) + ".txt")

        outfile = open("file0" + str(i+1) + ".txt", "w")
        mergearray(hold)
        for j in range(len(hold)):
            outfile.write(str(hold[j]))
            if(j < len(hold)-1):
                outfile.write("\n")
        hold.clear()
        outfile.close()

infile = open("test.txt", 'r')
file_size = os.stat("test.txt").st_size

split_file(infile, file_size)
sort_allfiles(file_size)

infile.close()