from checkio_referee import RefereeCodeGolf

import settings
import settings_env
from tests import TESTS


cover = """def cover(f, data):
    return f([[[str(ch) for ch in row] for row in grid] for grid in data])
"""


class Referee(RefereeCodeGolf):
    TESTS = TESTS
    DEFAULT_LENGTH = 200
    BASE_POINTS = 20
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "golf"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": None,
        "javascript": None
    }
