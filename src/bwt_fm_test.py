import os

import bwt_fm_simple as bfs
import bwt_fm_optimized as bfo


def test(algorithm, text, test, actual, expected):
    assert actual == expected, "type: {}, text: {}, test: {}\n{} <-- expected\n{} <-- actual".format(
        algorithm, text, test, expected, actual)


this_foler = os.path.dirname(os.path.abspath(__file__))


def main():

    simple_bwt_fms = {
        "empty": bfs.BwtFmSimple(""),
        "ABAABA": bfs.BwtFmSimple("ABAABA"),
        "BANANA": bfs.BwtFmSimple("BANANA"),
        "MAMA": bfs.BwtFmSimple("MAMA"),
        "ABRACADABRA": bfs.BwtFmSimple("ABRACADABRA"),
    }

    optimized_bwt_fms = {
        "empty": bfo.BwtFmOptimized("", 2, 2, os.path.join(this_foler, "test\\empty.suffix")),
        "ABAABA": bfo.BwtFmOptimized("ABAABA", 2, 1, os.path.join(this_foler, "test\\abaaba.suffix")),
        "BANANA": bfo.BwtFmOptimized("BANANA", 2, 2, os.path.join(this_foler, "test\\banana.suffix")),
        "MAMA": bfo.BwtFmOptimized("MAMA", 2, 2, os.path.join(this_foler, "test\\mama.suffix")),
        "ABRACADABRA": bfo.BwtFmOptimized("ABRACADABRA", 4, 4, os.path.join(this_foler, "test\\abracadabra.suffix"),
                                          os.path.join(this_foler, "test\\abracadabra.bwt")),
    }

    print("--------------------------- Start testing! ---------------------------")

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    print("Testing suffix array")
    test("simple", "", "suffix_array", simple_bwt_fms["empty"]._suffix_array, [0])
    test("simple", "ABAABA", "suffix_array", simple_bwt_fms["ABAABA"]._suffix_array, [6, 5, 2, 3, 0, 4, 1])
    test("simple", "BANANA", "suffix_array", simple_bwt_fms["BANANA"]._suffix_array, [6, 5, 3, 1, 0, 4, 2])
    test("simple", "MAMA", "suffix_array", simple_bwt_fms["MAMA"]._suffix_array, [4, 3, 1, 2, 0])
    test("simple", "ABRACADABRA", "suffix_array", simple_bwt_fms["ABRACADABRA"]._suffix_array,
         [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2])

    test("optimized", "", "suffix_array", optimized_bwt_fms["empty"]._suffix_array, [0])
    test("optimized", "ABAABA", "suffix_array", optimized_bwt_fms["ABAABA"]._suffix_array, [6, 2, 0, 1])
    test("optimized", "BANANA", "suffix_array", optimized_bwt_fms["BANANA"]._suffix_array, [6, 3, 0, 2])
    test("optimized", "MAMA", "suffix_array", optimized_bwt_fms["MAMA"]._suffix_array, [4, 1, 0])
    test("optimized", "ABRACADABRA", "suffix_array", optimized_bwt_fms["ABRACADABRA"]._suffix_array, [11, 3, 4])

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    print("Testing bwt")
    test("simple", "", "_bwt", simple_bwt_fms["empty"]._bwt, "$")
    test("simple", "ABAABA", "_bwt", simple_bwt_fms["ABAABA"]._bwt, "ABBA$AA")
    test("simple", "BANANA", "_bwt", simple_bwt_fms["BANANA"]._bwt, "ANNB$AA")
    test("simple", "MAMA", "_bwt", simple_bwt_fms["MAMA"]._bwt, "AMMA$")
    test("simple", "ABRACADABRA", "_bwt", simple_bwt_fms["ABRACADABRA"]._bwt, "ARD$RCAAAABB")

    test("optimized", "", "_bwt", optimized_bwt_fms["empty"]._bwt, "$")
    test("optimized", "ABAABA", "_bwt", optimized_bwt_fms["ABAABA"]._bwt, "ABBA$AA")
    test("optimized", "BANANA", "_bwt", optimized_bwt_fms["BANANA"]._bwt, "ANNB$AA")
    test("optimized", "MAMA", "_bwt", optimized_bwt_fms["MAMA"]._bwt, "AMMA$")
    test("optimized", "ABRACADABRA", "_bwt", optimized_bwt_fms["ABRACADABRA"]._bwt, "ARD$RCAAAABB")

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    print("Testing counts per char")
    test("simple", "", "_counts_per_char", simple_bwt_fms["empty"]._counts_per_char, {'$': 1})
    test("simple", "ABAABA", "_counts_per_char", simple_bwt_fms["ABAABA"]._counts_per_char,
         {'A': 4, 'B': 2, '$': 1})
    test("simple", "BANANA", "_counts_per_char", simple_bwt_fms["BANANA"]._counts_per_char,
         {'A': 3, 'B': 1, 'N': 2, '$': 1})
    test("simple", "MAMA", "_counts_per_char", simple_bwt_fms["MAMA"]._counts_per_char,
         {'A': 2, 'M': 2, '$': 1})
    test("simple", "ABRACADABRA", "_counts_per_char", simple_bwt_fms["ABRACADABRA"]._counts_per_char,
         {'A': 5, 'B': 2, 'C': 1, 'D': 1, 'R': 2, '$': 1})

    test("optimized", "", "_counts_per_char", optimized_bwt_fms["empty"]._counts_per_char, {'$': 1})
    test("optimized", "ABAABA", "_counts_per_char", optimized_bwt_fms["ABAABA"]._counts_per_char,
         {'A': 4, 'B': 2, '$': 1})
    test("optimized", "BANANA", "_counts_per_char", optimized_bwt_fms["BANANA"]._counts_per_char,
         {'A': 3, 'B': 1, 'N': 2, '$': 1})
    test("optimized", "MAMA", "_counts_per_char", optimized_bwt_fms["MAMA"]._counts_per_char,
         {'A': 2, 'M': 2, '$': 1})
    test("optimized", "ABRACADABRA", "_counts_per_char", optimized_bwt_fms["ABRACADABRA"]._counts_per_char,
         {'A': 5, 'B': 2, 'C': 1, 'D': 1, 'R': 2, '$': 1})

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    print("Testing first column")
    test("simple", "", "_first_column", simple_bwt_fms["empty"]._first_column,
         {'$': (0, 1)})
    test("simple", "ABAABA", "_first_column", simple_bwt_fms["ABAABA"]._first_column,
         {'A': (1, 5), 'B': (5, 7), '$': (0, 1)})
    test("simple", "BANANA", "_first_column", simple_bwt_fms["BANANA"]._first_column,
         {'A': (1, 4), 'B': (4, 5), 'N': (5, 7), '$': (0, 1)})
    test("simple", "MAMA", "_first_column", simple_bwt_fms["MAMA"]._first_column,
         {'A': (1, 3), 'M': (3, 5), '$': (0, 1)})
    test("simple", "ABRACADABRA", "_first_column", simple_bwt_fms["ABRACADABRA"]._first_column,
         {'A': (1, 6), 'B': (6, 8), 'C': (8, 9), 'D': (9, 10), 'R': (10, 12), '$': (0, 1)})

    test("optimized", "", "_first_column", optimized_bwt_fms["empty"]._first_column,
         {'$': (0, 1)})
    test("optimized", "ABAABA", "_first_column", optimized_bwt_fms["ABAABA"]._first_column,
         {'A': (1, 5), 'B': (5, 7), '$': (0, 1)})
    test("optimized", "BANANA", "_first_column", optimized_bwt_fms["BANANA"]._first_column,
         {'A': (1, 4), 'B': (4, 5), 'N': (5, 7), '$': (0, 1)})
    test("optimized", "MAMA", "_first_column", optimized_bwt_fms["MAMA"]._first_column,
         {'A': (1, 3), 'M': (3, 5), '$': (0, 1)})
    test("optimized", "ABRACADABRA", "_first_column", optimized_bwt_fms["ABRACADABRA"]._first_column,
         {'A': (1, 6), 'B': (6, 8), 'C': (8, 9), 'D': (9, 10), 'R': (10, 12), '$': (0, 1)})

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    print("Testing B-rank array")
    test("simple", "", "_b_rank", simple_bwt_fms["empty"]._b_rank, [0])
    test("simple", "ABAABA", "_b_rank", simple_bwt_fms["ABAABA"]._b_rank, [0, 0, 1, 1, 0, 2, 3])
    test("simple", "BANANA", "_b_rank", simple_bwt_fms["BANANA"]._b_rank, [0, 0, 1, 0, 0, 1, 2])
    test("simple", "MAMA", "_b_rank", simple_bwt_fms["MAMA"]._b_rank, [0, 0, 1, 1, 0])
    test("simple", "ABRACADABRA", "_b_rank", simple_bwt_fms["ABRACADABRA"]._b_rank,
         [0, 0, 0, 0, 1, 0, 1, 2, 3, 4, 0, 1])

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    print("Testing Tally matrix (downsampled)")
    test("optimized", "", "_tally", optimized_bwt_fms["empty"]._tally, {})
    test("optimized", "ABAABA", "_tally", optimized_bwt_fms["ABAABA"]._tally,
         {'A': [1, 1, 1, 2, 2, 3, 4], 'B': [0, 1, 2, 2, 2, 2, 2]})
    test("optimized", "BANANA", "_tally", optimized_bwt_fms["BANANA"]._tally,
         {'A': [1, 1, 1, 3], 'B': [0, 0, 1, 1], 'N': [0, 2, 2, 2]})
    test("optimized", "MAMA", "_tally", optimized_bwt_fms["MAMA"]._tally,
         {'A': [1, 1, 2], 'M': [0, 2, 2]})
    test("optimized", "ABRACADABRA", "_tally", optimized_bwt_fms["ABRACADABRA"]._tally,
         {'A': [1, 1, 4], 'B': [0, 0, 0], 'C': [0, 0, 1], 'D': [0, 1, 1], 'R': [0, 2, 2]})

    def full_tally_rank(bwt_fm):
        tally = {}
        for c in bwt_fm._counts_per_char:
            if c != '$':
                tally[c] = [bwt_fm._get_tally_rank(c, i) for i in range(0, len(bwt_fm._bwt))]
        return tally

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    print("Testing getting Tally-rank")
    test("optimized", "", "full_tally_rank", full_tally_rank(optimized_bwt_fms["empty"]), {})
    test("optimized", "ABAABA", "full_tally_rank", full_tally_rank(optimized_bwt_fms["ABAABA"]),
         {'A': [1, 1, 1, 2, 2, 3, 4], 'B': [0, 1, 2, 2, 2, 2, 2]})
    test("optimized", "BANANA", "full_tally_rank", full_tally_rank(optimized_bwt_fms["BANANA"]),
         {'A': [1, 1, 1, 1, 1, 2, 3], 'B': [0, 0, 0, 1, 1, 1, 1], 'N': [0, 1, 2, 2, 2, 2, 2]})
    test("optimized", "MAMA", "full_tally_rank", full_tally_rank(optimized_bwt_fms["MAMA"]),
         {'A': [1, 1, 1, 2, 2], 'M': [0, 1, 2, 2, 2]})
    test("optimized", "ABRACADABRA", "full_tally_rank", full_tally_rank(optimized_bwt_fms["ABRACADABRA"]),
         {'A': [1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 5, 5],
          'B': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
          'C': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
          'D': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          'R': [0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]})

    def full_b_rank(bwt_fm):
        return [bwt_fm._get_b_rank(i) for i in range(0, len(bwt_fm._bwt))]

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    print("Testing getting B-rank")
    test("simple", "", "full_b_rank", full_b_rank(simple_bwt_fms["empty"]), [0])
    test("simple", "ABAABA", "full_b_rank", full_b_rank(simple_bwt_fms["ABAABA"]), [0, 0, 1, 1, 0, 2, 3])
    test("simple", "BANANA", "full_b_rank", full_b_rank(simple_bwt_fms["BANANA"]), [0, 0, 1, 0, 0, 1, 2])
    test("simple", "MAMA", "full_b_rank", full_b_rank(simple_bwt_fms["MAMA"]), [0, 0, 1, 1, 0])
    test("simple", "ABRACADABRA", "full_b_rank", full_b_rank(simple_bwt_fms["ABRACADABRA"]),
         [0, 0, 0, 0, 1, 0, 1, 2, 3, 4, 0, 1])

    test("optimized", "", "full_b_rank", full_b_rank(optimized_bwt_fms["empty"]), [0])
    test("optimized", "ABAABA", "full_b_rank", full_b_rank(optimized_bwt_fms["ABAABA"]), [0, 0, 1, 1, 0, 2, 3])
    test("optimized", "BANANA", "full_b_rank", full_b_rank(optimized_bwt_fms["BANANA"]), [0, 0, 1, 0, 0, 1, 2])
    test("optimized", "MAMA", "full_b_rank", full_b_rank(optimized_bwt_fms["MAMA"]), [0, 0, 1, 1, 0])
    test("optimized", "ABRACADABRA", "full_b_rank", full_b_rank(optimized_bwt_fms["ABRACADABRA"]),
         [0, 0, 0, 0, 1, 0, 1, 2, 3, 4, 0, 1])

    def full_left_mapping(bwt_fm):
        return [bwt_fm._left_mapping(i) for i in range(0, len(bwt_fm._bwt))]

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    print("Testing getting left mapping")
    test("simple", "", "full_left_mapping", full_left_mapping(simple_bwt_fms["empty"]), [0])
    test("simple", "ABAABA", "full_left_mapping", full_left_mapping(simple_bwt_fms["ABAABA"]), [1, 5, 6, 2, 0, 3, 4])
    test("simple", "BANANA", "full_left_mapping", full_left_mapping(simple_bwt_fms["BANANA"]), [1, 5, 6, 4, 0, 2, 3])
    test("simple", "MAMA", "full_left_mapping", full_left_mapping(simple_bwt_fms["MAMA"]), [1, 3, 4, 2, 0])
    test("simple", "ABRACADABRA", "full_left_mapping", full_left_mapping(simple_bwt_fms["ABRACADABRA"]),
         [1, 10, 9, 0, 11, 8, 2, 3, 4, 5, 6, 7])

    test("optimized", "", "full_left_mapping", full_left_mapping(optimized_bwt_fms["empty"]), [0])
    test("optimized", "ABAABA", "full_left_mapping", full_left_mapping(optimized_bwt_fms["ABAABA"]),
         [1, 5, 6, 2, 0, 3, 4])
    test("optimized", "BANANA", "full_left_mapping", full_left_mapping(optimized_bwt_fms["BANANA"]),
         [1, 5, 6, 4, 0, 2, 3])
    test("optimized", "MAMA", "full_left_mapping", full_left_mapping(optimized_bwt_fms["MAMA"]), [1, 3, 4, 2, 0])
    test("optimized", "ABRACADABRA", "full_left_mapping", full_left_mapping(optimized_bwt_fms["ABRACADABRA"]),
         [1, 10, 9, 0, 11, 8, 2, 3, 4, 5, 6, 7])

    def full_text_positon(bwt_fm):
        return [bwt_fm._position_in_text(i) for i in range(0, len(bwt_fm._bwt))]

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    print("Testing getting position in original text by first column index")
    test("simple", "", "full_text_positon", full_text_positon(simple_bwt_fms["empty"]), [0])
    test("simple", "ABAABA", "full_text_positon", full_text_positon(simple_bwt_fms["ABAABA"]), [6, 5, 2, 3, 0, 4, 1])
    test("simple", "BANANA", "full_text_positon", full_text_positon(simple_bwt_fms["BANANA"]), [6, 5, 3, 1, 0, 4, 2])
    test("simple", "MAMA", "full_text_positon", full_text_positon(simple_bwt_fms["MAMA"]), [4, 3, 1, 2, 0])
    test("simple", "ABRACADABRA", "full_text_positon", full_text_positon(simple_bwt_fms["ABRACADABRA"]),
         [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2])

    test("optimized", "", "full_text_positon", full_text_positon(optimized_bwt_fms["empty"]), [0])
    test("optimized", "ABAABA", "full_text_positon", full_text_positon(optimized_bwt_fms["ABAABA"]),
         [6, 5, 2, 3, 0, 4, 1])
    test("optimized", "BANANA", "full_text_positon", full_text_positon(optimized_bwt_fms["BANANA"]),
         [6, 5, 3, 1, 0, 4, 2])
    test("optimized", "MAMA", "full_text_positon", full_text_positon(optimized_bwt_fms["MAMA"]), [4, 3, 1, 2, 0])
    test("optimized", "ABRACADABRA", "full_text_positon", full_text_positon(optimized_bwt_fms["ABRACADABRA"]),
         [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2])

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    print("Testing finding positions of predeseccors c in a given range")

    test("simple", "", "_find_predecessors_in_range (B, 1, 4)",
         simple_bwt_fms["empty"]._find_predecessors_in_range('B', 1, 4), None)
    test("simple", "", "_find_predecessors_in_range ($, 1, 4)",
         simple_bwt_fms["empty"]._find_predecessors_in_range('$', 1, 4), None)

    test("simple", "ABAABA", "_find_predecessors_in_range (A, 1, 4)",
         simple_bwt_fms["ABAABA"]._find_predecessors_in_range('A', 1, 4), (2, 2))
    test("simple", "ABAABA", "_find_predecessors_in_range (A, 1, 6)",
         simple_bwt_fms["ABAABA"]._find_predecessors_in_range('A', 1, 6), (2, 4))
    test("simple", "ABAABA", "_find_predecessors_in_range (A, 0, 1)",
         simple_bwt_fms["ABAABA"]._find_predecessors_in_range('A', 0, 1), (1, 1))
    test("simple", "ABAABA", "_find_predecessors_in_range (A, 5, 5)",
         simple_bwt_fms["ABAABA"]._find_predecessors_in_range('A', 5, 5), (3, 3))
    test("simple", "ABAABA", "_find_predecessors_in_range (A, 1, 1)",
         simple_bwt_fms["ABAABA"]._find_predecessors_in_range('A', 1, 1), None)
    test("simple", "ABAABA", "_find_predecessors_in_range (B, 1, 4)",
         simple_bwt_fms["ABAABA"]._find_predecessors_in_range('B', 1, 4), (5, 6))
    test("simple", "ABAABA", "_find_predecessors_in_range (B, 1, 2)",
         simple_bwt_fms["ABAABA"]._find_predecessors_in_range('B', 1, 2), (5, 6))
    test("simple", "ABAABA", "_find_predecessors_in_range (B, 0, 0)",
         simple_bwt_fms["ABAABA"]._find_predecessors_in_range('B', 0, 0), None)
    test("simple", "ABAABA", "_find_predecessors_in_range (B, 5, 6)",
         simple_bwt_fms["ABAABA"]._find_predecessors_in_range('B', 5, 6), None)
    test("simple", "ABAABA", "_find_predecessors_in_range (C, 5, 6)",
         simple_bwt_fms["ABAABA"]._find_predecessors_in_range('C', 5, 6), None)

    test("simple", "", "_find_predecessors_in_range (B, 1, 4)",
         optimized_bwt_fms["empty"]._find_predecessors_in_range('B', 1, 4), None)
    test("simple", "", "_find_predecessors_in_range ($, 1, 4)",
         optimized_bwt_fms["empty"]._find_predecessors_in_range('$', 1, 4), None)

    test("optimized", "ABAABA", "_find_predecessors_in_range (A, 1, 4)",
         optimized_bwt_fms["ABAABA"]._find_predecessors_in_range('A', 1, 4), (2, 2))
    test("optimized", "ABAABA", "_find_predecessors_in_range (A, 1, 6)",
         optimized_bwt_fms["ABAABA"]._find_predecessors_in_range('A', 1, 6), (2, 4))
    test("optimized", "ABAABA", "_find_predecessors_in_range (A, 0, 1)",
         optimized_bwt_fms["ABAABA"]._find_predecessors_in_range('A', 0, 1), (1, 1))
    test("optimized", "ABAABA", "_find_predecessors_in_range (A, 5, 5)",
         optimized_bwt_fms["ABAABA"]._find_predecessors_in_range('A', 5, 5), (3, 3))
    test("optimized", "ABAABA", "_find_predecessors_in_range (A, 1, 1)",
         optimized_bwt_fms["ABAABA"]._find_predecessors_in_range('A', 1, 1), None)
    test("optimized", "ABAABA", "_find_predecessors_in_range (B, 1, 4)",
         optimized_bwt_fms["ABAABA"]._find_predecessors_in_range('B', 1, 4), (5, 6))
    test("optimized", "ABAABA", "_find_predecessors_in_range (B, 1, 2)",
         optimized_bwt_fms["ABAABA"]._find_predecessors_in_range('B', 1, 2), (5, 6))
    test("optimized", "ABAABA", "_find_predecessors_in_range (B, 0, 0)",
         optimized_bwt_fms["ABAABA"]._find_predecessors_in_range('B', 0, 0), None)
    test("optimized", "ABAABA", "_find_predecessors_in_range (B, 5, 6)",
         optimized_bwt_fms["ABAABA"]._find_predecessors_in_range('B', 5, 6), None)
    test("optimized", "ABAABA", "_find_predecessors_in_range (C, 5, 6)",
         optimized_bwt_fms["ABAABA"]._find_predecessors_in_range('C', 5, 6), None)

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    print("Testing pattern search")
    test("simple", "", "find_pattern ($)", simple_bwt_fms["empty"].find_pattern("$"), None)
    test("simple", "", "find_pattern ($)", simple_bwt_fms["empty"].find_pattern("A"), None)
    test("simple", "", "find_pattern ($)", simple_bwt_fms["empty"].find_pattern("ANA"), None)

    test("simple", "ABAABA", "find_pattern (A)", set(simple_bwt_fms["ABAABA"].find_pattern("A")), {0, 2, 3, 5})
    test("simple", "ABAABA", "find_pattern (AB)", set(simple_bwt_fms["ABAABA"].find_pattern("AB")), {0, 3})
    test("simple", "ABAABA", "find_pattern (B)", set(simple_bwt_fms["ABAABA"].find_pattern("B")), {1, 4})
    test("simple", "ABAABA", "find_pattern (ABAABA)", set(simple_bwt_fms["ABAABA"].find_pattern("ABAABA")), {0})
    test("simple", "ABAABA", "find_pattern (D)", simple_bwt_fms["ABAABA"].find_pattern("D"), None)
    test("simple", "ABAABA", "find_pattern (ABBB)", simple_bwt_fms["ABAABA"].find_pattern("ABBB"), None)

    test("optimized", "", "find_pattern ($)", optimized_bwt_fms["empty"].find_pattern("$"), None)
    test("optimized", "", "find_pattern ($)", optimized_bwt_fms["empty"].find_pattern("A"), None)
    test("optimized", "", "find_pattern ($)", optimized_bwt_fms["empty"].find_pattern("ANA"), None)

    test("optimized", "ABAABA", "find_pattern (A)", set(optimized_bwt_fms["ABAABA"].find_pattern("A")), {0, 2, 3, 5})
    test("optimized", "ABAABA", "find_pattern (AB)", set(optimized_bwt_fms["ABAABA"].find_pattern("AB")), {0, 3})
    test("optimized", "ABAABA", "find_pattern (B)", set(optimized_bwt_fms["ABAABA"].find_pattern("B")), {1, 4})
    test("optimized", "ABAABA", "find_pattern (ABAABA)", set(optimized_bwt_fms["ABAABA"].find_pattern("ABAABA")), {0})
    test("optimized", "ABAABA", "find_pattern (D)", optimized_bwt_fms["ABAABA"].find_pattern("D"), None)
    test("optimized", "ABAABA", "find_pattern (ABBB)", optimized_bwt_fms["ABAABA"].find_pattern("ABBB"), None)
    print("--------------------------- Testing done! ---------------------------")


if __name__ == '__main__':
    main()
