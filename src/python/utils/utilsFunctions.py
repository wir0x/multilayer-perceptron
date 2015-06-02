import random
import logging
import math

log = logging


def random_weight(a, z):
    return random.uniform(a, z)


def get_product_vw_vx(vw, vx):
    log.info("product_vw_vx", vw)
    vs = []
    if not vw:
        log.warning("vector weight is empty")
    elif not vx:
        log.warning("vector x input is empty")
    elif len(vw) is not len(vx):
        log.warning("vector x and vector w yours len are not equals")
    else:
        for i in range(len(vw)):
            vs.append(vw[i] * vx[i])
    log.info("product vector ", vs)
    return vs


def get_sum_vector(vector):
    if not vector:
        log.warning("vector empty")

    sum_v = sum(vector)
    log.info("sum vector ", sum_v)
    return sum_v


def get_obtained_output(net):
    net_x = 1 / (1 + math.exp(-net))
    log.info("y_i ", net_x)
    return net_x


def partial_error(obtained_output, desired_output):
    result = (obtained_output - desired_output) * (1 - obtained_output) * obtained_output
    return result



