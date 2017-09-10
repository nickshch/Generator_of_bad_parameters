from gmodules import functions_dispatch
from extensions import extract_object_keys, get_json_from_file, get_rand_domain
from random import randint, seed


def bad_value_generator(input_object):
    seed()
    keys = extract_object_keys(input_object)
    bad_param_id = randint(0, len(keys) - 1)
    param_bad = keys[bad_param_id]
    if isinstance(param_bad, dict):
        dict_key = next(iter(param_bad.keys()))
        dict_value = next(iter(param_bad.values()))
        return functions_dispatch[dict_key](dict_value)
    return functions_dispatch[param_bad]()


def main():
    parsed_json = get_json_from_file('data.json')
    print(extract_object_keys(parsed_json['domain']))
    print(bad_value_generator(parsed_json['domain']))

if __name__ == '__main__':
    main()
