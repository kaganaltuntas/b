import discord
from bilgebotfikra import*
from bilgebotyazitura import*
from bilgebotparola import*
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def toplama(ctx, sayi1, sayi2):
    await ctx.send(sayi1+sayi2) 
@bot.command()
async def çarpma(ctx, sayi1, sayi2):
    await ctx.send(sayi1*sayi2)
@bot.command()
async def bölme(ctx, sayi1, sayi2):
    await ctx.send(sayi1/sayi2)
@bot.command()
async def çıkarma(ctx, sayi1, sayi2):
    await ctx.send(sayi1-sayi2)
@bot.command()
async def fıkra(ctx):
    await ctx.send(bilmece_sor())
@bot.command()
async def yazıtura(ctx):
    await ctx.send(yazi_tura())
@bot.command()
async def parola(ctx):
    await ctx.send(sifre_yap())    


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')



bot.run("TOKEN")
  

