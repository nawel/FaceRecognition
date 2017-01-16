from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

def SVMClassifyer(k, c, g, data, labels):
    clf = SVC(kernel =k, C =c, gamma = g)
    clf.fit(data, labels)
    return clf
    
def gridSearch(clf,C_range, gamma_range,crossVal, data, labels):
    param_grid = dict(gamma=gamma_range, C=C_range)
    grid = GridSearchCV(clf, param_grid=param_grid, cv=crossVal)
    grid.fit(data, labels)
    return grid.best_params_, grid.best_score_