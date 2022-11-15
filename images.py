from PIL import Image

def convert_image(info):
    image = Image.open(f"results/{info[-1]}.{info[1]}")
    image = image.convert("RGB")
    image.save(f"result/{info[-1]}.{info[2]}")

convert_image(["image", "png", "jpg", "test"])