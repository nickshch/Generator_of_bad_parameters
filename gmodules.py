import sys
from extensions import *
from random import randint


def generate_maxlength_string(maxlength):
    return get_rand_string(randint(maxlength, maxlength + 50), string.ascii_letters + string.digits), ERROR_TOO_LONG


def generate_minlength_string(minlength):
    return get_rand_string(randint(0, minlength), string.ascii_letters + string.digits), ERROR_TOO_SHORT


def generate_random_int():
    return randint(-sys.maxsize - 1, sys.maxsize), ERROR_BAD_TYPE


def generate_bad_password():
    variants = {
        0: generate_random_int(),
        1: [get_rand_unreliable_pass(), ERROR_UNRELIABLE]
    }
    return variants[randint(0, 1)]


def generate_bad_phone():
    variants = {
        0: generate_random_int(),
        1: [get_rand_string(randint(1, 20), string.ascii_letters + string.digits + string.punctuation), ERROR_BAD_VALUE]
    }
    return variants[randint(0, 1)]


def generate_bad_birthday():
    variants = {
        0: generate_random_int(),
        1: [get_rand_string(10, string.ascii_letters + string.digits + string.punctuation), ERROR_BAD_VALUE]
    }
    return variants[randint(0, 1)]


def generate_not_allowed_values(input_list):
    if is_domain(input_list[0]):
        return get_rand_domain(randint(2, 6), randint(2, 20)), ERROR_BAD_VALUE
    elif is_sex(input_list[0]):
        return get_rand_string(randint(0, 100), string.ascii_letters + string.digits), ERROR_BAD_VALUE


def generate_none():
    return None, 'required'

functions_dispatch = {
    'allowed_values': generate_not_allowed_values,
    'birthday': generate_bad_birthday,
    'domain': generate_random_int,
    'maxlength': generate_maxlength_string,
    'minlength': generate_minlength_string,
    'password': generate_bad_password,
    'phone': generate_bad_phone,
    'required': generate_none,
    'string': generate_random_int
}
