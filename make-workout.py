#!/usr/bin/env python3
# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

import sys
from modules.workout import *
from modules.violin import *
from modules.piano import *

# process the input files
for file in sys.argv[1:]:
  with open(file) as score:
    exec(score.read(), globals())

# output collected drills
write_drill_cards()

