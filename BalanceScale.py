listofweight = [16,2]
possible = False
totalpossible = False
balance = [1, 17]
numofweights = listofweight.__len__()
diffweight = abs(balance[0]-balance[1])
diffweight2 = ""
if diffweight in listofweight:
    print(diffweight)
    possible = True
    totalpossible = True
else:
    for x in range(0, numofweights-1):
        diffweight2 = abs(listofweight[x] + listofweight[x+1])
        if diffweight2 == diffweight:
            possible = True
            totalpossible = True
            print(listofweight[x],listofweight[x+1])
            break

if possible == False:
    for y in range(0, numofweights):
        for n in range(0, numofweights):
            if balance[0] + listofweight[y] == balance[1] + listofweight[n]:
                possible = True
                totalpossible = True
                if listofweight[y] > listofweight[n]:
                    print(listofweight[n], listofweight[y])
                else:
                    print(listofweight[y], listofweight[n])

if totalpossible == False:
    print("not possible")
