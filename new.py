from PIL import Image
from os import listdir
from os.path import isfile, join

def make_square(img, min_size=256):
    "return a white-background-color image having the img in exact center"
    x, y = img.size
    size = max(min_size, x, y)
    layer = Image.new('RGB', (size, size), (255,255,255))
    layer.paste(img, (int((size - x) / 2), int((size - y) / 2)))
    return layer

fileList = [f for f in listdir('./Meat/') if isfile(join('./', f))]

print(listdir('./Meat/'))
print (fileList)
print (len(fileList))

for f in listdir('./Meat/'):
    curFile = "./Meat/" + f
    print(curFile)

    orig_image = Image.open(curFile)
    rgb_image = orig_image.convert('RGB')
    new_image = make_square(rgb_image)
    new_image.save("Sausage/" + f)
