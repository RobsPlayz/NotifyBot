from discord.ext import commands
from discord.utils import find
import discord
import os
import logging
import asyncio
import random

client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


logging.basicConfig(level='INFO')

newUserMessage = "A New user has joined!" # customise this to the message you want to send new users


bot = commands.Bot(command_prefix="n!", description="help")

@bot.command()
async def mute(ctx,):
   role = discord.utils.get(ctx.guild.roles, name="Muted")
   user = ctx.message.author
   await user.add_roles(role)
@bot.command()
async def unmute(ctx,):
   role = discord.utils.get(ctx.guild.roles, name="Muted")
   user = ctx.message.author
   await user.remove_roles(role)
        
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send('User has been banned.')
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send('User has been kicked.')
                
@bot.command()
async def credits(ctx,):
    await ctx.send('Created by Drifty#6185 Helped by Bugless#1005 (Owner of Fortnite Drop)')
@bot.command()
async def invite(ctx,):
    await ctx.send('https://discordapp.com/oauth2/authorize?&client_id=513156006973538313&scope=bot&permissions=268575766')
@bot.command()
async def send(ctx, *sendit):
    count = 0
    if not "PRMS" in [x.name for x in ctx.author.roles]:
       await ctx.send('This command is not for you. If you are the owner, Do n!setup and give you the role PRMS.')
       return
    users = [x.id for x in ctx.guild.members]
    for x in users:
        try:
            await bot.get_user(x).send(' '.join(sendit))
        except discord.Forbidden:
            count += 1
            await ctx.send('Sent the message to all users.')
            
@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    await client.send_message(member, newUserMessage)
    print("Sent message to " + member.name)
@bot.command()
async def setup(ctx):
    guild = ctx.guild
    await guild.create_role(name="PRMS")
    await guild.create_role(name="Muted")
    await ctx.send('Setup!')

async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  ctx.guild.text_channels)
    if general and general.permissions_for(ctx.guild.me).send_messages:
        await general.send('Thanks for adding me! Upvote here: https://discordbots.org/bot/513156006973538313 Support here:'.format(guild.name))
        await guild.create_role(name="Muted")
        await guild.create_role(name="PRMS")
        await ctx.send('Auto-Setup!')
				
bot.load_extension('libneko.extras.help')
bot.run(os.environ.get('TOKEN'))

##Code thats unused
##role = discord.utils.get(ctx.guild.roles, name="role to add name")
##user = ctx.message.author
##await user.add_roles(role)
