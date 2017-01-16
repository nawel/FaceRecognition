import os
import math
import random

"""
   Function: LabelData 
   Input: Name of the database, either ORL or Shuffield, note that both 
   Output: Train set and test set
   
   Description: The function retreive the images from each folder, labled the images of the same person with the same label, 
                split the images randomly to train and test set.
   
"""
def LabelData(dataset):
    dataDir = "../Dataset/"+dataset+"/"
    listDir = os.listdir(dataDir)
    train_set = []
    test_set = []
    classId = 0
    
    for individuDir in listDir: 
        
        list_img = os.listdir(dataDir+ individuDir)
        t_size = math.floor(len(list_img)*0.7)
        random.shuffle(list_img)

        for img in list_img:
                
            tup = (dataDir+ individuDir+"/" + img, classId)
            if t_size >0:
                train_set.append(tup)
                t_size -= 1
            else:
                test_set.append(tup)

        classId += 1 
    return train_set, test_set 
LabelData("orl")
