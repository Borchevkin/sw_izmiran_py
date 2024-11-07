import glob
import csv
import os

def decimate_file(f_in, f_out, decima):
    input_lines = None
    output_lines = list()
    with open(f_in, "r") as f:
        input_lines = f.readlines()

    for idx in range(0, len(input_lines), decima):
        output_lines.append(input_lines[idx])

    with open(f_out, "w") as f:
        f.writelines(output_lines)

def main():
    DECIMA = 5      # Change this for decimate exry X string

    print("Script is started")

    files = glob.glob("./input/*.txt")    

    for filepath in files:
        print("Process >> " + filepath)

        try:
            out_filepath = "./output/" + os.path.splitext(os.path.basename(filepath))[0] + "_every_" + str(DECIMA) + ".txt"
            decimate_file(filepath, out_filepath, DECIMA)
    
        except Exception as e:
            print("Cannot process >> ", filepath)
            print("Reason >> " + str(e))
            
        finally:
            print()

    print("Script is finished")

if __name__ == "__main__":
    main()