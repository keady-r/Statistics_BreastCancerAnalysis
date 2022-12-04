#Variables pulled in from Jupyter notebook 

NoteBook1 = [
    "=========================",
    "1. BACKGROUND ON TOPIC   ", 
    "=========================",
    "2.     FUNCTIONALITY     ",
    "=========================",
    "2.1. Adding Labels to Graphs - https://www.w3schools.com/python/matplotlib_labels.asp", 
    "2.2. Scatter Plots - https://www.w3schools.com/python/matplotlib_scatter.asp",
    "2.3. PI Charts - https://www.w3schools.com/python/matplotlib_pie_charts.asp", 
    "2.4. Histograms - https://www.w3schools.com/python/matplotlib_histograms.asp",
    "2.5. SubPlots - https://www.w3schools.com/python/matplotlib_subplot.asp", 
    "2.6. PLotting Grids - https://www.w3schools.com/python/matplotlib_grid.asp",
    "2.7. Read a CSV file using pandas - https://www.w3schools.com/python/pandas/pandas_csv.asp",
    "2.8. Histograms and Density Plots - https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0",
    "=========================",
    "3. CLEAN-CODE PRACTICES  ",
    "=========================",
    "3.1. Solid Principle - https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/#:~:text=The%20SOLID%20Principles%20are%20five,and%20software%20architecture%20in%20general.", 
    "3.2. Clean Code - A HandBook of Agile Software Carftmanship. Robert C Martin page 136. ",  "4.       DATASETS        ",
    "=========================",
    "4.1. World Cancer Research International -  https://www.kaggle.com/datasets/ahmadjalalmasood123/worldwide-cancer-data", 
    "4.2. World Cancer Research International (Available to download at) - https://www.kaggle.com/datasets/mukhazarahmad/worldwide-cancer-data", 
    
    
]
NoteBook2 = [
    "=========================",
    "1. BACKGROUND ON TOPIC   ", 
    "=========================",
    "1.1. https://www.researchgate.net/publication/335984408_Breast_cancer", 
    "1.2. ", 
    "1.3",
    "1.4",
    "1.5",
    "1.6",
    "1.7",
    "1.8", 
    "1.9. Archimedes on the Circumference and Area of a Circle - https://www.ams.org/publicoutreach/feature-column/fc-2012-02?utm_medium=referral&utm_source=t.co",
    "1.10. The Perimeter-Area Relation - https://link.springer.com/chapter/10.1007/978-1-4899-2124-6_12", 
    "1.11. Oxford Dictionary - https://languages.oup.com/google-dictionary-en/",
    "1.12 Distribution of one variable - http://work.thaslwanter.at/Stats/html/statsDistributions.html", 
    "1.13. Shape, Center, and Spread of a Distribution- http://mathcenter.oxford.emory.edu/site/math117/shapeCenterAndSpread/", 
    "1.14 Histogram: Study the shape - https://www.pqsystems.com/qualityadvisor/DataAnalysisTools/interpretation/histogram_shape.php",
    "2.     FUNCTIONALITY     ",
    "=========================",
    "2.1. SubPlots - https://www.w3schools.com/python/matplotlib_subplot.asp", 
    "2.2. Formtting subplots - https://stackoverflow.com/questions/6541123/improve-subplot-size-spacing-with-many-subplots#:~:text=Adjust%20the%20Spacing&text=Change%20figsize%20%3A%20a%20width%20of,redundant%20labels%20on%20each%20subplot."
    "2.3. Histograms and Density Plots - https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0",
    "=========================",
    "3. CLEAN-CODE PRACTICES  ",
    "=========================",
    "3.1. Solid Principle - https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/#:~:text=The%20SOLID%20Principles%20are%20five,and%20software%20architecture%20in%20general.", 
    "3.2. Clean Code - A HandBook of Agile Software Carftmanship. Robert C Martin page 136. "
    "=========================",
    "4.       DATASETS        ",
    "=========================",
    "4.1. Breast Cancer Wisconsin (Diagnostic) Data Set -  https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data",
]
NoteBook3 = [
    "=========================",
    "1. BACKGROUND ON TOPIC   ", 
    "=========================",
    "2.     FUNCTIONALITY     ",
    "=========================",
    "2.1.Numpy Probability test https://towardsdatascience.com/how-to-code-a-fair-coin-flip-in-python-d54312f33da9", 

    "=========================",
    "3. CLEAN-CODE PRACTICES  ",
    "=========================",
    "3.1. Solid Principle - https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/#:~:text=The%20SOLID%20Principles%20are%20five,and%20software%20architecture%20in%20general.", 
    "",
    "3.2. Clean Code - A HandBook of Agile Software Carftmanship. Robert C Martin page 136. "
]

def ref(noteBookName):
    if noteBookName == "1_GlobalCancers_TrendsInFrequency":
        return NoteBook1
    elif noteBookName == "2_BreastCancer_TrendsInBenignAndMalignantCells":
        return NoteBook2
    else:
        return NoteBook3