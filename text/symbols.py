""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
from text.cmudict import valid_symbols

_pad = '_'
_eos = '~'
_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'(),-.:;? '

# Export all symbols:
symbols = [_pad, _eos] + list(_characters) + valid_symbols

# Special symbol ids
SPACE_ID = symbols.index(" ")
