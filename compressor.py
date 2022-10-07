import sys
import algorithms.equal as equal
from argparse import ArgumentParser

#region ArgumentParser
parser = ArgumentParser(description="Encodes/decodes text files with two ways: Equal with dictionary or RLE", add_help=True)

parser.add_argument('-f', '--file', type=str, help="File to encode/decode", metavar="FILE", required=True)

modeGroup = parser.add_mutually_exclusive_group(required=True)
modeGroup.add_argument('--equal', action="store_false", help="mode: equal with dictionary")
modeGroup.add_argument('--rle', action="store_false", help="mode: RLE")

procGroup = parser.add_mutually_exclusive_group(required=True)
procGroup.add_argument('-e', action="store_false", help="encode")
procGroup.add_argument('-d', action='store_false', help="decode")
#endregion

def main():
    args = parser.parse_args()
    path = args.file
    if args.equal:
        if args.e:
            equal.encode(path)
        elif args.d:
            equal.decode('q_encoded.txt')


    
main()