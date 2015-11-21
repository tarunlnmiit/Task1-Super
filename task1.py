from PIL import Image, ImageDraw

im = Image.open('img/office.jpg')
m,n = im.size

# draw = ImageDraw.Draw(im)
# p_x, p_y = map(int, input().strip().split())
# for i in range(0, m, p_x):
# 	for j in range(0, n, p_y):
# 		draw.line((i,j,i,j+p_y), fill=0)
# 		draw.line((i,j,i+p_x,j), fill=0)
# im.show()
for i in range(m):
	for j in range(n):
		r, g, b = im.getpixel((i, j))
		x = int((0.299*r) + (0.587*g) + (0.114*b))
		im.putpixel((i, j), (x,x,x))

im.show()