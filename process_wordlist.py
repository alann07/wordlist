import argparse
import logging
import sys
import random
from wordlist_service import WordlistService

logger = logging.getLogger(__name__)


def parse_args():
    wordlist_file_name = '<word-list-txt-file>'
    grid_file_name = '<grid-matrix-file>'
    parser = argparse.ArgumentParser()
    parser.add_argument(wordlist_file_name, help="wordlist input file")
    parser.add_argument(grid_file_name, help="grid matrix file")
    parser.add_argument('-x', help="x position on grid. integer 1 to 8, default=random int", type=int, choices=range(1, 9))
    parser.add_argument('-y', help="y position on grid, integer 1 to 8, default=random int", type=int, choices=range(1, 9))
    parser.add_argument('-check_all', help="check entire matrix to find out the longest word", type=int, default=0, choices=range(0, 2))

    args = parser.parse_args()
    args_dict = vars(args)

    x = args_dict['x']
    if x is None:
        x = random.randint(1, 8)
    y = args_dict['y']
    if y is None:
        y = random.randint(1, 8)

    check_all = args_dict['check_all']

    return args_dict[wordlist_file_name], args_dict[grid_file_name], x, y, check_all


def main():
    logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()],
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("Start Processing Fantastic Word List")
    wordlist_file_name, grid_file_name, x, y, check_all = parse_args()
    wordlist_service = WordlistService(wordlist_file_name, grid_file_name)
    max_len = 0
    longest_word = ''
    if check_all:
        logger.info("check entire grid")
        for x1 in range(1, wordlist_service.MATRIX_MAX_COLS+1):
            for y1 in range(1, wordlist_service.MATRIX_MAX_ROWS + 1):
                long_word = wordlist_service.find_longest_word(x1, y1)
                if len(long_word) > max_len:
                    max_len = len(long_word)
                    longest_word = long_word
                    x, y = x1, y1

    else:
        longest_word = wordlist_service.find_longest_word(x, y)

    if longest_word is None or len(longest_word) == 0:
        logger.info("No word found starting (" + str(x) + ", " + str(y) + ")")
    else:
        logger.info("Longest word found: " + longest_word + ", starting at (" + str(x) + ", " + str(y) + ")")


if __name__ == '__main__':
    main()