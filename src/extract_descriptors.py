"""
FaceRecognition - Extract descriptors

"""
__author__ = "Nawel Medjkoune, Fella Belkham"

 
def extract_sift(path, octave=3, contrast=0.03, edge=10, sigma=1.6):    
    """
    Extract SIFT keypoints and descriptors from an image
    """
    import numpy as np
    import cv2
    img=cv2.imread(path,0)
    sift = cv2.SIFT(nOctaveLayers=octave, contrastThreshold=contrast, edgeThreshold=edge, sigma=sigma)
    kp, des = sift.detectAndCompute(img,None)
    
    return kp,des
    
def extract_surf(path, hessian=50, octave=4, octaveLayers=2, ext=False):    
    """
    Extract SURF keypoints and descriptors from an image
    """
    import numpy as np
    import cv2
    img=cv2.imread(path,0)
    surf = cv2.SURF(hessianThreshold=hessian, nOctaves=octave, nOctaveLayers=octaveLayers, extended=ext)
    kp, des = surf.detectAndCompute(img,None)
    
    return kp,des

def matcher(kp1, kp2, des1, des2):
    import cv2
    import drawMatches as dm
    # BFMatcher with default params
    bf = cv2.BFMatcher()

    matches = bf.knnMatch(des1,des2, k=2)

    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])


    # cv2.drawMatchesKnn expects list of lists as matches.
    return good