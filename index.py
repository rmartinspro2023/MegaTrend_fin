
!pip install yfinance -q
import yfinance as yf
import pandas as pd


# Carregar os tickers do arquivo CSV
def load_tickers_from_csv(file_path):
    tickers = []
    with open(file_path, 'r') as file:
        for line in file:
            tickers.append(line.strip())
    return tickers
  
# Calcular a média móvel de 20 períodos
def calculate_20_period_sma(data):
   return data['Close'].rolling(window=20).mean()

# Obter a tendência com base na média móvel
def get_trend(closing_price, sma_20):
    if closing_price > sma_20:
        return 'Tendência de Alta'
    else:
        return 'Tendência de Baixa'
      
# Oter dados historicos do ativo
def HistoricoTicker(ticket):
  avgtrend = yf.Ticker(ticket)
  hist = avgtrend.history(period="60")
  return hist


# Definir o caminho do arquivo CSV e a data de hoje
csv_file_path = 'tickers.csv'  # Substitua pelo caminho do seu arquivo CSV
today = pd.Timestamp.today().strftime('%Y-%m-%d')

# Carregar os tickers do arquivo CSV
tickers = load_tickers_from_csv(csv_file_path)

# Coletar dados históricos e calcular a média móvel de 20 períodos para cada ticker
data = {'Ticker': [], 'Avg': [], 'Date': [], 'Trend': []}



for ticker in tickers:
  # EXTRACT
  dataTicker = HistoricoTicker(ticker)
  
  # Transform
  sma20 = calculate_20_period_sma(dataTicker)
  last_close_price = dataTicker['Close'][-1]
  trend = get_trend(last_closing_price,sma20[-1])

  # Load
  data['Ticker'].append(ticker)
  data['Avg'].append(sma20[-1])
  data['Date'].append(today)
  data['Trend'].append(trend)

# Criação de DataFrame com os dados transformados
  result_df = pd.DataFrame(data)
  result_df.to_csv(output_csv_path, index=False)
  
# Carregar tickers do arquivo CSV
tickers_list = load_tickers_from_csv(input_csv_path)

# Executar o pipeline ETL
etl_pipeline(tickers_list, output_csv_path)

print("ETL pipeline concluído. Resultados salvos em", output_csv_path)
