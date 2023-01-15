# A social network is a social structure made of individuals (or organizations) called nodes, which are tied (connected) by one or more specific types of interdependency, 
# such as friendship, kinship, financial exchange, dislike, sexual relationships, or relationships of beliefs, knowledge or prestige.

# A graph is an abstract representation of a set of objects where some pairs of the objects are connected by links. 
# The interconnected objects are represented by mathematical abstractions called vertices, and the links that connect some pairs of vertices are called edges.

# The exercise consists of:
# 1. to implement the social network as a graph, i.e., to define the graph data structure with the operations you consider necessary to implement a social network
# 2. to implement an operation that visits in a convenient way all the elements of the graph, such an operation should be associated to the __str__ operation of the graph implementation
# 3. to test it against a dummy social network.

class Edge:
    def __init__(self, t, rel):
        self._to = t
        self._rel = rel
    def getTo(self):
        return self._to
    def getRel(self):
        return self._rel
    def __str__(self):
        return " ...(" + self._rel + ")... " + str(self._to)
    def __eq__(self, other):
        if not isinstance(other, self.__clas__):
            return False
        return self._to == other._getTo() and self._rel == other.getRel()

class User:
    def __init__(self, username, follows = []):
        self._username = username
        self._follows = follows
    def getUsername(self):
        return self._username
    def showFollows(self):
        return '\n'.join([self._username + str(f) for f in self._follows])
    def addFollow(self, user, rel):
        self._follows.append(Edge(user, rel))
    def removeFollow(self, username):
        f = self.findFollow(username)
        if f != None:
            self._follows.remove(f)
    def findFollow(self, username):
        return next((f for f in self._follows if f.getTo().getUsername() == username), None)
    def __str__(self):
        return self._username
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self._username == other.getUsername()

class SocialNetwork:
    def __init__(self, name, users = []):
        self._name = name
        self._users = users
    def addUser(self, user):
        self._users.append(user)
    def removeUser(self, username):
        u = self.findUser(username)
        if u != None:
            self._users.remove(u)
    def findUser(self, username):
        return next((u for u in self._users if u.getUsername() == username), None)
    def __iter__(self):
        self._index = 0
        return self
    def __next__(self):
        if self._index < len(self._users):
            u = self._users[self._index]
            self._index += 1
            return u
        raise StopIteration
    def __str__(self):
        return f"{self._name}:\n\t{', '.join([str(u) for u in self._users])}"


sc = SocialNetwork('MyAmazingNetwork')
u1 = User('Paolo')
u2 = User('Martina')
u3 = User('Antonio')


sc.addUser(u1)
print(sc)
sc.addUser(u2)
sc.addUser(u3)

print(sc)

u1.addFollow(u2, 'friendship')
u1.addFollow(User('Adriana'), 'knowledge')
print(u1.showFollows())

u = sc.findUser('Paolo')
print(u)
print(sc.findUser('Giorgia'))

sc.removeUser('Luigi')
print(sc)
sc.removeUser(u3.getUsername())
print(sc)