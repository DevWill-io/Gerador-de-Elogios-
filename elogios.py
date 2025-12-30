import random

elogios = ["gentil", "bom", "fiel", "puro", "doce", "leal", "raro", "belo", "luz", "paz", "real", "nato", "vivo", "leve", "sutil", "fino", "sábio", "justo", "noite", "claro", "nato", "único", "firme", "hábil", "capaz", "limpo", "bravo", "grato", "forte", "mimo"]

# Primeiro elogio automático
vc = random.choice(elogios)
print(f'Você é {vc}')

# Variável de controle para o loop
continuar = True

while continuar:
    dn = input('\nQuer outro elogio? (sim/não): ').lower()

    if 'sim' in dn:
        vc = random.choice(elogios)
        print(f'Você é {vc}!')
    else:
        print('Poxa, tudo bem. Até a próxima! 👋')
        continuar = False # Isso quebra o loop
