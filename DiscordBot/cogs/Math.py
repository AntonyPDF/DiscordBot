import discord
import discord.ext
import math
import random
from discord.ext import commands, tasks
from random import choice
from random import randrange


def Prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def nthPrime(n):
    a = 0
    p = 1
    while a < n:
        p += 1
        if Prime(p):
            a += 1
    return p

def divisors(n):
    a = [1]
    for i in range(2, int(n/2+1)):
        if n % i == 0:
            a.append(i)
    a.append(n)
    return a 

class Math(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(name='add', help='Sums two numbers')
    async def add(self, ctx, a:float, b:float):
        await ctx.send(a + b)

    @commands.group(name='pa', help='Sums the terms of an aritmetic progression. Order: Number of Terms, First term, Last term')
    async def pa(self, ctx, a:int, b:float, c:float):
        await ctx.send((a*(b+c))/2)

    @commands.group(name='ipg', help='Sums the terms of an infinite geometric progression. Order: Reason, First Term')
    async def ipg(self, ctx, a:float, b:float):
        await ctx.send(b/(1-a))

    @commands.group(name='fact', help='Returns the factorial of a given number')
    async def fact(self, ctx, a:int):
        await ctx.send(math.factorial(a))

    @commands.group(name='mod', help='Module operation')
    async def mod(self, ctx, a:int, b:int):
        await ctx.send(a % b)

    @commands.group(name='fpg', help='Sums the terms of a finite geometric progresssion. Order: First Term, Reason, Number of Terms')
    async def fpg(self, ctx, a:float, b:float, c:int):
        await ctx.send((a*(b**c-1))/(b-1))
    
    @commands.group(name='mult', help='Multiplies two numbers')
    async def mult(self,ctx, a:float, b:float):
        await ctx.send(a*b)

    @commands.group(name='exp', help='Exponential operation')
    async def exp(self,ctx, a:float, b:float):
        await ctx.send(a**b)

    @commands.group(name='npri', help='Returns the nth prime')
    async def npri(self,ctx, a:int):
        await ctx.send(nthPrime(a))

    @commands.group(name='pri', help='Checks if a given number is prime')
    async def pri(self,ctx, a:int):
        await ctx.send(Prime(a))

    @commands.group(name='divr', help='Returns the divisors of a given number')
    async def divr(self,ctx, a:int):
        await ctx.send(divisors(a))

def setup(client):
    client.add_cog(Math(client))
