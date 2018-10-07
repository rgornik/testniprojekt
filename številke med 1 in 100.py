print "Dobrodosli v igri fizzbuzz"

izberi = raw_input("Izberi stevilko med 1 in 100: " )

try:
    izberi = int(izberi)
    for izberi in range(1, izberi+1):
        if izberi % 3 == 0:
            print "fizz"
        elif izberi % 5 == 0:
            print "buzz"
        elif izberi % 3 == 0 and izberi % 5 == 0:
            print "fizzbuzz"
        else:
            print izberi
except Exception as e:
    print "Vnesi celo stevilo"


text = "Program velike Crke spremeni v Male"

print text

print text.lower()