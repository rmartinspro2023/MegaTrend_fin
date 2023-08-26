# Projeto ETL MegaTrend_fin 
Este é um exemplo de um processo ETL (Extração, Transformação e Carga) para coletar informações financeiras

## Requisitos
Python 3.x
Biblioteca requests para fazer chamadas à API
Biblioteca csv para manipulação de arquivos CSV
## Passos do ETL
### 1. Extração
A extração é realizada utilizando a API pública da yahoo finance. O script faz uma chamada à API para obter informações sobre as cotações dos ativos listados em um csv.

### 2. Transformação
A transformação envolve o cálculo da média 20 periodos do ativo selecionado, e com base na ultima cotação compara se está abaixo ou acima da média.
Sendo acima da média = Movimento com tendencia altista
Sendo abaixo da média = Movimento com tendencia baixista

### 3. Carga
A carga envolve o carregamento dos dados em um arquivo CSV.

## Executando o ETL
Certifique-se de ter Python 3.x instalado.
Instale as bibliotecas necessárias executando pip install requests e pip install csv.
Execute o script index.py.
## Resultados
Após a execução bem-sucedida do ETL, os dados referente ao ativo e qual sua tendencia serão carregados no arquivo CSV result.csv.
