from discord.ext import commands
import discord
import os
import logging
logging.basicConfig(level='INFO')

bot = commands.Bot(command_prefix="n!", description="help")
@bot.event
async def on_ready():
  print('Im ready! Bot by Drifty!')
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
@bot.listen()
async def on_server_join(ctx)
    await ctx.send("Hello i am Noti a bot made by Drifty. Please do n!help for any help!")
  
  
bot.run(os.environ.get('TOKEN'))


