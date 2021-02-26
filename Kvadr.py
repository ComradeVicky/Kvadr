import math

def kvadr():
    g = input("a b c: ")
    e = g.split()

    try:
        a = float(e[0])
        if a == 0:
            print("neni kvadr debile")
            kvadr()
        b = float(e[1])
        c = float(e[2])
    except:
        print("SRAČKO")
        kvadr()
    rov = str(a) + "x\u00b2" + " + " + str(b) + "x" + " + " + str(c)
    f = rov.replace("+ -", "- ")

    print(f)

    D = b * b - (4 * a * c)
    print("Diskriminant: " + str(D))

    if D < 0:
        print("Nemá řešení")
    if D == 0:
        x = (-b + math.sqrt(D)) / (2 * a)
        if str(x).endswith(".0"):
            x = str(x).replace(".0", "")
            print("x = " + str(x))
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        if str(x1).endswith(".0"):
            x1 = str(x1).replace(".0", "")
        if str(x2).endswith(".0"):
            x2= str(x2).replace(".0", "")

        print("x1 = " + str(x1))
        print("x2 = " + str(x2))
    kvadr()
kvadr()