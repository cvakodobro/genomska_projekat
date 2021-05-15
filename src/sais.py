import argparse
import time
import subprocess
from os.path import isfile
import pysais
import ctypes, sys
# import sys
from Bio import SeqIO


def read_sequence(file_path):
    with open(file_path) as file:
        for record in SeqIO.parse(file, "fasta"):
            return str(record.seq)

def main():
    parser = argparse.ArgumentParser(description="Run SAIS algorithm on the given genome file")
    parser.add_argument("-g", "--genome", dest="file", required=True, help="Genome file")
    parser.add_argument("-sa", "--suffix_array", dest="sa_file", required=True, help="Output file for the suffix array")
    parser.add_argument("-bwt", "--bwt", dest="bwt_file", required=True, help="Output file for the BWT")

    args = parser.parse_args()
    # sys.argv[0]

    if not isfile(args.file):
        print(args.file, " is not a file")
        parser.print_usage()
        return

    text = read_sequence(args.file)
    print("Start printing sequence in file for the SAIS")
    start = time.time()
    sa_file = open("seq.txt", "w")
    sa_file.write(text + '$')
    sa_file.close()
    end = time.time()
    print("Done writing sequence in", end - start, "seconds")

    print("Start SAIS")
    subprocess.check_output(["./main", "seq.txt", args.sa_file, args.bwt_file])
    print("SAIS done")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    main()