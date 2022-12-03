#Variables pulled in from Jupyter notebook 

NoteBook1 = [
    "1. Example 1", 
    "2. Example 2",
    "3. Example 3", 
    "4. Example 4 ",
]
NoteBook2 = [
    "1. ", 
    "2. ",
    "3. ", 
    "4. ",
]
NoteBook3 = [
    "1.else ", 
    "2.else ",
    "3. ", 
    "4. ",
]
def ref(noteBookName):
    if noteBookName == "1_GlobalCancers_TrendsInFrequency":
        return NoteBook1
    elif noteBookName == "2_BreastCancer_TrendsInBenignAndMalignantCells":
        return NoteBook2
    else:
        return NoteBook3