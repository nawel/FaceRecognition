import os
import math

def LabelData(dataset):
    dataDir = "../Dataset/"+dataset+"/"
    listDir = os.listdir(dataDir)
    #targetDir = random.choice(listDir)
    train_set = []
    test_set = []
    classId = 0
    
    for individuDir in listDir: 
        
        list_img = os.listdir(dataDir+ individuDir)
        t_size = math.floor(len(list_img)*0.7)
        #print len(list_img), t_size

        for img in list_img:
#            if individuDir == targetDir:
                
            tup = (dataDir+ individuDir+"/" + img, classId)
            if t_size >0:
                train_set.append(tup)
                t_size -= 1
            else:
                test_set.append(tup)
#            else:
#                tup = (dataDir+ individuDir +"/" + img, classId)
#                if len(train_set) < train_size :
#                    train_set.append(tup)
#                else:
#                    test_set.append(tup)
    
        classId += 1 
    #pickle.dump(listImge, open(os.getcwd()+"/LabeledData.obj", "wb"))
    #print "The client individual is : " + targetDir
    return train_set, test_set 
   

#train_set, test_set, target = LabelData("sheffield")
#print train_set
#print test_set
#tr, ts, tar= LabelData("orl")
#print ts