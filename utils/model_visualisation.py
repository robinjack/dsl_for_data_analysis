import textx
import subprocess
import sys
import os
from utils.const import GRAMMAR_FILE_PATH



def remove_existing_file(name):
    if os.path.exists(f'{name}.dot'):
        subprocess.run(f'rm {name}.dot', shell=True)


def create_model_visualisation(name, grammar=GRAMMAR_FILE_PATH):
    subprocess.run(f'textx generate {name}.analysis --grammar {grammar} --target dot', shell=True)
    subprocess.run(f'dot -Tpng -O {name}.dot', shell=True)

def open_model(name):
    subprocess.run(f'open {name}.dot.png', shell=True)


def examine(name : str) -> None:
    remove_existing_file(name)
    create_model_visualisation(name)
    open_model(name)


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        name = args[1]
    else:
        name = input()

    examine(name)




