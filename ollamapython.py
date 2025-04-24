# To start, install Ollama. Next, create a bot with all possible intents.
# Grab the token and put it in the bottoken variable.
# On the Oauth page, only check the bot tab.
# Next invite it to your server with admin permissions.

# Module Imports
from ollama import chat
from ollama import ChatResponse
import discord
from discord.ext import commands
import asyncio

# Variable Setups
# Set bottoken to your bot's token.
bottoken = "Add your bot token."
intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix='!', intents=intents)
userdefmodel = "zephyr:7b"

# Bot Login
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Def the !ask Command      
@bot.command()
async def ask(ctx: commands.Context):
    print(ctx.message.author + ctx.message.clean_content[5:])
    prompt = str (ctx.message.clean_content[5:])
    print(prompt)
    response: ChatResponse = chat(model=userdefmodel, messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])
    print(response.message.content)
    data = {
        "content": (response.message.content),
        "username": userdefmodelmodel,
    }
    await ctx.send(response.message.content)

# Run the bot using the previously defined Botkey. MAKE SURE YOURE BOT HAS ALL INTENTIONS BUT ON OAUTH PAGE ONLY BOT CHECKBOX.
bot.run (str (bottoken))
