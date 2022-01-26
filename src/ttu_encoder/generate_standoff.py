# -*- coding: utf-8 -*-

import argparse
import sys
from ttu_encoder.modifiers.modifiers import Standoff
from ttu_encoder.interview import Interview
from ttu_encoder import __version__


__author__ = "Clifford Wulfman"
__copyright__ = "Clifford Wulfman"
__license__ = "mit"


def parse_args(args):
    parser = argparse.ArgumentParser(
        description="export standoff places to tsv")
    parser.add_argument(
        "--version",
        action="version",
        version="ttu-encoder {ver}".format(ver=__version__))

    parser.add_argument('file', help="the TEI document")

    parser.add_argument('-o', '--outfile',
                        dest="outfile",
                        default=sys.stdout.buffer,
                        help="output file (stdout by default)")

    return parser.parse_args(args)


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    interview = Interview()
    interview.read(args.file)
    modifier = Standoff(interview)
    modifier.modify()
    interview.write(args.outfile)


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()