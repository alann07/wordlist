import logging
import sys
from trie import Trie

logger = logging.getLogger(__name__)

class WordlistService:

    def __init__(self, wordlist_file_name, grid_file_name):
        '''
        Init the service. Create trie and matrix from here.
        :param wordlist_file_name:
        :param grid_file_name:
        '''
        self.MATRIX_MAX_ROWS = 8
        self.MATRIX_MAX_COLS = 8
        self.KNIGH_MOVES = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]

        self.word_trie = self.create_trie_from_file(wordlist_file_name)
        self.matrix = self.create_matrix_from_file(grid_file_name)

    def find_longest_word(self, x, y):
        '''
        Find the longest word starting from this coordindate.
        :param x: grid position. needs to convert to array index.
        :param y: grid position. Needs to convert to array index.
        :return:
        '''

        i_idx = y - 1
        j_idx = x - 1

        word_queue = []
        word_queue.insert(0, (self.matrix[i_idx][j_idx].lower(), i_idx, j_idx))

        long_word_list = []

        while len(word_queue) > 0:
            curr_item = word_queue.pop()
            curr_str = curr_item[0]
            is_curr_str_exist, is_curr_str_reaching_word_end = self.word_trie.search(curr_str)
            if is_curr_str_exist:
                if is_curr_str_reaching_word_end:
                    long_word_list.append(curr_str)
                knight_next_move_positions = self.get_next_knight_move_positions(curr_item[1], curr_item[2])

                for next_pos in knight_next_move_positions:
                    word_queue.insert(0, (curr_str + self.matrix[next_pos[0]][next_pos[1]].lower(), next_pos[0], next_pos[1]))

        longest_word = ''
        max_len = 0
        for word in long_word_list:
            if len(word) > max_len:
                max_len = len(word)
                longest_word = word
        return longest_word

    def create_trie_from_file(self, wordlist_file_name):
        '''
        Create a trie from input file.
        :param wordlist_file_name:
        :return:
        '''
        wordlist_file = None
        try:
            wordlist_file = open(wordlist_file_name, "r")
            wtrie = Trie()

            for line in wordlist_file:
                if line is None or len(line.strip()) == 0:
                    continue
                self.insert_line_to_trie(wtrie, line.strip())
            return wtrie
        except Exception as e:
            logger.error('Wordlist file read error: ' + format(e))
            sys.exit(-1)
        else:
            wordlist_file.close()

    def insert_line_to_trie(self, wtrie, line):
        i = 0
        start_ptr = 0
        end_ptr = 0
        while i < len(line):
            if line[i].isalpha():
                end_ptr = i
            else:
                if start_ptr != i:
                    curr_word = line[start_ptr: end_ptr + 1]
                    wtrie.insert(curr_word.strip().lower())
                start_ptr = i + 1
            i += 1

        if start_ptr <= end_ptr:
            curr_word = line[start_ptr: end_ptr + 1]
            wtrie.insert(curr_word.strip().lower())

    def create_matrix_from_file(self, grid_file_name):
        '''
        Create matrix from grid input file
        :param grid_file_name:
        :return:
        '''
        grid_file = None
        try:
            grid_file = open(grid_file_name, "r")
            matrix = [[0 for m in range(8)] for n in range(8)]

            i = 0
            for line in grid_file:
                if i >= self.MATRIX_MAX_ROWS:
                    sys.exit("exceeding row boundary " + self.MATRIX_MAX_ROWS)
                j = 0
                for char in line.split(' '):
                    if j > self.MATRIX_MAX_COLS:
                        sys.exit("exceeding column boundary " + self.MATRIX_MAX_COLS)
                    matrix[i][j] = char.strip()
                    j += 1
                i += 1

            return matrix
        except Exception as e:
            logger.error('grid file read error: ' + format(e))
            sys.exit(-1)
        else:
            grid_file.close()

    def get_next_knight_move_positions(self, i, j):
        next_positions = []
        for move in self.KNIGH_MOVES:
            next_pos = (i + move[0], j + move[1])
            if 0 <= next_pos[0] < self.MATRIX_MAX_ROWS and 0 <= next_pos[1] < self.MATRIX_MAX_COLS:
                next_positions.append(next_pos)
        return next_positions
