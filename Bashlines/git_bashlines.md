                                    GIT BASH LINES

                            BASH LINES FOR UPDATING REPO
                    
git add  BiLSTM_Model BiLSTM_Preprocess BERT_Model Checkpoints BERT_Preprocess Scraper frontend .gitignore Documentation Datasets LSTM_Inference Journal.md requirements.txt config_loader.py config.yaml Bashlines Tailwind_classes.md README.md LICENSE.md
git commit -m
git pull origin main --rebase 
git push origin main

git stash 
        (if pull dosent work)

git add -A 
        (if folders were changed)

                    BASH LINES FOR INITIALIZING GIT REPO


git remote add origin https://github.com/#username/#reponame.git
git push -u origin main

                    MISCELLANEOUS BASH LINES

git gc --prune=now 
                        (Deletes temp git files and activates garbage collector)

git branch 
                        (Displays branch)

git branch -d branch name 
                        (Deletes a branch)

git branch -m master main 
                        (Renames branch  (Master --> Main))

git rm -r --cached venv/   
                        (Manually remove certain files from commit)

rm -rf node_modules 
                        (Delete modules)






