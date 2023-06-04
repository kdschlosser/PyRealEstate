import pandas as pd 
import numpy as np


def weighted_Mean_Sale_Ratio ( y, x ):
  return np.mean(x) / np.mean(y)

def COD( y, x):
    ratio = x / y
    med =  np.median(ratio)
    dev = np.sum(np.abs(ratio - med))
    avgdev=dev / len(ratio)
    cod = 100 * (avgdev / med)
    return cod


def PRD(y, x):
    ratio = x / y
    mnratio = np.mean(ratio)
    mnx = np.mean(x)
    mny = np.mean(y)
    prd = mnratio / (mnx /mny)
    return prd
