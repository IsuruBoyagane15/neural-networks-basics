import numpy, os, random

weights = [random.random(), random.random(), random.random()]
bias = 1
learning_rate = 1


def perceptron(input_1, input_2, actual_output):
    predicted_output = input_1 * weights[0] + input_2 * weights[1] + bias * weights[2]
    if predicted_output > 0:  # activation function (here Heaviside)
        predicted_output = 1
    else:
        predicted_output = 0

    error = actual_output - predicted_output
    weights[0] = weights[0] + error * input_1 * learning_rate
    weights[1] = weights[1] + error * input_2 * learning_rate
    weights[2] = weights[2] + error * bias * learning_rate


# training
for i in range(40):
    perceptron(0, 0, 0)
    perceptron(0, 1, 1)
    perceptron(1, 0, 1)
    perceptron(1, 1, 1)


a = int(input())
b = int(input())
output = a * weights[0] + b * weights[1] + bias * weights[2]
if output > 0:  # activation function (here Heaviside)
    output = 1
else:
    output = 0
print(output)