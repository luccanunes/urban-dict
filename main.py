import discord
import asyncio
from os import getenv
from api import get_term
from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv('TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('now online - hello, meza')
    print(client.user.name)
    print(client.user.id)
    print('-'*20)
    activity = discord.Game('esperando meu ifood')
    await client.change_presence(status=discord.Status.online, activity=activity)


@client.event
async def on_message(message):
    global prefix
    prefix = '.'
    if client.user.mentioned_in(message) and len(message.mentions) == 1:
        msg = discord.Embed(
            title='Help', description=f"Feeling lost? Type {prefix}help", colour=discord.Color.from_rgb(19, 79, 230))
        await message.channel.send(embed=msg)
        return
    msg = message.content.strip().lower()
    if msg == f'{prefix}help':
        emb = discord.Embed(
            title='Commands', 
            description="Here's a list of all commands!",
            colour=discord.Color.from_rgb(19, 79, 230)
        )
        emb.set_thumbnail(url='https://i.imgur.com/QmU4ryP.png')
        emb.add_field(name=f'{prefix}ud <term>', value='searchs for that term in the urban dictionary.')
        await message.channel.send(embed=emb)
    if msg.startswith(f'{prefix}ud'):
        term = msg.split(' ')[1:]
        meaning = get_term(term)
        if type(meaning) == str:
            emb = discord.Embed(
                title=' '.join(term).title(), 
                description=meaning,
                colour=discord.Color.from_rgb(19, 79, 230)
            )
            await message.channel.send(embed=emb)
        else:
            emb = discord.Embed(
                title='Error', 
                description=meaning.get('Error'),
                colour=discord.Color.from_rgb(255, 0, 0)
            )
            await message.channel.send(embed=emb)



client.run(TOKEN)
