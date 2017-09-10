import sys
from extensions import *
from random import randint


def generate_maxlength_string(maxlength):
    return get_rand_string(randint(maxlength, maxlength + 50))


def generate_minlength_string(minlength):
    return get_rand_string(randint(0, minlength))


def generate_random_int():
    return randint(-sys.maxsize - 1, sys.maxsize)


def generate_not_allowed_values(list):
    if is_domain(list[0]):
        return get_rand_domain(randint(2, 6), randint(2, 20))
    elif is_sex(list[0]):
        return get_rand_string(randint(0, 100))


def generate_none():
    return None

functions_dispatch = {
    'allowed_values': generate_not_allowed_values,
    'domain': generate_random_int,
    'maxlength': generate_maxlength_string,
    'minlength': generate_minlength_string,
    'required': generate_none,
    'string': generate_random_int
}
