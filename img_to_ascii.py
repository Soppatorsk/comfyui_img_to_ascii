from PIL import Image, ImageFont, ImageDraw
import torch
import numpy as np
from ascii_magic import AsciiArt

columns = 256

class Img_to_ASCII:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {       
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "img_to_ascii"

    CATEGORY = "image/img_to_ascii"

    def img_to_ascii(self, image):
        #save file tmp
        image = tensor2pil(image)
        art = AsciiArt.from_pillow_image(image)
        convert(art.to_ascii(monochrome=True, width_ratio=2.2, columns=columns))
        return pil2tensor(image)

# Tensor to PIL
def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

# PIL to Tensor
def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

def convert(text, image_file=None):
    #img in

   #ascii out
    font_size = 8
    w = int(columns * font_size / 1.66)

    # font = ImageFont.truetype("LiberationMono.ttf", font_size)
    font = ImageFont.load_default()
    image = Image.new('RGBA', (w, w), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, spacing=4, fill='black', font=font)
    return image

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Img_to_ASCII": Img_to_ASCII
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "FirstNode": "My First Node"
}

