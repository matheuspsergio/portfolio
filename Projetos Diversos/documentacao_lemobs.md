# Bem vindos à documentação! [:leftwards_arrow_with_hook:](https://tabsoft.co/3RHZpBk)

Aqui pode ser encontrado um guia para utilização do dashboard, bem como informações acerca do modelo de dados, cálculos e explicações sobre as decisões tomadas em termos de limpeza de dados.

## Sobre o funcionamento dos filtros
Logo no início, é apresentado ao usuário 2 opções de visualização de mapa: por rodovia e por estado. __A visualização é mutuamente excludente__, não é possível ver ambos mapas simultaneamente. Entretanto, __os filtros acionados neles não são__. Ou seja, caso opte por filtrar por um (ou múltiplos) estado em particular e em seguida seja alternada para a visão de rodovias, o filtro de estado permanecerá ativo.<br/>
Com essa configuração de filtros, torna-se possível responder perguntas como:<br/>
-Quais rodovias passam por x estado? Ou: por quantos estados passa determinada rodovia?<br/>
-Quantos acidentes ocorrem em uma determinada rodovia para um trecho de um estado em particular?<br/>
Para que os filtros sejam desativados, é necessário abrir a visualização correspondente ao acionamento do filtro.<br/>
<br/>
Buscando manter a consistência da escala de cor dos mapas da legenda diante de todas as filtragens e que ela tivesse uma referência numérica (em vez de simplesmente claro pouco acidente e escuro muito), a amplitude dela foi fixada. Isso também é reflexo de um comprmetimento de usar filtros mutualmente excludentes que implicava q para que a legenda não sumisse conforme a seleção, ela na verdade está vinculada a um terceiro mapa que fica permanentemente oculto (Sheet de nome "Legenda") cuja função é apenas fornecer esse objeto legenda. Como lado negativo dessa decisão é a perda de resolução da escala de cores ao se realizar algumas filtragens, pois as cores acabam "achatadas".
<br/>
Uma solução para isso seria dividir o dashboard em 2 páginas, uma para estado e outra para rodovias e o botão de filtro passaria a agir como botão de navegação entre as páginas. Todovia, essa decisão não foi tomada pois foi levado em consideração o alto grau de redundância que as páginas teriam, sendo portanto algo pouco otimizado. Testes de desmpenho poderão ser feitos futuramente para reavaliar essa situação.
<br/>
<br/>
Já no gráfico de evolução de acidentes ao longo dos meses, cabe comentar sobre a opção de nível de detalhe disponibilizada pelo Tableau. Ela aparece como um ícone de "+" no lado esquerdo do eixo x. Ao clicar nele, a visualização muda: a resolução passa a ser diária e passa a existir 2 eixos x: um na parte inferior do gráfico, mostrando os dias; e um na parte superior, mostrando os meses em questão. Para retornar ao orignal, basta procurar pelo ícone de "-" que estará no canto superior esquerdo ao lado do rótulo de janeiro.

## Sobre o modelo de dados
Foram usadas 2 fontes de dados: uma base dos acidentes em rodovias federais no período de 2007 a 2020 disponibilizada na plataforma kaggle no formato de arquivos csv; um shapefile da malha rodoviária nacional obtido no site do [Departamento Nacional de Infraestrutura de Transportes](https://www.gov.br/infraestrutura/pt-br/assuntos/dados-de-transportes/bit/bitmodosmapas#maprodo).<br/>
Cada fonte tinha sua própria chave primária, sendo que a conexão entre elas foi feita com um left join usando as respectivas colunas identificadoras de rodovia como chave estrangeira. Ademais, como os acidentes estavam divididos em arquivos anuais, os arquivos também precisaram ser unidos no Tableau.

## Sobre a limpeza de dados
Por se tratar de uma junção de arquivos, algumas inconsistências de nomenclatura foram observadas. Nos casos em que era inequívoco como elas deveriam ser resolvidas (por exemplo utilização de letra e acentuação), foi realizado um agrupamento manual de categorias. No caso em particular dos tipos de acidentes, faz-se necessário explicitar 2 procedimentos adotados. A categoria “colisão lateral” recebeu dois tipos específicos de colisão lateral: colisão no mesmo sentido e no sentido oposto. Somente 18 registros faziam essa distinção de sentido de colisão lateral, enquanto todo o restante era considerado apenas colisão lateral. Inversamente, o padrão para colisão com objetos era distinguir se os objetos estavam fixos ou em movimento. Entretanto, foram excluídos da análise de tipo de acidente os registros de “colisão com objeto” que totalizaram 21 ocorrências.<br/>
Na análise das condições climáticas, optou-se por excluir neve e granizo a fim de favorecer uma melhor visualização dos demais tempos que possuem maior representatividade. De fato, neve e granizo sequer possuem 10% da frequência do tempo em antepenúltima posição em termos de quantidade de acidentes.<br/>
Devido à grande variabilidade de formas de escrever uma causa de acidente e do grande número de causas de acidente em si, fazer um agrupamento manual tornou-se pouco factível. A estratégia então foi filtrar as causas com uma contagem de acidentes superior a 100. Com isso, algumas causas aparecem repetidas na nuvem de palavras, porém sem prejuízo ao entendimento geral do contexto.<br/>
A categoria uso do solo foi majoritariamente dominada pelas categorias “Rural” e “Urbano”. Entretanto, a partir de 2017, (<10% do total) esse rótulos aparentemente foram substítuídos por “Sim” e “Não”. Como não havia uma maneira de atribuir um sentido para esses valores dentro desse contexto, eles foram removidos. Uma implicação disso é que ao realizar filtragem por ano dentro do período de 2017 a 2020, esse gráfico irá desaparecer.

## Sobre os cálculos
Letalidade: Somatório de mortes dividido pelo somatório da coluna de envolvidos em acidentes multiplicado por 100.<br/>
<br/>
Ranking de frequência: Foi utilizada a função rank disponibilizada pelo próprio Tableau.<br/>
<br/>
Frequência de acidente ponderada: Primeiro, foi realizada a contagem de segmentos distintos. Esse valor foi utilizado para dividir o total de acidentes que estava separado pelo tipo de pista. Assim, quanto menos frequente um tipo de pista for, maior o peso que cada acidente terá. Esse cálculo, entretanto, não leva em consideração a extensão de cada trecho.<br/>
<br/>
Gráfico de radar: Embora o Tableau não disponibilize nativamente essa opção de gráfico, com uma série de procedimentos e contas e possível criá-lo. De fato, isso é amplamente conhecido pela comunidade, e há uma série de guias ensinando como fazê-lo, que podem ser encontrados [neste blog](https://www.thedataschool.co.uk/ellen-blackburn/a-simple-way-to-make-a-radar-chart/), [neste vídeo no Youtube](https://www.youtube.com/watch?v=wWUXTQZZW2w) e no [próprio site do Tableau](https://www.tableau.com/pt-br/about/blog/2015/7/use-radar-charts-compare-dimensions-over-several-metrics-41592), embora esse último utilize um outro método.
