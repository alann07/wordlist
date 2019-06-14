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

    args = parser.parse_args()
    args_dict = vars(args)

    wordlist_f = None
    try:
        wordlist_f = open(args_dict[wordlist_file_name], "r")
    except Exception as e:
        logger.error('Wordlist file read error: ' + format(e))
        sys.exit(-1)

    grid_f = None
    try:
        grid_f = open(args_dict[grid_file_name], "r")
    except Exception as e:
        logger.error('grid file read error: ' + format(e))
        sys.exit(-1)

    x = args_dict['x']
    if x is None:
        x = random.randint(1, 8)
    y = args_dict['y']
    if y is None:
        y = random.randint(1, 8)

    return wordlist_f, grid_f, x, y


def main():
    logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()],
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    wordlist_file, grid_file, x, y = parse_args()
    wordlist_service = WordlistService()
    longest_word = wordlist_service.find_longest_word(wordlist_file, grid_file, x, y)
    if longest_word is None or len(longest_word) == 0:
        logger.info("No word found starting (" + str(x) + ", " + str(y) + ")")
    else:
        logger.info("Longest word found: " + longest_word + ", starting at (" + str(x) + ", " + str(y) + ")")


if __name__ == '__main__':
    main()