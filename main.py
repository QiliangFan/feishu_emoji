import json
import cv2
import numpy as np
import os
import imageio
from PIL import Image
import aspose.words as aw

def main():
    coords: dict = config["coords"]
    for name, cord in coords.items():
        print(name)
        x, y, w, h = cord["x"], cord["y"], cord["width"], cord["height"]
        croped = im.crop((x, y, x+w, y+h))
        png_file = os.path.join("img", name)
        croped.save(png_file)
        doc = aw.Document()
        builder = aw.DocumentBuilder()

        cvt = builder.insert_image(png_file)
        cvt.image_data.save(os.path.join("emoji", name.replace(".png", ".gif")))

if __name__ == "__main__":
    if not os.path.exists("img"):
        os.mkdir("img")
    if not os.path.exists("emoji"):
        os.mkdir("emoji")

    config = json.load(open("sprite-meta.json", "r"))
    print(config)
    im = Image.open("sprite-min.png")
    # im.info["transparency"] = 255
    main()