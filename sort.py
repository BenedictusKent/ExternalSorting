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


infile = open("test.txt", 'r')
file_size = os.stat("test.txt").st_size                                 # file size

split_file(infile, file_size)

infile.close()