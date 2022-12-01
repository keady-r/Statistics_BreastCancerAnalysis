import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from warnings import filterwarnings
filterwarnings("ignore")

fileGlobalCancersBothSexes = 'Global cancer incidence both sexes.csv'
fileGlobalCancersMen = 'Global cancer incidence in men.csv'
fileGlobalCancersWomen = 'Global cancer incidence in women.csv'
columnsGlobalCancers = ['Index','Rank','Cancer','New cases in 2020','% of all cancers'] 

fileBreastCancer = 'BreastCancerDataSet.csv'
columnsBreastCancer = ["id","diagnosis","radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]

female = pd.read_csv(fileGlobalCancersWomen)
female.head()

male = pd.read_csv(fileGlobalCancersMen)
male.head()

all_cancer = pd.read_csv(fileGlobalCancersBothSexes)
all_cancer.head()

breastCancer = pd.read_csv(fileBreastCancer)
breastCancer.head()
'''''
#Convert to text to read more easily 
with open (fileGlobalCancersBothSexes, "r") as f: 
    cancer_both = pd.read_csv(fileGlobalCancersBothSexes, sep= ',', header=None, names=columnsGlobalCancers)
    cancer_both.head()
    print(" Cancers in Male and Female ", file=open("BothSummary.txt", "w"))
    print(" ___________________________________________", file=open("BothSummary.txt", "a"))
    print('', file=open("BothSummary.txt", "a"))
    print(cancer_both,file=open("BothSummary.txt", "a"))
    print('____________________________________________', file=open("BothSummary.txt", "a"))
    
with open (fileGlobalCancersMen, "r") as f: 
    cancer_men = pd.read_csv(fileGlobalCancersMen, sep= ',', header=None, names=columnsGlobalCancers)
    cancer_men.head() 
    print(" Cancers in Male", file=open("MenSummary.txt", "w"))
    print(" ___________________________________________", file=open("MenSummary.txt", "a"))
    print('', file=open("MenSummary.txt", "a"))
    print(cancer_both,file=open("MenSummary.txt", "a"))
    print('____________________________________________', file=open("MenSummary.txt", "a"))
    
with open (fileGlobalCancersWomen, "r") as f: 
    cancer_women = pd.read_csv(fileGlobalCancersWomen, sep= ',', header=None, names=columnsGlobalCancers)
    cancer_women.head() 
    print(" Cancers in FeMale", file=open("WomenSummary.txt", "w"))
    print(" ___________________________________________", file=open("WomenSummary.txt", "a"))
    print('', file=open("WomenSummary.txt", "a"))
    print(cancer_both,file=open("WomenSummary.txt", "a"))
    print('____________________________________________', file=open("WomenSummary.txt", "a"))

with open (fileBreastCancer, "r" ) as f:
    breastCancer_data = pd.read_csv(fileBreastCancer, sep= ',', header=None,names=columnsBreastCancer)
    breastCancer_data.head() 
    print(" Breast Cancer ", file=open("BreatCancerDataSummary.txt", "w"))
    print(" ___________________________________________", file=open("BreatCancerDataSummary.txt", "a"))
    print('', file=open("BreatCancerDataSummary.txt", "a"))
    print(breastCancer_data,file=open("BreatCancerDataSummary.txt", "a"))
    print('____________________________________________', file=open("BreatCancerDataSummary.txt", "a"))
'''
'''''
#Scatter Plot
plt.plot(male['Cancer'], male ['New cases in 2020'], linestyle='none', marker='o', color='blue')
plt.xticks(rotation = 90)
plt.savefig('SCpltCancerInmales.png', dpi = 500)
plt.show()
plt.plot(female['Cancer'], female ['New cases in 2020'], linestyle='none', marker='o', color='red')
plt.xticks(rotation = 90)
plt.savefig('ScCancerInFemales.png', dpi = 500)
plt.show()

#Line Plot 
plt.plot(male["Cancer"],male["New cases in 2020"], color='b', linestyle='--')
plt.xticks(rotation = 90)
plt.savefig('LinPLtCancerInmales.png', dpi = 500)
plt.show()

#Bar Chart 
plt.hist(male['New cases in 2020'])
plt.xlabel('Cancer')
plt.ylabel('New cases in 2020')
plt.title('example')
plt.savefig('BarCancerInmales.png', dpi = 500)
plt.show()

#sideways bar chart 
plt.figure(figsize=(10,6))
plt.barh(male['Cancer'], male['New cases in 2020'])
plt.xlabel('Cancer')
plt.ylabel('New cases in 2020')
plt.title("Cancer in Men")
plt.savefig('SideBarCancerInmales.png', dpi = 500)
plt.show()

plt.figure(figsize=(10,6))
plt.barh(female['Cancer'], female['New cases in 2020'], color = "red")
plt.xlabel('Cancer')
plt.ylabel('New cases in 2020')
plt.title("Cancer in Women")
plt.savefig('barhCancerInFemales.png', dpi = 500)
plt.show()

#together - horizontal bar
plt.figure(figsize=(10,6))
plt.barh(male['Cancer'], male['New cases in 2020'], color ="blue")
plt.barh(female['Cancer'], female['New cases in 2020'], color = "red")
plt.xlabel('Cancer')
plt.ylabel('New cases in 2020')
plt.title("Cancer in Men(blue), Women (Red)")
plt.savefig('CancerInBoth.png', dpi = 500)
plt.show()
#Together - Bar
plt.figure(figsize=(10,7))
plt.bar(male['Cancer'], male['New cases in 2020'], color ="blue")
plt.bar(female['Cancer'], female['New cases in 2020'], color = "red")
plt.xlabel('Cancer')
plt.xticks(rotation = 90)
plt.ylabel('New cases in 2020')
plt.title("Cancer in Men(blue), Women (Red)")
plt.savefig('CancerInBoth.png', dpi = 500)
plt.show()
'''
def shape(dataset):
    print('='*20,'Dataset Shape','='*20)
    print(dataset.shape)
    print('\n')

def info(dataset):
    print('='*20,'Dataset Info','='*20)
    print(dataset.info())
    print('\n')

def describe(dataset):
    print('='*20,'Dataset Describe','='*20)
    print(dataset.describe())
    print('\n')
    

shape(male)
info(male)
describe(male)

shape(female)
info(female)
describe(female)

df3 = all_cancer[all_cancer['Cancer'] !='All cancers*']

fig = px.pie(names=df3['Cancer'],
            values=df3['% of all cancers'])

fig.update_layout(margin={'b':0,'l':0,'r':0,'t':100},
                 paper_bgcolor='rgb(248, 248, 255)',
                 plot_bgcolor='rgb(248, 248, 255)',
                 title={'font':{
                             'family':'monospace',
                             'size':22,
                             'color': 'grey'
                         },'text':'Global Cancer Incidence In Both Genders',
                        'x':0.45,'y':0.9})

fig.show()

''''''