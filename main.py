import disnake
from disnake.ext import commands
bot = commands.Bot(command_prefix='.')


class MyClient(disnake.Client):
    async def on_ready():
        print(f"{bot.user.name} Is Online!")
        try:
            print("Bot Is Starting..")
        except:
            print("Bot Has Had A Error!")

    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = disnake.Embed(title='A Error Has Ocurred! :x:',
                                  description='Error: MissingPermissions', color=disnake.Color.random())
            embed.set_thumbnail(
                url='https://media.tenor.com/images/22c7e7e0e27cac17fc6545d55942032c/tenor.gif')
            await ctx.reply(embed=embed)
            raise(error)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = disnake.Embed(title='A Error Has Ocurred! :x:',
                                  description='Error: MissingRequiredArgument', color=disnake.Color.red())
            embed.set_thumbnail(
                url='https://media.tenor.com/images/22c7e7e0e27cac17fc6545d55942032c/tenor.gif')
            await ctx.send(embed=embed)
        if isinstance(error, commands.CommandNotFound):
            embed = disnake.Embed(title='A Error Has Ocurred! :x:',
                                  description='Error: CommandNotFound', color=disnake.Color.red())
            await ctx.send(embed=embed)
        if isinstance(error, commands.NotOwner):
            embed = disnake.Embeds(title='A Error Has Ocurred! :x:',
                                   description='Error: NotOwner', color=disnake.Color.red())
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRole):
            embed = disnake.Embed(title='A Error Has Ocurred! :x:',
                                  description='Error: MissingRole', color=disnake.Color.red())
            await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
    embed = disnake.Embed(title='Owner(s)', color=disnake.Color.random())
    embed.add_field(name='Owner:', value='DeepSleepMusic#0001')
    embed.add_field(name='Co-Owner:', value='Sparky#3940')
    embed.add_field(name='Admin:', value='Ghost_Boi#0001')
    embed.add_field(name='Platform', value='Visual Studio Code')
    thumbnail = embed.set_thumbnail
    thumbnail(
        url='https://media1.tenor.com/images/17371ac53d1f82719e18cd14da9991b7/tenor.gif')
    await ctx.send(embed=embed)


@bot.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: disnake.Member, *, reason=None):
    guild = ctx.guild
    embed = disnake.Embed(title='Kicked! :white_check_mark:',
                          description=f'You Have Been Kicked From: {guild} For: {reason}', color=disnake.Color.random())
    await member.send(embed=embed)
    await member.kick(reason=reason)
    embed = disnake.Embed(title='Kicked! :white_check_mark:',
                          description=f'The Member: {member.mention} Has Been Kicked For: {reason}')
    thumbnail = embed.set_thumbnail
    thumbnail(
        url='https://media1.tenor.com/images/17371ac53d1f82719e18cd14da9991b7/tenor.gif')
    await ctx.send(embed=embed)


@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: disnake.Member, *, reason=None):
    guild = ctx.guild
    embed = disnake.Embed(title='Banned! :white_check_mark:',
                          description=f'You Have Been Banned From: {guild} For: {reason}', color=disnake.Color.random())
    await member.send(embed=embed)
    await member.ban(reason=reason)
    embed = disnake.Embed(title='Banned! :white_check_mark:',
                          description=f'The Member: {member.mention} Has Been Banned For: {reason}')
    embed.set_thumbnail(
        url='https://media1.tenor.com/images/17371ac53d1f82719e18cd14da9991b7/tenor.gif')
    await ctx.send(embed=embed)



@bot.command()
async def poll(ctx, *, text: str = None) -> None:
    """Creates a poll."""

    msg = await ctx.send(f"Poll: {text}")
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")




bot.run(input("Token: "))
