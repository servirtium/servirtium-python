import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
MOCKS_DIR = ROOT_DIR + "/test/.mocks/"

MD_1_DIR = ROOT_DIR + "/test/mocks1"
MD_2_DIR = ROOT_DIR + "/test/mocks2"


try:
    os.mkdir(MOCKS_DIR)
except FileExistsError:
    pass
