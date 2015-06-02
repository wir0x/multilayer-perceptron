from utils.utilsFunctions import *


def test():
    vx = [1, 0, 1, 0, 1, 1]
    vw = [1, 0, 0.5, 1.2, 0.1, 0.5]
    net = get_sum_vector(get_product_vw_vx(vw, vx))
    return get_obtained_output(net)


print(test())


