#!/bin/bash
# In a folder container all parts of the PageRank output, sort and find the max

for FILE in $(ls); do
  if [ "$FILE" != 'find-max-pagerank.sh' ]; then
    NB_LINES=$(wc -l < $FILE)
    ((NB_LINES++))
    # Add break line
    echo >> $FILE

    $(sort -rk 2n $FILE >> $FILE)

    # Keep only sorted lines
    $(sed -i -e "1,${NB_LINES}d" $FILE)

    # Save max
    $(tail -n 1 $FILE >> out)
  fi
done