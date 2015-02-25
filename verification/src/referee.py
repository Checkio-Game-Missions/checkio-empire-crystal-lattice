from checkio_referee import RefereeBase

import settings
import settings_env
from tests import TESTS


cover = """def cover(f, data):
    return f([[[str(ch) for ch in row] for row in grid] for grid in data])
"""



class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "check_lattice"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": None,
        "javascript": None
    }
