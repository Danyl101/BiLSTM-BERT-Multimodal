from .Clean_run import run_clean
from .bert_label import run_label
from .bert_label_balancing import run_balance

def preprocess_run():
    run_clean()
    run_label()
    run_balance()
    
if __name__=="__main__":
    preprocess_run()