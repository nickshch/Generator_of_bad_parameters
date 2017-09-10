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
    'minlength': generate_minlength_string,
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
                    keys_from_object.append(key)

    return keys_from_object


def bad_value_generator(object_key):
    keys = extract_params(parsed_json[object_key])
    bad_param_id = randint(0, len(keys) - 1)
    param_bad = keys[bad_param_id]
    if isinstance(param_bad, dict):
        dict_key = next(iter(param_bad.keys()))
        dict_value = next(iter(param_bad.values()))
        return dispatch[dict_key](dict_value)
    return dispatch[param_bad]()


def main():
    print(extract_params(parsed_json['login']))
    print(bad_value_generator('login'))

if __name__ == '__main__':
    main()
