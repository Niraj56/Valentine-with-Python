# =====================================================================
# Date : 14 Feb 2022
# Title: Valentine
# Made with Love by Niraj
# =====================================================================


import os
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import imageio
import matplotlib.pyplot as plt
from PIL import Image
import glob


# =====================================================================
# required variables
WORD_CLOUD_PNG = 'word_cloud.png'
WORD_CLOUD_GIF = 'word_cloud.gif'
HEART_IMAGE = 'heart1.png'
HEART_X_COORDS = np.array([  0,  44, 115, 170, 209, 250, 263, 245, 183, 123,  68,   0])
HEART_Y_COORDS = np.array([ 145,  178,  195,  184,  161,  126,   73,  -25,  -91, -149, -187, -223])
TEXT_POS = (-110, -254)
DRAW_SPEED = 3 # from 0 to 10
DRAW_WIDTH = 5 # width of the pen

SCREEN_SIZE = (720, 576) # size of the screen


# =====================================================================
# convert png image to gif and save
def to_gif(gif_file_name, png_file_name):
    # Create the frames
    frames = []
    imgs = glob.glob(png_file_name)
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)
     
    # Save into a GIF file that loops forever
    frames[0].save(gif_file_name, format='GIF',
                    append_images=frames[1:],
                    save_all=True,
                    duration=300, loop=0)

# =====================================================================
# random color for word cloud
def random_red_color_func(word=None, font_size=None, position=None, 
                              orientation=None, font_path=None, random_state=None):
    h = 0
    s = 100
    l = int(50 * (float(random_state.randint(60, 120))/100.0))
    return "hsl({}, {}%, {}%)".format(h, s, l)


# =====================================================================
# generate word cloud
def generate_word_cloud(words, image_file, saved_name, gif_file_name):
    mask = imageio.imread(image_file)
    word_cloud = WordCloud(width = 400, 
                           height = 400,
                           color_func = random_red_color_func,
                           background_color = 'white', 
                           stopwords = STOPWORDS, 
                           mask = mask, repeat=True).generate(words)
    
    plt.figure(figsize = (10,8), facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(saved_name)
    to_gif(gif_file_name, saved_name)
    

# =====================================================================
# draw animation
def draw_boundary():
    from turtle import Turtle, Screen, bye, getcanvas, ontimer
    t = Turtle()
    t.speed(1)
    s = Screen()
    s.setup(SCREEN_SIZE[0], SCREEN_SIZE[1])
    
   
    # t.shape('circle')
    
    xs = HEART_X_COORDS
    ys = HEART_Y_COORDS
    xs = np.flip(xs)
    ys = np.flip(ys)
    
    t.penup()
    t.speed(0)
    t.left(135)
    t.pensize(DRAW_WIDTH)
    t.goto(xs[0], ys[0])
    t.pendown()  
    t.speed(DRAW_SPEED)
    
    for i in range(12):
        t.color("red")      
        # t.fd(20)
        t.goto(xs[i], ys[i])   
        
        
        
    xs = -np.flip(xs)
    ys = np.flip(ys)
    
    for i in range(12):
        t.color("red")
        # t.fd(20)
        t.goto(xs[i], ys[i])  
        
    s.bgpic('word_cloud.gif')
        
    t.penup()
    t.speed(0)
    t.pensize(DRAW_WIDTH)
    t.goto(TEXT_POS[0], TEXT_POS[1])
    t.pendown()  
    t.speed(DRAW_SPEED)
    
        
    t.write("HAPPY VALENTINE'S DAY", font=('Arial', 16, 'bold'))
    
    
    s.exitonclick()
    
    bye()
    
    

    
# =====================================================================
if __name__ == '__main__':    
    name = input('Enter her/his name: ')
    words = ', '.join(name.split())
       
    generate_word_cloud(words, HEART_IMAGE, WORD_CLOUD_PNG, WORD_CLOUD_GIF)
    draw_boundary()
    
    os.remove(WORD_CLOUD_GIF)
    os.remove(WORD_CLOUD_PNG)
    
   