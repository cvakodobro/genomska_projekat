import os
import time
import sys
import psutil
import argparse
from os.path import isfile
from Bio import SeqIO

import bwt_fm_simple as bfs
import bwt_fm_optimized as bfo


def read_sequence(file_path):
    with open(file_path) as file:
        for record in SeqIO.parse(file, "fasta"):
            return str(record.seq)


def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024


def main():
    parser = argparse.ArgumentParser(description="Search for patterns in the fasta file")
    parser.add_argument("-a", "--algorithm", dest="algorithm", choices=["s", "o"],
                        required=True, help="Choose simple or optimized algorithm")
    parser.add_argument("-sa_f", "--suffix_array_factor", dest="suffix_array_factor", type=int,
                        choices=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512], default=128, help="Suffix array factor. Default 128")
    parser.add_argument("-t_f", "--tally_factor", dest="tally_matrix_factor", type=int,
                        choices=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512], default=128, help="Tally matrix factor. Default 128")
    parser.add_argument("-sa", "--suffix_array", dest="suffix_array_file", help="Suffix array file")
    parser.add_argument("-bwt", "--bwt", dest="bwt_file", help="BWT file")
    parser.add_argument("-g", "--genome", dest="file", required=True, help="Genome file")
    parser.add_argument("-p", "--patterns", dest="patterns", nargs='+', required=True,
                        help="Patterns to be searched for in the genome")
    args = parser.parse_args()

    if not isfile(args.file):
        print(args.file, " is not a file")
        parser.print_usage()
        return

    if args.algorithm == "o":
        if args.suffix_array_file is None:
            print("Suffix array file is required for optimized algorithm")
            parser.print_usage()
            return
        if not isfile(args.suffix_array_file):
            print(args.suffix_array_file, " is not a file")
            parser.print_usage()
            return

    if args.bwt_file is not None:
        if not isfile(args.bwt_file):
            print(args.bwt, " is not a file")
            parser.print_usage()
            return

    print("Start analizing file ", args.file)
    text = read_sequence(args.file)

    if args.algorithm == "s":
        print("Start making BwtFmSimple object")
        bwt_fm = bfs.BwtFmSimple(text, suffix_array_file=args.suffix_array_file, bwt_file=args.bwt_file)
    else:
        # print("Start making BwtFmOptimized object")
        bwt_fm = bfo.BwtFmOptimized(text, args.suffix_array_factor, args.tally_matrix_factor,
                                    args.suffix_array_file, args.bwt_file)

    for pattern in args.patterns:
        # print("Start searching for", pattern)
        start = time.time()
        positions = bwt_fm.find_pattern(pattern)
        end = time.time()
        print(pattern, "found on", len(positions) if positions != None else 0, "positions in", end - start, "seconds")

    print("Memory usage is", memory_usage(), "MB")


if __name__ == "__main__":
    main()
