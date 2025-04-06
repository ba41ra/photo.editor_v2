import os
from PIL import Image
for number in range(1,6):
    image = Image.open(f'photo11U/photo_{number}.jpg')
    file_path = f"photo_end_{number}"
    if not os.path.isdir(file_path):
        os.mkdir(f'photo11U/{file_path}')
    image_Vk = image.resize((1400, 1000))
    image_Vk.save(f"photo11U/photo_end_{number}/photo_Vk.png", "png")
    image_Inst = image.resize((1080, 1080))
    image_Inst.save(f"photo11U/photo_end_{number}/photo_Inst.png", "png")
    image_Fb = image.resize((1200, 628))
    image_Fb.save(f"photo11U/photo_end_{number}/photo_Fb.png", "png")