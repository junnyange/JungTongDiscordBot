#https://discord.com/api/oauth2/authorize?client_id=1035968056171696168&permissions=8&scope=bot

import asyncio,discord
from audioop import lin2adpcm
from pydoc import describe
from turtle import title
from discord.ext import commands
import numpy as np


import Dice
import User

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot Is Online")

@bot.command()
async def signUp(ctx):
    if User.checkName(ctx.author.name, ctx.author.id):
        User.signUp(ctx.author.name, ctx.author.id)
        await ctx.send("signUp Complete")
    else:
        await ctx.send("already signUp")

@bot.command()
async def 내정보(ctx):
    name,money,level = User.userInfo(ctx.author.name, ctx.author.id)
    if name == None:
        await ctx.send("사용자가 없습니다.")
    else:
        embed = discord.Embed(title="유저 정보", description = name, color = 0x62D0F6)
        embed.add_field(name="레벨", value = level)
        embed.add_field(name="보유 자산", value = money)
        await ctx.send(embed=embed)
@bot.command()
async def 주사위(ctx):
    result, _color, user, bot = Dice.dice()
    embed = discord.Embed(title = "주사위 게임 결과", description = None, color = _color)
    embed.add_field(name = "정통봇 의 숫자", value = ":game_die: " + bot, inline = True)
    embed.add_field(name = ctx.author.name+"의 숫자", value = ":game_die: " + user, inline = True)
    embed.set_footer(text="결과: " + result)
    await ctx.send(embed=embed)

@bot.command()
async def 명령어(ctx):
    embed =discord.Embed(title = "명령어",description = None,color = None)
    embed.add_field(name="!안녕",value = "봇이 인사를 합니다.",inline = False)
    embed.add_field(name="!주사위",value = "봇과 주사위 대결을 합니다.",inline = False)
    embed.add_field(name="!골라줘",value = "A와 B를 ,로 구분하여 사용하면 골라줍니다",inline = False)
    embed.add_field(name="!내전 N인",value = "사람을 ,로 구분하면 팀을 출력합니다.",inline = False)
    await ctx.channel.send(embed=embed)


@bot.event
async def on_message(message):  
    if message.author.bot : # 다른 봇이 채팅을 쳤을 때 인식안함
        return None

    if message.author == bot.user: # 이 봇이 채팅 쳤을 때 인식안함
        return
        
    if message.content.startswith("!내전 10인"):
        msg = message.content.replace("!내전 10인", " ")
        msg = msg.split(",")
        
        np.random.shuffle(msg)
        
        embed = discord.Embed(title='내전 팀', description='', color=0x62c1cc)
        embed.add_field(name="1팀", value=msg[0]+' '+msg[1]+' '+msg[2]+' '+msg[3]+' '+msg[4], inline=True)
        embed.add_field(name="2팀", value=msg[5]+' '+msg[6]+' '+msg[7]+' '+msg[8]+' '+msg[9], inline=True)
        embed.set_footer(text='')
        await message.channel.send(embed=embed)

    if message.content.startswith("!내전 8인"):
        msg = message.content.replace("!내전 8인", "")
        msg = msg.split(",")
        
        np.random.shuffle(msg)
        
        embed = discord.Embed(title='내전 팀', description='', color=0x62c1cc)
        embed.add_field(name="1팀", value=msg[0]+' '+msg[1]+' '+msg[2]+' '+msg[3], inline=True)
        embed.add_field(name="2팀", value=msg[4]+' '+msg[5]+' '+msg[6]+' '+msg[7], inline=True)
        embed.set_footer(text='')
        await message.channel.send(embed=embed)

    if message.content.startswith("!내전 6인"):
        msg = message.content.replace("!내전 6인", "")
        msg = msg.split(",")
        
        np.random.shuffle(msg)
        
        embed = discord.Embed(title='내전 팀', description='', color=0x62c1cc)
        embed.add_field(name="1팀", value=msg[0]+' '+msg[1]+' '+msg[2], inline=True)
        embed.add_field(name="2팀", value=msg[3]+' '+msg[4]+' '+msg[5], inline=True)
        embed.set_footer(text='')
        await message.channel.send(embed=embed)

    if message.content.startswith("!골라줘"):
        msg = message.content.replace("!골라줘", "")
        msg = msg.split(",")
        await message.channel.send(np.random.choice(msg))


    if message.content.startswith("!안녕"):
        await message.channel.send('안녕!')
         
    if message.content.startswith("!정보통신공학과"):  
        await message.channel.send('정보통신공학과는 21세기 지식 정보사회를 이끌어갈 학문과 기술의 발전, 창의적 기술개발, 그리고 정보산업사회에서 전문가로서의 자질을 양성하며, 궁극적으로 국가의발전과 인류의 번영에 기여할 수 있는 지식인을 양성하는 과다')
    
    await bot.process_commands(message) #commands도 사용하기 위함

bot.run("ttoken")
