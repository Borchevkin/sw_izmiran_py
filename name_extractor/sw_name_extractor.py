# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:55:17 2019
@author: Danil Borchevkin
"""

import glob
import os

def save_to_ascii_file(data_list, out_filepath, header=[]):
    write_list = []

    for data in data_list:
        output_str = ""
        for val in data:
            output_str += str(val) + "\t"
        output_str = output_str[:-1]
        output_str += "\n"
        write_list.append(output_str)

    with open(out_filepath,"w") as f:
        f.writelines(write_list)

def main():
    print("Script is started")

    input_folder = "./input"
    input_ext = ".dat"
    output_folder = "./output"

    files = glob.glob(input_folder + "/*" + input_ext)    

    data_to_save = []

    for filepath in files:
        print("Process >> " + filepath)
        try:
            extracted_date = os.path.basename(filepath)[12:26]
            data_to_save.append([extracted_date])
        except:
            print("Can't process file - " + filepath)
        finally:
            pass

    save_to_ascii_file(data_to_save, output_folder + "/extracted.dat")

if __name__ == "__main__":
    main()