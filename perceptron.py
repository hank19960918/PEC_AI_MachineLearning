import csv
import random
import matplotlib.pyplot as plt

notStressed=[]
stressed=[]
with open('raw.txt','r')as f:
    data = csv.reader(f, delimiter='\t')
    for rowIndex,row in enumerate(data):
        if rowIndex<199:
            notStressed.append((float(row[0]),float(row[1]),0))
        else:
            stressed.append((float(row[0]),float(row[1]),1))
random.shuffle(notStressed)
random.shuffle(stressed)
trainingList = notStressed[:99] + stressed[:100]
testingList = notStressed[99:199] + stressed[100:]
trainingNotStressedWife = [each[0] for each in trainingList[:99]]
trainingNotStressedHusband = [each[1] for each in trainingList[:99]]
trainingStressedWife = [each[0] for each in trainingList[99:]]
trainingStressedHusband = [each[1] for each in trainingList[99:]]
learningRate = 0.098
wi = random.random()
wj = random.random()
w0 = random.random()
for time in range(0, 1000):
# while True:
    missClassification=0
    for testingData in testingList:
        if (wi * testingData[0] + wj * testingData[1] + w0)<=0:
            prediction = 0
        else:
            prediction = 1
        if testingData[2]!=prediction:
            missClassification=missClassification+1
    if missClassification < 20:
        print(missClassification)
        break
    random.shuffle(trainingList)
    for trainingData in trainingList:
        if (wi * trainingData[0] + wj * trainingData[1] + w0)<=0:
            yHat=0
        else:
            yHat=1
        wi += learningRate * (trainingData[2] - yHat) * trainingData[0]
        wj += learningRate * (trainingData[2] - yHat) * trainingData[1]
        w0 += learningRate * (trainingData[2] - yHat)
predictions = []
for testingData in testingList:
    if (wi * testingData[0] + wj * testingData[1] + w0)<=0:
        predictions.append(0)
    else:
        predictions.append(1)
    if testingData[2]!=prediction:
            missClassification=missClassification+1
trueNotStressed = [testingList[index] for index in range(len(testingList)) if testingList[index][2] == predictions[index] and testingList[index][2] == 0]
falseNotStressed = [testingList[index] for index in range(len(testingList)) if testingList[index][2] != predictions[index] and testingList[index][2] == 0]
trueStressed = [testingList[index] for index in range(len(testingList)) if testingList[index][2] == predictions[index] and testingList[index][2] == 1]
falseStressed = [testingList[index] for index in range(len(testingList)) if testingList[index][2] != predictions[index] and testingList[index][2] == 1]
plt.figure()
a = [0,-w0/wj]
c = [-w0/wi,0]
plt.plot(a,c)
plt.title("classification result")
plt.ylabel("wife annual incomes ($100,000 units)")
plt.xlabel("husband annual incomes ($100,000 units)")
plt.scatter([each[1] for each in trueNotStressed], [each[0] for each in trueNotStressed], c = "red", label = "true not stressed")
plt.scatter([each[1] for each in falseNotStressed], [each[0] for each in falseNotStressed], c = "red", marker = "x", label = "false not stressed")
plt.scatter([each[1] for each in trueStressed], [each[0] for each in trueStressed], c = "blue", label = "true stressed")
plt.scatter([each[1] for each in falseStressed], [each[0] for each in falseStressed], c = "blue", marker = "x", label = "false stressed")

plt.legend()
plt.show() 
    

