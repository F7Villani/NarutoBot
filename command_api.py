import os
import requests
import json

class CommandApi:

  _commands = ['bitcoin', 'dolar']
  
  _bitApiURL = 'https://rest.coinapi.io/v1/exchangerate/BTC/BRL?apikey={0}'.format(os.environ['apiKey'])

  _dolarApiURL = 'https://economia.awesomeapi.com.br/last/USD-BRL'
  
  def isCommandApi(self, command): 
    if (command.startswith('dolar')):
      return True
    elif(command.startswith('bitcoin')):
      return True
    else:
      return False
  
  def getResponse(self, command):
    if (command == 'bitcoin'):
      return self.getBtcValue()
    else:
      command = command.replace("dolar", "")
      command = command.replace(" ","")  
      if (command == ""):
        print('entrei aqui')
        dolar = 1
      else:
        dolar = float(command)
      return self.getDolar(dolar)


  def getBtcValue(self):
    response = requests.get(self._bitApiURL)
    json_data = json.loads(response.text)
    btcValue = json_data['rate']
    strbtcValue = 'O bitcoin tá valendo R$ {0:.2f}, to certo!'.format(btcValue)
    return strbtcValue

  def getDolar(self, dolar):
    response = requests.get(self._dolarApiURL)
    json_data = json.loads(response.text)
    dolarBid = float(json_data['USDBRL']['bid'])
    value = dolarBid*dolar
    return "US$ {0:.2f} = R$ {1:.2f}\nBolsonaro filho da puta!!!".format(dolar,value)