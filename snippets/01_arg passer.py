import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("--test1", help="test 1")
parser.add_argument("--test2", help="test 2")


args = parser.parse_args()

print(args)
print(args.test1)
print(args.test2)
print(sys.argv)