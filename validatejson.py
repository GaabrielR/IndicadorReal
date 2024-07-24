import json
import chardet

def validar_propriedade_real(propriedade):
    campos_obrigatorios = {
        "TIPOENVIO": int,
        "NUMERO_REGISTRO": str,
        "REGISTRO_TIPO": int,
        "LOCALIZACAO": int,
        "TIPO_LOGRADOURO": int,
        "NOME_LOGRADOURO": str,
        "UF": int,
        "CIDADE": int
    }

    campos_opcionais = {
        "TIPO_DE_IMOVEL": str,
        "NUMERO_LOGRADOURO": str,
        "BAIRRO": str,
        "CEP": str,
        "COMPLEMENTO": str,
        "QUADRA": str,
        "CONJUNTO": str,
        "SETOR": str,
        "LOTE": str,
        "LOTEAMENTO": str,
        "CONTRIBUINTE": list,
        "RURAL": dict,
        "CONDOMINIO": dict
    }

    erros = []

    for campo, tipo_campo in campos_obrigatorios.items():
        if campo not in propriedade:
            erros.append(f"Campo obrigatório ausente: {campo}")
        elif not isinstance(propriedade[campo], tipo_campo):
            erros.append(f"Campo {campo} deveria ser do tipo {tipo_campo.__name__}.")

    for campo, tipo_campo in campos_opcionais.items():
        if campo in propriedade and not isinstance(propriedade[campo], tipo_campo):
            erros.append(f"Campo {campo} deveria ser do tipo {tipo_campo.__name__}.")

    return erros

def validar_json(dados):
    if "INDICADOR_REAL" not in dados or "CNS" not in dados["INDICADOR_REAL"]:
        return ["CNS ausente ou erro na lista de imóveis."]

    if not isinstance(dados["INDICADOR_REAL"]["CNS"], str):
        return ["Campo CNS deveria ser do tipo string."]

    erros = []

    for propriedade in dados["INDICADOR_REAL"]["REAL"]:
        erros_propriedade = validar_propriedade_real(propriedade)
        if erros_propriedade:
            numero_registro = propriedade.get('NUMERO_REGISTRO', 'desconhecida')
            erros.append(f"\nErro no registro da matrícula {numero_registro}:")
            erros.extend(erros_propriedade)

    return erros

def detectar_codificacao(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as arquivo:
        dados_brutos = arquivo.read()
        resultado = chardet.detect(dados_brutos)
        return resultado['encoding']

def main():
    caminho_arquivo = input("Por favor, insira o caminho do arquivo JSON: ")

    try:
        codificacao = detectar_codificacao(caminho_arquivo)
        # print(f"Codificação detectada: {codificacao}")

        with open(caminho_arquivo, 'r', encoding=codificacao) as arquivo:
            dados = json.load(arquivo)

        erros = validar_json(dados)

        if erros:
            print("Erros encontrados no arquivo JSON:")
            for erro in erros:
                print(erro)
        else:
            print("O arquivo JSON está correto.")
    except json.JSONDecodeError as e:
        linha, coluna = e.lineno, e.colno
        print(f"Ocorreu um erro ao ler o arquivo JSON na linha {linha}, coluna {coluna}: {e.msg}.")
    except UnicodeDecodeError as e:
        print(f"Ocorreu um erro de decodificação do arquivo JSON: {e}.")
        print("Verifique se o arquivo está no formato UTF-8. Pode ser necessário converter o arquivo para UTF-8.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}.")

    input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()
