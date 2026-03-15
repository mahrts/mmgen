"""This module loads and transforms images with pillow."""

import os
from random import randint
from PIL import Image, ImageDraw, ImageFont

class MemeEngine():
    """The Meme Engine Module is responsible for manipulating and drawing text onto images.

    Attribute:
        output_dir {str} -- the folder location for the output images.
    """

    def __init__(self, output_dir: str) -> None:
        self.output_dir = output_dir


    def make_meme(self, image_path: str, text = None, author = None, width=500):
        """Process the image with pillow and return the path to the processed image."""
        with Image.open(image_path) as img:

            if img.size[0] > width:
                new_width = width
                new_height = int(img.size[1] * width/img.size[0])
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            if text is not None and author is not None:
                caption_text = f"{text}\n   - {author}"
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("MemeGenerator/fonts/SwedenSansSemiBold.ttf",
                                         size=20)

                (x, y) = map(lambda elem: randint(0, elem),
                             (img.size[0] // 2, int(img.size[1] / (5/4))))
                draw.multiline_text((x, y), caption_text, font=font, fill='white')

                # save to output_dir
                if not os.path.isdir(self.output_dir):
                    os.mkdir(self.output_dir)
                tmp = self.output_dir + "/" + f"{randint(0,1000000)}.{image_path.split(".")[-1]}"
                img.save(tmp)
        return tmp
