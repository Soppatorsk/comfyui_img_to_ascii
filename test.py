from ascii_magic import AsciiArt 
from PIL import Image, ImageFont, ImageDraw
from fonts.ttf import Roboto

file = 'in.png'

columns = 256
font_size = 8
# w = int(columns * font_size / 1.66) # 1.66 magic number idk
w = int(columns * font_size / 1.66) 

def convert(text, font_size=12, image_file=None):
    font = ImageFont.truetype("LiberationMono.ttf", font_size)
    # font = ImageFont.truetype("Courier New.ttf", font_size, encoding='utf-8')
    image = Image.new('RGBA', (w, w), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    # draw.text((0, 0), text, spacing=font_size/3, fill='red', font=font)
    draw.text((0, 0), text, spacing=4, fill='black', font=font)
    # draw.text((0, 0), text, spacing=font_size/16, fill='black', font=font)
    if image_file == None:
        filename = text.replace(' ', '')
        image_file = '{}.png'.format(filename)
    image.save(image_file, 'PNG')

my_art = AsciiArt.from_image(file)
# my_art.to_html_file("out.html", monochrome=True, width_ratio=2, columns=columns)
# my_art.to_file("out.txt", monochrome=True, width_ratio=2, columns=columns)
convert(my_art.to_ascii(monochrome=True, width_ratio=2.2, columns=columns,), font_size=font_size, image_file="out.png")

