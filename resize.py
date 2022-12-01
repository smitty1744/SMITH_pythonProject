from PIL import Image

im = Image.open('images/shooter.png')
print(im.size)
new_size = im.resize((50, 50))
new_size.show()