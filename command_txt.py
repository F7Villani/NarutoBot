

class CommandTxt:

  command_dic = {'podcast': 'Ai se liga nesse podcast foda:\nhttps://open.spotify.com/episode/2C1w259mGVyHDWGB9n4pFj?si=fvt6vADJRiC6H_i2tc1oTw&dl_branch=1','invite':'Me chama pro teu server ai:\nhttps://discord.com/api/oauth2/authorize?client_id=858540603620327435&permissions=67584&scope=bot','limeira': 'Limeira é um município brasileiro situado no Centro-Leste do estado de São Paulo. Sua população estimada em 2017 era de 300.911 habitantes e aproximadamente 67% dessa população vai ser chacinada pelo Rafael no dia do juízo final, quando o Acre ascender aos céus e Recife se tornar a base da aliança revolucionária, onde Ldias liderará a retomada dos colostros aliado ao Mike e ao Sonic.','help':"```\n== NarutoBot ==\n\nComandos são acionados com ' $n ', por exemplo: ' $n podcast '\n\n-- Lista de Comandos --\n\npodcast   | Te recomenda um podcast foda\ninvite    | Gera o link pra você convidar o NarutoBot pro seu server\nlimeira   | Te conta uma linda história sobre limeira\nbaleia    | Te conta uma curiosidade sobre as baleias\nbitcoin   | Te mostra quanto tá valendo o bitcoin\ndolar x   | Converte x doláres em reais (o valor 'x' é opcional)\ngoogle    | Use esse comando para que o bot pesquise algo para você\nldias     | Te apresenta alguém da família Ldias\npergunta  | Faça uma pergunta simples para o bot```"}  


  def isCommandTxt(self,command):
    if (command in self.command_dic.keys()):
      return True
    else:
      return False

  def getTxt(self, command):
    return self.command_dic[command]

  def addCommand(self, command, txt):
    self.command_dic[command] = txt
  
  
  