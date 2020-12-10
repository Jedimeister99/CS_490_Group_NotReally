import os
from os import listdir
from PIL import Image
def main(args):
 CKfilePath = "/media/Data/CK+/CK+/cohn-kanade-images"
 image_path = CKfilePath
 CKimageName = ""
 CKimageList = []
 for subject in os.listdir(CKfilePath):
    if(os.path.isdir(os.path.join(CKfilePath, subject))):
       for seq in os.listdir(os.path.join(CKfilePath, subject)):
            if(os.path.isdir(os.path.join(CKfilePath, subject, seq))):
                CKtempList = []
                for image in os.listdir(os.path.join(CKfilePath, subject, seq)):
                        for filename in listdir(image_path):
                                if filename.endswith('.png'):
                                        try:
                                                img = Image.open("/media/Data/CK+/CK+/cohn-kanade-images/S999/001/S999_001_00000001") # open the image file
                                                img.verify() # verify that it is, in fact an image
                                                print('Valid Image', filename)
                                        except (IOError, SyntaxError) as e:
                                                print('Bad file:', filename)
