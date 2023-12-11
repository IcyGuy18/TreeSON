"""Building a TreeSON class"""

import pydotplus

class Node:
    def __init__(self, data: int | str | float | bool = 'unq_root'):
        self.data = data
        self.children: list[Node] = []
    
    def __repr__(self):
        return f"NODE<{self.data}>"

class Tree:
    def __init__(self, root: Node, filename: str = 'graphviz_tree'):
        self.root: Node = root
        self._filename = filename
    
    def construct_tree(self, data: dict | list) -> None:
        # A list of parents to be used when traversing the tree in order.
        # This is done because some values can repeat over, and we don't
        # want different nodes with same values to be connected to each
        # other.
        # They will be connected with the parents, so we check their
        # ancestry.
        ancestry = []
        if isinstance(data, list):
            return self._list_parse(data, ancestry)
        elif isinstance(data, dict):
            return self._dict_parse(data, ancestry)
        raise ValueError("Expected dict or list")
    
    def _dict_parse(self, data: dict, parents: list):
        for key, value in data.items():
            parent_node = Node(key)
            self.add_child(parent_node, parents)
            parents.append(key)
            if isinstance(value, list):
                self._list_parse(value, parents)
            elif isinstance(value, dict):
                self._dict_parse(value, parents)
            else:
                new_node = Node(value)
                self.add_child(new_node, parents)
            parents.pop()
    
    def _list_parse(self, data: list, parents: list):
        print(parents)
        for item in data:
            if isinstance(item, list):
                self._list_parse(item, parents)
            elif isinstance(item, dict):
                self._dict_parse(item, parents)
            else:
                new_node = Node(item)
                self.add_child(new_node, parents)
    
    def add_child(self, new_node: Node, ancestry: list):
        self._add([self.root], new_node, ancestry)
    
    def _add(self, node: list[Node], new_node: Node, ancestry: list):
        try:
            for c in node[0].children:
                if c.data == ancestry[0]:
                    return self._add([c], new_node, ancestry[1:])
            return node[0].children.append(new_node)
        except IndexError:
            return node[0].children.append(new_node)
    
    def pre_order_traversal(self) -> None:
        return self._PRO(self.root, 0)
    
    def _PRO(self, node: Node | None, tabber: int) -> None: # NOSONAR
        if node is None:
            return
        print(tabber * '  ', end = '└─')
        print(node.data)
        for child in node.children:
            self._PRO(child, tabber + 1)
    
    def post_order_traversal(self) -> None:
        return self._POO(self.root, 0)
    
    def _POO(self, node: Node | None, tabber: int) -> None: # NOSONAR
        if node is None:
            return
        for child in node.children:
            self._PRO(child, tabber + 1)
        print(tabber * '  ', end = '└─')
        print(node.data)

    def to_graphviz_dot(self):
        with open(f'{self._filename}.dot', 'w') as f:
            f.write('digraph G {\n')
        self._to_dot_language(self.root)
        with open(f'{self._filename}.dot', 'a') as f:
            f.write('}')
        # Finally, save the damn thing as a PNG
        graph = pydotplus.graph_from_dot_file(f'{self._filename}.dot')
        graph.write_png(f'{self._filename}.png')
        
    
    def _to_dot_language(self, node: Node | None) -> None:
        if node is None:
            return
        #print(node.data)
        for child in node.children:
            self._to_dot_language(child)
            with open(f'{self._filename}.dot', 'a') as f:
                f.write(f'\t"{node.data}" -> "{child.data}";\n')

