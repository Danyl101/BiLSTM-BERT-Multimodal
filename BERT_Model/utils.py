import os 
from config_loader import config
import csv


def text_acquire(dir):
    all_text=[]
    all_filename=[]
    for filename in os.listdir(dir):
        filepath=os.path.join(dir,filename)
        with open(filepath,"r",encoding="utf-8")as f:
            text=f.read()
            all_text.append(text)
            all_filename.append(filename)
    return all_text,all_filename
    
def text_chunking(texts,max_text=450,step=350):
    all_text=[]
    for text in texts:
        all_snippets=[]
        for start_idx in range(0,len(text),step):
            text_snippet=text[start_idx:start_idx+max_text]
            all_snippets.append(text_snippet)
        all_text.append(all_snippets)
    return all_text

def label_acquire(filename):
        with open(config['paths']['bert']['labels']['original_label'],"r",encoding="utf-8",errors="replace")as csvfile:
            reader=csv.reader(csvfile) #Reads csv file 
            header=next(reader) 
            for row in reader: #Iterates through each row
                if row[0]==filename:
                    label=row[1]
        return label