import discord
from discord.ext import commands

aboutRaphael = "Hello. I am a generative chatbot created by Plub as part of his Machine Learning exploratory project. My name is Raphael, which is a direct reference to a character from 'Tensei shitara Slime Datta Ken' Japanese Light Novel series."
aboutTransformer = "My text generation engine follows a model for neural networks, named the Transformer model. Using any datasets I have as a base, each and every character is statistically predicted to respond best to your messages. Currently I have been trained to talk similar to Hollywood movie dialogues, according to the Cornell movie-dialogs corpus dataset."

class Info(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def about(self, ctx):
    await ctx.send(aboutRaphael)
  
  @commands.command()
  async def engine(self, ctx):
    await ctx.send(aboutTransformer)

def setup(client):
  client.add_cog(Info(client))