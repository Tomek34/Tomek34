import os
import pathlib
from PIL import Image, ImageFilter

direktorij_di_je_slika = "D:\Algebra\Varijable\Vježbe1\Slike"
print(direktorij_di_je_slika)
putanja = pathlib.Path(direktorij_di_je_slika)
print(putanja.parent)

puna_putanja_do_slike = os.path.join(direktorij_di_je_slika, "pero.jpg")

im = Image.open(puna_putanja_do_slike)

print(im.filename)
print(im.format)
print(im.mode)
print(im.size)

#im.show()
if not os.path.exists("thumbnail.png"):
    new_image = im.resize((64, 64))
    print(new_image.size)
    print(im.size)
    new_image.show()
    new_image.save("thumbnail.png")
    new_image.close()
else:
    thumbnail = Image.open("thumbnail.png")
    thumbnail.show()
    thumbnail.close()

contour = im.filter(ImageFilter.SMOOTH_MORE)
contour.show()
im.close()