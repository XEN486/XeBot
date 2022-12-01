import discord, random, asyncio, io, requests, math, io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
from discord.ext import commands
from discord.commands import Option
import properties

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.slash_command(name='8ball')
    async def eightball(self, ctx, question:Option(str)):
        possibleChoices = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
                           'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.',
                           'Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

        newEmbed = discord.Embed(title='8-Ball')
        newEmbed.add_field(name=question, value=random.choice(possibleChoices))
        await ctx.respond(embed=newEmbed)

    @commands.slash_command(name='imagefilter')
    async def imagefilter(self, ctx, imagefilter:Option(str), attachment:Option(discord.Attachment)):
        await ctx.respond('Processing...')
        imageFilter = imagefilter
        contents = await attachment.read()
        img = Image.open(io.BytesIO(contents)).convert('RGB')
        if imageFilter == 'blur':
            img = img.filter(ImageFilter.BLUR)
        elif imageFilter == 'contour':
            img = img.filter(ImageFilter.CONTOUR)
        elif imageFilter == 'detail':
            img = img.filter(ImageFilter.DETAIL)
        elif imageFilter == 'edge_enhance':
            img = img.filter(ImageFilter.EDGE_ENHANCE)
        elif imageFilter == 'edge_enhance_more':
            img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif imageFilter == 'emboss':
            img = img.filter(ImageFilter.EMBOSS)
        elif imageFilter == 'find_edges':
            img = img.filter(ImageFilter.FIND_EDGES)
        elif imageFilter == 'sharpen':
            img = img.filter(ImageFilter.SHARPEN)
        elif imageFilter == 'smooth':
            img = img.filter(ImageFilter.SMOOTH)
        elif imageFilter == 'smooth_more':
            img = img.filter(ImageFilter.SMOOTH_MORE)
                
        with io.BytesIO() as imgBin:
            img.save(imgBin, 'PNG')
            imgBin.seek(0)
            await ctx.send(file=discord.File(fp=imgBin, filename=f'{imageFilter}.png'))

    @commands.slash_command(name='graph')
    async def graph(self, ctx, graphstring:Option(str)):
        await ctx.respond('Processing...')
        graphstring = graphstring.replace('``','').split(' ')
        plt.title(f'Graph')
        plt.xlabel('y', color='#1C2833')
        plt.ylabel('x', color='#1C2833')
        for graph in graphstring:
            x = np.linspace(-np.pi, np.pi,100)
            graphV = eval(graph)
            ax = plt.gca()
            ax.spines['top'].set_color('none')
            ax.spines['left'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['bottom'].set_position('center')
            plt.plot(x, graphV, '-r', label=graph)
            plt.grid(True)
            fig = plt.gcf()

        buf = io.BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        await ctx.send(file=discord.File(fp=buf, filename='graph.png'))
        plt.clf()

    @commands.slash_command(name='complexgraph')
    async def complexgraph(self, ctx, graphstring:Option(str)):
        await ctx.respond('Processing...')
        graphstring = graphstring.replace('``','').split(' ')
        plt.title(f'Graph')
        plt.xlabel('i', color='#1C2833')
        plt.ylabel('r', color='#1C2833')
        for graph in graphstring:
            x = np.linspace(-np.pi,np.pi,100)
            graphV = eval(graph)
            ax = plt.gca()
            ax.spines['top'].set_color('none')
            ax.spines['left'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['bottom'].set_position('center')
            real = graphV.real
            imaginary = graphV.imag
            plt.plot(real, imaginary, '-r', label=graph)
            plt.grid(True)
            fig = plt.gcf()

        buf = io.BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        await ctx.send(file=discord.File(fp=buf, filename='graph.png'))

        plt.clf()
        
    @commands.slash_command(name='stepcomplexgraph')
    async def stepcomplexgraph(self, ctx, i:Option(int), graphstring:Option(str)):
        await ctx.respond('Processing...')
        graphstring = graphstring.replace('``','').split(' ')
        plt.title(f'Graph')
        plt.xlabel('i', color='#1C2833')
        plt.ylabel('r', color='#1C2833')
        for graph in graphstring:
            for c in range(1, i):
                x = np.linspace(-np.pi,np.pi,100)
                graphV = eval(graph)
                ax = plt.gca()
                ax.spines['top'].set_color('none')
                ax.spines['left'].set_position('center')
                ax.spines['right'].set_color('none')
                ax.spines['bottom'].set_position('center')
                real = graphV.real
                imaginary = graphV.imag
                plt.plot(real, imaginary, '-r', label=graph)
                plt.grid(True)
                fig = plt.gcf()

        buf = io.BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        await ctx.send(file=discord.File(fp=buf, filename='graph.png'))

        plt.clf()
            
def setup(bot):
    bot.add_cog(Fun(bot))
