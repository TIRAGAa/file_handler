import argparse

parser = argparse.ArgumentParser()

# Options, именованные аргументы
parser.add_argument('--file', type=str, dest='file_names', nargs='+',
                    help='file names',)
parser.add_argument('--report', choices=['average-gdp', ...],
                    help='report type')

args = parser.parse_args()


if args.report == 'average-gdp':
    for file_name in args.file_names:
        with open(file_name, 'r') as f:
            data = f.read()
        print(data)

print(args)
