import matplotlib.pyplot as plt
import numpy as np
import math

# Get the input points from the user
#x = np.array([50, 90,   120,  131.2])
#y = np.array([80, 100,  125,  130])

#x = np.array([21,   36, 65,  92,  125, 167, 222, 240, 260, 284])
#y = np.array([0.6,  1,  1.9, 2.7, 3.5, 4.6, 5.6, 5.8, 6,   6.2])
x1 = np.array([8209, 3026,  1331,  9573,  18512, 23903, 58915, 70145, 119934])
y1 = np.array([5819, 2170,  1047,  6539,  11705, 15149, 31182, 36259, 57825])


print ("давление нагрев")
#for i in range (len(x)):
#    y[i] = y[i]  * 0.2 * 9.806
    #x[i] = [i] + 273.1
#    print (y[i])
    
#for i in range (len(x1)):
#    x1[i] = x1[i]  * 0.2 * 9.806
    #x[i] = [i] + 273.1
#    print (y1[i])
    
#print ("давление охлаждение")
#for i in range (9):  
#    y1[i] = y1[i] * 13546 * 9.81 / 1000
#    x1[i] += 273.1
#    print (y1[i])


#while True:
#    x = input("Enter the x-coordinate (or 'q' to quit): ")
#    if x == 'q':
#        break
#    x_dots.append(float(x))
#    y = input("Enter the y-coordinate: ")
#    y_dots.append(float(y))

# Convert the lists to numpy arrays
#x = np.array(x)
#y = np.array(y)

#x1 = np.array(x1)
#y1 = np.array(y1)

# Set the figure size
#plt.figure(figsize=(10, 6))

# Строим график точек
#plt.scatter(x, y)
#plt.scatter(x1, y1)

# Находим коэффициенты прямой по методу наименьших квадратов
#A = np.vstack([x, np.ones(len(x))]).T
#m, c = np.linalg.lstsq(A, y, rcond=None)[0]

#print ("коэффициент наклона прямой по МНК")
#print (m)

# Строим прямую
#y_pred = m * x + c
#plt.plot(x, y_pred, color='red')

# Set the axis labels and title
#plt.xlabel("T, C")
#plt.ylabel("P, Па")
#plt.title("график зависимости P(T)")

# Show the plot
#plt.show()




#for i in range (9):
#    x[i] = 1 / x[i]
#    y[i] = math.log(y[i])
#    x1[i] = 1 / x1[i]
#    y1[i] = math.log(y1[i])

# Set the figure size
plt.figure(figsize=(10, 6))

# Строим график точек
#plt.scatter(x, y)
plt.scatter(x1, y1)

# Находим коэффициенты прямой по методу наименьших квадратов
A1 = np.vstack([x1, np.ones(len(x1))]).T
m1, c1 = np.linalg.lstsq(A1, y1, rcond=None)[0]

# Находим коэффициенты прямой по методу наименьших квадратов
#A = np.vstack([x, np.ones(len(x))]).T
#m, c = np.linalg.lstsq(A, y, rcond=None)[0]

print ("коэффициент наклона прямой по МНК 1:")
print (m1)

#print ("коэффициент наклона прямой по МНК 2:")
#print (m)

# Строим прямую
#y_pred = m * x + c
#plt.plot(x, y_pred, color='blue')

# Строим прямую
y_pred1 = m1 * x1 + c1
#plt.plot(x1, y_pred1, color='yellow')


# Set the axis labels and title
plt.xlabel("исходные данные")
plt.ylabel("сжатые данные")
plt.title("LZW")

# Show the plot
plt.show()
