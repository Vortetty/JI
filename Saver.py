import json
from PIL import Image


OpenMe = "" #file to convert
ColorCount = 0 #0 and below will make no palette changes, any number above 0 will change the number of colors used to that many colors




Image.MAX_IMAGE_PIXELS = None

# saves a png as json
'''
config below
'''
saveto = OpenMe.split(".")[0] + ".ji"

if ColorCount <= 0:
    img = Image.open(OpenMe,mode="r").convert("RGBA")
else:
    img = Image.open(OpenMe,mode="r").convert("RGBA", palette=Image.ADAPTIVE, colors=ColorCount)#using adaptive color to avoid dithering

data = json.loads('{"image": [],"colormap": {},"name": ""}')

def rgb_to_hex(rgb):
    print("#" + ('%02x%02x%02x%02x' % rgb))
    return "#" + ('%02x%02x%02x%02x' % rgb)

colors = img.getcolors(img.size[0]*img.size[1])

for color in colors:
    colorid = colors.index(color)
    color = color[1]
    data["colormap"].update({colorid: rgb_to_hex(color)})

keys = list(data["colormap"].keys())
vals = list(data["colormap"].values())
width, height = img.size
for y in range(height):
    data["image"].append([])
    for x in range(width):
        if rgb_to_hex(img.load()[x, y]) == "#ffffff00":
            data["image"][y].append(str(" "))
        else:
            print(rgb_to_hex(img.load()[x, y]))
            data["image"][y].append(str(keys[vals.index(rgb_to_hex(img.load()[x, y]))]))

print(json.dumps(data, sort_keys=True, indent=4))

f = open(saveto, "w+")
f.write(json.dumps(data))  # , sort_keys=True, indent=4
f.close()
