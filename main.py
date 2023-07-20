import os
import discord
from discord.ext import commands

from utils import get_account_by_name, get_current_ranked_info

from dotenv import load_dotenv
load_dotenv('.env')

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def account(ctx, name, tag):
    user_info = get_account_by_name(name, tag)
    user_image = user_info['data']['card']['small']
    account_level = user_info['data']['account_level']
    account_region = user_info['data']['region'].upper()
    last_update = user_info['data']['last_update']

    embed = discord.Embed(title=f"{name}#{tag}", description='Account Information', color=0xc0f5fe)
    embed.set_thumbnail(url=user_image)
    embed.add_field(name='Account Level', value=account_level, inline=True)
    embed.add_field(name='Region', value=account_region, inline=True)
    embed.add_field(name='Last Update', value=last_update, inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def rank(ctx, name, tag):
    user_rank_info = get_current_ranked_info(name, tag)

    await ctx.send(user_rank_info['data']['current_data']['currenttierpatched'])


if __name__ == "__main__":
    bot.run(TOKEN)
