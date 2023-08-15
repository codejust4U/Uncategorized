import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss

np.random.seed(12)
races = ['asian','black','hispanic','other','white']

#generate random data
voter_race = np.random.choice(a=races,p=[0.05,0.15,0.25,0.05,0.5],size=1000)

voter_age = ss.poisson.rvs(loc=18,mu=30,size=1000)

#group data bu race
voter_frame = pd.DataFrame({'race':voter_race,'age':voter_age})
groups = voter_frame.groupby('race').groups

#extract individula groups
asian = voter_age[groups['asian']]
black = voter_age[groups['black']]
hispanic = voter_age[groups['hispanic']]
other = voter_age[groups['other']]
white = voter_age[groups['white']]


# perform ANOVA
ss.f_oneway(asian,black,hispanic,other,white)

import statsmodels.api as sm
from statsmodels.formula.api import ols

model = ols('age ~ race',data=voter_frame).fit()

anova_result = sm.stats.anova_lm(model,typ=2)
print(anova_result)


np.random.seed(12)

#generate random data
voter_race = np.random.choice(a=races,p=[0.05,0.15,0.25,0.05,0.5],size=1000)

# diff. dist. fpr white ages
white_ages = ss.poisson.rvs(loc=18,
                            mu=32,
                            size=1000)
voter_age = ss.poisson.rvs(loc=18,
                           mu=30,
                           size=1000)

voter_age = np.where(voter_race=='white',white_ages,voter_age)


#group age data by race
voter_frame = pd.DataFrame({"race":voter_race,"age":voter_age})
groups = voter_frame.groupby("race").groups

#extract individula groups
asian = voter_age[groups['asian']]
black = voter_age[groups['black']]
hispanic = voter_age[groups['hispanic']]
other = voter_age[groups['other']]
white = voter_age[groups['white']]

# perform ANOVA
ss.f_oneway(asian,black,hispanic,other,white)


model = ols('age ~ race',data=voter_frame).fit()

anova_result = sm.stats.anova_lm(model,typ=2)
print(anova_result)

# get all race pairs
race_pairs = []
for race1 in range(4):
    for race2 in range (race1+1,5):
        race_pairs.append((races[race1],races[2]))


#t-tests
for race1,race2 in race_pairs:
    print(race1, race2)
    print(ss.ttest_ind(voter_age[groups[race1]],voter_age[groups[race2]]))

from statsmodels.stats.multicomp import pairwise_tukeyhsd


tukey = pairwise_tukeyhsd(endog=voter_age,
                          groups=voter_race,
                          alpha=0.05)

tukey.plot_simultaneous()
plt.vlines(x=49.57,ymin=-0.5,ymax=4.5,color='r')
tukey.summary()

plt.show()
