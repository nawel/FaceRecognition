from DataSet import LabelData
from extract_descriptors import extract_sift
from extract_descriptors import extract_surf
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import random
from sklearn.metrics import accuracy_score

print 'Getting the data'
train, test  = LabelData("orl")

descriptors = []
labels = []

print 'Data description'
for img in train:
    kp, des = extract_sift(img[0])
    for d in des :
        descriptors.append(d)
        labels.append(img[1])
        
print 'Data description'

c = list(zip(descriptors, labels))
random.shuffle(c)
descriptors, labels = zip(*c)


print 'Training SVM'
#C_range = np.logspace(0, 12, 5,base=2.0 )
#gamma_range = np.logspace(-8, 4, 5, base=2.0)
#param_grid = dict(gamma=gamma_range, C=C_range)
svm = SVC(kernel ="rbf", C =10.0, gamma = 0.00001)
svm.fit(descriptors, labels)

# SIFT GRID SEARCH
"""C_range = [1,10,100,1000]
gamma_range = [0.1,0.001, 0.0001, 0.00001]
param_grid = dict(gamma=gamma_range, C=C_range)
grid = GridSearchCV(svm, param_grid=param_grid, cv=3)
grid.fit(descriptors, labels)"""

# SURF GRID SEARCH

"""C_range = [1,10,100,1000]
gamma_range = [0.1,0.001, 0.0001, 0.00001]
param_grid = dict(gamma=gamma_range, C=C_range)
grid = GridSearchCV(svm, param_grid=param_grid, cv=3)
grid.fit(descriptors, labels)



print("The best parameters are %s with a score of %0.2f"
      % (grid.best_params_, grid.best_score_))

scores = grid.cv_results_['mean_test_score'].reshape(len(C_range),
                                                     len(gamma_range))

"""







accuracy = 0
total_imgs = len(test)

for img in test:
    
    real_label = img[1]
    kp, des = extract_sift(img[0])
    pred = svm.predict(des)
    counts = np.bincount(pred)
    pred_label = np.argmax(counts)
    if real_label == pred_label :
        accuracy +=1
    print img[0] + " - Real: " + str(real_label) + " - Pred :" + str(pred_label)

