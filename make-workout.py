#!/usr/bin/env python3
# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

from workouts.workout import *
from workouts.violin import *
from workouts.piano import *

# process the input files
process_scores(sys.argv[1:], globals())

