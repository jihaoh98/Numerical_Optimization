import numpy as np


def Rosenbrock_function(input_data):
    variable_number = input_data.shape[0]
    function_sum = 0
    for i in range(1, int(variable_number / 2) + 1):
        function_sum = function_sum + 100 * (input_data[2 * i - 2] ** 2 - input_data[2 * i - 1]) ** 2 + \
                       (input_data[2 * i - 2] - 1) ** 2

    return function_sum


def calculate_gradient(input_data):
    current_gradient = np.ones_like(input_data)
    variable_number = input_data.shape[0]
    for i in range(variable_number):
        if i % 2 == 0:
            current_gradient[i] = 2 * (input_data[i] - 1) + 400 * input_data[i] * (input_data[i] ** 2 - input_data[i + 1])
        else:
            current_gradient[i] = 200 * (input_data[i] - input_data[i - 1] ** 2)

    return current_gradient


n = 8
c = 0.5
step_length = 1.0
x_initial = np.array([1.5 for i in range(n)])

x = x_initial.copy()
while np.linalg.norm(calculate_gradient(x)) > 1.0e-5:
    direction = - calculate_gradient(x)
    while Rosenbrock_function(x + step_length * direction) > Rosenbrock_function(x) + c * step_length * np.dot(direction, -direction):
        step_length = step_length / 2

    x = x + step_length * direction

# return final results
print(x)

