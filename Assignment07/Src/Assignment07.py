'''
Created on Feb 26, 2020
Assignment 07 by Jake Luebbe
@author: nicomp
'''
import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont

default_color_red = 228
default_color_green = 150
default_color_blue = 150

def generate_random_string(length):
    random_string = ""
    
    for i in range(0,length):
        random_string = random_string + random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVQXYZ')
    return random_string

def draw_random_ellipse(draw):
    # A random circle on the image
    a = random.randrange(10, 300, 1)
    b = random.randrange(10, 275, 1)
    c = a + random.randrange(10, 90, 1)
    d = b + random.randrange(10, 90, 1)
    draw.ellipse((a,b,c,d), fill=(default_color_red + random.randrange(-100,100,1), 
                                  default_color_green + random.randrange(-100,100,1), 
                                  default_color_blue + random.randrange(-100,100,1), 255), 
                                  outline = "black")

fontList = ["Aaargh.ttf", "Promocyja096.ttf", "CHOPS__.TTF", "shangri-la.ttf"]

def generate_captcha():
    '''
    Generate a captcha
    :return: A tuple (image, captcha string encoded in the image)
    '''
    #Added the random 6-10 character string length
    captcha_string = generate_random_string(random.randint(6,10))
#   print(">" + captcha_string + "<")
    captcha_image = Image.new("RGBA", (400, 200), (default_color_red,default_color_green,default_color_blue))
    draw = ImageDraw.Draw(captcha_image, "RGBA")
    for i in range(1,20):
        draw_random_ellipse(draw)

    #font = fontList[random.randint(0,3)]
    fontStyle = ImageFont.truetype(fontList[random.randint(0,3)], 48)     # font must be in the same folder as the .py file. 
    # Arbitrary starting co-ordinates for the text we will write
    x = 10 + random.randrange(0, 100, 1)
    y = 79 + random.randrange(-10, 10, 1)
    
    
    for letter in captcha_string:
#       print(letter)
        draw.text((x, y), letter, (0,0,0),font=fontStyle)    # Write in black
        x = x + 35
        y = y +  random.randrange(-10, 10, 1)
    
    return (captcha_image, captcha_string)  # return a heterogeneous tuple

def save_image( imageObject, outfilename ) :
    """
    Save an image to disk
    :param imageObject: The Image to save
    :param outfilename: The target file
    """
    try:
        imageObject.save( outfilename )
    except:
        print("save_image(): Unable to save" + outfilename)


