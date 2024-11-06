from izmiran.datfile import *


def main():
    INPUT_FILENAME = "./input/109705_25.dat"  # Input filename
    OUTPUT_FILENAME = "./output/output.dat"  # Output filename
    FILTER_COLUMND_IDX = 0  # Column index of filtered data
    FILTER_MIN_VAL = 90.0  # Minimum value of filtered data
    FILTER_MAX_VAL = 100.0  # Maximum value of filtered data
    AVG_START_IDX = 0  # Start index
    AVG_END_IDX = 10  # End index. Used half-interval approach, so interval is [0; 10)
    AVG_PERIOD = 5  # Period of averaging

    in_datfile = DatFile()
    in_datfile.read(INPUT_FILENAME)

    reversed_datfile = in_datfile.reverse()
    filtered_datfile = reversed_datfile.filter(column_idx=FILTER_COLUMND_IDX,
                                               min_val=FILTER_MIN_VAL,
                                               max_val=FILTER_MAX_VAL)
    out_datfile = filtered_datfile.avg(AVG_PERIOD,
                                       start_idx=AVG_START_IDX,
                                       end_idx=AVG_END_IDX)

    out_datfile.write(OUTPUT_FILENAME)


if __name__ == '__main__':
    main()
