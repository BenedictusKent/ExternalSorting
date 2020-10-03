import random
import time

outfile = open("input.txt", "w")

TOTAL_NUM = 100000000                   # 1bil: ~10GB   100mil: ~1GB

start = time.time()
for i in range(TOTAL_NUM):
    n = random.randint(-2**31, 2**31-1)
    outfile.write(str(n))
    if(i < TOTAL_NUM-1):
        outfile.write("\n")
end = time.time()

print("Time taken: ", str(end-start), "seconds / ", str((end-start)/60), "minutes")

outfile.close()