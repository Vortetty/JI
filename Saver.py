import json
from PIL import Image


OpenMe = "" #file to convert




Image.MAX_IMAGE_PIXELS = None

# saves a png as json
'''
config below
'''
saveto = OpenMe.split(".")[0] + ".ji"


img = Image.open(OpenMe,mode="r").convert("RGBA")

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
