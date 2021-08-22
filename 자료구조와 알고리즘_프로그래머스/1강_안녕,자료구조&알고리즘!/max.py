import time 

n = int(input("Number of elements: "))
haystack = [k for k in range(n)]

print("Searching for the maxium value...")

ts = time.time() #현재 시간의 time stamp
maximum = max(haystack) #실행 이후 time stamp
elapsed = time.time() - ts

print("Maximum elemnt = %d, Elapsed time = %.2f" % (maximum, elapsed)) 