import json
from gmodules import functions_dispatch
from extensions import extract_object_keys, get_json_from_file
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


def generate_bad_value_json(input_json, rounds):
    bad_jsons_list = []
    for i in range(0, rounds):
        params_dict = {}
        errors_dict = {}
        bad_list_element = {}
        for x in input_json:
            value, error = bad_value_generator(input_json[x])
            params_dict[x] = value
            errors_dict[x] = error
        bad_list_element['params'] = params_dict
        bad_list_element['errors'] = errors_dict

        bad_jsons_list.append(bad_list_element)
    return bad_jsons_list


def main():
    bad_values = generate_bad_value_json(get_json_from_file('data.json'), 2)
    print(json.dumps(bad_values, indent=2))

if __name__ == '__main__':
    main()
