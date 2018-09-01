import discord
from discord.ext import commands
import discord

class admin():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kick(self, ctx, user: discord.Member):
        if ctx.message.author.guild_permissions.kick_members or ctx.message.author.guild_permissions.administrator:
            await ctx.message.guild.kick(user)

def setup(bot):
    bot.add_cog(admin(bot))
