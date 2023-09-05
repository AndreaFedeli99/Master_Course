# Exam of Advanced Programming

###### 2023-09-05

## Exercise 1

An **alternade** is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original word, make up as many **real** words as the alternade length. All letters must be used, but the smaller words are not necessarily of the same length. For example, a word with seven letters where every letter is used will produce a four-letter word and a three-letter word.

In the majority of alternades, every second letter is used to make two smaller words, but in some cases, every third letter is used to make three smaller words and so on. Theoretically, a very long word could use every fourth/fifth/... letter to make four/five/... smaller words; e.g., «partitioned» is an alternade for «pin», «ate», «rid», and «to».

In this exercise is required to implement a generator, named `alternade_generator`, parametric on a dictionary filename and on hte number of the alternade, i.e., a couple word and a list of its spawns (spawned as for the rules above) checked into the dictionary that all the spawns are real words. As a dictionary use the file named `dictionary.txt` (it is already sorted do not change it).

### Test example:

```py
from alternade import *

if __name__ == "__main__":
    for i in range(2,5):
        tot = 0
        var_format = "«{0}» is an alternade for "+\
            ("«{{{}}}», "*(i-1)).format(*range(1,i))+"and «{{{}}}»".format(i)
        for w, a in alternade_generator("dictionary.txt", i):
            tot+=1
            print(var_format.format(w,*a))
        print("There are {0} alternade of lenght {1} in this dictionary\n"
                    .format(tot, i))
```

### Expected output:

```
«aids» is an alternade for «ad», and «is»
«aims» is an alternade for «am», and «is»
«allied» is an alternade for «ale», and «lid»
...
«wooded» is an alternade for «woe», and «odd»
«worry» is an alternade for «wry», and «or»
There are 235 alternade of lenght 2 in this dictionary

«abacuses» is an alternade for «ace», «bus», and «as»
«abased» is an alternade for «as», «be», and «ad»
...
«womanised» is an alternade for «was», «one», and «mid»
There are 83 alternade of lenght 3 in this dictionary

«ballyhoo» is an alternade for «by», «ah», «lo», and «lo»
«corporeal» is an alternade for «col», «or», «re», and «pa»
...
«violations» is an alternade for «van», «its», «oi», and «lo»
There are 15 alternade of lenght 4 in this dictionary
```

## Exercise 2



### Test example:

```py
from markdown_parser import translate

if __name__ == "__main__":
    print(translate("Advanced_Programming/Exams/2023-09-05/Es2/test.md"))
```

### Expected output:

```
<html>
<h3>header 1</h3>
<br />

<h1>header 3</h1>
<br />

<h2>header 2</h2>

<p>This is an example of a paragraph.</p>

<p>Some text with <strong>bold text</strong>, <em>italic text</em> and <code>console style text</code> inside a paragraph.</p>

<p>The following is an example of an unordered list:</p>
<ul>
    <li>first item</li>
    <li><em>second item</em></li>
    <li>third item</li>
</ul>

<p>The following is an example of an ordered list:</p>
<ol>
    <li>first item</li>
    <li>second item</li>
    <li><code>third item</code></li>
</ol>

</html>
```