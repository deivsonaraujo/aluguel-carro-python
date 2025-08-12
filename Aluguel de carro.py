print("======Aluguel de carro=======")

while True:
    try:
        c = int(input("Total de dias alugados: "))
        km = float(input("Quantos KM foram rodados: "))
        if c > 0 and km > 0:
            break
        print("Digite valores positivos!")
    except ValueError:
        print("Digite apenas números!")

pago = (c * 60) + (km * 0.50)
print(f"Você ficou {c} dias com o automóvel e rodou por {km}KM. O total a ser pago é R${pago:.2f}")

import sys

pagamento = input("Digite a numeração correspondente a forma de pagamento:\n 1 - Cartão\n 2 - Pix\n Digite... ")

if not pagamento.isdigit():
    print("Opção inválida! Encerrando sessão.")
    sys.exit()

pagamento = int(pagamento)

if pagamento == 1:
    opcao = input("Será débito ou crédito: ").lower()
    if opcao in ["débito", "debito"]:
        opcao1 = input("Aproximação ou inserir: ").lower()
        if opcao1 in ["aproximação", "aproximaçao", "aproximacao"]:
            print("Aproxime!")
            print("Pagamento realizado! Sessão encerrada.")
        elif opcao1 == "inserir":
            senha = input("Digite a senha: ")
            print("Pagamento autorizado! Encerrado.")
        else:
            print("Opção inválida. Encerrando!")
            sys.exit()

    elif opcao in ["crédito", "credito"]:
        opcao2 = input("Aproximação ou inserir: ").lower()
        if opcao2 in ["aproximacao", "aproximaçao", "aproximação"]:
            print("Aproxime!")
            print("Pagamento realizado! Sessão encerrada.")
        elif opcao2 == "inserir":
            senha = input("Digite a senha: ")
            print("Pagamento autorizado! Sessão encerrada.")
        else:
            print("Tipo de cartão inválido. Sessão encerrada.")
            sys.exit()

elif pagamento == 2:
    pix = input("Faça o Pix e confirme quando feito com 'OK': ").upper()
    if pix == "OK":
        print("Transação confirmada. Até a próxima!")
    else:
        print("Confirmação inválida. Encerrando!")
        sys.exit()

else:
    print("Forma de pagamento inválida. Encerrando a sessão.")
    sys.exit()