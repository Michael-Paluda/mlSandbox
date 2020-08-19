import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

pres =  pd.read_csv("C:\\Users\\Michael Paluda\\Downloads\\president_heights_party.csv", index_col = 'name')
y = pd.Series([1, 2, 3, 4], index = ['h', 'g', 'i', 'f'])

x = pd.DataFrame({'squared':[i ** 2 for i in range(25)],
                        'exponent':[2 ** i for i in range(25)]}, index = [i for i in range(25)])

data_url = 'http://bit.ly/2cLzoxH'
# read data from url as pandas dataframe
world = pd.read_csv(data_url)

plt.style.use('ggplot')