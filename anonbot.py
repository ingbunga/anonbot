import discord
import os
defalut_cannel_id = int(os.environ["default_cannel_id"])
class MyClient(discord.Client):
    async def on_message(self, message):
        if(str(message.channel)[:14] == 'Direct Message'and message.author.bot == False):
            await client.get_channel(defalut_cannel_id).send(message.content)
client = MyClient()
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
