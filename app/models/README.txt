### How to Install Models ###

1. Install all models with the same file configuration in the google drive 
  - Google Drive: (https://drive.google.com/drive/folders/1Qo4aksWxM6soiOZU7ctyfKHNT9_F_pij?usp=sharing)
2. Make sure all paths are correct and all tokenizer files are in the models folder
3. Run the main.py file or bot.py!!!

Debug Tips:
If the code is erroring with messages about file paths
Make sure the models folder is set up like:

*Models/
  -ASeriesOfUnfortunateEventsModel/
    -config.json
    -pytorch_model.bin
  -HarryPotterModel/
    -config.json
    -pytorch_model.bin
  -PhineasAndFerbModelModel/
    -config.json
    -pytorch_model.bin
  -SpongebobModel/
    -config.json
    -pytorch_model.bin
  -ASOUEMaitextgen.tokenizer.json
  -HPaitextgen.tokenizer.json
  -PAFaitextgen.tokenizer.json
  -SBaitextgen.tokenizer.json
  
#######################################
If paths are alright make sure to check that config.json files have .json at the end and pytorch_model.bin has the .bin extension!

Thanks! 
