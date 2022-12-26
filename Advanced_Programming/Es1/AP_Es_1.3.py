# Beyond the well-known Celsius and Fahrenheit, there are other six temperature scales: Kelvin, Rankine, Delisle, Newton, Réaumur, and Rømer 
# (Look at: http://en.wikipedia.org/wiki/Comparison_of_temperature_scales to read about them).

# 1. Write a function (table) that given a pure number returns a conversion table for it (as a string) among any of the 8 temperature scales (remember that functions are objects as well).
# 2. Write a function (toAll) that given a temperature in a specified scale returns a string for all the corresponding temperatures in the other scales, the result must be sorted on the temperatures and the scale must be specified.

def toCelsius(t): return t 
def fromCelsius(t): return t
def toKelvin(t): return t + 273.15
def fromKelvin(t): return t - 273.15
def toFahrenhite(t): return t * 9/5 + 32
def fromFahrenhite(t): return (t - 32) * 5/9
def toRankine(t): return t * (9/5) + 491.67 
def fromRankine(t): return (t - 491.67) * 5/9
def toDelisle(t): return (100 - t) * 3/2
def fromDelisle(t): return 100 - t * 2/3
def toNewton(t): return t * 0.33
def fromNewton(t): return t * 100/33
def toRéaumur(t): return t * 4/5
def fromRéaumur(t): return t * 5/4
def toRømer(t): return  t * 21/40 + 7.5
def fromRømer(t): return (t - 7.5) * 40/21

toT = {'F': toFahrenhite, 'K': toKelvin, 'R': toRankine, 'De': toDelisle, 'N': toNewton, 'Ré': toRéaumur, 'Rø': toRømer, 'C': toCelsius}
fromT = {'F': fromFahrenhite, 'K': fromKelvin, 'R': fromRankine, 'De': fromDelisle, 'N': fromNewton,'Ré': fromRéaumur, 'Rø': fromRømer, 'C': fromCelsius}

def fromTtoAll(val, scale):
    t_celsius = fromT[scale](val)
    return {scale:convert(t_celsius) for scale,convert in toT.items()}

def table(val):
    temperatures = [[temp for scale,temp in sorted(fromTtoAll(val, scale).items(), key=lambda x : x[0])] for scale in sorted(toT.keys())]
    res = " "+(8*"{: ^6} ")+"\n"+(8*("{:<3}"+(8*"{: 6.1f} ")+"\n"))
    scales = values_res = sorted(toT.keys())
    for i in range(len(temperatures)):
        values_res += [scales[i]] + temperatures[i]
    return res.format(*values_res)

print(table(25))

def toAll(val, scale):
    temperatures = fromTtoAll(val, scale)
    del temperatures[scale]
    res = (7*"{{{}[1]:.1f}}◦{{{}[0]}} ").format(*[e for l in zip(range(7),range(7)) for e in l])
    return res.format(*sorted(temperatures.items(), key=lambda item:item[1]))

print("25°F corresponds to ", toAll(25, 'F'))