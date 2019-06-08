# graph-diff
Utilities to view diff between graphs

# Getting starget

## Intall prerequists
1. graph-easy
1. `pip install -r requirements.txt`

## Generate and view diff
```
cat samples/before.dot | graph-easy --as boxart
cat samples/after.dot | graph-easy --as boxart
python generate-diff-graph.py samples/before.dot samples/after.dot ./diff.dot
cat diff.dot | ./diff-graph-color
```

