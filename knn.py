import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import random
import heapq

h = []
w = []
with open("raw.txt") as f:
    data = f.readlines()
    for i in data:
        i = i.strip().split('\t')
        h.append(float(i[0]))
        w.append(float(i[1]))
h_unstress = h[0:199]
h_stress = h[199:399]
w_unstress = w[0:199]
w_stress = w[199:399]
# plt.xlabel("Husband") 
# plt.ylabel("Wife")
# plt.scatter(h_unstress, w_unstress, c=(0, 0, 1))
# plt.scatter(h_stress, w_stress, c=(1, 0, 0))

train = [[], [], []]
test = [[], [], []]
stress = shuffle([h_stress, w_stress])
unstress = shuffle([h_unstress, w_unstress])
for i in range(len(stress[0])):
    if i < 100:
        train[0].append(stress[0][i])
        train[1].append(stress[1][i])
        train[2].append(1)
    else:
        test[0].append(stress[0][i])
        test[1].append(stress[1][i])
        test[2].append(1)

for i in range(len(unstress[0])):
    if i < 100:
        train[0].append(unstress[0][i])
        train[1].append(unstress[1][i])
        train[2].append(0)
    else:
        test[0].append(unstress[0][i])
        test[1].append(unstress[1][i])
        test[2].append(0)

train_stress_h = sum(stress[0])/len(stress[0])
train_stress_w = sum(stress[1])/len(stress[1])
train_unstress_h = sum(unstress[0])/len(unstress[0])
train_unstress_w = sum(unstress[1])/len(unstress[1])


right = 0
wrong = 0
result_wrong = [[], []]
for i in range(len(test[0])):
    length_stress = (pow((train_stress_h - test[0][i]), 2) + pow((train_stress_w - test[1][i]), 2)) ** 0.5
    length_unstress = (pow((train_unstress_h - test[0][i]), 2) + pow((train_unstress_w - test[1][i]), 2)) ** 0.5
    if length_stress > length_unstress and test[2][i] == 0:
        right += 1
    elif length_stress > length_unstress and test[2][i] == 1:
        wrong += 1
        result_wrong[0].append(test[0][i])
        result_wrong[1].append(test[1][i])
    if length_stress < length_unstress and test[2][i] == 1:
        right += 1
    elif length_stress < length_unstress and test[2][i] == 0:
        wrong += 1
        result_wrong[0].append(test[0][i])
        result_wrong[1].append(test[1][i])
    
def knn(K):
    wrong_classify = 0
    right_classify = 0
    for j in range(len(test[0])):
        length = []
        for i in range(len(train[0])):
            new_length = 0
            new_length = (pow((train[0][i] - test[0][j]), 2) + pow((train[1][i] - test[1][j]), 2)) ** 0.5
            length.append(new_length)
        test2 = list(map(length.index, heapq.nsmallest(K, length)))
        result_stress = 0
        result_unstress = 0
        for index in test2:
            if train[2][index] == 1:
                result_stress += 1
            elif train[2][index] == 0:
                result_unstress += 1
        if result_stress > result_unstress and test[2][j] == 1:
            right_classify += 1
        elif result_stress > result_unstress and test[2][j] == 0:
            wrong_classify += 1
        elif result_stress < result_unstress and test[2][j] == 0:
            right_classify += 1
        elif result_stress < result_unstress and test[2][j] == 1:
            wrong_classify += 1
    return wrong_classify

classify_result = [[],[]]
for i in range(1,23,2):
    number = knn(i)
    classify_result[0].append(i)
    classify_result[1].append(number)
print(classify_result[0])
print(classify_result[1])
plt.figure(1)
plt.scatter(train[0][0:100], train[1][0:100], c=(0, 0, 1), label = "true not stress")
plt.scatter(train[0][100:], train[1][100:], c=(1, 0, 0), label = "true stress")
plt.scatter(train_stress_h, train_stress_w, c=(1, 1, 0), label = "true stress mean")
plt.scatter(train_unstress_h, train_unstress_w, c=(1, 1, 0), label = "true unstress mean")
plt.scatter(result_wrong[0], result_wrong[1], c=(0, 0, 0), label = "wrong plot")
plt.legend()
# plt.figure(2)
# plt.scatter(test[0][0:100], test[1][0:100], c=(0, 0, 1))
# plt.scatter(test[0][100:], test[1][100:], c=(1, 0, 0))
plt.figure(3)
plt.xlabel("K")
plt.ylabel("classify_wrong")
plt.plot(classify_result[0], classify_result[1], label = "wrong number")
plt.legend()
plt.show()