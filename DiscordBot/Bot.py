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

client = discord.Client()

help_command = commands.DefaultHelpCommand(no_category = 'Others')

client = commands.Bot(command_prefix = '*', help_command = help_command)

client.load_extension('cogs.Math')
client.load_extension('cogs.Music')
client.load_extension('cogs.Misc')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('!help'))
    print(f'Logged as {client.user}')

client.run('TOKEN')
