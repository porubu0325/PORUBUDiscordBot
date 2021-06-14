# -*- coding: utf-8 -*-
from discord.ext import commands
import os
# import traceback
import discord
import random
import datetime
import time

#intents = discord.Intents().all()
PREFIX='pg!'
bot = commands.Bot(command_prefix=PREFIX)
token = 'DISCORD_BOT_TOKEN'


# @bot.event
# async def on_command_error(ctx, error):
#     orig_error = getattr(error, "original", error)
#     error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#     await ctx.send(error_msg)


@bot.command()
async def end(ctx):
    if ctx.message.author.id == 655361522465243147:  # このidのとこは自身のIDに変更してね
        color = random.randint(0x000000, 0xffffff)
        await ctx.send(embed=discord.Embed(title="おしまい。", description=f"終了中...", color=color))
        await ctx.message.delete()
        await bot.close()
    else:
        color = random.randint(0x000000, 0xffffff)
        await ctx.send(embed=discord.Embed(title="違う！", description="お前……。", color=color))
        await ctx.message.delete()


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
 

@bot.command()
async def Hello(ctx):
    await ctx.send('Hello World')
        


@bot.event #メインチャンネル
async def on_message(message):
    print("It's me, MAAAARIIIIO!!!!!!!!!!!!!!")
    if message.author == bot.user:
        return
    # GLOBAL_CH_NAME = "nandatoglobal"

    # if message.channel.name == GLOBAL_CH_NAME:

    #     await message.delete()

    #     channels = bot.get_all_channels()
    #     global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]

    #     embed = discord.Embed(title="nandatoglobal",
    #         description=message.content, color=0x00bfff)

    #     embed.set_author(name=message.author.display_name, 
    #         icon_url=message.author.avatar_url_as(format="png"))
    #     embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
    #         icon_url=message.guild.icon_url_as(format="png"))

    #     for channel in global_channels:
    #         await channel.send(embed=embed)
    # if message.author.bot and not(message.channel.id == 707158257818664991 and message.author != bot.user):
    #     return
    if message.content == f"{PREFIX}global":
        if discord.utils.get(message.guild.text_channels, name="nandatoglobal"):
            await message.channel.send("もう参加しています。")
            return
        category_id = message.channel.category_id
        category = message.guild.get_channel(category_id)
        ch = await category.create_text_channel("nandatoglobal")
        bot.global_list.append(ch)
        await message.channel.send("グローバルチャットのチャンネルを作成しました。")
        return

    if message.content == f"{PREFIX}dglobal":
        if discord.utils.get(message.guild.text_channels, name="nandatoglobal"):
            tyaneru = discord.utils.get(message.guild.text_channels, name="nandatoglobal")
            await tyaneru.delete()
            await message.channel.send("グローバルチャットのチャンネルを削除しました。")
            bot.global_list = []
            for guild in bot.guilds:
                tmp = discord.utils.get(guild.text_channels, name="nandatoglobal")
                if tmp:
                    bot.global_list.append(tmp)
            return

    GLOBAL_CH_NAME = "nandatoglobal" # グローバルチャットのチャンネル名

    if message.channel.name == GLOBAL_CH_NAME:
        # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する

        await message.delete() # 元のメッセージは削除しておく

        channels = bot.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        # channelsはbotの取得できるチャンネルのイテレーター
        # global_channelsは hoge-global の名前を持つチャンネルのリスト

        embed = discord.Embed(title="nandatoglobal",
            description=message.clean_content, color=0x00bfff)

        embed.set_author(name=f"{message.author.display_name}:{message.author.id}", 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))
        # Embedインスタンスを生成、投稿者、投稿場所などの設定
        
        if message.attachments and message.attachments[0].proxy_url:
            embed.set_image(url=message.attachments[0].proxy_url)

        for channel in global_channels:
            # メッセージを埋め込み形式で転送
            await channel.send(embed=embed)
    await bot.process_commands(message)


@bot.event
async def on_ready():
    print("やってるよー")
    bot.global_list = []  # グローバルチャット参加チャンネルのリスト
    for guild in bot.guilds:
        tmp = discord.utils.get(guild.text_channels, name="nandatoglobal")
        if tmp:
            bot.global_list.append(tmp)
            print(tmp)
    await bot.change_presence(activity=discord.Game(name=f"プレイ中：ここ"))
    for channel in bot.get_all_channels():
        if channel.name == 'ver.0.0.1 Under Construction':
            await channel.send(embed=discord.Embed(title=f"起動！！！（ここをクリックするとPORUBU.comに行きます）)", description=f"なんだとぼっと\n起動しました。", url="https://www.porubu.com/"))

if __name__ == '__main__':
	bot.run(token)
