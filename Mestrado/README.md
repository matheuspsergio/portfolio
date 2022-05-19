# Avaliação do potencial do Global Fishing Watching para o monitoramento da pesca industrial no Brasil


Compreender os padrões espaço-temporais das pescarias é fundamental para garantir a preservação de espécies e o equilíbrio dos ecossistemas. Assim, minha dissertação analisou o material sobre atividade pesqueira disponível no site da organização [Global Fishing Watch](https://globalfishingwatch.org/), de forma a averiguar se ele poderia ser utilizado para o Brasil. A principal  questão é que essa base de dados é de abrangência global de forma que os países não foram olhados individualmente em detalhe[1](https://www.fao.org/documents/card/en/c/ca7012en/), [2](https://www.science.org/doi/10.1126/science.aao5646]). Em especial, o Brasil é um país que sabidamente há escassez de dados no que tange a pesca, de forma que uma análise mais minuciosa é necessária para atestar qualidade do material fornecido pela GFW. Para tanto, os 3 scripts na desta página foram escritos:
<br />
<br />
_1-Limpeza de dados, em que somente os dados referentes ao Brasil foram aproveitados_
<br />
<br />
_2-Acurácia dos algoritmos. Aqui os resultados produzidos pelos algoritmos da GFW foram testados. Em resumo, grande parte parte do conteúdo presente no dataset da GFW, tais como petrecho, comprimento e arqueação bruta foram inferidas a partir dos dados de navegação dos barcos. O que fiz então, foi validar se as estimativas geradas foram boas._
<br />
<br />
_3-Análise da atividade pesqueira. Após a validação, os dados foram utilizados para estudar os principais padrões encontrados encontrados para poder comparar com o que é descrito na literatura_
<br />
<br />
<br />
##Resumo principais achados
A minha dissertação mostrou que, a despeito da baixa adesão do uso de AIS no Brasil, os dados da GFW podem ainda ser largamente aproveitados para estudos sobre a pesca de grande porte. Mais do que a situação brasileira, esse trabalho mostra como esses dados podem ser empregados para qualquer país com situação similar e o que é necessário para fazê-lo de forma confiável. Como principais achados, pode-se listar:
• É importante haver uma referência oficial sobre a frota a ser a analisada, sem confiar nos dados sobre embarcações gerados pelos algoritmos da GFW.
• Os dados do GFW podem ser usados em estudos sobre a pesca no Brasil de cerco e espinhel horizontal.
• Com o devido refinamento, é possível usar os dados do espinhel horizontal para avaliar a pesca de vara e isca-viva.
• Não há embarcações o suficiente para utilizar os dados da GFW para seguir 
embarcações individualmente, as análises devem considerar a frota como um todo. Entretanto, no caso do espinhel, é possível dividir em setor sul/sudeste e norte/nordeste.
• Tais estudos devem possuir abrangência temporal superior a um dia, mas podem ser inferiores a um mês.
• Não é possível fazer o monitoramento da maioria das áreas de proteção marinha do 
Brasil, é necessária uma escala espacial maior.
<br />
<br />
Cabe destacar que meu projeto de mestrado extrapolou apresentado aqui, incluindo, por exemplo, análises cartográficas feitas no ArcGis. De fato, parte dos scripts foram escritos apenas para dar suporte a outras atividades, de forma que por vezes eles podem não ser facilmente compreendidos do resto. Esse foi o meu primeiro proejto escrito sem qualquer tipo de guia ou orientação e o código era utilizado somente por mim. Reconheço que por conta disso algumas partes não estão tão "pythônicas"

Adicionalmente, acrescentei um glossário com as definições de termos específicos do contexto da pesca e de análise espacial que aparecem nestes arquivos e que podem ser necessários para a compreensão de tudo que foi feito. __Caso tenha alguma sugestão, por favor entre em contato!__
