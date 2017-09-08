import sys
import json
from random import randint

from params import json_string
from extensions import rand_string


def bad_login_generator():
    parsed_json = json.loads(json_string)
    print(parsed_json['login'][0])

    bad_param = randint(0, 3)
    if bad_param == 0:
        return randint(-sys.maxsize-1, sys.maxsize)
    elif bad_param == 1:
        return 'None'
    elif bad_param == 2:
        rand_string(randint(0, 3))
    elif bad_param == 3:
        rand_string(randint(32, 100))

print(randint(-sys.maxsize-1, sys.maxsize))
