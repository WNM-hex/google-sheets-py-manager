import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

#sempre ativar o venv na pasta para começar a usar: terminal :
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#  .\venv\Scripts\Activate.ps1

# Credenciais e acesso
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('.json file name', scope)
client = gspread.authorize(creds)

# Abrir planilha pelo nome
sheet = client.open("sheets name").sheet1

# Ler  e printar todos os dados
data = sheet.get_all_records()
df = pd.DataFrame(data)
print(df)
