# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

from modules.workout import *
from dataclasses import dataclass

# data structures
#@dataclass # PianoNote
#class PianoNote(Note):

def piano(number, name, video_id, meter, tempo, tonic, sections):
  process_piece(Piece("piano", number, name, video_id, meter, tempo, tonic, sections), None, None, None, None)


