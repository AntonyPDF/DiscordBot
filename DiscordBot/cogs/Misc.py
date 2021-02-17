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
from bs4 import BeautifulSoup
from random import randrange

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

    @commands.group(name='dream', help='Shows chads dream')
    async def dream(self, ctx):
        await ctx.send(file = discord.File('C:/Users/admin/Desktop/Images Bot/Dream.PNG'))
    
    @commands.group(name='clear', help='Clears a specified quantity of messages')
    async def clear(self, ctx, a:int):
        await ctx.channel.purge(limit = a)
    
def setup(client):
    client.add_cog(Misc(client))
