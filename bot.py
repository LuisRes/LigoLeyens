import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")


if TOKEN is None:
    raise ValueError("No DISCORD_TOKEN found in environment variables.")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as {0}'.format(self.user))
    
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)