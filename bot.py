from discord.ext import commands
import discord



bot = commands.Bot(command_prefix="n!", description="help")
@bot.event
async def on_ready():
  print('Im ready!')
@bot.command()
async def send(ctx, *sendit):
    count = 0
    if not "PRMS" in [x.name for x in ctx.author.roles]:
       await ctx.send('This command is not for you')
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
bot.run('TOKEN')




