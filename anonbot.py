import discord
import os
class MyClient(discord.Client):
    async def on_message(self, message):
        if(str(message.channel)[:14] == 'Direct Message'and message.author.bot == False):
            await client.get_channel(637654161026056215).send(message.content)
client = MyClient()
access_token = os.environ["BOT_TOKEN"]
client.run('access_token')
