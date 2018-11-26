from discord.ext import commands
from discord.utils import find
import discord
import os
import logging
import asyncio
import random
import sys, traceback
client=discord.Client()

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['noti!', 'noty!', 'n!']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return 'n!'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

#hhh#


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.simple',
                      'cogs.members',
                      'cogs.owner']

bot = commands.Bot(command_prefix=get_prefix, description='help')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    await bot.change_presence(activity=discord.Game(name='Created by Drifty#6185', type=1, url='https://eloot.gg/ref=drifty'))
    print(f'Successfully logged in and booted...!')

logging.basicConfig(level='INFO')

newUserMessage = "A New user has joined!" # customise this to the message you want to send new users

@bot.command()
async def mute(ctx,):
   role = discord.utils.get(ctx.guild.roles, name="Muted")
   user = ctx.message.author
   await user.add_roles(role)
   await ctx.message.add_reaction('✅')
@bot.command()
async def unmute(ctx,):
   role = discord.utils.get(ctx.guild.roles, name="Muted")
   user = ctx.message.author
   await user.remove_roles(role)
   await ctx.message.add_reaction('✅')
        
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send('User has been banned.')
    await ctx.message.add_reaction('✅')
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send('User has been kicked.')
    await ctx.message.add_reaction('✅')             
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
       await ctx.message.add_reaction('❌')
       return
    users = [x.id for x in ctx.guild.members]
    for x in users:
        try:
            await bot.get_user(x).send(' '.join(sendit))
        except discord.Forbidden:
            count += 1
            await ctx.send('Sending message to all users...')
	    await ctx.message.add_reaction('✅')
            
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
    await ctx.message.add_reaction('✔')

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
