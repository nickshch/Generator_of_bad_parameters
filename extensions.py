import random
import string
import json

keys_for_bad_values = ['required', 'string', 'minlength', 'maxlength', 'allowed_values',
                       'password', 'domain', 'phone', 'birthday']


def rand_string(size):
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(size))


def get_json_from_file(file):
    with open(file, 'r') as fp:
        data = json.load(fp)
    return data


def extract_object_keys(input_object):
    keys_from_object = []
    for key in input_object:
        if key in keys_for_bad_values:
            keys_from_object.append(key)
        elif isinstance(key, dict):
            for subkey in key:
                if subkey in keys_for_bad_values:
                    keys_from_object.append(key)

    return keys_from_object
