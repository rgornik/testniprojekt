def ime_funkcije(x, y):
    return x + y

rezultat = ime_funkcije(1, 2)
print rezultat
print rezultat + 5

print ime_funkcije(4, 6)
print ime_funkcije(45, 22)

def test_ime_funkcije():
    assert ime_funkcije(2, 3) == 5
    print "Test passed"

test_ime_funkcije()

print __name__

if __name__ == "__main__":
    test_ime_funkcije()
    print __name__