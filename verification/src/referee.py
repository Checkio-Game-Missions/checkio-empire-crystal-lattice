from checkio_referee import RefereeCodeGolf


import settings_env
from tests import TESTS


cover = """def cover(f, data):
    return f([[[str(ch) for ch in row] for row in grid] for grid in data])
"""


class Referee(RefereeCodeGolf):
    TESTS = TESTS
    DEFAULT_LENGTH = 200
    BASE_POINTS = 20
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "golf"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": None,
        "javascript": None
    }
