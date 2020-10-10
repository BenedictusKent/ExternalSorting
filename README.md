# ExternalSorting
## Definition
A way to sort numbers in a file that has the size bigger than the RAM itself. If your RAM is 4 GB, then it is impossible
to sort numbers in array that has the size bigger than 4 GB.  
To solve this issue, we can use **External Sorting**.  
This method works by:  
1. Split the big file to smaller chunks [MUST be smaller than the RAM]
2. Sort each and every smaller file with any sorting methods
3. Merge them together in a single file