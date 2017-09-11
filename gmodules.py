import sys
from extensions import *
from random import randint

##TODO all errors to constants
def generate_maxlength_string(maxlength):
    return get_rand_string(randint(maxlength, maxlength + 50), string.ascii_letters + string.digits), 'toolong'


def generate_minlength_string(minlength):
    return get_rand_string(randint(0, minlength), string.ascii_letters + string.digits), 'weak'


def generate_random_int():
    return randint(-sys.maxsize - 1, sys.maxsize), 'badtype'


def generate_bad_password():
    variants = {
        0: generate_random_int(),
        1: [get_rand_unreliable_pass(), 'unreliable']
    }
    return variants[randint(0, 1)]


def generate_not_allowed_values(input_list):
    if is_domain(input_list[0]):
        return get_rand_domain(randint(2, 6), randint(2, 20)), 'badvalue'
    elif is_sex(input_list[0]):
        return get_rand_string(randint(0, 100), string.ascii_letters + string.digits), 'badvalue'


def generate_none():
    return None, 'required'

functions_dispatch = {
    'allowed_values': generate_not_allowed_values,
    'birthday': generate_random_int,
    'domain': generate_random_int,
    'maxlength': generate_maxlength_string,
    'minlength': generate_minlength_string,
    'password': generate_bad_password,
    'phone': generate_random_int,
    'required': generate_none,
    'string': generate_random_int
}
