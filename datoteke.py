#write_file = open ("ime_datoteke.txt", "w"):
with open("ime_datoteke.txt", "a") as write_file:
    write_file.write("vrstica 1\n")
#konec konteksta - datoteka zaprta

with open("ime_datoteke.txt", "r") as read_file:
    vsebina = read_file.read()
print vsebina

vsebina = vsebina.split("\n")

for line in vsebina:
    print line
    line = line.split()
    print line
    if len(line) == 2:
        print line[-1]