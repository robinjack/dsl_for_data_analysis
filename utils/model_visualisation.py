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
    if name.endswith('.analysis'):
        name = name[:-len('.analysis')]
    remove_existing_file(name)
    create_model_visualisation(name)
    open_model(name)


def show_options_for_analysis():
    while True:
        fps = [(i, val) for i,val in enumerate(
            [f for f in os.listdir('examples') if f.endswith('.analysis')])]
        for i, val in fps:
            print(' - '.join([str(i), val]))
        name = input()
        try:
            int_input = int(name)
            examine('examples/' + fps[int_input][1])
        except Exception as e:
            examine('examples/' + name)


def main():
    args = sys.argv
    if len(args) > 1:
        name = args[1]
    else:
        name = input()

    examine(name)


if __name__ == "__main__":
    show_options_for_analysis()





