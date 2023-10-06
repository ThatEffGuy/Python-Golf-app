#Golf program

#Libraries

import csv

#declare lists
surnameList  = []
forenameList = []
scoreList    = []

#methods functions
def fillLists():
    with open ("scores.txt", "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            surnameList.append(row[0])
            forenameList.append(row[1])
            scoreList.append(int(row[2]))
        #endfor
    #endwith
#can take print out laters
    print(surnameList)
    print(forenameList)
    print(scoreList)
    return surnameList, forenameList, scoreList
#End fill lists

def findMaximum(scoreList):
    maxScore = None
    maxPostition = None
    if len(scoreList)>0:
        maxScore = scoreList[0]
        for index in range(len(scoreList)):
            if scoreList[index]> maxScore:
                maxScore = scoreList[index]
                maxPosition = index
            #end if
        #end for
    #end if
    return maxScore, maxPosition
#end findMax


def findMinimum(scoreList):
    minScore = None
    minPostition = None
    if len(scoreList)>0:
        minScore = scoreList[0]
        for index in range(len(scoreList)):
            if scoreList[index]< minScore:
                minScore = scoreList[index]
                minPosition = index
            #end if
        #end for
    #end if
    return minScore, minPosition

def writeToFile(maxScore,maxPosition, minScore,minPosition):
    #write to file Winner
    winnerName = forenameList[minPosition] + " " + surnameList[minPosition]
    print (winnerName + " had the Lowest score of " + str(minScore))
    with open ("winner.txt","w") as f:
        f.write(winnerName + " had the Lowest score of " + str(minScore))
    #end with

    #write to File loser
    winnerName = forenameList[maxPosition] + " " + surnameList[maxPosition]
    print (winnerName + " had the highest score of " + str(maxScore))
    with open ("loser.txt","w") as f:
        f.write(winnerName + " had the highest score of " + str(maxScore))
    #end with
#end writeToFile

#main program
surnameList, forenameList, scoreList = fillLists()
maxScore, maxPosition = findMaximum(scoreList)
minScore, minPosition = findMinimum(scoreList)
writeToFile(minScore, minPosition, maxScore, maxPosition)

