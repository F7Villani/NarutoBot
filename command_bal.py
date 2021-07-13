import random

class CommandBal:

  curiosidades = ["Baleias nunca dormem completamente. Por serem mamíferos, as baleias precisam do oxigênio que existe na superfície. Por isso elas são nadadoras conscientes, ou seja, precisam decidir quando respirar.","Para dormir, por exemplo, elas entram em um estado de semiconsciência, ficam meio acordadas, mesmo dormindo.","Exatamente por precisar do oxigênio da atmosfera, a baleia sai, de vez em quando, do fundo do mar, para respirar na superfície e encher os pulmões.","Elas podem ser tão grandes quanto os dinossauros. A baleia-azul é semelhante, em termos de tamanho, à alguns dinossauros, como o Titanossauro ou Argentinossauro, que tinham mais de 40 metros de comprimento.","Elas cantam. Uma das formas de comunicação das baleias é a música. Elas cantam para fins de reprodução, segundo os cientistas. No entanto, as suas canções não pode ser escutadas pelo ouvido humano, porque elas se comunicam em uma frequência mais baixa do que as pessoas conseguem escutar.","As baleias belugas são, particularmente, fãs de música.","O coração de uma baleia-azul bate tão alto que pode ser escutado a três quilômetros de distância.","Elas são feministas. As fêmeas são as figuras mais importantes na sociedade das baleias. São elas que lideram os grupos e ficam com seus filhotes durante a vida inteira.","Moby Dick realmente existiu. A baleia Moby Dick, imortalizada na obra de Herman Melville, existiu de fato. Estudos indicam que aconteceu mesmo um episódio semelhante ao relatado no livro. A baleia de verdade chamava-se Mocha Dick e afundou um navio inglês, por volta de 1820.","Elas se alimentam de modo diferente. Baleias têm um órgão próximo ao queixo, que não existe em nenhum outro animal, e é responsável por ajudá-las a filtrar os alimentos que elas capturam no mar, tendo em vista que elas engolem muita água nesse processo.","Os bebês das baleias são famintos. Se você acha que bebês humanos mamam muito é por que não conhece os filhotes das baleias. Eles podem mamar cerca de 500 litros em apenas um dia. Isso que é apetite!","Elas vivem muito. Cientistas descobriram uma espécie de baleia que pode ter vivido cerca de 200 anos: a baleia da Groenlândia. E ela pode ajudar os pesquisadores a decifrarem como os humanos podem viver mais.","A baleia azul é o mais pesado animal do planeta Terra! Pesa cerca de 140 toneladas e somente a sua língua, pesa 6 toneladas. Dependendo de seu tamanho, as baleias conseguem armazenar cerca de 1 tonelada no seu estômago.","As baleias nadam cerca de 5 km/h quando estão embaixo d’água. Diminuindo a velocidade para 1 km/h quando estão se alimentando ou em área de reprodução.","Até hoje, a maior baleia caçada foi a baleia-azul fêmea, que pesava em torno de 170 toneladas e media 34 metros.","No século XIX, o óleo de baleia era usado na iluminação e lubrificação, as barbatanas davam resistência aos espartilhos e também serviam nos chicotes."]

  def getCuriosidade(self):
    return random.choice(self.curiosidades)
