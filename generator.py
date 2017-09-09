import sys
import json
from random import randint, seed

from params import json_string
from extensions import rand_string

parsed_json = json.loads(json_string)
seed()

keys_for_bad_things = ['required', 'string', 'minlength', 'maxlength', 'allowed_values',
                       'password', 'domain', 'phone', 'birthday']

def generate_maxlength_string(maxlength):
    return rand_string(randint(maxlength, maxlength + 50))


def generate_minlength_string(minlength):
    return rand_string(randint(0, minlength))


def generate_random_int():
    return randint(-sys.maxsize - 1, sys.maxsize)


def generate_none():
    return None


dispatch = {
    'maxlength': generate_maxlength_string,
    'string': generate_random_int,
    'required': generate_none
}


def extract_params(input_object):
    keys_from_object = []
    for key in input_object:
        if key in keys_for_bad_things:
            keys_from_object.append(key)
        elif isinstance(key, dict):
            for subkey in key:
                if subkey in keys_for_bad_things:
                    keys_from_object.append(subkey)

    return keys_from_object


def bad_value_generator(object_key):
    keys = extract_params(parsed_json[object_key])
    bad_param_id = randint(0, len(keys) - 1)
    return dispatch[keys[bad_param_id]]()
    # print(parsed_json[object_key][0])


# maxlength = parsed_json['login'][3]['maxlength']
# rand_string(randint(maxlength, maxlength+50))
# for x in parsed_json['login']:
#     if 'maxlength' in x:
#         print('found maxlength')
#
print(bad_value_generator('login'))
