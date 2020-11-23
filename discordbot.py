from discord.ext import commands
import os
import traceback
import discord
import random
import datetime
import time

# intents = discord.Intents().all()
PREFIX='po.'
# bot = commands.Bot(command_prefix=PREFIX, intents=intents)
bot = commands.Bot(command_prefix=PREFIX)
token = 'DISCORD_BOT_TOKEN'


@bot.event
async def on_ready():
    print("やってるよー")
    bot.global_list = []  # グローバルチャット参加チャンネルのリスト
    for guild in bot.guilds:
        tmp = discord.utils.get(guild.text_channels, name="nandatoglobal")
        if tmp:
            bot.global_list.append(tmp)
            print(tmp)
    await bot.change_presence(activity=discord.Game(name=f"Ver.0.0.1 Under Construction")) # プレイちゅう
    for channel in bot.get_all_channels():
        if channel.name == '起動時メッセージ':
            await channel.send(embed=discord.Embed(title=f"起動しました！！！（ここをくりっくすると...）", description=f"おはよう、だな。\n頑張ろうか、君。", url="https://www.porubu.com/"))


# @bot.event
# async def on_command_error(ctx, error):
#     orig_error = getattr(error, "original", error)
#     error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#     await ctx.send(error_msg)


@bot.command()
async def end(ctx):
    if ctx.message.author.id == 655361522465243147:  # このidのとこは自身のIDに変更してね
        color = random.randint(0x000000, 0xffffff)
        await ctx.send(embed=discord.Embed(title="シャットダウン", description=f"ぼっとのしすてむをくろーずします", color=color))
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
        

@bot.command()
async def sglobal(ctx):
    if discord.utils.get(ctx.guild.text_channels, name="nandatoglobal"):
        await ctx.channel.send("既に参加しているようだ。")
        return
    category_id = ctx.channel.category_id
    category = ctx.guild.get_channel(category_id)
    ch = await category.create_text_channel("nandatoglobal")
    bot.global_list.append(ch)
    await ctx.send("グローバルチャットのチャンネルに登録した。")


@bot.command()
async def dglobal(ctx):
    if discord.utils.get(ctx.guild.text_channels, name="nandatoglobal"):
        tyaneru = discord.utils.get(ctx.guild.text_channels, name="nandatoglobal")
        await tyaneru.delete()
        await ctx.channel.send("グローバルチャットのチャンネルを削除した。また使ってくれよ？")
        bot.global_list = []
        for guild in bot.guilds:
            tmp = discord.utils.get(guild.text_channels, name="nandatoglobal")
            if tmp:
                bot.global_list.append(tmp)


@bot.command
async def on_message(message):
    # if message.author == bot.user:
    #     return
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
    if message.author.bot and not(message.channel.id == 707158257818664991 and message.author != bot.user):
        return
    em = discord.Embed(description=message.clean_content)
    if message.author.avatar_url:
        em.set_thumbnail(url=message.author.avatar_url)
        em.set_author(name=f"{message.author}:{message.author.id}",icon_url=message.author.avatar_url_as(static_format="png"),)
    else:
        em.set_thumbnail(url="https://i.gyazo.com/3eaebd54e3f3febca711275a3d587757.png")
        em.set_author(name=f"{message.author}:{message.author.id}", icon_url="https://i.gyazo.com/3eaebd54e3f3febca711275a3d587757.png",)
    
    if message.attachments and message.attachments[0].proxy_url:
        em.set_image(url=message.attachments[0].proxy_url)
    
    em.set_footer(text=f"サーバー: {message.guild.name}({message.guild.id})",icon_url=message.guild.icon_url)
    # em.set_author(name=f"{message.author}:{message.author.id}",icon_url=message.author.avatar_url,)
    # gurobanissuu = 30

    if message.channel in bot.global_list:
        print("haihai")
        for ch in bot.global_list:
            print("haihai2")
            if message.guild != ch.guild:
                print("haihai3")
                # print(ch.guild)
                ruizi = os.path.join(os.path.dirname(__file__), 'ngserver.txt')
                with open(ruizi, 'r', encoding='utf-8') as f:
                    nagnanokana = [ngs.strip().lower() for ngs in f.readlines()]
                    mariogaarunoda = str(message.guild.id)
                    if mariogaarunoda in nagnanokana:
                        # print("をい")
                        await message.add_reaction("🆖")
                        return
                ruizini = os.path.join(os.path.dirname(__file__), 'ng.txt')
                # with open(ruizini, 'r', encoding='utf-8') as file:
                with open(ruizini, 'r', encoding='utf-8') as f2:
                    ngng = [ugugugu.strip().lower() for ugugugu in f2.readlines()]
                    akutaaaaa = str(message.author.id)
                    if akutaaaaa in ngng:
                        await message.add_reaction("🆖")
                        return
                ruizisan = os.path.join(os.path.dirname(__file__), 'ngwords.txt')
                with open(ruizisan, 'r', encoding='utf-8') as file:
                    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]
                    if any(bad_word in message.content for bad_word in bad_words):
                        await message.add_reaction("🆖")
                        return
                # day_count = (datetime.datetime.utcnow() - message.guild.created_at) // datetime.timedelta(days=1)
                # print(day_count)
                # if day_count > 60:
                # nissuu = (datetime.datetime.utcnow() - message.author.created_at) // datetime.timedelta(days=1)
                    # print(nissuu)
                # if nissuu > gurobanissuu:
                await ch.send(embed=em)
                await message.add_reaction("✅")
                    # if message.attachments and message.attachments[0].proxy_url:
                        # await ch.send(f"サーバー: {message.guild.name}({message.guild.id})\n{message.author}:{message.author.id}\n**{message.clean_content}**\n{message.attachments[0].proxy_url}")
                    # else:
                        # await ch.send(f"サーバー: {message.guild.name}({message.guild.id})\n{message.author}:{message.author.id}\n**{message.clean_content}**")
                # else:
                    # pass
    await bot.process_commands(message)

bot.run(token)
