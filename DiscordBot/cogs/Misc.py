import discord
import os
import asyncio
import discord.voice_client
import functools
import discord.ext
import itertools
import async_timeout
import math
import random
import youtube_dl
import requests
from async_timeout import timeout
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
from random import choice
from discord.ext import commands
import logging
from urllib import request
import codecs
import aiohttp
from itertools import permutations
from bs4 import BeautifulSoup
from random import randrange
from googlesearch import search 

def Permutations(n): 
    a = permutations(n)
    b = []
    c = 'No strings with length longer than 5'
    if len(n) > 5:
        return c
    else:
        for i in a:
            b.append(''.join(i))     
    return b 

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(name='len', help='Returns the length of a given string')
    async def len(self, ctx, a:str):
        await ctx.send(len(a))

    @commands.group(name='rng', help='Generates a random number in a given limit')
    async def rng(self, ctx, a:int):
        await ctx.send(randrange(a))
    
    @commands.group(name='gay', help='Gay')
    async def gay(self, ctx):
        await ctx.send('{} is gay'.format(ctx.message.author))

    @commands.group(name='chad', help='Shows chad')
    async def chad(self, ctx):
        await ctx.send(file = discord.File('C:/Users/admin/Desktop/Images Bot/gigachad.jpg'))

    @commands.group(name='dream', help='Shows chads dream')
    async def dream(self, ctx):
        await ctx.send(file = discord.File('C:/Users/admin/Desktop/Images Bot/Dream.PNG'))
    
    @commands.group(name='clear', help='Clears a specified quantity of messages')
    async def clear(self, ctx, a:int):
        await ctx.channel.purge(limit = a+1)
    
    @commands.group(name='perm', help='Permutates a given( string')
    async def perm(self, ctx, a:str):
        await ctx.send(Permutations(a))
    
    @commands.group(name='armor', help='Gives armor defense on LOL based on the armor value')
    async def armor(self, ctx, a:int):
        await ctx.send(a/(a+100))

    @commands.group(name='google', help='Googles a given term or sentence')
    async def armor(self, ctx, a:str):
        await ctx.send(search(a)[0])    

def setup(client):
    client.add_cog(Misc(client))
