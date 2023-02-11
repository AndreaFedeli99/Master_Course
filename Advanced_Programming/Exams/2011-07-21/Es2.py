from crossing import *

class TestCountries:

    def testNeighbors(self, country):
        start = set([country])
        neighbors = crossing(country, 1)
        for n in neighbors:
            assert any(start.intersection(crossing(n,1))), "{0} is not contained in {1}'s neighbors list".format(country.upper(), n)
        print("*** Test for {0} passed".format(country.upper()))

    def testTrip(self, country, steps):
        def runTest(c):
            start = set([c])
            destinations = crossing(c, steps)
            for d in destinations:
                assert any(start.intersection(crossing(d, steps))) , "{0} reach {1} in {3} steps, but {1} doesn't reach {0} in {3} steps".format(country.upper(), d.upper(), steps)
        for c in crossing(country, steps):
            runTest(c)
        print("*** Test for ({0}, {1}) passed".format(country.upper(), steps))

if __name__ == "__main__":
    test = TestCountries()

    for steps in range(8):
        test.testTrip('italy', steps)
        for country in crossing('italy', steps):
            test.testNeighbors(country)
        print()

    print()

    test.testTrip('sweden', 5)
    
    test.testTrip('germany', 2)
    
    test.testTrip('iceland', 3)
