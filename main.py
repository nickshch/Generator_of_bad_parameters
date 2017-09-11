import json
from generator.extensions import get_json_from_file
from generator.generator import generate_sets_param_error_from_json


def main():
    data_json = get_json_from_file('data.json')
    count_of_sets = 4
    bad_values = generate_sets_param_error_from_json(data_json, count_of_sets)
    print(json.dumps(bad_values, indent=4))

if __name__ == '__main__':
    main()
