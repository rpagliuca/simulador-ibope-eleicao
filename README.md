# Simulação de IBOPE para Eleições

Aviso: a simulação pode demorar vários minutos para finalizar.

## Instruções

Comando: `python simular-ibope-eleicao.py`

## Como funciona

São gerados 200.000.000 de votos (representando a população brasileira) entre diferentes candidatos
com probabilidade real conhecida.

Em seguida, são escolhidos 1.000 votos ao acaso, representando o procedimento do IBOPE para determinar
o percentual de itenção de votos.

No final da simulação, é exibido o percentual obtido por amostragem.

Verifica-se que, na grande maioria dos casos, o erro é menor de 2 pontos percentuais para mais ou para menos.
