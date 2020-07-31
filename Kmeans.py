import csv
import random
import matplotlib.pyplot as plt

def center_x(dist):
    sum = 0
    for i in range(len(dist)):
        sum = sum + dist[i][0]
    sum = sum / len(dist)
    return sum

def center_y(dist):
    sum = 0
    for i in range(len(dist)):
        sum = sum + dist[i][1]
    sum = sum / len(dist)
    return sum


data_train = []
with open('raw.txt','r')as f:
    data = csv.reader(f, delimiter='\t')
    for rowIndex,row in enumerate(data):
        data_train.append((float(row[0]),float(row[1])))

point1_x = data_train[0][0]
point1_y = data_train[0][1]
point2_x = data_train[1][0]
point2_y = data_train[1][1]
point3_x = data_train[1][0]
point3_y = data_train[1][1]
center_keep_x1 = 0
center_keep_y1 = 0
center_keep_x2 = 0
center_keep_y2 = 0
center_keep_x3 = 0
center_keep_y3 = 0
i = 0
while True:
    i += 1
    dist1_label = []
    dist2_label = []
    for i in range(len(data_train)):
        dist1 = (pow((point1_x - data_train[i][0]), 2) + pow((point1_y - data_train[i][1]), 2)) ** 0.5
        dist2 = (pow((point2_x - data_train[i][0]), 2) + pow((point2_y - data_train[i][1]), 2)) ** 0.5
        if dist1 < dist2:
            dist1_label.append((data_train[i][0], data_train[i][1]))
        else:
            dist2_label.append((data_train[i][0], data_train[i][1]))
    point1_x = center_x(dist1_label)
    point1_y = center_y(dist1_label)
    point2_x = center_x(dist2_label)
    point2_y = center_y(dist2_label)
    if center_keep_x1 == point1_x and center_keep_y1 == point1_y and center_keep_x2 == point2_x and center_keep_y2 == point2_y:
        break
    else:
        center_keep_x1 = point1_x
        center_keep_y1 = point1_y
        center_keep_x2 = point2_x
        center_keep_y2 = point2_y
print(i)
plt.figure(1)
plt.scatter([each[0] for each in dist1_label], [each[1] for each in dist1_label], c="yellow")
plt.scatter([each[0] for each in dist2_label], [each[1] for each in dist2_label], c="black")
plt.scatter(point1_x, point1_y , c="red", marker = "x")
plt.scatter(point2_x, point2_y , c="blue", marker = "x")
plt.show() 
    
        
    


    


    

    




        
    
    


