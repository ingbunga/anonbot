import discord
import os
defalut_channel_id = int(os.environ["default_channel_id"])
music_channel_id = int(os.environ["music_channel_id"])
class MyClient(discord.Client):
    async def on_message(self, message):
        if(str(message.channel)[:14] == 'Direct Message'and message.author.bot == False):
            cmd = message.content.split(' ')[1]
            if cmd == '음악채널':
                await client.get_channel(music_channel_id).send(message.content[5:])
            else:
                await client.get_channel(defalut_channel_id).send(message.content)
client = MyClient()
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
