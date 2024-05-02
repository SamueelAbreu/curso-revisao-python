#  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.

# Counter 

"""
Modulo colections = Counter

Collections -> Hight-performace Container Datetypes

Counter -> recebe um iteravel como parametro e cria um objeto do tipo collections Counter que e
parecido com um dicionario, contendo como chave o elemento da lista passada como parametro e com o valor
e a quantidade de ocorrencias desse elementos

# Exemplo 1
from collections import Counter

lista = [1,1,1,1,2,3,5,6,55,67,8,234,54364,67897,809,546,231,312]
res = Counter(lista)

print(type(res))
print(res)

# Saida: Counter({1: 4, 2: 1, 3: 1, 5: 1, 6: 1, 55: 1, 67: 1, 8: 1, 234: 1, 54364: 1, 67897: 1, 809: 1, 546: 1, 231: 1, 312: 1})
# Para cada elemento da lista o Counter criou uma chave e colocou a quantidade de ocorrencias

# Exemplo 2
print(Counter('Geek University'))
# saida: Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
# Inclusive contou os espaços! 

"""

# Utilizando counter
from collections import Counter
# Exemplo 3
# Wikipedia Dinho(Cantor) do Mamonas Assassinas
texto = """Alecsander Alves Leite (Irecê, 5 de março de 1971 – São Paulo, 2 de março de 1996), mais conhecido como Dinho, foi um cantor, compositor e humorista brasileiro, conhecido por ser o vocalista da banda Mamonas Assassinas.[3]

Dinho, nascido em Irecê, mudou-se para Guarulhos com os pais com apenas dois meses. Seu apelido foi criado por sua avó, que, por ser de origem espanhola, não conseguia pronunciar Alecsander, o nome de batismo do cantor.

Em julho de 1990, entrou para a banda Utopia após conhecer os irmãos Sérgio Reoli e Samuel Reoli, baterista e baixista, respectivamente, e o guitarrista Bento Hinoto, quando estes perguntaram, numa apresentação, se alguém na plateia estava hábil para cantar a canção "Sweet Child o' Mine", da banda de rock estadunidense Guns N' Roses. Depois da entrada do tecladista Júlio Rasec, gravaram um disco homônimo, que seria o primeiro e último disco da banda. O álbum continha quatorze faixas, incluindo "Pelados em Santos" e "Robocop Gay", que geraram reconhecimento ao grupo.

Em 1996, Dinho faleceu em decorrência de um acidente aéreo de comoção nacional no qual também morreram os outros integrantes da banda e os outros tripulantes da aeronave.

Biografia e carreira
Primeiros anos e apelido

Vista panorâmica de Irecê, na Bahia, cidade natal de Dinho.
Dinho nasceu em Irecê, na Bahia, mas com apenas dois meses de vida migrou com os pais, Hildebrando Alves Leite e Célia Ramos Alves, para Guarulhos, em São Paulo, onde a família buscaria um futuro melhor. Seu apelido foi dado pela avó materna, Carmen Ramos, de origem espanhola,[4] que não conseguia pronunciar Alecsander e por isso o apelidou de Dinho.[5]

Dinho começou a cantar ainda na infância, e aos cinco anos de idade já era a grande atração do coral infantil da igreja que frequentava. Ainda durante a infância, teve suas primeiras aulas de canto na igreja Assembleia de Deus de Guarulhos em Vila Barros (Ministério de Madureira), dadas pelo professor Donizete Severo. Em 1993, o professor de canto morreu em um acidente na fábrica em que trabalhava e desde então Dinho nunca mais voltou à igreja.[6]

Humor e saída da escola
Desde a infância seu carisma era notável. Na escola, Dinho fazia sucesso com as meninas e era um verdadeiro terror para diretores e professores. Certa vez, em uma reunião de pais e mestres, uma professora desabafou para o pai de Dinho: "Botei o Dinho no fundo da sala, e ele não deixou ninguém do fundão estudar. Então o passei para o meio, e ele começou a incomodar os alunos da frente e os de trás. Então decidi colocá-lo na primeira fila, mas aí ele não me deixou dar aula. O que eu faço?". Aos dezessete anos, após ser eleito Garoto Verão de Guarulhos, vencer um concurso de dança no Programa Silvio Santos, do SBT, e se apresentar algumas vezes no Perdidos na Noite, da Rede Bandeirantes, Dinho completou o segundo ano do segundo grau e decidiu largar os estudos.[6]

1989-1995: Utopia e fracasso comercial

Dinho se apresentando com a banda Utopia.
Em julho de 1990, Dinho estava assistindo um show da banda Utopia, formada à época por Sérgio Reoli, Samuel Reoli e Bento Hinoto no Parque Cecap, em Guarulhos, quando subiu ao palco para cantar a música "Sweet Child o' Mine", dos Guns N' Roses.[7] Apesar de não saber cantar em inglês, seu carisma e sua presença de palco lhe garantiram o posto de novo vocalista do grupo, que posteriormente teria Márcio Araújo (tecladista) e Júlio Rasec (então percussionista, posteriormente tecladista) como integrantes. A banda fazia pequenos shows em Guarulhos, especialmente no Parque Cecap, porém as músicas sérias do Utopia jamais fizeram o sucesso que os músicos esperavam. O fracasso pareceu ficar mais nítido em 1992, quando o LP da banda vendeu menos de cem cópias. Apesar das adversidades, Dinho não desistiu, e chegou a ir até a prefeitura de Guarulhos pedir para que o Utopia fizesse um show na inauguração do Ginásio Paschoal Thomeu, em Guarulhos. O fato de ser um completo desconhecido fez com que Dinho fosse destratado e humilhado pelos responsáveis do evento, que recusaram de maneira hostil a participação do Utopia na inauguração do ginásio.[6]

Chegou a trabalhar como office boy e como animador de comícios, especialmente para o vereador Geraldo Celestino, fazendo imitações cômicas de celebridades como Maguila, Silvio Santos e Luiz Inácio Lula da Silva. Em meados de 1992, começou a trabalhar como apresentador de um quadro musical do extinto programa Sábado Show, da Record, que era comandado pelo ex-sogro Savério Zacanini, que foi o responsável por dar as primeiras oportunidades de Dinho e da banda Utopia se apresentarem na televisão.[6]

1995-96: Mamonas Assassinas e sucesso

Dinho (à esquerda) com Júlio Rasec, Samuel Reoli, Bento Hinoto e Sérgio Reoli, respectivamente, da esquerda para a direita.
Com o passar do tempo, Dinho acabou percebendo que seu lado cômico e algumas músicas de brincadeira faziam mais sucesso do que as músicas sérias do Utopia. Após uma gravação despretensiosa das músicas "Mina" (que posteriormente seria reescrita e rebatizada como "Pelados em Santos") e "Robocop Gay", o grupo Utopia acabou sendo convencido pelo produtor Rick Bonadio a trocar o rock sério pela música cômica, e assim, em 1995, surgiu o grupo Mamonas Assassinas.[6]

Com o sucesso instantâneo, inesperado e arrebatador que o grupo Mamonas Assassinas teve em 1995, Dinho passou de um completo desconhecido para frontman da banda mais popular do Brasil, tornando-se uma das celebridades mais assediadas do país em questão de semanas. Com a fama, conheceu alguns de seus ídolos, como Humberto Gessinger, Chitãozinho & Xororó, Roberto Leal e Morten Harket, vocalista da icônica banda A-ha, com quem Dinho e os Mamonas Assassinas dividiram o palco em um show na casa noturna Toco Dance Club, tocando o clássico hit "Take on Me".[6]

Em 6 de janeiro de 1996,[8] os Mamonas Assassinas voltaram para Guarulhos para realizar um inesquecível show no Ginásio Paschoal Thomeu,[9] onde foram humilhados anos antes. Antes da apresentação como Mamonas Assassinas, os cinco integrantes da banda subiram ao palco sem as famosas fantasias e fizeram um show como se fossem Utopia, tocando as músicas "Será", do Legião Urbana, "Bichos Escrotos", dos Titãs e "Horizonte Infinito", música do fracassado disco do Utopia. Em tom irônico, Dinho agradeceu aos Mamonas Assassinas pela chance de realizar o sonho do Utopia de tocar no ginásio. Em seguida, eles foram ao camarim para vestir as fantasias de presidiário e voltar ao palco como Mamonas Assassinas. No fim do show, Dinho sentou-se no palco e num raro momento de seriedade fez um desabafo para o público:[10]

"Há cinco anos eu estava aí, no meio de vocês, querendo estar aqui. E as pessoas olhavam pra mim e diziam: 'É impossível chegar até aqui' (...) Nós somos a banda Mamonas Assassinas, de Guarulhos, e levamos o nome dessa cidade pelo país e fora. E vamos levar o nome dessa cidade pro exterior também! Porque a gente ainda é daqui. O sucesso não sobe na cabeça das pessoas. Sobe apenas na cabeça das pessoas fracas. E nós não somos pessoas fracas. Se a gente fosse fraco, nós teríamos desistido há cinco anos, quando as pessoas diziam que a gente nunca ia chegar até aqui. Mas nós estamos aqui! (...)"
— Dinho
Guarulhos, SP, 6 de janeiro de 1996.
Vida pessoal

Dinho e a ex-namorada Mirella Zacanini na capa do livro "Pitchulinha, Minha Vida com Dinho - Até que os Mamonas nos Separem".
Dinho namorou Mirella Zacanini, que escreveu o livro Pitchulinha, Minha Vida com Dinho - Até que os Mamonas nos Separem, de 1992 a julho de 1995, quando começou a fazer sucesso.[11] Zacanini, mais tarde, viria a escrever a canção "Mil Momentos", dedicada ao cantor.[12]

Posteriormente, ele manteve relacionamento com Valéria Zoppello, este que durou até sua morte em 1996. Zoppello reside até hoje na Serra da Cantareira, local onde aconteceu o acidente que matou o vocalista. Segundo a fotógrafa, eles iriam se casar no fim do mesmo ano, pretendiam ter filhos e ela iria estar na próxima turnê da banda Mamonas Assassinas.[13][14]

Morte
Ver artigo principal: Acidente do Learjet 25D prefixo PT-LSD em 1996
Em 2 de março de 1996, às 21h58, Dinho e os outros quatro músicos do grupo Mamonas Assassinas, após um show em Brasília, partiram em um Learjet 25D prefixo PT-LSD com destino a Guarulhos, na grande São Paulo.[15] A aeronave, já próxima ao destino, arremeteu em contato com a torre de controle, após o piloto informar que havia condições visuais para tal. Foi realizada, então, uma curva para a esquerda, mas a direção correta para chegar ao aeroporto era à direita.[16] E, por volta das das 23h16, o avião em que o grupo estava colidiu na Serra da Cantareira, no norte da cidade de São Paulo.[17]

Imagem pública
Ruy Brissac, ator que interpretou Dinho no musical O Musical Mamonas, revelou que fazer o personagem do cantor foi um desafio, devido às suas performances, nas quais cantava, dançava e fazia humor. O ator o caracterizou como alguém bem performático.[18]

Nas apresentações, os membros da banda Mamonas Assassinas se apresentavam com diferentes roupas. Dinho, por sua vez, aparecia apenas de cueca, gravata e chifres ao cantar "Bois Don't Cry"; vestido feminino ao cantar "Robocop Gay"; roupa de coelho ao cantar "Chopis Centis"; entre outras, dependendo da canção a ser interpretada.[19]

Homenagens
Em 10 de janeiro de 1996, foi homenageado, ainda em vida, com o título de "Cidadão Emérito de Dracena".[20] Por conta de ser a cidade natal de sua mãe.

Póstumas
Em 2008, foi interpretado por Fabrízio Teixeira no especial Por Toda Minha Vida - Mamonas Assassinas, que concorreu ao Emmy Internacional de melhor programa artístico.

Em 2016, foi interpretado por Ruy Brissac na peça "O Musical Mamonas". Ruy Brissac voltou a interpretá-lo em Mamonas Assassinas - A Série, realizada em parceria com a RecordTV, com roteiro de Carlos Lombardi e direção de Léo Miranda.[21][22] E virou nome de ruas, Rua Alecsander Alves (nome de batismo do Dinho), em Juiz de Fora (MG) e no bairro Villa Barros em Guarulhos (SP).[23][24][25]

Em 2019, foi inaugurado uma praça na sua cidade natal de Irecê, o cantor foi eternizado com a instalação de uma escultura de corpo inteiro, em um ato que contou com a presença dos seus pais, Hildebrando Alves e Célia Ramos, que presenciaram apresentações da Orquestra Sinfônica de Irecê e da banda cover do Mamonas Assassinas, composta por artistas locais.[26]

Discografia
Com o Utopia
Álbum demo
A Fórmula do Fenômeno (1992)
Com os Mamonas Assassinas
Álbuns de estúdio
Mamonas Assassinas (1995)
Coletâneas
Atenção, Creuzebek: A Baixaria Continua (1998)
One: 16 Hits (2009)
Pelados em Santos (2011)
Álbuns ao vivo
Mamonas Ao Vivo (2006)
Mamonas: 20 Anos de Fenômeno (2015)o"""

palavras = texto.split()
# print(palavras)
res = Counter(palavras)
# print(res)

# pegando as 5 palavras com mais ocorrencia no texto
print(res.most_common(10))