from datetime import datetime


def registrar_log(mensagem):
  
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs ocorrencia.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{data_hora}] {mensagem}\n")


#--------------------------------------------------------------------------


def exibir_logs():
    try:
        with open('logs ocorrencia.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

            if conteudo.strip():
                print('\n=== LOGS DE OCORRÊNCIAS ===')
                print(conteudo)
            else:
                print('Nenhum log registrado.')

    except FileNotFoundError:
        print('Arquivo de logs não encontrado.')


def exibir_protocolos():
    print('\n=== PROTOCOLOS DE VOTAÇÃO ===')
    print('Funcionalidade ainda não implementada.')
