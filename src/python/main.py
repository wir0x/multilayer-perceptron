from src.python.utils.utilsFunctions import *

# Step 1
'''Define input and output vector'''
input_vector = [[1, 0, 1, 0, 1, 1],
                [0, 1, 0, 1, 0, 0],
                [1, 1, 0, 0, 1, 1],
                [0, 0, 1, 1, 1, 1],
                [1, 1, 0, 1, 0, 0]]

output_vector = [[1, 1, 1, 0, 0, 1, 0],
                 [0, 0, 1, 0, 0, 1, 0],
                 [0, 1, 1, 0, 1, 1, 1],
                 [1, 1, 0, 1, 0, 1, 1],
                 [1, 0, 0, 0, 1, 0, 1]]

# Step 2
'''define number of hidden layers'''
hidden_layer_1 = [None] * 4
hidden_layer_2 = [None] * 4


# Step 3
'''define learning factor, weights'''


def random_weight(n):
    pesos = []
    for i in range(n):
        pesos.append(random.uniform(-2, 2))
    return pesos


learning_factor = 0.6
weights = random_weight(67)

product_w_x = []

'''find Net(i)'''


# Step 4
def product_w_x(vector, w):
    _temp_vector = []
    for i in range(len(vector)):
        print("result : ", vector[i] * w[i])
        _temp_vector.append(vector[i] * w[i])
    return sum(_temp_vector)


def sum_vector(vector):
    return sum(vector)