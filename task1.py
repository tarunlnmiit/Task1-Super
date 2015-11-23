from PIL import Image, ImageDraw

im = Image.open('office.jpg')

var = int(input('Enter Variable Pixel Size: '))

draw = ImageDraw.Draw(im)
m,n = im.size

for i in range(0,m,var):
	for j in range(0,n,var):
		box = (i,j,i+var,j+var)
		region = im.crop(box)
		region = region.convert('L')
		pixels = list(region.getdata())
		avg = sum(pixels) // len(pixels)
		region.putdata([avg]*len(pixels))
		im.paste(region,box)
		
for i in range(0,m,var):
	for j in range(0,n,var):
		draw.line((i,j,i+var,j), fill=0, width=1)
		draw.line((i,j,i,j+var), fill=0, width=1)

im.show()
