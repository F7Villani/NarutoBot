class CommandAsk:

  _permitameURL = 'https://permita.me/?q='

  def getLink(self, command):
    text = command.replace('google', '')
    text = text.split(' ')
    link = self._permitameURL
    for word in text:
      link += word+'+'
    return 'Tá ai a resposta amigo:\n'+link