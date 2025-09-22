from torch.utils.data import Dataset,DataLoader
import os
from transformers import BertTokenizer, BertModel
import torch
import csv
from torch import nn
from config_loader import config

from .utils import text_acquire, text_chunking ,label_acquire

train_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..',config['paths']['bert']['model_data']['train_data_folder'])

val_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..',config['paths']['bert']['model_data']['val_data_folder'])

test_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..',config['paths']['bert']['model_data']['test_data_folder'])

tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')

class BERTDataset():
    def __init__(self,folder_path,tokenizer):
        self.folder_path=folder_path
        self.filepath=[os.path.join(folder_path,f) for f in os.listdir(folder_path) if f.endswith('txt')]
        self.tokenizer=tokenizer
        pass
    
    def __len__(self):
        return len(self.filepath)

    def __getitem__(self,idx):
        filepath=self.filepath[idx]
        with open(filepath ,"r")as f:
            text=f.read()
            filename=os.path.basename(filepath)
            
            snippets=text_chunking(text)
            for snippet in snippets:
                encodings=self.tokenizer(snippet,padding="max_length",truncation=True,max_length=450,return_tensors="pt")
            input_ids = torch.cat([e["input_ids"] for e in encodings], dim=0)
            attention_mask = torch.cat([e["attention_mask"] for e in encodings], dim=0)
            
            label=label_acquire(filename)

            return {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "filename": filename,
                "label": label
            }
            
train_dataset=BERTDataset(train_folder,tokenizer)
val_dataset=BERTDataset(val_folder,tokenizer)
test_dataset=BERTDataset(test_folder,tokenizer)

train_loader=DataLoader(train_dataset,batch_size=1,shuffle=True)
val_loader=DataLoader(val_dataset,batch_size=1,shuffle=False)
test_loader=DataLoader(test_dataset,batch_size=1,shuffle=False)
    
    
    
    

