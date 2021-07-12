mport discord
import discord.ext
import math
from discord.ext import commands, tasks

def comb(i, j):
    c = 'Factorial of negative numbers not defined'
    if j > i:
        return c
    else:
        return math.comb(i, j)

def bhask(a, b, c):
    if b**2 - (4*a*c) < 0:
        o = 'Cannot process non positive values for the discriminate'
        return o
    else:
        x = (b*(-1) + (b**2 - (4*a*c))**0.5)/2*a
        y = (b*(-1) - (b**2 - (4*a*c))**0.5)/2*a
        v = [x, y]
        return v

def Prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def fact(n):
    if n > 807 or n < 0 or n-int(n) != 0:
        a = 'Error'
        return a
    else:
        return math.factorial(n)
    
def nthPrime(n):
    a = 0
    p = 1
    while a < n:
        p += 1
        if Prime(p):
            a += 1
    return p

def soma(a):
    x = 0
    y = 0
    while x < a+1:
        y += x
        x += 1
    return y
print(soma(4))    

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

    @commands.group(name='pa', help='Sums the terms of an aritmetic progression  Order: Number of Terms, First term, Last term')
    async def pa(self, ctx, a:int, b:float, c:float):
        await ctx.send((a*(b+c))/2)

    @commands.group(name='ipg', help='Sums the terms of an infinite geometric progression. Order: Reason, First Term')
    async def ipg(self, ctx, a:float, b:float):
        await ctx.send(b/(1-a))

    @commands.group(name='fact', help='Returns the factorial of a given number')
    async def fact(self, ctx, a:int):
        await ctx.send(fact(a))

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
    
    @commands.group(name='comb', help='Returns the combinatorics of two given numbers')
    async def comb(self,ctx, a:int, b:int):
        await ctx.send(comb(a, b))

    @commands.group(name='log', help='Returns the log of the given number')
    async def log(self,ctx, a:int):
        await ctx.send(math.log10(a))

    @commands.group(name='ln', help='Returns the ln of the given number')
    async def ln(self,ctx, a:float):
        await ctx.send(math.log(a))
    
    @commands.group(name='bhask', help='Returns the roots of a quadratic equation')
    async def bhask(self,ctx, a:float, b:float, c:float):
        await ctx.send(bhask(a, b, c))

def setup(client):
    client.add_cog(Math(client))
