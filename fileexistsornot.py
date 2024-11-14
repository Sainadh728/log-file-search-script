#!/usr/bin/env python3


import os


file_path=input("enter the file name")

if os.path.exists(file_path):
    print(f"{file_path} exists.")
else:
    print(f"{file_path} does not exists")
