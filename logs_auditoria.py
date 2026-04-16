def exibir_logs():
    try:
        with open('logs ocorrencia.txt', 'r', encoding='utf-8') as arquivo:
        conteudo=arquivo.read()
        if conteudo_strip():
            print('logs de ocorrencias')
            print(conteudo)
        else:
            print('Nenhum logs registrado')
        except FileNotFoundError:
            print('Arquivo logs Nao encontrado')
        
def exibir_protocolos():
    protocolos=buscar_procolos_no_banco()
    print('Protocolos de Votação')
    if not protocolos:
        print('Nenhum Protocolo Encontrado')
        return
    for protocolo in sorted(protocolos):
    print(protocolo)
