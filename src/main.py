import os
import time
import sys
import psutil
import argparse
from Bio import SeqIO
from os.path import isfile

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
    genome = input("Full path to genome file: ")
    if not isfile(genome) or genome=="":
        print(genome, " is not a file")
        return

    while True:
        algorithm = input("Choose simple (s) or optimized (o) algorithm (default: o): ")
        if algorithm!="s" and algorithm!="o" and algorithm!="":
            print("Choose valid algorithm (s or o)")
            continue
        else:
            break
    if algorithm=="":
        algorithm="o"

    if algorithm=="o":
        while True:
            try:
                suffix_array_factor = int(input("Choose suffix array factor"))
                tally_matrix_factor = int(input("Choose tally matrix factor"))
            except ValueError:
                print("Insert valid suffix array factor or tally matrix factor")
                continue
            else:
                break

    if algorithm == "o":
        while True:
            suffix_array_file = input("Full path to suffix array file: ")
            if suffix_array_file is None:
                print("Suffix array file is required for optimized algorithm")
                continue
            if not isfile(suffix_array_file):
                print(suffix_array_file, " is not a file")
                continue
            else:
                break

    while True:
        suffix_array_file = input("Full path to suffix array file: ")
        suffix_array_file = None if suffix_array_file=="" else suffix_array_file
        if suffix_array_file is None:
            if algorithm == "o":
                print("Suffix array file is required for optimized algorithm")
                continue
            else:
                break
        if not isfile(suffix_array_file):
            print(suffix_array_file, " is not a file")
            continue
        else:
            break

    while True:
        bwt_file = input("Full path to BWT file: ")
        bwt_file = None if bwt_file == "" else bwt_file
        if bwt_file is not None:
            if not isfile(bwt_file):
                print(bwt_file, " is not a file")
                continue
            else:
                break
        else:
            break

    patterns = input("Insert target patterns (use space as a separator): ")
    if patterns=="":
        patterns=["ATGCATG", "TCTCTCTA", "TTCACTACTCTCA"]
    else:
        patterns=patterns.split(" ")

    print("Start analizing file ", genome)
    text = read_sequence(genome)

    if algorithm == "s":
        print("Start making BwtFmSimple object")
        bwt_fm = bfs.BwtFmSimple(text, suffix_array_file=suffix_array_file, bwt_file=bwt_file)
    else:
        print("Start making BwtFmOptimized object")
        bwt_fm = bfo.BwtFmOptimized(text, suffix_array_factor, tally_matrix_factor,
                                    suffix_array_file, bwt_file)

    for pattern in patterns:
        print("Start searching for", pattern)
        start = time.time()
        positions = bwt_fm.find_pattern(pattern)
        end = time.time()
        print(pattern, "found on", positions if positions is not None else 0, "positions in", end - start, "seconds")

    print("Memory usage is", memory_usage(), "MB")


if __name__ == "__main__":
    main()
