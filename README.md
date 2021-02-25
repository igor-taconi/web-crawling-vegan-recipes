# Web Crawler Vegan Recipes

Um Crawler diversos sites de culinária para obter o título, a imagem, os ingredientes, o modo de preparo, o tempo de preparo e o link da página, de receitas vegas

## Pré-requisitos
Para você rodar o projeto é necessário tem instalado em sua máquina o `Python3.6+`.

## Como rodar esse projeto
-   ### Clone esse repositório.
```
git clone https://github.com/igor-taconi/web-crawling-vegan-recipes.git
```
-   ### Crie um virtualenv com Python 3.
```
cd web-crawling-vegan-recipes
python -m venv .venv
```
-   ### Ative o virtualenv.
```
source .venv/bin/activate
```
-   ### Instale as dependências.
```
pip install -r requirements.txt
```
-   ### Rode o prjeto.  
##### Obtenha uma lista de todos os spiders disponíveis:
```
scrapy list
```
###### Execute o spider com o nome `spider_name`:
```
scrapy crawl tudogostoso
```

## Dados
Após o script terminar sua execução aparecerá um arquivo _recipes.db_.  
Você pode entrar no site [SQL Online IDE](https://sqliteonline.com/) para visualizar o arquivo ou baixar o [DB Browser for SQLite](https://sqlitebrowser.org/dl/) em sua máquina, ou usar da forma que quiser.

## Contribuindo
Sinta-se à vontade para crair novos spiders ou corrigir ao no projeto e enviar pull requests.
