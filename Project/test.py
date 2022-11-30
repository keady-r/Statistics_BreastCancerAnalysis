import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

filename = 'BeachWaterQuality.csv' 
columns = ['Beach','Date','Total_Coliforms','E_Coli','Enterococci','Sufficient','OBJECTID'] 

    
with open (filename, "r") as f: 
    beach = pd.read_csv(filename, sep= ',', header=None, names=columns)
    beach.head()

sns.FacetGrid(beach,hue="Date",height=5).map(sns.histplot,"Total_Coliforms").add_legend()
plt.savefig('Total_coliforms.png', dpi = 500)
sns.FacetGrid(beach,hue="Date",height=5).map(sns.histplot,"E_Coli").add_legend()
plt.savefig('Ecoli.png', dpi = 500)
sns.FacetGrid(beach,hue="Date",height=5).map(sns.histplot,"Enterococci").add_legend()
plt.savefig('Enterococci.png', dpi = 500)

sns.FacetGrid(beach,hue="Beach",height=5).map(sns.distplot,"Total_Coliforms").add_legend()
plt.savefig('3.png', dpi = 500)
sns.FacetGrid(beach,hue="Beach",height=5).map(sns.distplot,"E_Coli").add_legend()
plt.savefig('2.png', dpi = 500)
sns.FacetGrid(beach,hue="Beach",height=5).map(sns.distplot,"Enterococci").add_legend()
plt.savefig('1.png', dpi = 500)
plt.show()
plt.clf()

filename = "Scatter Plot: Petal Length vs Petal Width.jpg"
plt.show()
plt.savefig(filename)
plt.clf()

sns.scatterplot(x= "E_Coli", y = "Date", legend = True, hue = "Beach" )
plt.legend(labels=["Coli"])
