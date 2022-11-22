menu = 'MENU'
print('{:^20}'.format(menu))

print('(0) - Apresentação formal')
print('(1) - O que você quer fazer pelo mundo?')
print('(2) - Conta pra gente um desafio que você superou '
            'e um ponto forte que te ajudou a lidar com ele?')
print('(3) - O que te inspira no seu dia-dia de trabalho/estudo?')


opcao = int(input('Selecione uma opção: '))

if opcao == 0:
    print('Me chamo Railene')
    if opcao == 1:
        print('Me desafiar a cada dia e buscar conhecimento, isso inclui ser autodidata,'
              'pra área de TI é essencial; e ao estar apta a me introduzir no mercado,'
              'será um grande ganho como pessoa e futura profissional.')
        if opcao == 2:
            print('Não imaginava estudar para TI, mas me encontrei na área, qando iniciei'
                  'estudos de lógica de programação e algoritmos foi um desafio aprender'
                  'vetores, o que me ajudou a superá-lo foi rever a aula, buscar outras fontes'
                  'no google, fazer exercícios primeiramente rabiscando no caderno e em seguida'
                  'colocando a mão na massa no VisualG.')
            if opcao == 3:
                print('Bater cabeça para resolver um problema até encontrar uma solução'
                        'não é muito fácil, mas após isso é recompensador enxergar que superei'
                        'uma dificuldade e que com paciência é possível aprender.')

