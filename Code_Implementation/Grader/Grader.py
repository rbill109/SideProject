"""
Created on Thu July 1 2021

@author: yumin cho
"""

import os, sys, subprocess, argparse, time

# Get txt files
file_list = [file for file in os.listdir(os.getcwd()) if file.endswith("txt")]

txt_list = [[],[]]
for file in file_list:
    if file.startswith('in'):
        txt_list[0].append(file)
    else:
        txt_list[1].append(file)
txt_list = list(zip(*txt_list))

# Get my code
parser = argparse.ArgumentParser()
parser.add_argument('--code', '-c', default='AA.py', help='Enter the code name to be graded')
args = parser.parse_args()
my_code = args.code

# Grade the code
for idx, i in enumerate(txt_list):
    batcmd = f"python {my_code} < {i[0]}"
    start = time.time()
    output = subprocess.check_output(batcmd, shell=True, text=True).strip()
    end = time.time() - start
    if end > 1:
        print("Time Exceed...")
    else:
        try:
            with open(i[1], "rt") as f:
                answer = ''.join(f.readlines()).strip()
        except:
            with open(i[1], "rt", encoding="utf16") as f:
                answer = ''.join(f.readlines()).strip()
        if output == answer:
            print(f"Problem {idx+1}: Correct! =>{end: .3f}s")
        else:
            print(f"Problem {idx+1}: Wrong...")

