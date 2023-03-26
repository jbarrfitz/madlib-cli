import os
import re
from madlib_cli.madlib import read_template, parse_template, merge


def main():
    welcome_prompt = """
    Welcome to the MadLib generator. You will be asked to select a MadLib
    template and then be provided with a number of prompts to fill in the 
    misting words from the template. Once done, the generator will display
    for you the completed MadLib.
    ********************************************************************** 
    """
    template_selection_prompt = """
    Please select a template by number:
    **********************************************************************
    """
    print(welcome_prompt)
    print(template_selection_prompt)
    template_number = 1
    template_directory = './assets'
    template_pattern = r".*_template\.txt$"
    for file in os.listdir(template_directory):
        if re.match(template_pattern, file):
            print(f"{template_number}. {file}")
            template_number += 1


if __name__ == "__main__":
    main()
