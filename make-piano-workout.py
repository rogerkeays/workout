#!/usr/bin/env python3
# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

from workout import *
from dataclasses import dataclass

# globals
set_mp3_dir(os.environ['HOME'] + "/library/workout/piano/00.inbox")

# data structures
#@dataclass # PianoNote
#class PianoNote(Note):

# constructors
def piece(number, name, meter, tempo, tonic, sections):
  "construct and process a piece in one step)"
  process_piece(Piece(number, name, meter, tempo, tonic, sections), None, None, None, None)


# process the input files
process_scores(sys.argv[1:], globals())

