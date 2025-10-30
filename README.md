# Experimentos com o Garoa Badge

Repositório para compartilhar os experimentos com o [Garoa Badge](https://garoa.net.br/wiki/Badge#REV._0) usando MicroPython.

## Exibindo QR code

A pasta `qrcode-generator` contém um projeto Python (gerenciado pelo `uv`) para a criação de QR codes a partir de URLs, salvando no formato `.pbm` (P4).

O formato `.pbm` é indicado para a exibição de imagens em displays OLED pois é possível criar imagens monocromáticas usando pouco espaço de armazenamento.

No modo P4, os bits da imagem são empacotados em bytes, tornando o arquivo menor e evitando estourar a memória do ESP8266.

### Estrutura do Projeto

```
├── micropython
│   ├── main.py          # Código principal para rodar no ESP8266
│   └── qr-code.pbm      # Imagem PBM gerada (QR Code)
├── qrcode-generator
│   ├── create_qrcode.py # Script Python para gerar o QR Code
│   ├── pyproject.toml   # Configuração do projeto (usando uv)
│   └── uv.lock          # Lockfile do uv
└── README.md
```

### 1. Gerar o QR Code com `uv`

Dentro da pasta `qrcode-generator`, o script `create_qrcode.py` gera o arquivo `qr-code.pbm` no formato PBM (P4).

Utilize o `uv` para instalar as dependências e executar o arquivo:

```
cd qrcode-generator
uv sync
uv run create_qrcode.py
````

Isso irá gerar o arquivo `qr-code.pbm`.  

### 2. Enviar os arquivos para o ESP8266

Certifique-se de que o ESP8266 já esteja com MicroPython gravado.

Caso não esteja, siga as instruções da [documentação do MicroPython](https://micropython.org/download/?port=esp8266).

Para acessar o REPL da placa e gerenciar os arquivos, utilize o `mpremote` [(instruções para instalação)](https://docs.micropython.org/en/latest/reference/mpremote.html).


#### Usando `mpremote`

Conecte o adaptador FTDI no Garoa Badge e execute:

```
cd micropython
mpremote cp main.py :
mpremote cp qr-code.pbm :
```

O `mpremote` deverá reconhecer a porta serial automaticamente, caso tenha apenas um dispositivo conectado no computador.

### 3. Executar no ESP8266

Depois que os arquivos estiverem copiados, o ESP8266 executará automaticamente o `main.py` na inicialização.

Também é possível reiniciar a placa via `mpremote` com o comando `mpremote reset`.

O arquivo disponível nesse repositório possui três modos:
- Exibição de nome completo (default): aperte o botão prog
- Exibição de @: aperte o botão up
- Exibição do QR code: aperte o botão down

Você pode escanear com a câmera do celular — ele deve abrir o link configurado no script `create_qrcode.py`.

