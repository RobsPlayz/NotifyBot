from discord.ext import commands
from discord.utils import find
import discord
import os
import logging
if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')

logging.basicConfig(level='INFO')

bot = commands.Bot(command_prefix="n!", description="help")

@bot.event
async def on_ready():
  print('Im ready! Bot by Drifty!')
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
async def n(ctx):
    guild = ctx.guild
    await guild.create_role(name="PRMS")

@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello bot by Drifty!'.format(guild.name))
        
bot.load_extension('libneko.extras.help')
bot.run(os.environ.get('TOKEN'))


