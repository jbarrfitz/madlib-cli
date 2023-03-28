import pytest
import os
import tempfile
from madlib_cli.madlib import read_template, parse_template, merge, write_madlib


def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)


def test_write_madlib():
    # Credit going to Chat GPT which helped me figure out how to create a temp file
    madlib_text = "Here is merged MadLib text"
    expected = madlib_text
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file_path = temp_file.name
        write_madlib(madlib_text, file_path)
        with open(file_path, "r") as new_file:
            actual = new_file.read()
            assert actual == expected
    os.remove(file_path)
