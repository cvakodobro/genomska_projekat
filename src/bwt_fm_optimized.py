import bwt_fm_interface as bfi


class BwtFmOptimized(bfi.BwtFmInterface):
    def __init__(self, text, suffix_array_factor, tally_factor, suffix_array_file=None, bwt_file=None):
        super().__init__(text, suffix_array_factor, tally_factor, suffix_array_file, bwt_file)

        if self._bwt_file == None:
            self._suffix_array = self._downsample_suffix_array()
        self._tally = self._build_tally()

    def _downsample_suffix_array(self):
        return [position for index, position in enumerate(self._suffix_array) if index % self._suffix_array_factor == 0]

    def _build_suffix_array(self):
        with open(self._suffix_array_file, "r") as file:
            if self._bwt_file != None:
                return [int(position) for index, position in enumerate(file.read().split(' '))
                        if index % self._suffix_array_factor == 0]
            else:
                return[int(x) for x in file.read().split(' ')]

    def _build_tally(self):
        current_count = dict()
        tally = dict()
        for c in self._counts_per_char:
            if c != '$':
                current_count[c] = 0
                tally[c] = []
        for i, c in enumerate(self._bwt):
            if c != '$':
                current_count[c] += 1
            if i % self._tally_factor == 0:
                for c in current_count:
                    tally[c].append(current_count[c])
        return tally

    def _get_b_rank(self, bwt_index):
        c = self._bwt[bwt_index]
        if c == '$':
            return 0
        return self._get_tally_rank(c, bwt_index) - 1

    def _get_tally_rank(self, c, bwt_index):
        tally_index = bwt_index // self._tally_factor
        c_count = self._tally[c][tally_index]
        current_index = tally_index * self._tally_factor + 1
        while (current_index <= bwt_index):
            if self._bwt[current_index] == c:
                c_count += 1
            current_index += 1
        return c_count

    def _position_in_text(self, first_column_index):
        difference = 0
        while (first_column_index % self._suffix_array_factor != 0):
            first_column_index = self._left_mapping(first_column_index)
            difference += 1
        return (self._suffix_array[first_column_index // self._suffix_array_factor] + difference) % len(self._bwt)

    def _find_predecessors_in_range(self, c, start, end):
        if c == '$' or c not in self._counts_per_char:
            return None
        start_tally = self._get_tally_rank(c, start - 1) if start != 0 else 0
        end_tally = self._get_tally_rank(c, end)
        c_count = end_tally - start_tally
        if c_count == 0:
            return None
        else:
            first_b_rank = start_tally
            last_b_rank = end_tally - 1
            return (self._get_first_column_index(c, first_b_rank), self._get_first_column_index(c, last_b_rank))
