class Img_to_ASCII:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE")
    RETURN_NAMES = ()

    FUNCTION = "img_to_ascii"

    #OUTPUT_NODE = False

    CATEGORY = "image/img_to_ascii"

    def img_to_ascii(self):
        
        return ()


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Img_to_ASCII": Img_to_ASCII
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "FirstNode": "My First Node"
}