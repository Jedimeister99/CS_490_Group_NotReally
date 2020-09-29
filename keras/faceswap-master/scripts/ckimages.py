#!/usr/bin python3

"""extract images from CK+ dataset"""

#To-Do:
#go to CK+ dataset
    #open subject file from CK+ dataset
    #go to individual subjects
    #from subjects go to sequences
        #extract image paths as strings, append to list
#change line 46 in extract.py to extract images from list

import os
import glob



#os.chdir("/media/Data/CK+/CK+/cohn-kanade-images")
#cohn-kanade-images level?

def main ():
    imagePaths = []
    sourceDir = "/media/Data/CK+/CK+/cohn-kanade-images"

    for subject in (os.listdir(sourceDir)):
        #sequence level?
        #print(subject)
        for sequence in (os.listdir(os.path.join(sourceDir, subject))):
            print(sequence)
            for file in (os.listdir(os.path.join(sourceDir, subject, sequence))):
                if file.endswith(".png"):
                    imagePaths.append(os.path.join(sourceDir,subject,sequence,file))
    for x in range(len(imagePaths)):
        print(imagePaths[x])



if __name__ == "__main__":
    main()







