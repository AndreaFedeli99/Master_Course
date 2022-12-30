# A monoid is an algebraic structure consisting of a set together with a single associative binary operation and an identity element. E.g., the set of booleans with the or operator is a monoid whose identity is false.

# A group is an algebraic structure consisting of a set together with an operation that combines any two of its elements to form a third element. 
# To qualify as a group, the set and the operation must satisfy a few conditions called group axioms, namely closure, associativity, identity and invertibility. E.g., the set Z (the integers with sign) with the + operator 
# is a group but with the * is not since inverting the operation break the closure property.

# A ring is an algebraic structure consisting of a set together with two binary operations (usually called addition and multiplication), where each operation combines two elements to form a third element. 
# To qualify as a ring, the set together with its two operations must satisfy certain conditions, namely, the set must be an abelian (i.e., commutative) group under addition and a monoid under multiplication such that 
# multiplication distributes over addition.

# Write the Monoid, Group and Ring classes implementing the monoids, groups and rings algebraic structures respectively. 
# Each class must be general, in the sense that the operations and the sets are not a priori defined and they should implement methods to check the properties characterizing the algebraic structure.

# Test your implementation with the following examples (S is the set, add=additive operation, mul=multiplicative operation, i=identity):

# Monoids:
# S = {True, False} add = or i = False
# S = Zn={0,1,...,n-1} add = + where a+b=(a+b)%n i = 0

# Groups:
# S = itertools.permutations('RGB'), given "a" a function that swaps 1st with 2nd element in the permutation, and "b" a function that swaps 2nd with 3rd element add = function composition i = a(a(x))
# S = Q-{0} add = * i = 1

# Rings:
# S = {0} add = + where 0+0=0 mul = * where 0*0=0 i = 0
# S = Z add = + mul = * i = 0
# S = Z4 = {0,1,2,3} add = + where a+b=(a+b)%4 mul = * where a*b=(a*b)%4 i = 0
# Note infinite sets can be implemented through iterators; property checks on infinite sets should be on a finite subset.

import itertools

class identity:
    def __set__(self, obj, id):
        assert all([obj._add(elem, id) == elem and obj._add(id, elem) == elem for elem in iter(obj._set)]), "Identity element not admitted"
        obj._id = id

class closure:
    def __set__(self, obj, add):
        assert all([add(sx, dx) in obj._set for dx in iter(obj._set) for sx in iter(obj._set)]), "Operator not admitted: operator MUST be a closure"
        obj._add = add

class axioms_checker:
    def __set__(self, obj, op):
        self.check_axioms(obj, op)
        obj._add = op
    def check_axioms(self, obj, op):
        assert all([op(sx, dx) in obj._set for dx in iter(obj._set) for sx in iter(obj._set)]), "Operator not admitted: operaton MUST be a closure" # closure
        assert all([op(op(x, y), z) == op(x, op(y, z)) for z in iter(obj._set) for y in iter(obj._set) for x in iter(obj._set)]), "Operator not admitted: operator MUST be associative" # associativity
        assert any([op(elem, inv) == obj._id and op(inv, elem) == obj._id for inv in iter(obj._set) for elem in iter(obj._set)]), "Operator not admitted: operator MUST be invertible" # invertibility

class abelian:
    def __set__(self, obj, add):
        assert all([add(sx, dx) == add(dx, sx) for dx in iter(obj._set) for sx in iter(obj._set)]), "Addition operator not admitted: MUST be abelian"
        obj._add = add

class algebric_structure:
    def __init__(self, set, add, id):
        self.set = set
        self.add = add
        self.id = id
    def set_set(self, set):
        self.set = set
    def get_set(self):
        return self.set
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    def set_add(self, add):
        self.add = add

class monoid(algebric_structure):
    def __init__(self, set, add, id):
        self._set = set
        super().set_add(add)
        super().set_id(id)
    add = closure()
    id = identity()

m = monoid({True, False}, lambda sx, dx: sx or dx, False)

class group(algebric_structure):
    def __init__(self, set, add, id):
        self._set = set
        super().set_add(add)
        super().set_id(id)
    add = axioms_checker()
    id = identity()

class ring(algebric_structure):
    def __init__(self, set, add, mul, id):
        self._set = set
        super().set_add(add)
        super().set_id(id)
        self._mul = monoid(set, mul, id)
    id = identity()
    add = abelian()

r = ring({0}, lambda sx, dx: sx + dx, lambda sx, dx: sx * dx, 0)