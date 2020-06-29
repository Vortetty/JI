import json
import sys

from PIL import Image, ImageDraw, ImageColor


OpenMe = ""+".ji"



# saves json back to png
'''
config below
'''
saveto = OpenMe.split(".")[0] + ".png"


data = open(OpenMe, "r").read()

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data)

print(data)

img = Image.new('RGBA', (len(x["image"][0]), len(x["image"])), (0, 0, 0, 0))

d = ImageDraw.Draw(img)

print(sys.argv[0])
x["colormap"].update(json.loads(sys.argv[0]))

for (indexY, valueY) in enumerate(x["image"]):
    for (indexX, valueX) in enumerate(x["image"][indexY]):
        if(valueX == [""] or valueX.isspace()):
            d.line((indexX, indexY, indexX, indexY), (0, 0, 0, 0))
        else:
            d.line((indexX, indexY, indexX, indexY), ImageColor.getrgb(x["colormap"][valueX]))

img.save(saveto)
