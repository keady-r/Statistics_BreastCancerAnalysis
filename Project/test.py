import sys
sys.path.insert(1, 'SetUp/')
import PackageInstall 

from PackageInstall import *

breastCancer = pd.read_csv("DataSets/BreastCancerDataSet.csv")
breastCancer.head()

breastCancer_subsection=breastCancer.loc[2:;,1]

sns.pairplot(breastCancer, hue = 'diagnosis')
plt.show()

