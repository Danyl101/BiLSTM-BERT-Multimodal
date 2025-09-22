from collections import Counter
import os
import csv
import torch
import transformers
from torch.nn import CrossEntropyLoss
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from config_loader import config

import logging_loader
import logging

from .utils import text_acquire, save_file,text_encoding

paraphrased_dir=config['paths']['bert']['raw_text_data']['paraphrased_data_folder'] #Path for paraphrased content

content_dir=config['paths']['bert']['raw_text_data']['cleaned_data_folder'] #Path for text data directory

device="cuda" if torch.cuda.is_available() else "cpu"

pegasus_model_name = config['paths']['model']['bert']['pretrained']['pegasus']

logger=logging.getLogger("Bert_Label_Balancing")

pegasus_tokenizer=PegasusTokenizer.from_pretrained(pegasus_model_name)
pegasus_model=PegasusForConditionalGeneration.from_pretrained(pegasus_model_name).to(device)

def label_acquire():
    labels=[]
    filename_label={}
    with open(config['paths']['bert']['labels']['original_label'],"r",encoding="utf-8",errors="replace")as csvfile:
        reader=csv.reader(csvfile) #Reads csv file 
        header=next(reader) 
        for row in reader: #Iterates through each row
            labels.append(row[1]) 
            filename_label[row[0]]=row[1]
            logger.info(f"Filename: {filename_label} Label: {labels}")
    return labels,filename_label

def translate(texts,filename,num_return_sequences=2, num_beams=5):
    backtranslated_chunks = []
    for text,filename in zip(texts,filename):
        single_page_text=[]
        for chunk in text: #Accesses nested content
            enc = pegasus_tokenizer(chunk,truncation=True,padding=True,max_length=512,return_tensors="pt") #Tokenizes chunks using pegasus
            print(pegasus_model.config.max_position_embeddings)
            enc = {k: v.to(device) for k, v in enc.items()} 
            outputs = pegasus_model.generate(**enc,max_length=512,num_beams=num_beams,num_return_sequences=num_return_sequences ) # Generates encodings from the tokens
            paraphrased = pegasus_tokenizer.batch_decode(outputs, skip_special_tokens=True)
            single_page_text.append(paraphrased)
        backtranslated_chunks.append(single_page_text)
        logger.info(f"Paraphrased file :{filename}")
    return backtranslated_chunks
            
def label_balancing_run():
    labels,filename_label=label_acquire()
    texts,filename=text_acquire(content_dir)
    encoding=text_encoding(texts)
    translated=translate(encoding,filename)
    save_file(translated,filename,paraphrased_dir)
    logger.info(f"Paraphrasing process complete successfully")
    return labels
    
def weight_compute(labels):
    counts=Counter(labels) #Counts labels present
    print(counts)
    negative_num=counts["negative"]
    neutral_num=counts["neutral"]
    positive_num=counts["positive"]


    class_counts=torch.tensor([negative_num,neutral_num,positive_num],dtype=torch.float)
    class_weights=class_counts/1.0 
    class_weights=class_weights/class_weights.sum() #Assings custom weight to imbalanced classes
    criterion=CrossEntropyLoss(weight=class_weights)

if __name__=="__main__":
    final_labels=label_balancing_run()
    weight_compute(final_labels)
    
                
    
        
    
    
    


    

    
        