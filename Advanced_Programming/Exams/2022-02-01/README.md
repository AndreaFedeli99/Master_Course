# Exam of Advanced Programming

###### 2022-02-01

## Exercise 1

Morse code is a method used in telecomunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes. Each code symbol is formed by a sequence of dots and dashes. The dot duration is the basic unit of time measurement in Morse code transimissions. The duration of a dash is three times the duration of a dot. Each dot or dash within an encoded character is followed by a period of signal absence, called space, equal to the dot duration. The letters of a word are separated by a space of duration equal to three dots, and words are separated by a space equal to seven dots.

The exercise consists of defining a class `Morse` with a method `decode` to decode a text written in Morse code and a method `encode` to encode normal text in Morse code. To simplify we restrict the Morse code to only these symbols:
<table>
  <tr>
    <th>Letter</th><th>Morse</th>
    <th>Letter</th><th>Morse</th>
    <th>Letter</th><th>Morse</th>
    <th>Letter</th><th>Morse</th>
    <th>Letter</th><th>Morse</th>
    <th>Letter</th><th>Morse</th>
  </tr>
  <tr>
    <td>A</td><td>­­._­</td>
    <td>F</td><td>.._.</td>
    <td>K</td><td>_._</td>
    <td>P</td><td>._ _.</td>
    <td>U</td><td>.._</td>
    <td>Z</td><td>_ _..</td>
  </tr>
  <tr>
    <td>B</td><td>_...</td>
    <td>G</td><td>_ _.</td>
    <td>L</td><td>._..</td>
    <td>Q</td><td>_ _._</td>
    <td>V</td><td>..._</td>
  </tr>
  <tr>
    <td>C</td><td>_._.</td>
    <td>H</td><td>....</td>
    <td>M</td><td>_ _</td>
    <td>R</td><td>._.</td>
    <td>W</td><td>._ _</td>
  </tr>
  <tr>
    <td>D</td><td>_..</td>
    <td>I</td><td>..</td>
    <td>N</td><td>_.</td>
    <td>S</td><td>...</td>
    <td>X</td><td>_.._</td>
  </tr>
  <tr>
    <td>E</td><td>.</td>
    <td>J</td><td>._ _ _</td>
    <td>O</td><td>_ _ _</td>
    <td>T</td><td>_</td>
    <td>Y</td><td>_ ._ _</td>
  </tr>
</table>

###### Note: consecutive dashes are separeted for clarity

The symbol to separate two words is a space `" "`. The symbol to separate two symbols inside a word is `u`.

The solution must respect the following constraints:
- Every primitive Python's data structure is forbidden, except for lists
- Use of `itertools` is **FORBIDDEN**

### Test example:

```py
if __name__ == "__main__":
  M = Morse()
  print(f"SOS SAVE THE DEVS CHATGPT RULEZ, {M.encode('SOS SAVE THE DEVS CHATGPT RULEZ')}")
  print(f"....u.u._..u._..u___ .__u___u._.u._..u_.., {M.decode('....u.u._..u._..u___ .__u___u._.u._..u_..')}")
```

### Expected output:

```code
SOS SAVE THE DEVS CHATGPT RULEZ, ...u___u... ...u­._u..._u. _u....u. _..u.u..._u... _._.u....u._u_u__.u.__.u_ ._.u.._u._..u.u__..
....u.u._..u._..u___ .__u___u._.u._..u_.., HELLO WORLD
```

## Exercise 2

As you probably know, Python doesn't provide a `switch` statement. The language solution to such a lack is the `if-elif-else` construct that lacks the clearness, elegance and the simplicity of a `switch` statement.

A more convenient solution involves decorators and object-orientation. In this approach the decorators are used to associate an expression to a method representing the alternative code to execute when the expression is matched; in other words the couple, composed by the annotation and the method, represents one entry of the `swtich`. Any class that needs to use a `switch` will inherit from a super class that defines how to deal with different decorations.

The exercise consists of implementing such an approach defining a super class named `Switch` and decorator `@case` used to annotate the different cases. Both should be in the module `switch.py`

The solution must respect the following constraints:
- The `Switch` class must have a method named `match` and a mechanism to deal with default entries and many entries associated to the same function.
- The expression to match could be a generic expression not limited to one kind.

### Test example:

```py
from switch import Switch, case

class N(Switch):
  @case(1)
  def january(self): return "January"    
  @case(2)
  def february(self): return "February"    
  @case(3)
  def march(self): return "March"    
  @case(4)
  def april(self): return "April"    
  @case(5)
  def may(self): return "May"    
  @case(6)
  def june(self): return "June"    
  @case(7)
  def july(self): return "July"    
  @case(8)
  def august(self): return "August"    
  @case(9)
  def september(self): return "September"    
  @case(10)
  def october(self): return "October"    
  @case(11)
  def november(self): return "November"    
  @case(12)
  def december(self): return "December"    
  
  def month(self, n): return self.match(n)()

class S(Switch):
  @case((12, 1, 2))
  def winter(self, n): return "{} comes in {}".format(N().month(n), "winter")
  @case((3, 5, 4))
  def spring(self, n): return "{} comes in {}".format(N().month(n), "spring")
  @case((6, 7, 8))
  def summer(self, n): return "{} comes in {}".format(N().month(n), "summer")
  @case("default")
  def fall(self, n): return "{} comes in {}".format(N().month(n), "fall")

  def season(self, n): return self.match(n)(n)

if __name__ == "__main__":
  s = S()
  print(s.season(7))
  print(s.season(1))
  print(s.season(10))
  print(s.season(4))
```

### Expected output:

```code
July comes in summer
January comes in winter
October comes in fall
April comes in spring
```