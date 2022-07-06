perguntas = {
    'Pergunta 1':{
        'pergunta':'Quanto é 2+2? ',
        'respostas':{'a':'1','b':'6','c':'5','d':'4',},
        'resposta_certa':'d'
    },
    'Pergunta 2':{
        'pergunta':'Quanto é 5*5/2? ',
        'respostas':{'a':'12.5','b':'12','c':'10','d':'20',},
        'resposta_certa':'a'
    },
    'Pergunta 3':{
        'pergunta':'Quanto estados tem o Brasil? ',
        'respostas':{'a':'20','b':'25','c':'27','d':'26',},
        'resposta_certa':'c'
    },
    'Pergunta 4':{
        'pergunta':'Quanto é 100*25+12? ',
        'respostas':{'a':'3700','b':'2500','c':'2512','d':'3000',},
        'resposta_certa':'c'
    },
    'Pergunta 5':{
        'pergunta':'Quanto é 10+6-5/2? ',
        'respostas':{'a':'13','b':'13.5','c':'5.5','d':'12',},
        'resposta_certa':'b'
    },
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha a opção correta: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Digite a alternativa: ')
    if resposta_usuario == pv['resposta_certa']:
        print('Certa resposta!')
        respostas_certas += 1
    else:
        print('Resposta incorreta!')
    print(' ')

qtd_perguntas = len(perguntas)
porcetagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} resposta(s).')
print(f'Sua porcetagem de acerto foi de {porcetagem_acerto}%.')
