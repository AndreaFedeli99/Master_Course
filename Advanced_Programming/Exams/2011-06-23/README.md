# Exam of Advanced Programming

###### 2011-06-23

## Exercise 1

Sometimes methods should be activate only when meet a given condition; an easily way to realize such a behavior consists of call them and test if the condition is met. Such a naïve approach is not always satisfactory. A similar behavior can be achieved by checking the condition before calling the method and really call it only when the condition matches.

Implements such a behavior through a **parametric** decorator `guarded`. Such a decorator should have a parameter which expresses the condition to be matched; this is a predicate, i.e., a function which returns a boolean. Of course we are speaking about decorators applicable on method not class definitions.

### Test example:

```py
class ToBeGuarded:
    @guarded(lambda x,y,z: (x**2+y**2)==z**2)
    def m1(self, x, y, z):
        print("### m1({0},{1},{2}) has been called!".format(x,y,z))
    
    @guarded(lambda x: x%2 == 0)
    def m2(self, i):
        print("### m2({0}) has been called!".format(i))

    @guarded(lambda x,y: x<y)
    def m3(self, x, y):
        print("### m3({0},{1}) has been called!".format(x,y))

if __name__ == "__main__":

    to_be = ToBeGuarded()
    to_be.m1(1,2,3)
    to_be.m1(3,4,5)
    to_be.m2(5)
    to_be.m3('a','b')
    to_be.m2(7)
    to_be.m1(5,4,3)
    to_be.m3(3.15, 3.156)
    to_be.m2(3)
    to_be.m3(25, 7)
```

### Expected output:

```code
The condition was not met
### m1(3,4,5) has been called!
The condition was not met
### m3(a,b) has been called!
The condition was not met
The condition was not met
### m3(3,15,3.156) has been called!
The condition was not met
The condition was not met
```

## Exercise 2

Even if python has its own implementation for the complex numbers we go to implement a class (`mycomplex`) to support the complex numbers this should permit, at least, to execute the following main program.

### Test example:

```py
if __name__ == "__main__":
    a = mycomplex(6,7)
    b = mycomplex(3.5,-8)
    c = a+b
    d = -9.5+c
    print("a :-", a)
    print("b :-", b)
    print("c = a+b :-", c)
    print("d = -9.5+c :-", d)
    e = a-b
    print("e = a-b :-", e)
    f = 7-b
    print("f = 7-b :-", f)
    g = e*f
    print("g = e*f :-", g)
    h = 7*g
    print("h = 7*g :-", h)
    i = mycomplex(0,-1)*mycomplex(0,-1)
    print("i :-", i)
    j = a/g
    print("j = a/g :-", j)
    k = a*(b+c)-d*(e+f-g)/(h+i*j)
    print("k :-",k)
```

### Expected output:

```code
a :- 6+7i
b :- 3.5-8i
c = a+b :- 9.5-i
d = -9.5+c :- -i
e = a-b :- 2.5+15i
f = 7-b :- 3.5+8i
g = e*f :- -111.25+72.5i
h = 7*g :- -778.75+507.5i
i :- -1
j = a/g :- -0.00907399202481-0.0688347363757i
k :- 141.024262995+36.8652506165i
```