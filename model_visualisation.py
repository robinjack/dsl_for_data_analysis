import textx
import subprocess
import sys

args = sys.argv

name = args[1]

subprocess.run(f'rm {name}.dot', shell=True)
subprocess.run(f'textx generate {name}.analysis --grammar {name}.tx --target dot', shell=True)
subprocess.run(f'dot -Tpng -O {name}.dot', shell=True)
subprocess.run(f'open {name}.dot.png', shell=True)