A simple guide to using **TreeSON**

# What it does

Simple - it takes your data in JSON format and converts it into a data structure tree that can be used to print out a viewable PNG file.

# Prerequisites

The modules mentioned in the requirements is optional, but necessary for making PNGs. Moreover, the Graphviz executable needs to be installed on your operating system as well.

# Installation

1. Run `git clone https://github.com/IcyGuy18/TreeSON.git`.
2. `cd` to the cloned directory by typing `cd TreeSON`.
3. Run `setup.py` by typing: `pip install -e .`.

# How to use

Here's an example of loading up a JSON data and using it to construct a tree.

```py
from treeson.tree import Node, Tree
import json

if __name__ == "__main__":
    # Load up the JSON contents (if not stored in variable already).
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Make a root node with unique data (by default, it will be called 'unq_root').
    root_node = Node()

    # We make a tree based on the root node.
    tree = Tree(root_node)

    # Run this command with the loaded JSON data passed in.
    # Everything will be done behind the back.
    tree.construct_tree(data)
    
    # (Optional) Convert the tree to Graphviz-compatible DOT image (as well as a PNG image).
    tree.to_graphviz_dot()

    # (Optional) Print out the tree in a pre-order traversal fashion.
    tree.pre_order_traversal()
    # Note: you can also do 'post_order_traversal()'.
```

# To-Do

- Probably make the data structure tree more modular so as to keep it separated from the JSON end of things.
- Add more functionalities.
- Add docstrings.