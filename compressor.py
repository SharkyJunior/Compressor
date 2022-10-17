from argparse import ArgumentParser

import algorithms.equal as equal
import algorithms.rle as rle

# region ArgumentParser
parser = ArgumentParser(description="Encodes/decodes text files with " +
                        "two ways: Equal with dictionary or RLE",
                        add_help=True)

parser.add_argument('-f', '--file', type=str, help="File to encode/decode",
                    metavar="FILE", required=True)

modeGroup = parser.add_mutually_exclusive_group(required=True)
modeGroup.add_argument('--equal', action="store_true",
                       help="mode: equal with dictionary")
modeGroup.add_argument('--rle', action="store_true", help="mode: RLE")

procGroup = parser.add_mutually_exclusive_group(required=True)
procGroup.add_argument('-e', action="store_true", help="encode")
procGroup.add_argument('-d', action='store_true', help="decode")
# endregion


def main():
    args = parser.parse_args()
    print(args.equal)
    print(args.rle)
    print(args.e)
    print(args.d)
    path = args.file
    if args.equal:
        if args.e:
            equal.encode(path)
        elif args.d:
            equal.decode(path)
    elif args.rle:
        if args.e:
            rle.encode(path)
        elif args.d:
            rle.decode(path)


main()
