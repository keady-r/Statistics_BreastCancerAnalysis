# Description of this Repository
Within this repository you will find the submission for my 2022 Programming for Data Analysis Project for the Atlantic Technological University. This project aims to explore the trend in cancer research. 

## Structure of the layout:
In addition to the research into the topic documented within the Jupyter notebook pages extensive reseach was also done into how to best write and format the code. Paricular attention was that given to the SOLID princiles of coding () and the clean code practices of "". 

Within this repository you should find:
1. SetUp: This folder contains the necessary code to run the project. A conscious decision was made not to put the functions/references/packages directly into the jupyyter Notebooks to best adhere to the following clean code practices - DRY ('Don't Repeat Yourself), and S - Single Responsibility, from the S.O.L.I.D principles. 
    - Functions - File containing fucntions that can be used across multiple jupyter notebooks. 
    - PackageInstall - containing the necessary python packages to run the code. 
    - References - Contains a list of all the references used throughout research project and an appropriate function to ensure the references are appended to the correct notebook. 
2. Jupyter NoteBooks - Devided out into a Start, Middle, and End. Labeled in the asending order to which they should be ran in the following Order (1-4):
    - 1_GlobalCancers_TrendsInFrequency
    - 2_BreastCancer_TrendsInBenignAndMalignantCells
    - 3_SimulatedCaseStudy

3. Dataset Folder - containg the datasets used within this research project and from which the trending within the Jupyter Notesbooks is based off. 

# To Run this project 
- Download the repository from gihub. 
- Install the packages from the Package Install script. 
- Open the Jupyter Notebooks and run the code from Jupyter Notebook

# Authors Notes:
## Idea Behind the Project 
Initally this project was aimed at researching the potential for hydrolic energy in Ireland, to evalute the current structure and calculate cost savings (if any) when compared to the more dominitly used fossil fuel while also comparing the environmental imapct. Though there were some datasets avaialbe that initially sparked an interest, the efforts were in vain (on this ocasion at least) as there was limit resources to support and compare the datasets. 

The direction of the project shifted towards healthcare and one topic stood out amongst the rest for it's extensive research and access to datasets, that being, the study of cancer. Through investigation it quickly became apparent that one of the most predominate cancers in males was prostate cancer while in females, breast cancer. I was curious as to why the leading cause of this disease in either sex inheritantly revolved around organs/tissues that were laregly specific to the gender and upon googling, no justification was given and hence the problem statement for this project was created : Is your Sex the reason for cancer ---> FInal title to come". 

From the initiation of this project let me state that I do not intent to answer this problem statement indefinitely as I am aware that this area has been researched extensively and that there are many different variables when it comes to cancer such as genetics, environmental exposures, underlining healthissues, ages etc. The purpose of this project instead is to showcase my ability to synthesis a dataset, evaluate any possible trends and relationships while using python and relvant python programming packages. 

I decided to create a functions script so that the same functions can be ran across different Jupyter notebooks. This decision was made in order to keep the code DRY 'Don't Repeat Yourself' and SOLID principles in mind (S - The Single Responsibility Principle). 

 