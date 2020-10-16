# -*- coding: utf-8 -*-

"""essai_docopt
Usage:
  essai_docopt.py [options] <input>

Options:
  -h --help         show this
  -o output_file    specify output file [default: ../res.txt]
"""

from docopt import docopt

def main():
    arguments = docopt(__doc__)
    if arguments['<input>'].endswith('.csv'):
        print(arguments['<input>'])

if __name__ == "__main__":
    main()