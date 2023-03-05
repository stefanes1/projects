import numpy

#rules
#each column must add to 42
#apart from the base ring, the first layer (ring11, ring22, ring33, ring44) will always be included in the solution

#we require ring11[i] + ring22[j] + ring33[k] + ring44[l] = 42
#The gaps are denoted by "g". Where there is "g", we can use a ring in a lower position. For example, ring44[i] = "g". Then
#we can use ring34[i]. If this is also "g" we can use ring24[i]. This goes down to the base ring
#where there are no gaps.

#base ring
base1 = [12,2,5,10,7,16,8,7,8,8,3,4]
base2 = [6,3,3,14,14,21,21,9,9,4,4,6]
base3 = [7,8,9,10,11,12,13,14,15,4,5,6]
base4 = [11,14,11,14,14,11,14,11,14,11,11,14]

#first ring
ring11 = [1,0,9,0,12,0,6,0,10,0,10,0]
ring12 = [3,26,6,0,2,13,9,0,17,19,3,12]
ring13 = [9,20,12,3,6,0,14,12,3,8,9,0]
ring14 = [7,0,9,0,7,14,11,0,8,0,16,2]

#second ring
ring22 = [22,0,16,0,9,0,5,0,10,0,8,0]
#1 in position 4 could be 1 or 7
ring23 = [11,26,14,7,12,0,21,6,15,4,9,18]
ring24 = [17,4,5,0,7,8,9,13,9,7,13,21]

#third ring
ring33 = [4,0,7,15,0,0,14,0,9,0,12,0]
ring34 = [7,3,0,6,0,11,11,6,11,0,6,17]

#fourth ring
ring44 = [3,0,6,0,10,0, 7,0,15,0,8,0]

nogaps = 0
onegap = 0
twogaps = 0
threegaps = 0
fourgaps = 0

#Work on Test 42 function
def test42(ring11, ring22, ring33, ring44, ringGap12, ringGap13, ringGap14, ringGap23, ringGap24, ringGap34, baseRing1, baseRing2,
           baseRing3, baseRing4, count1, count2, count3, count4, count5):

   for count in range(1,12):
        #first - check for gaps (this gap check is on a stationary state, therefore it is easier than checking all arrangements for gaps
        # )
        # To check for gaps, add all 8 arguments, telling code to stop adding any more numbers
        # once 4 non-zero numbers have been added. This will account for the "g"s.
        # 2: code needs to stop running once 4 non-zero numbers have been added. DONE.

        #3 code needs to know the position of all other rings at this point

        #fix indexing problem
        idx1 = count + count1
        if idx1 > 11:
            idx1 -= 12
        idx2 = count + count2
        if idx2 > 11:
            idx2 -= 12
        idx3 = count + count3
        if idx3 > 11:
            idx3 -= 12
        idx4 = count + count4
        if idx4 > 11:
            idx4 -= 12
        idx5 = count + count5
        if idx5 > 11:
            idx5 -= 12

        nonZerocount = 0
        placeholder = 0

        #Check if base tiles are covered by rings above
        base1covered = False
        base2covered = False
        base3covered = False
        base4covered = False


        sumCols = ring44[idx1]

        if sumCols > 0:
            base4covered = True
            placeholder = sumCols
            nonZerocount += 1

        #print(nonZerocount)

        sumCols += ring33[idx2]
        if sumCols > placeholder:
            base3covered = True
            placeholder = sumCols
            nonZerocount += 1

        #print(nonZerocount)

        sumCols += ring22[idx3]
        if sumCols > placeholder:
            base2covered = True
            placeholder = sumCols
            nonZerocount += 1

        #print(nonZerocount)

        sumCols += ring11[idx4]
        if sumCols > placeholder:
            base1covered = True
            placeholder = sumCols
            nonZerocount += 1

        #print(nonZerocount)
        if nonZerocount < 4 and base4covered != True:
            sumCols += ringGap34[idx2]
            if sumCols > placeholder:
                base4covered = True
                placeholder = sumCols
                nonZerocount += 1

        #print(nonZerocount)

        if nonZerocount < 4 and base3covered != True:
            sumCols += ringGap23[idx3]
            if sumCols > placeholder:
                base3covered = True
                placeholder = sumCols
                nonZerocount += 1

        #print(nonZerocount)

        if nonZerocount < 4 and base2covered != True:
            sumCols += ringGap12[idx4]
            if sumCols > placeholder:
                base2covered = True
                placeholder = sumCols
                nonZerocount += 1

        #print(nonZerocount)

        if nonZerocount < 4 and base1covered != True:
            sumCols += baseRing1[idx5]
            if sumCols > placeholder:

                placeholder = sumCols
                nonZerocount += 1

        #print(nonZerocount)

        if nonZerocount < 4 and base4covered != True:
            sumCols += ringGap24[idx3]
            if sumCols > placeholder:
                base4covered = True
                placeholder = sumCols
                nonZerocount += 1

        #print(nonZerocount)


        if nonZerocount < 4 and base3covered != True:
            sumCols += ringGap13[idx4]
            if sumCols > placeholder:
                base3covered = True
                placeholder = sumCols
                nonZerocount += 1

        #print(nonZerocount)

        if nonZerocount < 4 and base2covered != True:
            sumCols += baseRing2[idx5]
            if sumCols > placeholder:
                placeholder = sumCols
                nonZerocount += 1

        #print(nonZerocount)

        if nonZerocount < 4 and base4covered != True:
            sumCols += ringGap14[idx4]
            if sumCols > placeholder:
                base4covered = True
                placeholder = sumCols
                nonZerocount += 1

        #print(nonZerocount)

        if nonZerocount < 4 and base3covered != True:
            sumCols += baseRing3[idx5]
            if sumCols > placeholder:
                placeholder = sumCols
                nonZerocount += 1

        #print(nonZerocount)

        if nonZerocount < 4 and base4covered != True:
            sumCols += baseRing4[idx5]
            nonZerocount += 1

        #print(sumCols)
        if sumCols != 42:
            #print(sumCols)
            return False
        #else:
            #no 42s next to this one. Therefore, we need a new index when a 42 is found
            #print(idx1, idx2, idx3, idx4)
   return True


n42s = 0
#start from the fourth ring
for i in range(12):
    for j in range(12):
        for k in range(12):
            for l in range(12):
                for m in range(12):
                    #replace the gaps with 0s
                    nonZerocount = 0
                    placeholder = 0
                    trialSum = ring44[i]

                    if trialSum > 0:
                        placeholder = trialSum
                        nonZerocount += 1

                    trialSum += ring33[j]
                    if trialSum > placeholder:
                        placeholder = trialSum
                        nonZerocount += 1

                    trialSum += ring22[k]
                    if trialSum > placeholder:
                        placeholder = trialSum
                        nonZerocount += 1

                    trialSum += ring11[l]
                    if trialSum > placeholder:
                        placeholder = trialSum
                        nonZerocount += 1

                    if nonZerocount < 4:
                        trialSum += ring34[j]
                        if trialSum > placeholder:
                            placeholder = trialSum
                            nonZerocount += 1

                    if nonZerocount < 4:
                        trialSum += ring23[k]
                        if trialSum > placeholder:
                            placeholder = trialSum
                            nonZerocount += 1

                    if nonZerocount < 4:
                        trialSum += ring12[l]
                        if trialSum > placeholder:
                            placeholder = trialSum
                            nonZerocount += 1

                    if nonZerocount < 4:
                        trialSum += base1[m]
                        if trialSum > placeholder:
                            placeholder = trialSum
                            nonZerocount += 1

                    if nonZerocount < 4:
                        trialSum += ring24[k]
                        if trialSum > placeholder:
                            placeholder = trialSum
                            nonZerocount += 1

                    if nonZerocount < 4:
                        trialSum += ring13[l]
                        if trialSum > placeholder:
                            placeholder = trialSum
                            nonZerocount += 1

                    if nonZerocount < 4:
                        trialSum += base2[m]
                        if trialSum > placeholder:
                            placeholder = trialSum
                            nonZerocount += 1

                    if nonZerocount < 4:
                        trialSum += ring14[l]
                        if trialSum > placeholder:
                            placeholder = trialSum
                            nonZerocount += 1

                    if nonZerocount < 4:
                        trialSum += base3[m]
                        if trialSum > placeholder:
                            placeholder = trialSum
                            nonZerocount += 1

                    if nonZerocount < 4:
                        trialSum += base4[m]
                        if trialSum > placeholder:
                            placeholder = trialSum
                            nonZerocount += 1

                    #print(nonZerocount)

                    #if trial = 42, we have found a possible solution
                    if trialSum == 42:
                        n42s += 1
                        #print("42")
                        #SOME TEST FUNCTION TO CHECK OTHER VALUES OF RING
                        #check i + 1, i + 2, i + 3 and so on
                        test = test42(ring11, ring22, ring33, ring44, ring12, ring13, ring14, ring23, ring24, ring34, base1, base2, base3, base4, i, j, k, l, m)
                        #print("test = ",test)
                        if test == True:
                            print("solution = ", i, j, k, l, m)



                #B Gaps in 3rd layer



print(n42s)
#print("No gaps:",nogaps, "1 gap:",onegap,"2 gaps:",twogaps,"3 gaps:",threegaps,"4 gaps:",fourgaps)

