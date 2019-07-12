# graph-diff
Utilities to view diff between graphs

# Getting started

## Install prerequisites 
Debian / Ubuntu:
```
sudo apt-get install libgraph-easy-perl
```
## Install

### From source
```
git clone https://github.com/yeger00/graph-diff
pip install -e .
```

### From PyPI
```
pip install graphdiff
```

## Generate and view diff
```
cat samples/before.dot | graph-easy --as boxart
cat samples/after.dot | graph-easy --as boxart
python -m graphdiff samples/before.dot samples/after.dot > ./diff.dot
cat ./diff.dot | ./diff-graph-color
```

# git-graph-diff-tool
It is possible to use graph-diff with git, with `git-graph-diff-tool` provided in this library. An usage example:
![](images/git-log-example.gif?raw=true "git-graph-diff-tool example")

## Install
For every repository you would like to install you need to add to .gitattributes file a rules to know how to handle .dot files. For example:
```
echo "*.dot diff=graph_diff" >> .gitattributes
```
Then, configure the difftool to be the `git-graph-diff-tool`. For example:
```
git config diff.graph_diff.command /path/to/git-graph-diff-tool
```
Then, you can use git as usual, while adding `--ext-diff` flag to enable external difftools.
```
git log -p --ext-diff
```
