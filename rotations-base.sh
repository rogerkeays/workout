# create a directory for each drill and one file defining each drill variable
function drill { 
  mkdir -p $1; 
  i=0
  for var in ${@:2}; do
    i=$((i+1))
    touch $1/$i.$var
  done
}

# create a set of drills for each scale key
function scale {
  for TONIC in 0 1 2 3 4 5 6 7 8 9 X Y; do
    drill $1/00.$TONIC/$2 ${@:3} $SCALE_VARS
  done
}


