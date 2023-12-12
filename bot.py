import discord
import os
import datetime
import socket
from discord.ext import commands

token = os.getenv("DISCORD_QGMZMY_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
@commands.has_permissions(administrator=True)
async def synccommands(ctx):
    await bot.tree.sync()
    await ctx.send("同步完成")

@bot.hybrid_command()
async def ping(ctx, ip: str):
    """ping一个IP"""
    ping = os.popen(f"ping {ip} -n 1").read()
    await ctx.send(ping)
    print(ping)

@bot.hybrid_command()
async def time(ctx):
    """查看当前时间"""
    time = f"{os.popen('date /t').read()}{os.popen('time /t').read()}"
    await ctx.send(time.replace("\n", ""))
    print(time)

@bot.hybrid_command()
async def hello(ctx):
    """回复“Hello world!”可用于查看机器人是否在线"""
    await ctx.send("Hello world!")
    import __hello__

@bot.hybrid_command()
async def dns(ctx, url: str):
    """域名解析"""
    addrs = socket.getaddrinfo(url, None)
    await ctx.send(socket.getaddrinfo(url, None)[0][4][0])
    print(socket.getaddrinfo(url, None)[0][4][0])

bot.run(token)