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

    for subject in (glob.glob(sourceDir + "/*/")):

        print(subject)
        for sequence in (glob.glob(subject + "*/")):
            # print(os.path.join(sourceDir, subject))
            #print("\t" + sequence)
            for png in glob.glob(sequence + "*.png"):
                #print("\t\t" + png)
                imagePaths.append("*.png")

    print(imagePaths)





if __name__ == "__main__":
    main()







