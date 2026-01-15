#!/usr/bin/env python3
# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

from modules.workout import *
from modules.violin import *
from modules.piano import *

# process the input files
process_scores(sys.argv[1:], globals())

