""" from https://github.com/keithito/tacotron
Cleaners are transformations that run over the input text at both training and eval time.

Cleaners can be selected by passing a comma-delimited list of cleaner names as the "cleaners"
hyperparameter. Some cleaners are English-specific. You'll typically want to use:
  1. "english_cleaners" for English text
  2. "transliteration_cleaners" for non-English text that can be transliterated to ASCII using
     the Unidecode library (https://pypi.python.org/pypi/Unidecode)
  3. "basic_cleaners" if you do not want to transliterate (in this case, you should also update
     the symbols in symbols.py to match your data).
"""

import re
from norm import Normalizer
from g2p import Grapheme2Phonem

# Regular expression matching whitespace:
_whitespace_re = re.compile(r'[^a-zA-Z0-9А-Яа-яЁё]+')

normalizer = Normalizer()
graphem_to_phonem = Grapheme2Phonem()


def lowercase(text):
    return text.lower()


def russian_cleaners(text):
    text = lowercase(text)
    text = normalizer(" ".join(re.split(_whitespace_re, text)))
    return " ".join(["".join(graphem_to_phonem(i)) for i in text.split(" ") if len(i)])
