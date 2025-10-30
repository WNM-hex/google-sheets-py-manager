# google-sheets-py-manager
By:WNM-hex
---------------------------------------
terminal:
no mesmo lugar que esta o arquivo "main.py" use cd (change directory)

-adciona o arquivo venv-
vvvvv
python -m venv venv

-ative ele em todo o terminal usado- (ainda será concertado)
vvvvv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1

-o arquivo deve possuir-
vvvvv
venv + main.py + .JSON

(voce deve possuir o nome da planilha do qual voce compartinhou com a conta de serviço que esta no .json)

# requerimentos:
-
nodeJS (last LTS build)
projetoe conta no google cloud (https://console.cloud.google.com)
-------------------------------------------------------------------------------------------------
-
to make your .JSON: IAM & adminn => service accounts => create service account.
                    service accounts => ... (options) => manage keys => create new key => .json
-------------------------------------------------------------------------------------------------
APIS: google cloud: APIs & Services
-Google Docs API					
-Google Drive API					
-Google Sheets API
(other dependencies may apear in errors, just pip install them)
