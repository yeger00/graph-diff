# graph-diff
Utilities to view diff between graphs

# Getting starget

## Install prerequisites 
1. graph-easy

## Install
```
git clone https://github.com/yeger00/graph-diff
pip install -e .
```

## Generate and view diff
```
cat samples/before.dot | graph-easy --as boxart
cat samples/after.dot | graph-easy --as boxart
python -m graphdiff samples/before.dot samples/after.dot ./diff.dot
cat ./diff.dot | ./diff-graph-color
```

# git-diff
TODO
