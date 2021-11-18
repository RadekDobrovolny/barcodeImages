import code128
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

def generate_barcode_image(code):
  barcode_image = code128.image(code, height=150, thickness = 2, quiet_zone=True)

  w, h = barcode_image.size
  new_h = h + 90

  new_image = Image.new('RGB', (w, new_h), (255, 255, 255))
  new_image.paste(barcode_image, (0, 20))

  draw = ImageDraw.Draw(new_image)
  fnt = ImageFont.truetype("arial.ttf", 30)
  draw.text( (65, new_h - 60), code, fill=(0, 0, 0), font=fnt)

  # new_image = new_image.resize((int(w / 2), int(new_h / 2)))
  new_image.save("output/" + code + '.png', 'PNG')


codes = open('codes.txt', 'r')
lines = codes.readlines()
 
for line in lines:
  print(line)
  if os.path.exists(line + ".png"):    
    os.remove(line + ".png")
  generate_barcode_image(line.strip())

print("Hotovo!")
