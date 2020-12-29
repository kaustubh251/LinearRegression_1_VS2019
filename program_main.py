import numpy
import matplotlib.pyplot as plt
file1 = open("datapoints.txt","rt")
z = file1.read()
count = 0
x = {}
y = {}
Z = z.split()
n = len(Z)
count2 = 0
while count != (n-2):
    x[count2] = Z[count]
    y[count2] = Z[count+1]
    count = count + 2
    count2 = count2 + 1
count = 0
X = []
Y = []
for num in x:
    X.append(int(x[count]))
    count +=1
count = 0
for num in y:
    Y.append(int(y[count]))
    count+=1
A = []
count = 0
for num in X:
    arr = [1, num, num*num]
    A.insert(count, arr)
    count+=1
A_T = numpy.transpose(A)
B = numpy.matmul(A_T,A)
C = numpy.matmul(A_T,Y)
D = numpy.linalg.inv(B)
E = numpy.matmul(D,C)
vel = 32
dist = E[0] + E[1]*vel + E[2]*vel*vel
print(dist)

