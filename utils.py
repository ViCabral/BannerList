from PIL import Image, ImageDraw, ImageFont
import numpy as np
import imageio
def frame_build(background, product, price):
    '''
    background - pill image that with the supermake
    t background

    products - product introduced by user

    prices - price of the respective product
    '''
    #--------Text insertion----------------------
    #im = Image.open("background.jpg")
    draw = ImageDraw.Draw(background)
    tmp = price.split(",")
    price_d = tmp[0]
    price_q =  f",{tmp[1]}"
    
    #d = ImageDraw.Draw(background)
    name = ImageFont.truetype("arial.ttf", 75)
    font = ImageFont.truetype("arial.ttf", 250)
    font2 = ImageFont.truetype("arial.ttf", 150)
    font3 = ImageFont.truetype("arial.ttf", 70)
    font4 = ImageFont.truetype("arial.ttf", 90)
    # draw multiline text
    x = 650 
    y = 600
    draw.text((x, y), "R$", font=font3, fill=(0,0,0))
    x_s, _ = draw.textsize("R$", font=font3)
    draw.text((650, 250), product, font=name, fill=(0,0,0))
    draw.text(((x + x_s + 20), 450), price_d, font=font, fill=(255,0,0))
    x_s1, _ = draw.textsize(price_d, font=font)
    draw.text(((x + x_s + x_s1 + 20), 450), price_q, font=font2, fill=(255,0,0))
    #im.show()

    #-------Product inserction-------------------
    product_im = Image.open(f"dataset/{product}.png")
    product_im = product_im.resize((550,550))
    background.paste(product_im,(0,100),mask=product_im) 
    return background

def video_build(product_list, price_list):
    fps = 25 
    seconds = 5
    total_frames = seconds*fps
    write_to = 'output.mp4'
    writer = imageio.get_writer(write_to, format='mp4', mode='I', fps=fps) 
    for i in range(len(product_list)):
        for j in range(total_frames):
            processed = frame_build(Image.open("background.jpg"), 
                                     product_list[i], price_list[i])
            writer.append_data(np.asarray(processed))
    writer.close()
    

if __name__ == '__main__':
    video_build(["cebola", "cebola"], ["8,00", "15,00"])