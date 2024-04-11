#!usr/bin/env python3

"""
A script to check whether your uploaded predictions file is in the right format.
It check the amount of lines, the amount of columns and the header of the file.
Made by Roel Glas on 26-03-2018 and fixes by Olga on 13-05-2019.

python3 ./predictions_file_format_check.py <C:/path/to/your/predictions.txt>
"""

import sys

LINES_NEEDED = 4 # When you run it on your final file for submission, be sure you change this number to 58!
HEADER = "\"Sample\"\t\"Subgroup\""
NO_COLS = 2


def get_filename():
    """Get filename from arguments."""

    try:
        sys.argv[1]
    except:
        sys.exit('\nERROR: No file given\n')

    return(sys.argv[1])


def load_linesplit_predictions(filename):
    """Load prediction file and split in lines."""

    try:
        prediction_object = open(filename,'r')
    except:
        sys.exit("\nERROR: Something went wrong when trying to load the file. Is the filename / path correct?\n")

    prediction_text = prediction_object.read()
    pred_linesplit = prediction_text.splitlines()

    return(pred_linesplit)


def determine_correct_lines(pred_linesplit):
    """Determine if the number of predictions is correct."""

    correct_lines = len(pred_linesplit) == LINES_NEEDED

    if correct_lines:
        correct_lines_string = 'Correct'
    else: 
        correct_lines_string = 'INCORRECT'
    
    return(correct_lines_string)


def determine_correct_header(pred_linesplit):
    """Determine if header is correct."""

    header = pred_linesplit[0]
    correct_header = header == HEADER
    
    if correct_header:
        correct_header_string = 'Correct'
    else:
        correct_header_string = 'INCORRECT'

    return(correct_header_string)


def determine_correct_cols(pred_linesplit):
    """Determine if amount of columns is correct."""

    correct_cols = True

    for i in range(len(pred_linesplit)):
        pred_colsplit = pred_linesplit[i].split('\t')
        correct_cols_for_line = len(pred_colsplit) == NO_COLS
        if correct_cols_for_line == False:
            correct_cols = False

    if correct_cols:
        correct_cols_string = 'Correct'
    else:
        correct_cols_string = 'INCORRECT'
    
    return(correct_cols_string)


def print_statement(correct_lines_string, correct_cols_string, correct_header_string):
    """A command line print statement if correct results are obtained."""

    print("The amount of lines in you file are: " + correct_lines_string + "\n" +
          "The amount of columns in your file are:"+ correct_cols_string + "\n" +
          "The header in your file is: " + correct_header_string)


def main():
    """All steps for the check."""

    filename = get_filename()
    pred_linesplit = load_linesplit_predictions(filename)
    correct_lines_string = determine_correct_lines(pred_linesplit)
    correct_cols_string = determine_correct_cols(pred_linesplit)
    correct_header_string = determine_correct_header(pred_linesplit)
    print_statement(correct_lines_string, correct_cols_string, correct_header_string)


if __name__ == '__main__':
    main()
