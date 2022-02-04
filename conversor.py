#!/usr/bin/env python

# simple python script to change lower camel case strings in a file to snake case
import sys
import re
import os

# detect if the string is lower camel case
def is_camel(word):
    bol = re.sub("(.)([a-z][a-z]+)", r"\1_\2", word)
    return bol


# convert string to snake case
def convert(word):
    word = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', word)
    return re.sub(r"([a-z\d])([A-Z])", r'\1_\2', word).replace("-", "_").lower()


path = os.getcwd()
filenames = [x for x in os.listdir(path) if x.endswith(".py") and "conversor" not in x]

for filename in filenames:
    old_file = open(filename).read()
    new_file = open(filename, "w")
    for w in old_file.split():
        if is_camel(w) != None:
            old_file = old_file.replace(w, convert(w))
    new_file.write(old_file)
