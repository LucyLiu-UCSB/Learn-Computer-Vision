import argparse

parser = argparse.ArgumentParser()

## add a positional argument using add_argument() including a help
parser.add_argument('first_number', help='this is the string text in connection with fisrt_argument', type=int)
# We add 'second_number' argument using add_argument() including a help The type of this argument is int
# note that the default is str
parser.add_argument("second_number", help="second number to be added", type=int)

## ArgumentParser parses arguments through the parse_args() method:
args = parser.parse_args()
print("args: '{}'".format(args))
print("the sum is: '{}'".format(args.first_number + args.second_number))

## Additionally, the arguments can be stored in a dictionary calling vars() function:
args_dict = vars(parser.parse_args())
# We print this dictionary:
print("args_dict dictionary: '{}'".format(args_dict))

## get and print the first argument of the script
print("first raw argument is '{}'".format(args.first_number))
# For example, to get the first argument using this dictionary:
print("first argument from the dictionary: '{}'".format(args_dict["first_number"]))



# run python Chapter3_argparse.py -h