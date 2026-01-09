# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

from workout import *
from dataclasses import dataclass

# globals
MP3_DIR = os.environ['HOME'] + "/library/workout/piano/00.inbox"

# todo: data structures
#@dataclass # PianoNote
#class PianoNote(Note):

# functions
def process(piece):
  process_all([piece])

def process_all(pieces):
  process_pieces(pieces, MP3_DIR, None, None, None, None)

