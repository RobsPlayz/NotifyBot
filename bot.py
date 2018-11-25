from discord.ext import commands
from discord.utils import find
import discord
import os
import logging
import asyncio
import random
import sys, traceback

client=discord.Client()
##START OF MAYBECRASH

class MembersCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member: discord.Member):
        """Says when a member joined."""
        await ctx.send(f'{member.display_name} joined on {member.joined_at}')

    @commands.command(name='coolbot')
    async def cool_bot(self, ctx):
        """Is the bot cool?"""
        await ctx.send('This bot is cool. :)')

    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member=None):
        """Simple command which shows the members Top Role."""

        if member is None:
            member = ctx.author

        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')
    
    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member: discord.Member=None):
        """A simple command which checks a members Guild Permissions.
        If member is not provided, the author will be checked."""

        if not member:
            member = ctx.author

        # Here we check if the value of each permission is True.
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        # And to make it look nice, we wrap it in an Embed.
        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        # \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
        embed.add_field(name='\uFEFF', value=perms)

        await ctx.send(content=None, embed=embed)
        # Thanks to Gio for the Command.

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(MembersCog(bot)) 

##END OF MAYBECRASH

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['noti!', 'notify! ', 'n!']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return 'n!'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.simple',
                      'cogs.members',
                      'cogs.owner']

bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')

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
