from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = 'DISCORD_BOT_TOKEN'


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
 

@bot.command()
async def Hello(ctx):
    await ctx.send('Hello World')
        

@bot.command
async def on_message(message):
    if message.author.bot:
        return
    GLOBAL_CH_NAME = "nandatoglobal"

    if message.channel.name == GLOBAL_CH_NAME:

        await message.delete()

        channels = client.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]

        embed = discord.Embed(title="nandatoglobal",
            description=message.content, color=0x00bfff)

        embed.set_author(name=message.author.display_name, 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))

        for channel in global_channels:
            await channel.send(embed=embed)
    await bot.process_commands(message)

bot.run(token)
