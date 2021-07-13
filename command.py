import command_txt
import command_api
from random import choice
import command_bal
import command_ask
import discord

class Command:

  _letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']

  _cmdTxt = command_txt.CommandTxt()
  _cmdApi = command_ask.CommandAsk()
  _cmdAsk = command_api.CommandApi()
  _cmdBal = command_bal.CommandBal()

  def __init__(self, commandPattern = '$n '):
    self.commandPattern = commandPattern
  

  def getCommandRespose(self, command):
    command = command.replace('$n ', "").lower()
    if(self.cmdTxt.isCommandTxt(command)):
      response = self.cmdTxt.getTxt(command)
    elif(self.cmdApi.isCommandApi(command)):
      response = self.command_api.getResponse(command)
    elif(command.startswith('baleia')):
      response = self.cmdBal.getCuriosidade()
    elif(command.startswith('google')):
      response = self.cmdAsk.getLink(command)
    elif(command.startswith('ldias')):
      image = choice(self._letters)+'.jpg'
      response = 'Ldias', file = discord.File('./Ldias/{0}'.format(image))
    elif(msg.startswith('pergunta')):
      responses = ['Sim','Não','Não sei','Talvez','Me pergunta mais tarde','Certamente','Óbvio que não','Ah sei lá sobre','Claro que sim', 'Acho que sim, mas posso estar errado','Tenho que pesquisar um pouco antes de responder']
      await message.channel.send(choice(responses))
    else:
      await message.channel.send('Tô programado pra isso não vlw')
    return response