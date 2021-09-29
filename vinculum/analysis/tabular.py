import pandas as pd
import numpy as np
import scipy
from fastcore.all import L

def get_corr(df):
    return pd.DataFrame(np.round(scipy.stats.spearmanr(df).correlation, 4),index=df.columns,columns=df.columns)


def corr_drop_cols(cor, thresh):
    ''' input:  cor is a correlation df such as df.corr().abs().  Thresh is the cutoff for what is too corrolated
        output: list of columns to drop
    '''
    max_corr = dict()
    drop_list = L()
    for col in cor.columns:
        max_corr[col] = 0
        for row in cor.index:
            if row == col: continue
            if row in drop_list: continue
            if cor.loc[row,col] > max_corr[col]: max_corr[col] = cor.loc[row,col]
        if max_corr[col] > thresh: drop_list.append(col)
    return drop_list


def rf_feat_importance(m, df):
    '''Code from github.com/fastai/fastbook chapter 9'''
    return pd.DataFrame({'cols':df.columns, 'imp':m.feature_importances_}).sort_values('imp', ascending=False)


def plot_fi(fi):
    '''Code from github.com/fastai/fastbook chapter 9'''
    return fi.plot('cols', 'imp', 'barh', figsize=(12,7), legend=False)