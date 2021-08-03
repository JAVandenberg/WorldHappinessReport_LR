# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:49:49 2021

@author: james
"""
import pandas as pd
import seaborn as sns
import numpy as np

from scipy.stats import spearmanr




# given dataframe df
df = pd.read_csv('whr.csv')

# columns to be used as value variables
cols = ['Social support', 'Logged GDP per capita', 'Healthy life expectancy', 'Perceptions of corruption']

# melt the desired columns from dataframe df
dfm = df.melt(id_vars=['Generosity', 'Regional indicator'], value_vars=cols)

# plot the points with color in a FacetGrid
p = sns.lmplot(data=dfm, col='variable', col_wrap=2, col_order=cols, x='value', y='Generosity', hue='Regional indicator', sharey=False, sharex=False, fit_reg=False)

# use regplot to plot the regression line for all points
for i, col in enumerate(cols):
    sns.regplot(x=col, y='Generosity', data=df, scatter=False, ax=p.axes[i], ci=False)

# add plot formatting
p.set_titles(row_template='{row_name}', col_template='{col_name}')  # shorten the column names
p.fig.suptitle("What Impacts Generosity Around the World?", size=22, x=.415)
p.fig.subplots_adjust(hspace=.2, wspace=0.2, top=0.9)  # add spacing between plots

p.savefig('Generosity.png', dpi=300)





#correlation
np.corrcoef(df['Generosity'], df['Social support'])
#array([[ 1.        , -0.11494585],
      

np.corrcoef(df['Generosity'], df['Logged GDP per capita'])
#array([[ 1.       , -0.1992864],

np.corrcoef(df['Generosity'], df['Healthy life expectancy'])
#array([[ 1.        , -0.16175028]


np.corrcoef(df['Generosity'], df['Perceptions of corruption'])
#array([[ 1.        , -0.16396173],
       

spearmanr(df['Generosity'],df['Social support'])
#SpearmanrResult(correlation=-0.08940156785534588, pvalue=0.27824625374953743)

spearmanr(df['Generosity'],df['Logged GDP per capita'])
#Out[29]: SpearmanrResult(correlation=-0.15314192637482774, pvalue=0.062236574988716244)

spearmanr(df['Generosity'],df['Healthy life expectancy'])
# SpearmanrResult(correlation=-0.13827493726636125, pvalue=0.09262036551817333)

spearmanr(df['Generosity'],df['Perceptions of corruption'])
#SpearmanrResult(correlation=-0.1619261495173412, pvalue=0.04850072283757959)





