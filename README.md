# Validador de Arquivos JSON

## Descrição

Este projeto é uma ferramenta para validar arquivos JSON enviados por cartórios, garantindo que as propriedades dos imóveis estejam no formato correto. Desenvolvido por mim, enquanto trabalhava no ONR (Operador Nacional do Sistema do Registro Eletrônico de Imóveis), o projeto visa agilizar e facilitar o troubleshooting dos arquivos enviados pelos cartórios de todo o Brasil.

## Funcionalidades

- Validação de campos obrigatórios e opcionais.
- Detecção de erros de tipo e ausência de campos.
- Suporte para diferentes codificações de arquivo.

## Campos Validados

### Campos Obrigatórios
Os seguintes campos são obrigatórios e devem estar presentes e no formato correto em cada registro de imóvel:
- `TIPOENVIO`: Tipo de envio (número inteiro).
- `NUMERO_REGISTRO`: Número do registro (string).
- `REGISTRO_TIPO`: Tipo de registro (número inteiro).
- `LOCALIZACAO`: Localização (número inteiro).
- `TIPO_LOGRADOURO`: Tipo de logradouro (número inteiro).
- `NOME_LOGRADOURO`: Nome do logradouro (string).
- `UF`: Unidade Federativa (número inteiro).
- `CIDADE`: Cidade (número inteiro).
- `CNS`: Identificador do cartório (string).

### Campos Opcionais
Os seguintes campos são opcionais, podendo ou não estar presentes, e devem estar no formato correto quando incluídos:
- `TIPO_DE_IMOVEL`: Tipo de imóvel (string).
- `NUMERO_LOGRADOURO`: Número do logradouro (string).
- `BAIRRO`: Bairro (string).
- `CEP`: CEP (string).
- `COMPLEMENTO`: Complemento (string).
- `QUADRA`: Quadra (string).
- `CONJUNTO`: Conjunto (string).
- `SETOR`: Setor (string).
- `LOTE`: Lote (string).
- `LOTEAMENTO`: Loteamento (string).
- `CONTRIBUINTE`: Contribuinte (lista).
- `RURAL`: Informações rurais (dicionário).
- `CONDOMINIO`: Informações do condomínio (dicionário).
