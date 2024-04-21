from PIL import Image

img = Image.open("image_path/use/alert2.png")
(w, h) = img.size
print('w=%d, h=%d', w, h)

new_img = img.resize((45, 45))
new_img.save("crop_image_path/45x_png/alert77.png")
