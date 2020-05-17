import discord
class MyClient(discord.Client):
    async def on_message(self, message):
        if(str(message.channel)[:14] == 'Direct Message'and message.author.bot == False):
            await client.get_channel(637654161026056215).send(message.content)
client = MyClient()
client.run('NTExMDMxNjUwNzA1MDgwMzIw.XsD5fg.sLSpkh6FfxuI_o_zC7y8zKTiYeI')