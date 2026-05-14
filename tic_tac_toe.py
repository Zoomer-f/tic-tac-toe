tf = {"a" : "1", "b" : "2", "c" : "3", "d" : "4", "e" : "5", "f" : "6", "g" : "7", "h" : "8", "i" : "9"}
tfs = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
def p(a) :
    print(a)
def add (o, l):
    l.append(o)
def reset ():
    tf["a"] = "1"
    tf["b"] = "2"
    tf["c"] = "3"
    tf["d"] = "4"
    tf["e"] = "5"
    tf["f"] = "6"
    tf["g"] = "7"
    tf["h"] = "8"
    tf["i"] = "9"
def map ():
    p(" " + tf["a"] + " / " + tf["b"] + " / " + tf["c"] + " ")
    p("---/---/---")
    p(" " + tf["d"] + " / " + tf["e"] + " / " + tf["f"] + " ")
    p("---/---/---")
    p(" " + tf["g"] + " / " + tf["h"] + " / " + tf["i"] + " ")

iN = ""
end = False
tempint = 0
tempint2 = 0
tempstr = ""

num = []
num2 = []
for wasd in range(1, 10):
    add(str(wasd), num)
for wasdd in range(1, 10):
    add(str(wasd), num2)

map()

while end == False:
    p("player x :")
    iN = input()
    if iN == "reset":
        reset()
        map()
        continue
    if iN == "st":
        break
    if iN in num:
        for v in num:
            if iN == v:
                tempint = num.index(v)
                num[tempint] = "gfkmn"
                tempstr = tfs[tempint]
                tf[tempstr] = "\033[31mx\033[0m"
                tempint = 0
                tempint = ""
                map()
    p("player o :")
    iN = input()
    if iN == "reset":
        reset()
        map()
        continue
    if iN == "st":
        break
    if iN in num:
        for v in num:
            if iN == v:
                tempint = num.index(v)
                num[tempint] = "vvotzo"
                tempstr = tfs[tempint]
                tf[tempstr] = "\033[32mo\033[0m"
                tempint = 0
                tempint = ""
                map()