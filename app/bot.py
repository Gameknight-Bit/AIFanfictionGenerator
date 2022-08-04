#Bot for Prometheus :)#
from sunau import AUDIO_FILE_ENCODING_LINEAR_24
from aitextgen import aitextgen
from discord.ext import commands
import discord
import random
#import nltk
#nltk.download('punkt')
from nltk import tokenize

#######################################
## ----------- CONSTANTS ----------- ##
#######################################
# Feel free to change :3

MAX_LENGTH = 200 #Maximum generated text length for each response
TEMP_MULTIPLIER = 1 #Temperature multiplier for the AI's response (higher = more random)

PREFIX = '~' #Prefix for the bot    

token = '' #Change to the bot's api token
#######################################

bot = commands.Bot(command_prefix=PREFIX)

#Loading Models
ai1 = aitextgen(model_folder="models/PhineasAndFerbModel", tokenizer_file="models/PAFaitextgen.tokenizer.json", to_gpu=False)
ai2 = aitextgen(model_folder="models/SpongebobModel", tokenizer_file="models/SBaitextgen.tokenizer.json", to_gpu=False)
ai3 = aitextgen(model_folder="models/HarryPotterModel", tokenizer_file="models/HPaitextgen.tokenizer.json", to_gpu=False)
ai4 = aitextgen(model_folder="models/ASeriesOfUnfortunateEventsModel", tokenizer_file="models/ASOUEMaitextgen.tokenizer.json", to_gpu=False)

###########################
## AI TEXT GEN MODELS!!! ##
###########################
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
    output = ai1.generate(int(self.num), prompt=self.prompt, temperature=.8 * TEMP_MULTIPLIER, return_as_list = True)
    sent = [tokenize.sent_tokenize(i) for i in output]
    filter_sent = [j for i in sent for j in i if j.endswith(marks)]
    sentences = "\n\n".join(i for i in filter_sent)
    return sentences

  def sponge(self):
    output = ai2.generate(int(self.num), prompt=self.prompt, temperature=.6 * TEMP_MULTIPLIER, return_as_list = True)
    sent = [tokenize.sent_tokenize(i) for i in output]
    filter_sent = [j for i in sent for j in i if j.endswith(marks)]
    sentences = "\n\n".join(i for i in filter_sent)
    return sentences

  def harry(self):
    output = ai3.generate(n=int(self.num), max_length=MAX_LENGTH, temperature=.6 * TEMP_MULTIPLIER, top_p=0.9, prompt=self.prompt, return_as_list=True)
    output = self.clean(output)
    return "\n\n".join(output)

  def unfortunate(self):
    output = ai4.generate(n=int(self.num), max_length=MAX_LENGTH, temperature=.8 * TEMP_MULTIPLIER, top_p=0.9, prompt=self.prompt, return_as_list=True)
    output = self.clean(output)
    return "\n\n".join(output)
###########################



@bot.command()
async def generate(ctx, *, text):
  message = await ctx.send('Thinking...')
  if " ".join(text.split(" ")[1:]).strip() == "":
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
    prompt = " ".join(text.split(" ")[1:])

    # Output
  user = Fanfic("user", 1, prompt)
  if str.lower(text.split(" ")[0]) == "phineasandferb":
    output = user.ferb()
  elif str.lower(text.split(" ")[0]) == "spongebob":
    output = user.sponge()
  elif str.lower(text.split(" ")[0]) == "harrypotter":
    output = user.harry()
  elif str.lower(text.split(" ")[0]) == "aseriesofunfortunateevents":
    output = user.unfortunate()
  else:
    user.prompt = text
    prompt = text
    output = user.ferb()

  # Embed
  embed=discord.Embed(title="Generated Response", color=0x1fbd67)
  embed.add_field(name="Prompt", value=str(prompt), inline=False)
  embed.add_field(name="Response", value=output, inline=False)
  #embed.set_thumbnail(url="https://static.wixstatic.com/media/12b467_a4ceef0f338c41c7885cb083ea36a00f~mv2_d_1742_1743_s_2.png/v1/fill/w_85,h_85,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/ai%20camp%20logo.png%22)
  await message.edit(embed=embed, content="")

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.command()
async def cmds(ctx):
  embed = discord.Embed(title="Commands", color=0x1fbd67)
  embed.add_field(name="~generate <type> <prompt>", value="""Generates response to prompt by using a specified model. \n-type: "PhineasAndFerb", "Spongebob", "HarryPotter", "ASeriesOfUnfortunateEvents" | What generation type you want to use.""", inline=False)
  embed.add_field(name="~cmds", value="Shows all commands.", inline=False)
  await ctx.send(embed=embed, content="")

bot.run(token)
