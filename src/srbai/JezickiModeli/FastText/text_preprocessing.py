import re
import string
from typing import List, Dict, Tuple
from operator import itemgetter

import numpy as np

from globals import ModelConfig, LanguageConfig
from io_utils import open_corpus


def remove_white_space(text: str) -> str:
    """
    Removes multiple occurrences of space, newlines, return lines with a single space
    """
    cleaned_text = re.sub(r"(\s+|\n+|\r+)", " ", text)
    return cleaned_text


def remove_numbers(text: str) -> str:
    """
    Removes all numbers in text
    """
    cleaned_text = re.sub(r"[0-9]+", " ", text)
    return cleaned_text


def remove_punctuation(text: str) -> str:
    """
    Removes all occurrences of punctuation
    """
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation))
    return cleaned_text


def to_lowercase(text: str) -> str:
    """
    Turns all words into lowercase
    """
    return text.lower()


def clean_text(text: str) -> str:
    """
    Cleans text using above functions
    """
    no_whitespace = remove_white_space(text)
    no_numbers = remove_numbers(no_whitespace)
    no_punctuation = remove_punctuation(no_numbers)
    lowercase = to_lowercase(no_punctuation)
    return lowercase


def make_word_list(text: str) -> List[str]:
    """
    Makes a list from single whitespace separated text
    """
    split_text = text.split(" ")
    return [word for word in split_text if word != ""]


def remove_stopwords(word_list: List[str], stopwords_path: str) -> List[str]:
    """
    Removes all stopwords from text.
    Stopwords path is the path to the comma separated stopwords.
    """
    # preprocess stopwords
    with open(stop