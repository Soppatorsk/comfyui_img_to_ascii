from PIL import Image, ImageFont, ImageDraw
import torch
import numpy as np
from ascii_magic import AsciiArt

class Img_to_ASCII:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {       
                "images": ("IMAGE",),
                "columns": ("INT", {"default": 256, "min": 1, "max": 512}),
                "font_size": ("INT", {"default": 8, "min": 1, "max": 64}),
                "width": ("INT", {"default": 1233, "min": 1, "max": 9999}),
                "width_ratio": ("FLOAT", {"default": 1.45, "min": 0.1, "max": 10, "step": 0.01}),
                "spacing": ("INT", {"default": 0, "min": 0, "max": 64}),
                "font_path": ("STRING", {"default": "C:\lib.ttf"}),
                "color": ("STRING", {"default": "black"}), 
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("images")
    FUNCTION = "img_to_ascii"

    CATEGORY = "image/img_to_ascii"

    def img_to_ascii(self, images, columns, font_size, width, width_ratio, spacing, font_path, color):
        batch_tensor = []
        for image in images:
            image = tensor2pil(image)
            image = image.convert("RGBA")

            art = AsciiArt.from_pillow_image(image)
            ascii = art.to_ascii(monochrome=True, width_ratio=width_ratio, columns=columns)

            font = ImageFont.truetype(font_path, font_size)
            # w = int(columns * font_size / 1.66)
            image = Image.new('RGBA', (width, width), (0, 0, 0, 0))
            draw = ImageDraw.Draw(image)
            draw.text((0, 0), ascii, spacing=spacing, fill=color, font=font)
            batch_tensor.append(pil2tensor(image))
        batch_tensor = torch.cat(batch_tensor, dim=0)
    
        return (batch_tensor, )
        # return (pil2tensor(image), )

# Tensor to PIL
def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

# PIL to Tensor
def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Img_to_ASCII": Img_to_ASCII
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "FirstNode": "My First Node"
}

