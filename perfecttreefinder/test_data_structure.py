from binary_trees import BinaryTree


def test_constructor():
    t = BinaryTree()
    assert t.value is None
    assert t.level is 0
    assert t.l is None
    assert t.r is None


def test_insertion():
    t = BinaryTree()
    t.insert([True, False])


def test_imperfect():
    t = BinaryTree()
    t.insert([True])
    print('this is t:', t)
    assert t.r.is_perfect_tree(), 'Tree without nodes should be perfect'
    assert not t.is_perfect_tree(), 'Tree with one node should be imperfect'

    t = BinaryTree()
    t.insert([True, False])
    t.insert([True, True])
    t.insert([False, False])
    assert not t.is_perfect_tree(), 'Should be imperfect'
    t.insert([False, True])
    assert t.is_perfect_tree(), 'Should be perfect'
    t.insert([False, True, False])
    t.insert([False, True, True])
    assert not t.is_perfect_tree(), 'Should be imperfect'


def test_to_bool_array():
    t = BinaryTree()

    t.insert([True, False, False, True, True])

    print('To Bool array::', t.r.l.to_bool_array())
    assert t.r.l.to_bool_array() == (True, False)
    assert t.r.l.l.r.r.to_bool_array() == (True, False, False, True, True)
    assert t.r.l.l.r.r.depth() - t.r.l.l.r.r.level == 0
    assert t.r.l.l.r.r.depth_from_here() == 0


def test_find_perfect_trees():
    t = BinaryTree()
    print('find perfect tree:', t.find_perfect_trees())
    assert t.find_perfect_trees() == {(tuple(), 0)}

    t.insert([True, True, False])
    t.insert([True, True, True])
    t.insert([True, False, False])
    t.insert([True, False, True])

    print('Perfefect trees found:', t.find_perfect_trees())
    assert t.find_perfect_trees() == {((True, ), 2)}

    t.insert([False, True, True, False])
    t.insert([False, True, True, True])
    t.insert([False, True, False, False])
    t.insert([False, True, False, True])

    assert t.find_perfect_trees() == {((True, ), 2), ((False, True), 2)}

    t.insert([False, False, True, True, False])
    t.insert([False, False, True, True, True])
    t.insert([False, False, True, False, False])
    t.insert([False, False, True, False, True])
    t.insert([False, False, False, True, False])
    t.insert([False, False, False, True, True])
    t.insert([False, False, False, False, False])
    t.insert([False, False, False, False, True])

    assert t.find_perfect_trees() == {(
        (True, ), 2), ((False, True), 2), ((False, False), 3)}

    print(t.find_perfect_trees())
