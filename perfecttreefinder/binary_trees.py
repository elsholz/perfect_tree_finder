from typing import Set, List


class BinaryTree:
    def __init__(self, value: bool=None, parent: 'BinaryTree'=None, level: int=0):
        self.r: BinaryTree = None
        self.l: BinaryTree = None
        self.parent: BinaryTree = parent
        self.level: int = level
        self.value: bool = value

    def insert(self, path: List[bool]) -> None:
            x = path[0]
            if x:
                if not self.r:
                    self.r = BinaryTree(value=x, parent=self, level=self.level+1)
                node = self.r
            else:
                if not self.l:
                    self.l = BinaryTree(value=x, parent=self, level=self.level+1)
                node = self.l
            if len(path) > 1:
                node.insert(path[1:])

    def is_perfect_tree(self) -> bool:
        if self.r and self.l:
            return self.l.is_perfect_tree() and self.r.is_perfect_tree() and self.r.depth() == self.l.depth()
        elif not self.r and not self.l:
            return True
        else:
            return False

    def to_bool_array(self) -> List[bool]:
        if self.parent:
            return self.parent.to_bool_array() + (self.value, ) 
        elif self.value:
            return (self.value, )
        else:
            return tuple()

    def find_perfect_trees(self, transform=True) -> Set['BinaryTree']:
        res = set()
        if self.is_perfect_tree():
            res = {(self, self.depth() - self.level)}
        else:
            if self.l:
                res |= self.l.find_perfect_trees(transform=False)
            if self.r:
                res |= self.r.find_perfect_trees(transform=False)
        if transform:
            res = {(bt.to_bool_array(), bt.depth_from_here()) for bt, d in res}
        return res


    def depth(self) -> int:
        if self.l and self.r:
            return max(self.r.depth(), self.l.depth())
        elif self.l:
            return self.l.depth()
        elif self.r:
            return self.r.depth()
        else:
            return self.level

    def depth_from_here(self) -> int:
        return self.depth() - self.level

    def __str__(self) -> str:
        return f'BinaryTree({self.value}, l={str(self.l)}, r={str(self.r)})'
