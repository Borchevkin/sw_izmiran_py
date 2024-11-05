from izmiran.datfile import *

def main():
    input_filename = "./input/109705_25.dat"    # Input filename
    output_filename = "./output/output.dat"  # Output filename
    start_idx = 0   # Start index
    end_idx = 10    # End index. Used half-interval approach, so interval is [0; 10)
    period = 5      # Peroid of averaging

    in_datfile = DatFile()
    in_datfile.read(input_filename)
    
    # NOTE: it's specific only for v0.1.0 izmiran module.
    # NOTE: reverse field directly
    in_datfile.data_list_of_records.reverse()

    out_datfile = in_datfile.avg(period, start_idx=start_idx, end_idx=end_idx)
    out_datfile.write(output_filename)

if __name__ == '__main__':
    main()