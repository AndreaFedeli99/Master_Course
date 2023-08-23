from quadtree import *

if __name__ == '__main__':
    img = [
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 1, 1, 0,
        0, 0, 0, 0, 1, 1, 0, 0,
        1, 1, 1, 1, 1, 1, 0, 0,
        1, 1, 1, 1, 1, 1, 0, 0,
        1, 1, 1, 1, 0, 0, 0, 0,
        1, 1, 1, 1, 0, 0, 0, 1
    ]

    q = quadtree(img)
    print("Image space {0}.".format(len(img)))
    print("Using a quadtree representation the saved space is {0}.".format(q.count()))