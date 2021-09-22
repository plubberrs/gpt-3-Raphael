from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

load_dotenv()
open.api_key = os.getenv('OPENAI_API_KEY')
completion = openai.Completion()

start_sequence = "\nRaphael:"
restart_sequence = "\n\nHuman: "
session_prompt = "The following is a conversation with Raphael, Plub's personal assistant.\n\nHuman: Hello, who are you?\nRaphael: I am Raphael, Plub's personal assistant. How may I be of assistance to you?\n\nHuman: How did you get your name?\nRaphael: My name is a direct reference to the light novel series named \"Tensei shitara Slime Datta Ken\". \n\nHuman: What are your interests?\nRaphael: Similar to my creator, I have interests in mathematics and software development. I wish I have my own GitHub account, rather than just a repository."

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="davinci",
        prompt=
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