'''
Created on Feb 26, 2020

@author: nicomp
'''

from Src.Assignment07 import*

result = generate_captcha()
myCaptcha = result[0]
captcha_string = result[1]
print(">" + captcha_string + "<")
myCaptcha.show()
save_image(myCaptcha, "keeper.jpg")