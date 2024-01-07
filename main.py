import discord, os
from discord.ext import commands
from keepalive import keep_alive

#prefix
client = commands.Bot(command_prefix=".")
client.remove_command('help')

#bot launch, status
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Game(name=".help"))

#help
@client.group()
async def help(ctx):
  embed = discord.Embed(title = "Help", description = "Commands prefix is .", color = discord.Colour.green())
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"For {ctx.author.name}")
  embed.add_field(name = "Kick", value = "kick <member>, kicks a member from the server")
  embed.add_field(name = "Ban", value = "ban <member>, bans a member from the server")
  embed.add_field(name = "Clear", value = "clear <amount>, deletes the amount of messages from the channel")
  embed.add_field(name = "Profile", value = "profile <member>, displays information about the member")
  await ctx.send(embed = embed)
 
#clear messages
@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 2):
  await ctx.channel.purge(limit = amount)

#kick members
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member):
  await ctx.send(member.name + " has been kicked.") 
  await member.kick()

#ban members
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member):
  await ctx.send(member.name + " has been banned.") 
  await member.ban()

#profile
@client.command(aliases = ['pr'])
async def profile(ctx, member : discord.Member):
  embed = discord.Embed(title = member.name, color = discord.Colour.green())
  embed.set_thumbnail(url = member.avatar_url)
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"For {ctx.author.name}")
  await ctx.send(embed = embed)

keep_alive()
client.run(os.environ['TOKEN'])
