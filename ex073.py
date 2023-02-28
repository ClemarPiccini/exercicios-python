# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time do Santos.
times = ('Palmeiras', 'Flamengo', 'Internacional', 'Fluminense', 'Corinthians',
'Athletico-PR', 'Fortaleza', 'São Paulo', 'América', 'Botafogo', 'Santos', 'Goiás', 
'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Grêmio', 'Vasco', 'Bahia')
print('=-'*20)
print('Lista de times do brasileirão: {}'.format(times))
print('=-'*20)
print('Os 5 primeiros times são: {}'.format(times[0:5]))
print('=-'*20)
print('Os 4 ultimos colocados são: {}'.format(times[-4:]))
print('=-'*20)
print('Os times em ordem alfabetica: {}'.format(sorted(times))) #sorted usado para mostrar em ordem alfabetica
print('=-'*20)
print('O time do Santos esta na posição:{}'.format(times.index('Santos')+1)) #index para encontrar e +1 pois a contagem inicia do zero
print('=-'*20)
