"""convert dfxp files to ass"""
import argparse
import os.path
import timeit
from bs4 import BeautifulSoup as bs

__author__ = 'EngelEatos'

def is_valid_file(parser, arg, ext):
    """check if provided file meets requirements"""
    if not os.path.exists(arg) or not os.path.isfile(arg):
        parser.error("The file %s does not exist!" % arg)
    f_ext = arg[arg.rfind('.') + 1:]
    if f_ext != ext:
        parser.error(
            "Wrong file extension. required '%s', found '%s'" % ext, f_ext)
    return arg

def main():
    """main"""
    print("Coded by " + __author__)
    parser = argparse.ArgumentParser(description="convert dfxp to ass")
    parser.add_argument("-i", dest="input", required=True, help="input dfxp file",
                        metavar="FILE", type=lambda x: is_valid_file(parser, x, "dfxp"))
    parser.add_argument("-o", dest="output", required=True, help="output ass file",
                        metavar="FILE")
    args = parser.parse_args()
    with open(args.input, 'r') as input_file:
        ass = input_file.read()
    soup = bs(ass, 'html.parser')
    p_elements = soup.find('div', attrs={'xml:lang': 'de'}).find_all('p')
    with open(args.output, 'w+') as output_file:
        output_file.write(open('header.txt', 'r').read())
        for element in p_elements:
            output = "Dialogue: 0,%s,%s,Main Dialog,,0,0,0,,%s\n" % (
                element.get('begin'), element.get('end'),
                " ".join(element.text.lstrip().strip().replace("\n", '').split()))
            output_file.write(output)

if __name__ == '__main__':
    print("finished in %.10fs" % timeit.timeit(main, number=1))
