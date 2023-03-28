import os
import re
import textwrap
from madlib_cli.madlib import read_template, parse_template, merge, write_madlib


def main():
    welcome_prompt = """**********************************************************************
Welcome to the MadLib generator. You will be asked to select a MadLib
template and then be provided with a number of prompts to fill in the 
misting words from the template. Once done, the generator will display
for you the completed MadLib.
********************************************************************** 
"""
    template_selection_prompt = """Please select a template by number:
**********************************************************************
"""
    print(welcome_prompt)
    print(template_selection_prompt)
    template_list = ['']
    template_directory = './assets'
    template_pattern = r".*_template\.txt$"
    for file in os.listdir(template_directory):
        if re.match(template_pattern, file):
            template_list.append(file)
    if len(template_list) == 1:
        print("Sorry...there are no MadLib templates loaded.")
        quit()
    for template in range(1, len(template_list)):
        (print(f"{template}. {template_list[template]}"))
    template_selection = None
    while (
            template_selection is None
            or template_selection < 1
            or template_selection > len(template_list) - 1
    ):
        try:
            template_selection = int(input('> '))
        except ValueError:
            print('Please enter a number corresponding with your template selection')
    template_path = template_directory + "/" + template_list[template_selection]
    madlib_text = read_template(template_path)
    stripped_text, parts = parse_template(madlib_text)
    prompt_responses = []
    for part in parts:
        prompt_response = None
        while prompt_response is None:
            prompt_response = input("Please enter a(n) " + part + " > ")
        prompt_responses.append(prompt_response)
    final_madlib = merge(stripped_text, prompt_responses)
    output_path = template_path.replace("_template.txt", "_output.txt")
    write_madlib(final_madlib, output_path)
    print("**********************************************")
    print("YOUR MADLIB:")
    print(textwrap.fill(final_madlib, width=46))
    print("**********************************************")


if __name__ == "__main__":
    main()
