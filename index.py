import disnake
from disnake.ext import commands
import requests

import disnake  # para slash sugiro disnake/ mas também pode usar discord.py / pycord
from disnake.ext import commands
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

bot = commands.Bot(
    command_prefix='!',command_sync_flags=command_sync_flags)

@bot.event
async def on_ready():
  print("BOT INICIADO")
@bot.slash_command(name='postimg', description='post img')
async def postimg(inter,title:str,description:str,imglink:str, channel:disnake.TextChannel):
  if inter.author.guild_permissions.administrator:
    await inter.response.send_message(f'PostImg enviado para {channel} {inter.author.mention}')
    embed = disnake.Embed(title=title,description=description)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1079511643530207306/1128190849495351346/Sem_titulo28.png")
    embed.set_image(url=imglink)
    embed.set_author(name=inter.author.name, icon_url=inter.author.avatar)
    await channel.send(embed=embed)
  else:
    await inter.response.send_message(f'{inter.author.mention} Você não e admin')
#post 2
@bot.slash_command(name='posttext', description='post text')
async def posttext(inter,title:str,description:str, channel:disnake.TextChannel):
  if inter.author.guild_permissions.administrator:
    await inter.response.send_message(f'Post Text enviado para {channel}  =>  {inter.author.mention}')
    embed = disnake.Embed(title=title,description=description)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1079511643530207306/1128190849495351346/Sem_titulo28.png")
    embed.set_author(name=inter.author.name, icon_url=inter.author.avatar)
    await channel.send(embed=embed)
  else:
    await inter.response.send_message(f'{inter.author.mention} Você não e admin')
@bot.slash_command(name='rank', description='ranking dos jogadores')
async def rank(inter):
  
  url = "http://browserarcade.freevar.com/get3.php"
  response = requests.get(url)
  data = response.json()
  embed = disnake.Embed(title="Rank dos Jogadores", color=disnake.Color.blue())
  for player in data:
      position = player["posicao"]
      name = player["nome"]
      achievements = player["conquistas"]
      badges = player["emblemas"]
      embed.add_field(name=f"#{position}", value=f"Nome: {name}\nConquistas: {achievements}\nEmblemas: {badges}", inline=False)
  await inter.response.send_message(embed=embed)
@bot.slash_command(name='accountinfo', description='ver informações da conta de algum jogador do banco de dados')
async def account(inter,name:str):
    url = f"http://browserarcade.freevar.com/get2.php?nome={name}"
    response = requests.get(url)
    data = response.json()

    if "id" in data:
        embed = disnake.Embed(title="Informações da Conta", color=disnake.Color.blue())
        embed.add_field(name="Nick", value=data["nome"], inline=False)
        embed.add_field(name="ID", value=data["id"], inline=False)
        embed.add_field(name="Conquistas", value=data["conquistas"], inline=False)
        embed.add_field(name="Emblemas", value=data["emblemas"], inline=False)

        await inter.response.send_message(embed=embed)
    else:
        await inter.response.send_message("Conta não encontrada.")  
bot.run('token')