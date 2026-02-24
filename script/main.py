import argparse
from core import main

parser = argparse.ArgumentParser()

parser.add_argument('--files', type=str, dest='file_names', nargs='+',
                    help='file names',)
parser.add_argument('--report', dest='report', help='report type')

args = parser.parse_args()

if __name__ == "__main__":
    main(args.file_names, args.report)
