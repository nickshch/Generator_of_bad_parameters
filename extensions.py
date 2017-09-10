import random
import string
import json
import re

KEYS_FOR_BAD_VALUES = ['required', 'string', 'minlength', 'maxlength', 'allowed_values',
                       'password', 'domain', 'phone', 'birthday']
SEX_LIST = ['male', 'female']


def get_rand_string(size):
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(size))


def get_rand_domain(*argv):
    domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(argv[0]))
    for i in range(1, len(argv)):
        domain = '.' + domain
        domain = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(argv[i])) + domain
    return domain


def get_json_from_file(file):
    with open(file, 'r') as fp:
        data = json.load(fp)
    return data


def is_domain(input_string):
    if re.match(r'[a-z0-9\-]{2,}\.[a-z]{2,}', input_string) is None:
        return False
    else:
        return True


def is_sex(input_string):
    if input_string in SEX_LIST:
        return True
    else:
        return False


def extract_object_keys(input_object):
    keys_from_object = []
    for key in input_object:
        if key in KEYS_FOR_BAD_VALUES:
            keys_from_object.append(key)
        elif isinstance(key, dict):
            for subkey in key:
                if subkey in KEYS_FOR_BAD_VALUES:
                    keys_from_object.append(key)

    return keys_from_object
