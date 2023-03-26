import re


def read_template(madlib_template):
    try:
        with open(madlib_template, "r") as template:
            return template.read()
    except FileNotFoundError:
        return "File was not found."


def parse_template(madlib_template):
    """
    Separates parts of a string (the madlib 'template') into the characters found
    within braces (parts) and the remainder of the string including the braces
    themselves (stripped)
    :param madlib_template: template for a madlib that includes prompt text between
    braces.
    :return: (str) stripped - the template text with the text between the braces
    removed,
    (tuple) parts - each of the words (prompts) found within braces in the original template
    string.
    """
    # Thanks to Chat GPT for helping with the regex string (not my forte)!
    regex = r"\{([^}]+)\}"
    parts = re.findall(regex, madlib_template)
    stripped = re.sub(regex, '{}', madlib_template)
    return stripped, tuple(parts)


def merge(stripped_template, user_prompt_responses):
    completed_madlib = stripped_template
    for response in user_prompt_responses:
        completed_madlib = completed_madlib.replace('{}', response, 1)
    return completed_madlib