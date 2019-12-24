import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
MOCKS_DIR = ROOT_DIR + "/test/.mocks/"

try:
    os.mkdir(MOCKS_DIR)
except FileExistsError:
    pass
