# Exam of Advanced Programming

###### 2022-02-15

## Exercise 1

Write two functions:

- `anagram` that takes a word and prints all its anagrams
- `anagrams` that prints all the anagrams of each word, in ascendent order, inside a text file, named `wordlist-text.txt`. Once a word is used as an anagram it can't be used as another key for other anagrams, for example if *carets* appears as an anagram of another word, i.e. *crates*, it cannot be used as key for other anagrams.

The anagram words are contained inside the file `wordlist-text.txt`.

The solution must respect the following constraints:

- It must use a functional programming approach, so iteration (except for comprehensions) is forbidden.
- `itertools.groupby` and `functools.reduce` are the only two module's functions that are allowed. Every other module's function is forbidden.

##### Note: an anagram is a word, phrase, or name formed by rearranging the letters of another

### Test example:

```py
from anagrams import *

if __name__ == "__main__":
    print("caters :- ", anagram("caters"))
    print("astride :- ", anagram("astride"))
    print("spine :- ", anagram("spine"))

    print(anagrams())
```

### Output example:

```code
caters :-  carets, caster, crates, reacts, recast, traces
astride :-  aridest, staider, tardies, tirades
spine :-  pines, snipe

abed :- bade, bead
abet :- beat, beta
abets :- baste, betas, beast, beats
abut :- tabu, tuba
acme :- came, mace
acre :- care, race
acres :- cares, races, scare
actors :- costar, castor
actress :- casters, recasts
airmen :- marine, remain
alert :- alter, later
alerted :- altered, related, treadle
ales :- leas, sale, seal
aligned :- dealing, leading
allergy :- gallery, largely, regally
amen :- mane, mean, name
anew :- wane, wean
angel :- angle, glean
antler :- learnt, rental
apt :- pat, tap
arches :- chaser, search
arcs :- cars, scar
are :- ear, era
aridest :- astride, staider, tardies, tirades
arm :- mar, ram
arrest :- rarest, raters, starer
artist :- strait, traits
arts :- rats, star, tars
ascent :- secant, stance
ascot :- coats, coast, tacos
asleep :- elapse, please
asp :- pas, sap, spa
aspired :- despair, diapers, praised
asps :- pass, saps, spas
assert :- asters, stares
aster :- rates, stare, taser, tears
ate :- eat, eta, tea
auctioned :- cautioned, education
awls :- laws, slaw
baker :- brake, break
bard :- brad, drab
bared :- beard, bread, debar
barely :- barley, bleary
bats :- stab, tabs
begin :- being, binge
below :- bowel, elbow
bleats :- stable, tables
bluets :- bustle, sublet, subtle
bores :- robes, sober
brag :- garb, grab
calipers :- replicas, spiracle
caller :- cellar, recall
canter :- nectar, recant, trance
canters :- nectars, recants, scanter, trances
capes :- paces, space
caret :- cater, crate, trace
carets :- caters, caster, crates, reacts, recast, traces
catered :- created, reacted
cider :- cried, dicer
claimed :- decimal, declaim, medical
claps :- clasp, scalp
code :- coed, deco
construe :- counters, recounts, trounces
corset :- escort, sector
cratered :- retraced, terraced
cruel :- lucre, ulcer
dale :- deal, lade, lead
danger :- gander, garden, ranged
dare :- dear, read
darters :- retards, starred, traders
dater :- rated, trade, tread
daters :- trades, treads, stared
dates :- sated, stead
dearth :- hatred, thread
dearths :- hardest, hatreds, threads, trashed
decanter :- cantered, recanted
deigns :- design, signed, singed
deist :- diets, edits, sited, tides
deltas :- lasted, slated
demerit :- merited, mitered
demo :- dome, mode
denter :- rented, tender
desert :- deters, rested
detail :- dilate, tailed
detains :- instead, sainted, stained
detour :- routed, toured
diaper :- paired, repaid
diet :- edit, tide, tied
direst :- driest, stride
discounter :- introduces, reductions
does :- dose, odes
doters :- sorted, stored
dowry :- rowdy, wordy
drapes :- padres, parsed, rasped, spared, spread
drawer :- redraw, reward, warder, warred
dues :- sued, used
duster :- rudest, rusted
earned :- endear, neared
earnest :- eastern, nearest
earns :- nears, saner, snare
ears :- eras, sear
earth :- hater, heart
east :- eats, sate, seat, teas
elan :- lane, lean
emigrants :- mastering, streaming
emit :- item, mite, time
emits :- items, mites, smite, times
emoter :- meteor, remote
endive :- envied, veined
enlarge :- general, gleaner
enlist :- inlets, listen, silent, tinsel
enters :- nester, resent, tenser
eons :- nose, ones
esprit :- priest, sprite, stripe
esprits :- persist, spriest, sprites, stripes
ester :- reset, steer, terse, trees, reset, steer, terse, trees, steer, reset, terse, trees
ether :- there, three
evil :- live, veil, vile
filets :- itself, stifle
filter :- lifter, trifle
flow :- fowl, wolf
forest :- fortes, foster, softer
gilder :- girdle, glider
glare :- lager, large, regal
gnus :- guns, snug, sung
goer :- gore, ogre
gory :- gyro, orgy
gust :- guts, tugs
hare :- hear, rhea
hares :- hears, rheas, share, shear
heaps :- phase, shape
heros :- hoers, horse, shore
hoes :- hose, shoe
hops :- posh, shop
ideals :- ladies, sailed
inks :- sink, skin
ires :- rise, sire
kale :- lake, leak
lair :- liar, rail
lame :- male, meal
lameness :- nameless
lament :- mantel, mantle, mental
lapse :- leaps, pales, peals, pleas, sepal
last :- salt, slat
late :- tale, teal
leap :- pale, peal, plea
leapt :- petal, plate, pleat
least :- slate, stale, steal, tales, teals
lemons :- melons, solemn
limes :- miles, slime, smile
lips :- lisp, slip
lisper :- perils, pliers
list :- silt, slit
lister :- liters, litres, relist, tilers
livers :- silver, sliver
loop :- polo, pool
looped :- poodle, pooled
loops :- polos, pools, sloop, spool
lopes :- poles, slope
lots :- lost, slot
lusters :- results, rustles
manes :- manse, means, names
marines :- remains, seminar
mast :- mats, tams
master :- stream, tamers
mate :- meat, tame, team
mates :- meats, steam, tames, teams
merit :- mitre, remit, timer
merits :- mister, miters, mitres, remits, timers
mesa :- same, seam
nails :- slain, snail
nape :- neap, pane
naps :- pans, snap, span
nets :- nest, sent, tens
nope :- open, peon, pone
noter :- toner, tenor
notes :- onset, stone, tones
now :- own, won
observe :- obverse, verbose
opt :- pot, top
opts :- post, pots, stop, tops
owns :- snow, sown
paled :- pedal, plead
palest :- pastel, petals, plates, pleats, staple
paltry :- partly, raptly
panel :- penal, plane
pares :- parse, pears, rapes, reaps, spare, spear, parse, pears, spare, spear
parley :- pearly, player, replay
parroted :- predator, prorated, teardrop
pars :- raps, rasp, spar, raps, rasp, spar
parses :- passer, spares, sparse, spears
parsley :- parleys, players, replays, sparely
part :- rapt, trap
parties :- pastier, pirates, traipse
parts :- strap, traps
past :- pats, spat, taps
paste :- peats, septa, spate, tapes
paws :- swap, wasp
pelts :- slept, spelt
pertness :- presents, serpents
pest :- pets, step
piers :- pries, spire
pines :- snipe, spine
pinto :- piton, point
pintos :- piston, pitons, points
pores :- poser, prose, ropes, spore
potters :- protest, spotter
present :- repents, serpent
rashes :- shares, shears
rattles :- starlet, startle
ravine :- vainer
realist :- saltier, retails
recused :- reduces, rescued, secured
reigns :- resign, signer, singer
reins :- resin, rinse, risen, siren
repaint :- painter, pertain
repaints :- painters, pantries, pertains
rescue :- recuse, secure
resort :- roster, sorter
restrain :- retrains, strainer, terrains, trainers
retrain :- terrain, trainer
rite :- tier, tire
rites :- tiers, tires, tries
rosiest :- sorties, stories
saint :- satin, stain
salve :- slave, vales, veals
seated :- sedate, teased
serve :- sever, veers, verse
setter :- street, tester
sinew :- swine, wines
skate :- stake, steak, takes, teaks
skated :- staked, tasked
slates :- steals, tassel
state :- taste, teats
stew :- wets, wets
stow :- tows, twos
sway :- ways, yaws
taster :- tetras, treats
thickets :- thickest, thickset
weird :- wired, wider
whiter :- wither, writhe
```