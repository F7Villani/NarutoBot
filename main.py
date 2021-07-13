import os
import discord
import command_bal
import command_txt
import command_api
import command_ask
from random import choice
from keep_alive import keep_alive

command_bal = command_bal.CommandBal()
command_txt = command_txt.CommandTxt()
command_api = command_api.CommandApi()
command_ask = command_ask.CommandAsk()
client = discord.Client()

letters = ['a','b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online,activity=discord.Game('NarutoBot  |  $n help'))
  print("TAMO ON - {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content.lower()
  
  if ('paia' in msg):
    await message.channel.send("Inheeé é paia memo :/")
  
  message.content = message.content.lower()

  if message.content.startswith('$n'):
    msg = message.content.replace('$n ', "").lower()
    if(command_txt.isCommandTxt(msg)):
      await message.channel.send(command_txt.getTxt(msg))
    elif(command_api.isCommandApi(msg)):
      await message.channel.send(command_api.getResponse(msg))
    elif(msg == 'baleia'):
      await message.channel.send(command_bal.getCuriosidade())
    elif(msg.startswith('google')):
      await message.channel.send(command_ask.getLink(msg))
    elif(msg.startswith('ldias')):
      image = choice(letters)+'.jpg'
      await message.channel.send('Ldias', file = discord.File('./Ldias/{0}'.format(image)))
    elif(msg.startswith('pergunta')):
      responses = ['Sim','Não','Não sei','Talvez','Me pergunta mais tarde','Certamente','Óbvio que não','Ah sei lá sobre','Claro que sim', 'Acho que sim, mas posso estar errado','Tenho que pesquisar um pouco antes de responder']
      await message.channel.send(choice(responses))
    else:
      await message.channel.send('Tô programado pra isso não vlw')
    
    


keep_alive()
client.run(os.environ['TOKEN'])
