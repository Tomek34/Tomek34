a = int(input("Upišite prvi broj: "))

binarni_a = bin(a)
print("Integer a:", a, "pretvoren u binarni format izgleda:", binarni_a)

# oct
# hex

hexadecimalni_a = hex(a)
print("Integer a:", a, "pretvoren u hexadecimalni format izgleda:", hexadecimalni_a)

octodecimalni_a = oct(a)
print("Integer a:", a, "pretovren u octodecimalni format izgleda:", octodecimalni_a)


hex_boja = "ea4335"

crveni_dio = "ea"
plavi_dio = "35"
zeleni_dio = "43"

red = int("ea", 16)
green = int("43", 16)
blue = int("35", 16)
print(red, green, blue)

print("RGB kod hex boje", hex_boja, "je :", red, green, blue)

red = int(crveni_dio, 16)
green = int(zeleni_dio, 16)
blue = int(plavi_dio, 16)
print("RGB kod hex boje", hex_boja, "je :", red, green, blue)

hex_red = hex(red)
hex_green = hex(green)
hex_blue = hex(blue)
print("Hex kod RGB boje", red, green, blue, "je :", hex_red, hex_green, hex_blue)


ime = "Tomislav"
broj = int(ime, 36)
print(broj)
print(hex(broj))
print(bin(broj))
print(oct(broj))