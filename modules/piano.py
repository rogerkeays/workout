# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

from modules.workout import *
from dataclasses import dataclass

# data structures
#@dataclass # PianoNote
#class PianoNote(Note):

def piano(number, name, meter, tempo, tonic, sections):
  "construct and process a piece in one step)"
  set_mp3_dir(os.environ['HOME'] + "/library/workout/piano/00.inbox")
  process_piece(Piece(number, name, meter, tempo, tonic, sections), None, None, None, None)


