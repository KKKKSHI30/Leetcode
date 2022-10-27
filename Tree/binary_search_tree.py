from typing import MutableMapping


class Tree:
    """abstract base class representing a tree stucture."""

    # nested position class
    class Position:
        def element(self):
            """return the element stored at this Position"""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """return the element stored at this position"""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            return not (self == other)

    # abstract methods that concrete subclass must support
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        "Return the number of children taht Position p has."
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        "Generate an iteratioin of Position representing p's children."
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("must be implemented by subclass")

    # concrete methods implemented in this class
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p):
        """Return the height of the tree."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))


class BinaryTree(Tree):
    """abstract base class representing a binary tree structure."""

    # additional abstract methods
    def left(self, p):
        """Return a Position representing p's left child.

        Return None if p does not have a left child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """Return a Position representing p's right child.

        Return None if p does not have a right child.
        """
        raise NotImplementedError("must be implemented by subclass")

    # concrete methods implemented in this class
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)  # possibly None
            else:
                return self.left(parent)  # possibly None

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class Node:  # lightweight, nonpublic class for storing a node
        __slots__ = 'element', 'parent', 'left', 'right'

        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self.container = container
            self.node = node

        def element(self):
            """Return the element stored at this Position."""
            return self.node.element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other.node is self.node

    def validation(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p.container is not self:
            raise ValueError("p does not belong to this container")
        if p.node.parent is p.node:
            raise ValueError("p is no longer valid")
        return p.node

    def make_position(self, node):
        return self.Position(self, node) if node is not None else None

    # binary tree constructore
    def __init__(self):
        """Create an initially empty binary tree."""
        self.root = None
        self.size = 0

    # public accessors
    def __len__(self):
        """Return the total number of elements in the tree"""
        return self.size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self.make_position(self.root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self.validation(p)
        return self.make_position(node.left)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self.validation(p)
        return self.make_position(node.left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self.validation(p)
        return self.make_position(node.right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self.validation(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    def add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """
        if self.root is not None:
            raise ValueError("Root exist")
        self.size = 1
        self.root = self.Node(e)
        return self.make_position(self.root)

    def add_left(self, p, e):
        """Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left chidl.
        """
        node = self.validation(p)
        if node.left is not None:
            raise ValueError("Left child exists")
        self.size += 1
        node.left = self.Node(e, node)
        return self.make_position(node.left)

    def add_right(self, p, e):
        """Create a new right child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self.validation(p)
        if node.right is not None:
            raise ValueError("Right child exists")
        self.size += 1
        node.right = self.Node(e, node)
        return self.make_position(node.right)

    def replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self.validation(p)
        old = node.element
        node.element = e
        return old

    def delete(self, p):
        """Delete the node at Position p and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self.validation(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
        child = node.left if node.left else node.right  # might be None
        if child is not None:
            child.parent = node.parent  # child's grandparent becomes parent
        if node is self.root:
            self.root = child  # child becomes root
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self.size -= 1
        node.parent = node  # convention for deprecated node
        return node.element

    def attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self.validation(p)
        if not self.is_leaf(p):
            raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):  # all 3 trees must be same type
            raise TypeError("Tree types must match")
        self.size += len(t1) + len(t2)
        if not t1.is_empty():  # attached t1 as left subtree of node
            t1.root.parent = node
            node.left = t1.root
            t1.root = None  # set t1 instance to empty
            t1.size = 0
        if not t2.is_empty():
            t2.root.parent = node
            node.right = t2.root
            t2.root = None
            t2.size = 0


class MapBase(MutableMapping):
    class Item:
        __slots__ = 'key', 'value'

        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __eq__(self, other):
            return self.key == other.key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self.key < other.key


class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree."""

    # override position class
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """Return key of map's key-value pair."""
            return self.element().key

        def value(self):
            """Return value of map's key-value pair."""
            return self.element().value

    # nonpublic utilities
    def subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searchedd."""
        if k == p.key():    # found match
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self.subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self.subtree_search(self.right(p), k)
        return p

    def subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p."""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        """Return the first Position in the tree (or None if empty)."""
        return self.subtree_first_position(self.root() if len(self) > 0 else None)

    def last(self):
        """Return the last Position in the tree (or None if empty)."""
        return self.subtree_last_position(self.root() if len(self) > 0 else None)

    def before(self, p):
        """Return the Position just before p in the natural order.

        Return None if p is the first position.
        """
        self.validation(p)
        if self.left(p):
            return self.subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
        return above

    def after(self, p):
        """Return the Position just after p in the natural order.

        Return None if p is the last position.
        """
        self.validation(p)
        if self.right(p):
            return self.subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
        return above

    def find_position(self, k):
        """Return position with key k, or else neightbor (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self.subtree_search(self.root(), k)
            self.rebalanced_access(p) # hook for balanced tree subclasses
            return p

    def find_min(self):
        """Return (key, value) pair with minimum key (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        """Return (key, value) pair with least key greater than or equal to k.

        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        if self.is_empty():
            raise KeyError("Key Error:" + repr(k))
        else:
            p = self.subtree_search(self.root(), k)
            self.rebalance_access(p)
            if k != p.key():
                raise KeyError("Key Error:" + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        if self.is_empty():
            leaf = self.add_root(self.root(), k)
        else:
            p = self.subtree_search(self.root(), k)
            if p.key() == k:
                p.element.value = v
                self.rebalance_access(p)
            else:
                item = self.Item(k, v)
                if p.key() < k:
                    leaf = self.add_right(p, item)
                else:
                    leaf = self.add_left(p, item)
        self.rebalance_insert(leaf)

    def __iter__(self):
        """Generate an iteration of all keys in the map in order."""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """Remove the item at given Position."""
        self.validation(p)
        if self.left(p) and self.right(p):
            replacement = self.subtree_last_position(self.left(p))
            self.replace(p,replacement.element())
            p = replacement
        parent = self.parent(p)
        self.delete(p)
        self.rebalance_delete(parent)

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self.subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)   # rely on positional version
                return      # successful deletion complete
            self.rebalance_acess(p)
        raise KeyError("Key Error: " + repr(k))

    def rebalance_insert(self, p):
        pass

    def rebalance_delete(self, p):
        pass

    def rebalance_access(self, p):
        pass

    def relink(self, parent, child, make_left_child):
        """Relink parent node with child node (we allow child to be None)."""
        if make_left_child:
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent

    def rotate(self, p):
        """Rotate Position p above its parent."""
        x = p.node
        y = x.parent
        z = y.parent   # grandparent (possibly None)
        if z is None:
            self.root = x    # x becomes root
            x.parent = None
        else:
            self.relink(z,x,y == z.left)



































