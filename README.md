# JI
JI stands for Json Image. Thats right. I wrote an image format that only uses json to store the image.

# The Format (a .JI file)

```json
{
	"image":[
		["0", "4", "4", "4", "3"],		
		["2", "0", "4", "3", "2"],		
		["2", "2", "1", "2", "2"],		
		["2", "3", "4", "0", "2"],		
		["3", "4", "4", "4", "0"]
	],
	"colormap":{
		"0":"#ff0000ff",
		"1":"#800080ff",
		"2":"#ffffffff",
		"3":"#0000ffff",
		"4":"#00000000"
	},
	"name":"test"
}
```

Basically, i store an image using numbers for each pixel, then i map each number to a hex color in the rgba format.

the format is also lossless.

attatched you can see the Mona Lisa as a jpeg and a .JI
