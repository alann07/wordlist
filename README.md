#Word List

This is a command line application.

## Design Idea

The very first thought was to use a trie. A trie can store a word list efficiently. We need ony 2 operations for the trie, insert and search.

Both insert and search are O(1) time complexity. Besides, storing the whole word list is taking less space than storing word by word.

## How It Works

* Store the wordlist and the grid in their seperate files. They are the input to the app.
* Choose a position (x, y) on the grid. If not choosen, a random positiuon is generately.
* Directly read the whole word list into a trie. This will save us from other temperoary space usage.
* For the starting position, save the corresponding character and its position into q queue.
* Pop the queue. If the character exists in the trie, look for all possible knight moves from that position and save string and position into queue. If encountering a complete word, store it in a seperate long_word list
* Stop until queue is empty
* Find longest word from long_word list.

I add a flag to iterate every position through the entire grid, in order to search the maximum in this grid.

## How to Run It

Go to the root directory of this project and run "python process_wordlist.py -h", you will get following

```
usage: process_wordlist.py [-h] [-x {1,2,3,4,5,6,7,8}] [-y {1,2,3,4,5,6,7,8}]
                           [-check_all {0,1}]
                           <word-list-txt-file> <grid-matrix-file>

positional arguments:
  <word-list-txt-file>  wordlist input file
  <grid-matrix-file>    grid matrix file

optional arguments:
  -h, --help            show this help message and exit
  -x {1,2,3,4,5,6,7,8}  x position on grid. integer 1 to 8, default=random int
  -y {1,2,3,4,5,6,7,8}  y position on grid, integer 1 to 8, default=random int
  -check_all {0,1}      check entire matrix to find out the longest word

```
I run the following under Python 3.

Case for nothing is found, when specifying a position
```
(venv) ~/dev/wordlist [master] $ python process_wordlist.py LoveLabourLost_Wordlist.txt LoveLabourLost_Grid.txt -x 7 -y 4
2019-06-14 08:33:35,625 - __main__ - INFO - Start Processing Fantastic Word List
2019-06-14 08:33:35,752 - __main__ - INFO - No word found starting (7, 4)
```

Case for a word is found, when specifying a position,
```
(venv) ~/dev/wordlist [master] $ python process_wordlist.py LoveLabourLost_Wordlist.txt LoveLabourLost_Grid.txt -x 2 -y 2
2019-06-14 08:34:05,596 - __main__ - INFO - Start Processing Fantastic Word List
2019-06-14 08:34:05,707 - __main__ - INFO - Longest word found: ear, starting at (2, 2)
```

Case for a word is found, without specifying any position. A random position is generate.
```
(venv) ~/dev/wordlist [master] $ python process_wordlist.py LoveLabourLost_Wordlist.txt LoveLabourLost_Grid.txt 
2019-06-14 00:21:53,311 - __main__ - INFO - Start Processing Fantastic Word List
2019-06-14 00:21:53,422 - __main__ - INFO - Longest word found: cannon, starting at (7, 7)
```

Case for check_all flag set to 1, when all position of the grid is checked in order to find the longest one.
```
(venv) ~/dev/wordlist [master] $ python process_wordlist.py LoveLabourLost_Wordlist.txt LoveLabourLost_Grid.txt -check_all 1
2019-06-14 00:34:23,107 - __main__ - INFO - Start Processing Fantastic Word List
2019-06-14 00:34:23,222 - __main__ - INFO - check entire grid
2019-06-14 00:34:23,240 - __main__ - INFO - Longest word found: honorificabilitudinitatibus, starting at (3, 3)
```

## Performance

* Searching one position costs about 120ms, which includes wordlist and grid loading.
* Searching entire grid costs about 140ms, which includes wordlist and grid loading,

WOW !!!

## TODO

If I can spend more time, I will

* Add unit tests and function tests.
* Check against much large datasets.