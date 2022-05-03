from turtle import width
from PIL import ImageFont, ImageDraw, Image, EpsImagePlugin
from elaphe import barcode


img_size = 668, 626
case = "Z00-13999"  # from sql column NewCaseNo
case_font_size = 135  # font size
level_font_size = 150  # font size
other_font_size = 100  # font size
level = "3"  # from sql column LevelNo
block = "1"  # from sql column BlockNo
method = "ABPAS4"  # from sql column Method
text_vpc = "VPC.LT"
code = "123333333676357"  # from sql column Code
r_code = "R" + code
d_options = options=dict(columns=16, rows=16)

dtm = barcode('datamatrix',r_code,d_options, rows=10, margin = .3, scale = 10)  # doctest: +ELLIPSIS


dtm.save("test.png")
dtm.copy()
print(dtm)

image = Image.new('RGB', img_size, color=(255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", case_font_size)
fontl = ImageFont.truetype("arial.ttf", level_font_size)
fonto = ImageFont.truetype("arial.ttf", other_font_size)
draw.text((10, 10), case, align='right', font=font,fill=(
    0, 0, 0))  # put the text on the image
print(draw.textsize(method))
print(draw.textsize(level))
print(draw.textlength(level))
print(draw.textlength(method))

draw.text((80, 220), level, font=fontl, fill=(
    0, 0, 0))  # put the text on the image
draw.text((20, 450), block, font=fonto, fill=(
    0, 0, 0))  # put the text on the image
draw.multiline_text((80, 450), method, font=fonto, fill=(
    0, 0, 0))  # put the text on the image
draw.text((290, 510), text_vpc, font=fonto, fill=(
    0, 0, 0))  # put the text on the image
image.paste(dtm,(280,150))

image.save("testlabel.png")  # save it.
