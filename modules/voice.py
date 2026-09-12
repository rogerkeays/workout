# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

from modules.workout import *

# constructors
def voice(number, name, video_id, meter, tempo, tonic, sections, speed=1.0, video=False, etude=False):
  process_piece(Piece("voice", number, name, video_id, meter, tempo, tonic, sections, speed, video, etude), None, None, None, None)


