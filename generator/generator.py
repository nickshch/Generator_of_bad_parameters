import json
import random

from .gmodules import generator_modules

from .extensions import extract_object_keys


def generate_value_error_from_object(input_object):
    keys = extract_object_keys(input_object)
    param_for_error_id = random.randint(0, len(keys) - 1)
    param_for_error = keys[param_for_error_id]
    if isinstance(param_for_error, dict):
        dict_key = next(iter(param_for_error.keys()))
        dict_value = next(iter(param_for_error.values()))
        return generator_modules[dict_key](dict_value)
    return generator_modules[param_for_error]()


def generate_sets_param_error_from_json(input_json, rounds):
    random.seed()
    bad_jsons_list = []
    for i in range(0, rounds):
        params_dict = {}
        errors_dict = {}
        bad_list_element = {}
        for x in input_json:
            value, error = generate_value_error_from_object(input_json[x])
            params_dict[x] = value
            errors_dict[x] = error
        bad_list_element['params'] = params_dict
        bad_list_element['errors'] = errors_dict

        bad_jsons_list.append(bad_list_element)
    return bad_jsons_list
