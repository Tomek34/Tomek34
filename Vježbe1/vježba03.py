
#help(input)

import sys


ime = input("Kako se zovete? ")
print("Pozdrav", ime)

prvi_broj = input("Unesi prvi broj")
drugi_broj = input("Unesi drugi broj")

zbroj = prvi_broj+drugi_broj
print(prvi_broj, "+", drugi_broj, "=", zbroj)

oduzimanje = prvi_broj-drugi_broj
print(prvi_broj, "-", drugi_broj, "=", oduzimanje)

print(prvi_broj, "*", drugi_broj, "=", prvi_broj*drugi_broj)
print(prvi_broj, "/", drugi_broj, "=", prvi_broj/drugi_broj)
print(prvi_broj, "**", drugi_broj, "=", prvi_broj**drugi_broj)
print(prvi_broj, "%", drugi_broj, "=", prvi_broj%drugi_broj)


try:
    prvi_broj = int(input("Unesi prvi broj: "))
except ValueError:
    print("Niste unijeli broj!")
    sys.exit(1)

try:
    drugi_broj = int(input("Unesi drugi broj: "))
except ValueError:
    print("Niste unijeli broj!")
    sys,exit(1)


prvi_broj = int(input("Unesi prvi broj: "))
drugi_broj = int(input("Unesi drugi broj: "))

zbroj = prvi_broj+drugi_broj
print(prvi_broj, "+", drugi_broj, "=", zbroj)

oduzimanje = prvi_broj-drugi_broj
print(prvi_broj, "-", drugi_broj, "=", oduzimanje)

djeljenje = prvi_broj/drugi_broj
print(prvi_broj, "/", drugi_broj, "=", djeljenje)

množenje = prvi_broj*drugi_broj
print(prvi_broj, "*", drugi_broj, "=", množenje)