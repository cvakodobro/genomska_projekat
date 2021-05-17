from collections import Counter
import time


class BwtFmInterface:
    def __init__(self, text, suffix_array_factor=None, tally_factor=None, suffix_array_file=None, bwt_file=None):
        self._suffix_array_file = suffix_array_file
        self._bwt_file = bwt_file
        self._suffix_array_factor = suffix_array_factor
        self._tally_factor = tally_factor
        self._text = text + '$'

        print("Start building suffix array")
        start = time.time()
        self._suffix_array = self._build_suffix_array()
        end = time.time()
        print("Done building suffix array in", end - start, "seconds")

        print("Start building BWT")
        start = time.time()
        self._bwt = self._build_bwt()
        end = time.time()
        print("Done building BWT in", end - start, "seconds")

        self._counts_per_char = self._build_counts_per_char()
        self._first_column = self._build_first_column()

    def _build_suffix_array(self):
        pass

    def _build_bwt(self):
        if self._bwt_file == None:
            bwt = [self._text[suffix_start - 1] if suffix_start != 0 else '$' for suffix_start in self._suffix_array]
            return ''.join(bwt)
        else:
            with open(self._bwt_file, "r") as file:
                return file.read()

    def _build_counts_per_char(self):
        return dict(Counter(self._bwt))

    def _build_first_column(self):
        first_column = {}
        total_count = 0
        for c, count in sorted(self._counts_per_char.items()):
            first_column[c] = (total_count, total_count + count)
            total_count += count
        return first_column

    def _get_b_rank(self, bwt_index):
        pass

    def _get_first_column_index(self, c, b_rank):
        return self._first_column[c][0] + b_rank

    def _left_mapping(self, bwt_index):
        c = self._bwt[bwt_index]
        b_rank = self._get_b_rank(bwt_index)
        return self._get_first_column_index(c, b_rank)

    def _position_in_text(self, first_column_index):
        pass

    def _find_predecessors_in_range(self, c, range):
        pass

    def find_pattern(self, pattern):
        if not pattern:
            return None
        if pattern[-1] not in self._counts_per_char or pattern[-1] == '$':
            return None
        start, end = self._first_column[pattern[-1]]
        current_range = (start, end - 1)
        for c in pattern[-2::-1]:
            current_range = self._find_predecessors_in_range(c, current_range[0], current_range[1])
            if current_range == None:
                return None
        # return [self._position_in_text(i) for i in range(current_range[0], current_range[1] + 1)]
        return current_range[1]-current_range[0]+1