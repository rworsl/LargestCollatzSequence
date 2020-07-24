seqLen = 0
maxLen = 0
printout = ""
finalString = ""
bestNum = 0
j = 2

while j < 1000000:
    i = j
    printout = ""
    seqLen = 0
    while i != 1:
        if i % 2 == 0:
            i /= 2
            seqLen += 1
            printout = printout + str(int(i)) + " -> "
        else:
            i = (i * 3) + 1
            seqLen += 1
            printout = printout + str(int(i)) + " -> "
    if seqLen > maxLen:
        maxLen = seqLen
        bestNum = j
        finalString = printout
    j += 1

print("***FINAL SOLUTION***")
print(printout)
print(seqLen)
print("Answer is " + str(bestNum))
