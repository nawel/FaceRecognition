from __future__ import division
from DataSet import LabelData
from extract_descriptors import extract_sift
from extract_descriptors import extract_surf
from SVM import SVMClassifyer
import numpy as np
import random
import cv2 
from image_processing import *

"""
Testing the SIFT Descriptors

"""
print 'Getting the data ...'
train, test  = LabelData("orl")
descriptors = []
labels = []

print 'Applying Sift ...'
for img in train:
    im=cv2.imread(img[0])
    kp, des = extract_sift(im)
    for d in des :
        descriptors.append(d)
        labels.append(img[1])
        
c = list(zip(descriptors, labels))
random.shuffle(c)
descriptors, labels = zip(*c)

print "Training the classifyer ..."

svm = SVMClassifyer("rbf", 10, 0.00001, descriptors, labels)

accuracy = 0
total_imgs = len(test)

for img in test:
    
    real_label = img[1]
    im=cv2.imread(img[0])
    kp, des = extract_sift(im)
    pred = svm.predict(des)
    counts = np.bincount(pred)
    pred_label = np.argmax(counts)
    if real_label == pred_label :
        accuracy +=1
    #print img[0] + " - Real labe: " + str(real_label) + " - Pred label:" + str(pred_label)
accuracy = accuracy/total_imgs*100
print "Accuracy obtained using SIFR is: %.2f" % accuracy + "%"

"""
Testing variation on the SIFT Descriptors

"""
listFunctions =["gaussian_blur","median_blur","brightness","darker","erosion","dilation","gaussian_noise","salt_pepper"]
accuracy = 0
total_imgs = len(test)

for fnc in listFunctions: 
    print "Testing Surf with " + fnc
    for img in test:
            real_label = img[1]
            im=cv2.imread(img[0])
            im = globals()[fnc](im)
            kp, des = extract_sift(im)
            pred = svm.predict(des)
            counts = np.bincount(pred)
            pred_label = np.argmax(counts)
            if real_label == pred_label :
                accuracy +=1        
        #print img[0] + " - Real labe: " + str(real_label) + " - Pred label:" + str(pred_label)
    accuracy = accuracy/total_imgs*100
    print "Accuracy obtained after applying "+ fnc + " is: %.2f" % accuracy + "%"


"""
Testing the SURF Descriptors

"""
print 'Getting the data ...'
train, test  = LabelData("orl")
descriptors = []
labels = []

print 'Applying Sift ...'
for img in train:
    im=cv2.imread(img[0])
    kp, des = extract_surf(im)
    for d in des :
        descriptors.append(d)
        labels.append(img[1])
        
c = list(zip(descriptors, labels))
random.shuffle(c)
descriptors, labels = zip(*c)

print "Training the classifyer ..."
svm = SVMClassifyer("rbf", 10000, 0.1, descriptors, labels)

accuracy = 0
total_imgs = len(test)

for img in test:
    
    real_label = img[1]
    im=cv2.imread(img[0])
    kp, des = extract_surf(im)
    pred = svm.predict(des)
    counts = np.bincount(pred)
    pred_label = np.argmax(counts)
    if real_label == pred_label :
        accuracy +=1
    #print img[0] + " - Real labe: " + str(real_label) + " - Pred label:" + str(pred_label)
accuracy = accuracy/total_imgs*100
print "Accuracy obtained is: %.2f" % accuracy + "%"


"""
Testing variation on the SURF Descriptors

"""
listFunctions =["gaussian_blur","median_blur","brightness","darker","erosion","dilation","gaussian_noise","salt_pepper"]
accuracy = 0
total_imgs = len(test)

for fnc in listFunctions: 
    print "Testing Surf with " + fnc
    for img in test:
            real_label = img[1]
            im=cv2.imread(img[0])
            im = globals()[fnc](im)
            kp, des = extract_surf(im)
            pred = svm.predict(des)
            counts = np.bincount(pred)
            pred_label = np.argmax(counts)
            if real_label == pred_label :
                accuracy +=1        
        #print img[0] + " - Real labe: " + str(real_label) + " - Pred label:" + str(pred_label)
    accuracy = accuracy/total_imgs*100
    print "Accuracy obtained after applying "+ fnc + " is: %.2f" % accuracy + "%"

