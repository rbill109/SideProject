"""
Created on Thu July 1 2021

@author: yumin cho
"""

import re, os, shutil, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--opt', '-o', default='copy', help='Remove or Copy Grader.py')
args = parser.parse_args()
opt = args.opt

section = [file for file in os.listdir(os.getcwd())]
for path in section:
    for (path, dir, _) in os.walk(os.path.join(".",path)):
        subdir = [i for i in dir if re.compile(r"\d. ").search(i)]
        for i in subdir:
            copypath = os.path.join(path, i)
            if opt == "copy":
                shutil.copyfile("Grader.py", os.path.join(copypath,"Grader.py"))
            else:
                os.remove(os.path.join(copypath,"Grader.py"))
        break