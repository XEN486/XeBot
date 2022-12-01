import discord, properties, os, asyncio, random
from discord.ext import commands
from discord.ext import tasks

os.environ["JISHAKU_NO_UNDERSCORE"] = "true"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "true" 
os.environ["JISHAKU_HIDE"] = "true"

extensions = ['Fun', 'General', 'Jishaku']
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=properties.PREFIX, intents=intents)
for extension in extensions:
    print(f'Loading extension: {extension}')
    bot.load_extension(f'Extensions.{extension}.{extension}')
extensions.remove('Jishaku') # hide it from view
bot.remove_command('help')

@bot.event
async def on_ready():
    properties.GUILD_IDS = [guild.id for guild in bot.guilds]
    bot.owner_ids = properties.OWNERS
    print(f'Logged in as user \'{bot.user.name}#{bot.user.discriminator}\' with id \'{bot.user.id}\' in {len(properties.GUILD_IDS)} servers.')

@bot.event
async def on_command_error(ctx,error):
    embed = discord.Embed(color=0xFF0000, title='We have run into an error!')
    embed.add_field(name='Error', value = repr(error))
    await ctx.send(embed=embed)


#@bot.command()
#async def help(ctx, extension:str=None):
#    if not extension:
#        embed = discord.Embed(color=0xFF0000, title='Extensions')
#        extensionList = '\n'.join(extensions)
#        embed.add_field(name='Extensions', value = f'''
#```
#{'!!NL!!'.join(extensions)}
#```
#Write '{properties.PREFIX}help <extension> to get a list of commands for any extension.'
#'''.replace('!!NL!!','\n'))
#        await ctx.send(embed=embed)
#    else:
#        command = bot.get_command(extension)
#        subcommands = []
#        for command in bot.commands:
#            if command.cog and command.cog.qualified_name == extension:
#                subcommands.append(command.name)
#        commandString = '```\n'+'\n'.join(subcommands)+'```\n'+f'Write {properties.PREFIX}help <extension>\' to get a list of commands for any extension.'
#        embed = discord.Embed(color=0x00FF00, title=f'{extension}')
#        embed.add_field(name='Subcommands', value = commandString)
#        await ctx.send(embed=embed)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'Extensions.{extension}.{extension}')
    embed = discord.Embed(title='Extension Loader', description=f'Loaded \'{extension}\'.')
    await ctx.send(embed=embed)

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'Extensions.{extension}.{extension}')
    embed = discord.Embed(title='Extension Unloader', description=f'Unloaded \'{extension}\'.')
    await ctx.send(embed=embed)

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id not in properties.OWNERS:
        await ctx.send('You are not a bot owner.')
    else:
        bot.reload_extension(f'Extensions.{extension}.{extension}')
        embed = discord.Embed(title='Extension Reloader', description=f'Reloaded \'{extension}\'.')
        await ctx.send(embed=embed)

async def changeStatus():
    await bot.wait_until_ready()
    statuses = ['with complex numbers', 'with my commands', 'Half-Life', 'Half-Life 2']

    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(15)

bot.loop.create_task(changeStatus())
bot.run(properties.TOKEN)
    
