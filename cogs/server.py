import discord
from discord.ext import commands

class Server(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(manage_messages = True)
  async def clear(self, ctx, amount = 2):
    await ctx.channel.purge(limit = amount)

  def check_me(ctx):
    return ctx.author.id == 492746058166697986

  @commands.command()
  @commands.check(check_me)
  async def kick(self, ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'Kicked {member.mention}')

  @commands.command()
  @commands.check(check_me)
  async def ban(self, ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'Banned {member.mention}')

  @commands.command()
  @commands.check(check_me)
  async def unban(self, ctx, *, member):
    banned_users = ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user
      if (user.name, user.discriminator) == (member.name, member.discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.mention}')
        return

def setup(client):
  client.add_cog(Server(client))