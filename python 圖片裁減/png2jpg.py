from PIL import Image

img = Image.open("image_path/高科大電子創意競賽時程表.png")
(w, h) = img.size
print('w=%d, h=%d', w, h)

new_img = img.resize((896, 806))
new_img = new_img.convert("RGB")
new_img.save("crop_image_path/高科大電子創意競賽時程表.jpg")