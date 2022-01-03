import discord
import json

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} is online'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('a!announce '):
        announcement = message.content.replace("a!announce ", "", 1)
        await message.channel.send("@everyone " + announcement)
        await message.delete()


token_file = open('token.json', 'r')
token = json.load(token_file)
token = token["token"]
token_file.close()
client.run(token)