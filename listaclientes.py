import pandas as pd

def formatar_telefone(telefone):
    telefone_limpo = ''.join(filter(str.isdigit, str(telefone)))
    if len(telefone_limpo) >= 11:
        telefone_limpo = telefone_limpo[1:]
    
    return f"55{telefone_limpo}"

arquivo_excel = "clientes.xlsx"
tabela = pd.read_excel(arquivo_excel)

print(tabela.columns)

with open("saida.txt", "w", encoding="utf-8") as arquivo_saida:
    for index, linha in tabela.iterrows():
        telefone_formatado = formatar_telefone(linha['telefone'])
        nome = f'"{linha["nome"]}"'
        cpf = f'"{linha["cpf"]}"'
        endereco = f'"{linha["endereço"]}"'
        cep = f'"{linha["cep"]}"'
        cidade = f'"{linha["cidade"]}/{linha["estado"]}"'
        
        linha_formatada = f"{telefone_formatado},{nome},{cpf},{endereco},{cep},{cidade}"
        
        arquivo_saida.write(linha_formatada + "\n")

print("Arquivo de saída gerado com sucesso: saida.txt")
