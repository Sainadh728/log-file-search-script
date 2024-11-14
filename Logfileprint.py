#!/usr/bin/env python3


def search_log_file(file_path,search_word):
    try:
        with open(file_path,'r') as file:
            for line_number,line in enumerate(file,start=1):
                if search_word in line:
                    print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

    except Exception as e:
        print(f"An error occured: {e}")



file_path=input("enter the path to the log file")

search_word=input("enter the word you want to search for:")

search_log_file(file_path,search_word)
