from izmiran.datfile import *
import glob
import os


def main():
    INPUT_FOLDER = "./input"  # Input folder path.
    OUTPUT_FOLDER = "./output"  # Output folder path.
    FILTER_COLUMND_IDX = 0  # Column index of filtered data
    FILTER_MIN_VAL = 90.0  # Minimum value of filtered data
    FILTER_MAX_VAL = 100.0  # Maximum value of filtered data
    AVG_START_IDX = 0  # Start index. If doesn't used use None.
    AVG_END_IDX = 10  # End index. Used half-interval approach, so interval is [0; 10). If doesn't used use None.
    AVG_PERIOD = 5  # Period of averaging

    for filepath in glob.glob(f"{INPUT_FOLDER}/*.dat"):
        in_datfile = DatFile()
        in_datfile.read(filepath)

        reversed_datfile = in_datfile.reverse()
        filtered_datfile = reversed_datfile.filter(column_idx=FILTER_COLUMND_IDX,
                                                min_val=FILTER_MIN_VAL,
                                                max_val=FILTER_MAX_VAL)
        out_datfile = filtered_datfile.avg(AVG_PERIOD,
                                        start_idx=AVG_START_IDX,
                                        end_idx=AVG_END_IDX)
        
        in_filename = os.path.splitext(os.path.basename(filepath))[0]
        out_filename = in_filename + "_avg_" + str(AVG_PERIOD)
    
        out_datfile.write(f"{OUTPUT_FOLDER}/{out_filename}.dat")

if __name__ == '__main__':
    main()
