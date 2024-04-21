from PIL import Image
import os

DIR = "image_path"
SAVE_DIR = "crop_image_path"
SIZE = 80
WID=240
HEI=240

for path in os.listdir(DIR):
    #image_path/path
    im = Image.open(DIR + "/" + path)

    # resize 到 240*240
    im = im.resize((WID, HEI))

    for i in range(int(WID/SIZE)):
        for j in range(int(HEI/SIZE)):
            # (left, upper, right, lower)
            img = im.crop((i*SIZE, j*SIZE, (i+1)*SIZE, (j+1)*SIZE))
            img.save(SAVE_DIR+"/"+str(i)+"_"+str(j)+path)
