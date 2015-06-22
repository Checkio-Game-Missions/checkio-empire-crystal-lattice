from checkio_referee import RefereeCodeGolf, ENV_NAME


import settings_env
from tests import TESTS


cover = """def cover(f, data):
    return f([[[str(ch) for ch in row] for row in grid] for grid in data])
"""


class Referee(RefereeCodeGolf):
    TESTS = TESTS
    DEFAULT_MAX_CODE_LENGTH = 300
    MAX_CODE_LENGTHS = {
        ENV_NAME.JS_NODE: 330
    }
    BASE_POINTS = 10
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "golf"
