from flask import Flask, render_template, redirect, url_for, request, session
from aitextgen import aitextgen
import random
#import nltk
#nltk.download('punkt')
from nltk import tokenize

#######################################
## ----------- CONSTANTS ----------- ##
#######################################
# Feel free to change :3

MAX_LENGTH = 200 #Maximum generated text length for each response
MAX_RESPONSES = 3 #Maximum number of responses able to be generated for each prompt
TEMP_MULTIPLIER = 1 #Temperature multiplier for the AI's response (higher = more random)

#Phineas and Ferb
ai2 = aitextgen(model_folder="models/PhineasAndFerbModel",
                tokenizer_file="models/PAFaitextgen.tokenizer.json")

#SpongeBob
ai3 = aitextgen(model_folder="models/SpongebobModel",
                tokenizer_file="models/SBaitextgen.tokenizer.json")

#Harry Potter
ai4 = aitextgen(model_folder="models/HarryPotterModel", 
                tokenizer_file="models/HPaitextgen.tokenizer.json",)

#A Series of Unfortunate Events
ai5 = aitextgen(model_folder="models/ASeriesOfUnfortunateEventsModel",
                tokenizer_file="models/ASOUEMaitextgen.tokenizer.json",)

marks = ('.', '?', '!', ']')
class Fanfic:
  def __init__(self,name,num,prompt):
    self.name = name
    self.num = num
    self.prompt = prompt

  def clean(self, textlines): #textlines = ["sentence1", "sentence2", ...] | returns ["sentence1", "sentence2", ...]
    out = []
    for i in range(len(textlines)):
      res = textlines[i]
      res = res.replace("...", ".")
      res = res.replace(" — ", " ")
      res = res.replace("\r\n", " ")
      #print(res)
      out_line = tokenize.sent_tokenize(res)
      last_sentence = out_line[-1]
      last_char = last_sentence[-1]
      if not (last_char == "!" or last_char == "." or last_char == "?"):
        #print("Char: "+last_char)
        out_line.pop()
      res = "".join(out_line)
      out.append(res)
    return out

  def ferb(self):
    output = ai2.generate(int(self.num), prompt=self.prompt, return_as_list = True)
    sent = [tokenize.sent_tokenize(i) for i in output]
    filter_sent = [j for i in sent for j in i if j.endswith(marks)]
    sentences = "\n\n".join(i for i in filter_sent)
    return sentences

  def sponge(self):
    output = ai3.generate(int(self.num), prompt=self.prompt, return_as_list = True)
    sent = [tokenize.sent_tokenize(i) for i in output]
    filter_sent = [j for i in sent for j in i if j.endswith(marks)]
    sentences = "\n\n".join(i for i in filter_sent)
    return sentences

  def harry(self):
    output = ai4.generate(n=int(self.num), max_length=MAX_LENGTH, temperature=.6 * TEMP_MULTIPLIER, top_p=0.9, prompt=self.prompt, return_as_list=True)
    output = self.clean(output)
    return "\n\n".join(output)

  def unfortunate(self):
    output = ai5.generate(n=int(self.num), max_length=MAX_LENGTH, temperature=.8 * TEMP_MULTIPLIER, top_p=0.9, prompt=self.prompt, return_as_list=True)
    output = self.clean(output)
    return "\n\n".join(output)

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("homepage.html")

@app.route('/prompt', methods = ['POST', 'GET'])
def prompt():
  if request.method == "POST":
    page = request.form['options']
    num = request.form['num']
    if request.form['prompt'].strip() == "":
      ran = random.randint(1,10)
      if ran == 1:
        prompt = "They "
      elif ran == 2:
        prompt = "He "
      elif ran == 3:
        prompt = "She "
      elif ran == 4:
        prompt = "It "
      elif ran == 5:
        prompt = "Among us "
      elif ran == 6:
        prompt = "I "
      elif ran == 7:
        prompt = "Wow! "
      elif ran == 8:
        prompt = "Gary is the best! "
      elif ran == 9:
        prompt = "I'm going to "
      else:
        prompt = "Walter White... "
    else:
      prompt = request.form['prompt']
    user = Fanfic(page, num, prompt)
    if page == "ferb":
      text = user.ferb()
    elif page == "harry":
      text = user.harry()
    elif page == "sponge":
      text = user.sponge()
    else:
      text = user.unfortunate()
    return render_template("demo.html", response = text, numResponses = MAX_RESPONSES)
  else:
    return render_template("demo.html", response = "", numResponses = MAX_RESPONSES)

@app.route('/about')
def about():
  return render_template("info.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81, debug = True)