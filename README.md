# ExternalSorting
## Definition
A way to sort numbers in a file that has the size bigger than the RAM itself.  
If your RAM is 4 GB, then it is impossible to sort numbers in array that has the size bigger than 4 GB.  
To solve this issue, we can use **External Sorting**.  
This method works by:  
1. Split the big file to smaller chunks [MUST be smaller than the RAM]
2. Sort each and every smaller file with any sorting methods
3. Merge them together in a single file  
Here's the visuals:  
![External Sorting Visuals](img/extsort.jpg)]  

## Dive into Code
### Versions
The Python version I used at the time was Python 3.7.6
### Creating the large file
The large file can be created with **largefile.py**.  The range of numbers is from (-2^31) to (2^31-1)
#### Usage
1. Change the filename (output is a text file).
2. Change the size 
#### Compilation
```
python3 largefile.py
```
#### Limitations
Found no way to make a big file just by specifying the file size.  
Instead, I used total numbers to make the file. Approximately:
* 100 million numbers = 1 GB
* 1 billion numbers = 10 GB  

**WARNING!** This is just an approximation, so at times the file can be bigger or lower than what you want depending on
the number of bytes in each and every line of numbers. 