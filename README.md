# Estrutura do Projeto com Clean Architecture
Vamos adotar a seguinte estrutura de pastas para o projeto, seguindo os princípios da Clean Architecture:

```python
/missao-drone
    /src
        /core
            __init__.py
            models.py              # Entidades e classes de domínio
            mission.py             # Entidades de missão, comandos, etc.
            weather.py             # Entidade relacionada ao clima
        /use_cases
            __init__.py
            mission_manager.py     # Lógica de gestão de missão (caso de uso)
        /interfaces
            __init__.py
            api.py                 # API REST (Flask/FastAPI) ou outros pontos de entrada
            mavsdk_controller.py   # Interface de comunicação com o MAVSDK (driver)
            weather_api.py         # Interface para a API de meteorologia
        /infrastructure
            __init__.py
            mavsdk_driver.py       # Implementação de comunicação com o MAVSDK
            weather_api_client.py  # Implementação de chamada para API externa
        /tests
            __init__.py
            test_mission_manager.py
            test_mavsdk_driver.py
            test_weather_api_client.py
    requirements.txt
    main.py
    Dockerfile
    .env
```
<br>
<br>
  
# Explicação de Cada Pasta e Arquivo

<br>
<br>

## /core
Aqui ficam as entidades e modelos de domínio.  
Elas são responsáveis por representar o estado e comportamento do sistema. Não devem depender de qualquer outra camada, como infraestrutura ou framework de API.

**models.py:** Contém as classes e modelos principais do domínio do sistema, como as entidades Mission e Weather.

### Exemplo:
```python
# src/core/models.py

class Mission:
    def __init__(self, start_lat, start_lon, end_lat, end_lon, altitude):
        self.start_lat = start_lat
        self.start_lon = start_lon
        self.end_lat = end_lat
        self.end_lon = end_lon
        self.altitude = altitude

class Weather:
    def __init__(self, temperature, wind_speed, conditions):
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.conditions = conditions
```

<br>
<br>

## /use_cases
Essa camada contém a lógica de aplicação ou casos de uso.  
Ela deve orquestrar a execução do sistema, chamando as interfaces para interagir com o domínio e a infraestrutura.  

**mission_manager.py:** Contém a lógica para gerir a missão (e.g., iniciar a missão, controlar o drone, verificar o clima, etc).

### Exemplo:
```python
# src/use_cases/mission_manager.py
from src.interfaces.mavsdk_controller import MAVSDKController
from src.interfaces.weather_api import WeatherAPI
from src.core.models import Mission, Weather

class MissionManager:
    def __init__(self, mavsdk_controller: MAVSDKController, weather_api: WeatherAPI):
        self.mavsdk_controller = mavsdk_controller
        self.weather_api = weather_api

    def start_mission(self, mission: Mission):
        weather_start = self.weather_api.get_weather(mission.start_lat, mission.start_lon)
        weather_end = self.weather_api.get_weather(mission.end_lat, mission.end_lon)

        # Se necessário, logica para alterar a missão com base no clima
        if weather_start.temperature < 0:
            print("Clima ruim, missão adiada")
            return

        # Lógica de controle de voo
        self.mavsdk_controller.arm_and_takeoff(mission.altitude)
        self.mavsdk_controller.go_to(mission.end_lat, mission.end_lon, mission.altitude)
        print(f"Missão concluída de {mission.start_lat}, {mission.start_lon} para {mission.end_lat}, {mission.end_lon}")
```
<br>
<br>

## /interfaces
Aqui ficam as interfaces de comunicação com o sistema.  
Isso pode incluir controladores de APIs REST, interfaces com o MAVSDK ou com APIs externas (como a de meteorologia).

**api.py:** Exposição da API REST usando Flask ou FastAPI. Serve como camada de entrada para interagir com a aplicação.

### Exemplo com FastAPI:
```python
# src/interfaces/api.py
from fastapi import FastAPI
from pydantic import BaseModel
from src.use_cases.mission_manager import MissionManager
from src.interfaces.mavsdk_controller import MAVSDKController
from src.interfaces.weather_api import WeatherAPI
from src.core.models import Mission

app = FastAPI()

class MissionRequest(BaseModel):
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float
    altitude: float

@app.post("/start_mission")
async def start_mission(request: MissionRequest):
    mavsdk_controller = MAVSDKController()
    weather_api = WeatherAPI()
    mission_manager = MissionManager(mavsdk_controller, weather_api)

    mission = Mission(
        start_lat=request.start_lat,
        start_lon=request.start_lon,
        end_lat=request.end_lat,
        end_lon=request.end_lon,
        altitude=request.altitude
    )
    
    mission_manager.start_mission(mission)
    return {"message": "Missão iniciada"}
```

**mavsdk_controller.py e weather_api.py:** Contêm a interface de comunicação com o MAVSDK e a API de Meteorologia, respectivamente.
<br>
Essas classes vão interagir com a camada de infraestrutura.

## /infrastructure
Aqui ficam as implementações concretas para as interfaces definidas nas camadas superiores.  
As classes dessa camada implementam as interações reais com serviços como o MAVSDK e APIs externas.

**mavsdk_driver.py:** Implementação concreta de interação com o MAVSDK.

### Exemplo:
```python
# src/infrastructure/mavsdk_driver.py
from mavsdk import System

class MAVSDKController:
    def __init__(self):
        self.drone = System()

    def connect(self, connection_url="udp://:14540"):
        self.drone.connect(system_address=connection_url)

    def arm_and_takeoff(self, altitude):
        # Lógica de armamento e decolagem
        pass

    def go_to(self, lat, lon, alt):
        # Lógica de navegação do drone
        pass
```

**weather_api_client.py:** Implementação da chamada à API de meteorologia.

### Exemplo:
```python
# src/infrastructure/weather_api_client.py
import requests

class WeatherAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, latitude, longitude):
        response = requests.get(self.base_url, params={
            "lat": latitude,
            "lon": longitude,
            "appid": self.api_key
        })
        return response.json()
```

<br>
<br>

## /tests
Aqui ficam os testes unitários e de integração para o seu microsserviço.  
Cada classe ou módulo terá seus testes específicos para garantir o comportamento esperado.  

**test_mission_manager.py:** Testes para o caso de uso de gestão de missão.
**test_mavsdk_driver.py:** Testes para a comunicação com o MAVSDK.
**test_weather_api_client.py:** Testes para a integração com a API de meteorologia


# Configuração e Variáveis de Ambiente
Na raiz do projeto, você terá o arquivo .env que pode armazenar informações sensíveis como API keys ou configurações do banco de dados.

```python
# .env
WEATHER_API_KEY="sua-chave-de-api"
MAVSDK_URL="udp://:14540"
```


Além disso, você pode configurar o arquivo requirements.txt para listar todas as dependências do seu projeto:
```
fastapi
uvicorn
mavsdk
requests
python-dotenv
```

# Dockerfile (se necessário)
Aqui está um exemplo básico de Dockerfile para criar uma imagem Docker do seu microsserviço.


```
# Dockerfile

# Imagem base
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar arquivos de requisitos e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código para o container
COPY ./src /app

# Expor a porta do servidor FastAPI (ou Flask)
EXPOSE 8000

# Iniciar a aplicação com Uvicorn
CMD ["uvicorn", "src/interfaces/api:app", "--host", "0.0.0.0", "--port", "8000"]

```

# Passo 8: Main (Iniciar a Aplicação)
Se você estiver usando FastAPI (ou Flask), o arquivo main.py será o ponto de entrada para o servidor.

```python
# main.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.interfaces.api:app", host="0.0.0.0", port=8000, reload=True)

```
