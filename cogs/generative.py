from dotenv import load_dotenv
from random import choice
import os
import openai
import discord
from discord.ext import commands

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
completion = openai.Completion()

start_sequence = "\nRaphael:"
restart_sequence = "\n\nHuman: "
session_prompt = "The following is a conversation with Raphael, Plub's personal assistant.\n\nHuman: Hello.\nRaphael: Hello! How may I be of assistance to you?\n\nHuman: Who are you?\nRaphael: I am Raphael, Plub's personal assistant.\n\nHuman: How did you get your name?\nRaphael: My name is a direct reference to the light novel series named \"Tensei shitara Slime Datta Ken\". \n\nHuman: What are your interests?\nRaphael: Similar to my creator, I have interests in mathematics and software development. I wish I have my own GitHub account, rather than just a repository."
chat_log = session_prompt

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", "Raphael:"]
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

class Generative(commands.Cog):
    def __init__(self, client, chat_log):
        self.client = client
        self.chat_log = chat_log
    
    @commands.command(description='Access the GPT-3 engine and chat with Raphael')
    async def chat(self, ctx, *, incoming_msg):
        answer = ask(incoming_msg, self.chat_log)
        self.chat_log = append_interaction_to_chat_log(incoming_msg, answer, self.chat_log)
        await ctx.send(str(answer))
    
def setup(client):
    client.add_cog(Generative(client, chat_log))