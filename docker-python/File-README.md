# template Dockerfile para projetos em Python

### Aqui está um passo-a-passo para configurar um Dockerfile para projetos em Python:

1. Criar um novo diretório para o seu projeto: Crie um novo diretório para seu projeto e adicione os seguintes arquivos: * main.py (ou qualquer outro nome para o arquivo principal do seu projeto) * requirements.txt (para especificar as dependências do projeto) * Dockerfile (arquivo que define as configurações para construir a imagem do Docker)

2. Especificar a imagem base: No Dockerfile, comece com a linha FROM python:latest para usar a imagem oficial do Python mais recente como base para sua imagem.

3. Instalar dependências: Use o comando RUN pip install -r requirements.txt para instalar as dependências especificadas no arquivo requirements.txt.

4. Copiar arquivos do projeto: Use o comando COPY . /app para copiar todos os arquivos do diretório atual (incluindo main.py) para a pasta /app dentro da imagem.

5. Definir comando para execução: Use o comando CMD ["python", "main.py"] para definir o comando padrão para executar o container. Nesse caso, o Python executará o arquivo main.py.

6. Salvar e construir a imagem: Salve o Dockerfile e execute o comando docker build -t meu-projeto . para construir a imagem com o nome meu-projeto.

### Exemplo de Dockerfile:

'''PYTHON

FROM python:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"] '''


### Observações:

Substitua meu-projeto pelo nome que você deseja dar à sua imagem.
Certifique-se de que o arquivo requirements.txt está atualizado com as dependências corretas do seu projeto.
Se você tiver arquivos adicionais que precisam ser copiados para a pasta /app, adicione linhas adicionais ao Dockerfile para fazer isso.
Com essas etapas, você criou um Dockerfile básico para um projeto em Python. Agora, você pode construir e executar a imagem com o comando docker run -it meu-projeto.
