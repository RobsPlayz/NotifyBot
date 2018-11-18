from discord.ext import commands
from discord.utils import find
import discord
import os
import logging

logging.basicConfig(level='INFO')

bot = commands.Bot(command_prefix="n!", description="help")

@bot.command()
async def credits(ctx,):
    await ctx.send('By Drifty')
@bot.command()
async def invite(ctx,):
    await ctx.send('https://discordapp.com/oauth2/authorize?&client_id=513156006973538313&scope=bot&permissions=268436512')
@bot.command()
async def send(ctx, *sendit):
    count = 0
    if not "PRMS" in [x.name for x in ctx.author.roles]:
       await ctx.send('This command is not for you. Bot by Drifty')
       return
    users = [x.id for x in ctx.guild.members]
    for x in users:
        try:
            await bot.get_user(x).send(' '.join(sendit))
        except discord.Forbidden:
            count += 1
    await ctx.send(f'Sent this message for {ctx.guild.members-count} / {ctx.guild.members} users')
@bot.command()
async def setup(ctx):
    guild = ctx.guild
    await guild.create_role(name="PRMS")
 
    
@bot.event
await bot.send_message(message.channel, '{} has joined.'.format(user.name))
@bot.event
async def on_ready():
  print('Im ready! Bot by Drifty!')
@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello bot by Drifty!'.format(guild.name))
        
       

bot.load_extension('libneko.extras.help')
bot.run(os.environ.get('TOKEN'))


