import numpy as np
from skimage.filters import threshold_otsu, threshold_local

'''
getOtsu: returns otsu threshold for a gray image
'''
def Otsu(im):
    h = im.get_histogram()
    h = h / np.sum(h)
    accum = getAccum(h)
    media_t = np.zeros(256,  np.float32)
    #compute media for each t in [0..255]
    for i in range(0,256):
        media_t[i] = media_t[i-1] + i*h[i]
    mu = media_t[255]
    best_t = 0
    best_val = 0
    eps = 0.0001
    for t in range(1,256):
        w0 = accum[t]
        w1 = 1.0 - w0
        mu_0 = media_t[t] / (w0 + eps)
        mu_1 = (mu - media_t[t]) / (w1 + eps)
        val = w0*(mu_0 - mu)*(mu_0 - mu) + w1*(mu_1 - mu)*(mu_1 - mu)
        if val > best_val:
            best_val = val
            best_t = t
    return best_t

def Adaptative(im):
    block_size = 35
    return threshold_local(im.image, block_size, offset=10)
#compute accum
def getAccum(histogram, length=256):
    accum=np.zeros(length)
    accum[0]=histogram[0]
    for i in range(1,length):
        accum[i]=accum[i-1]+histogram[i]
    return accum