import discord
import os
import requests
import json
from dotenv import load_dotenv

# Load .env file
load_dotenv()

client = discord.Client()

def get_chuck_norris_joke():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    json_data = json.loads(response.text)
    chuck_norris_joke = json_data['value']
    return chuck_norris_joke

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('joke'):
        await message.channel.send(get_chuck_norris_joke())

discord_token = os.environ.get('DISCORD_TOKEN')

client.run(discord_token)
