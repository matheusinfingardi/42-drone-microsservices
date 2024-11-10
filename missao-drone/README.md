my-drone-service/
├── src/
│   ├── adapters/               # Implementações de interfaces da camada de Use Cases
│   │   ├── controllers/
│   │   │   └── connect_controller.py
│   │   └── repositories/
│   │       └── drone_repository.py
│   ├── domain/                 # Entidades e interfaces
│   │   ├── models/
│   │   │   └── drone.py
│   │   ├── repositories/
│   │   │   └── drone_interface.py
│   │   └── usecases/
│   │       └── connect_drone.py
│   ├── infrastructure/         # Dependências externas e configurações
│   │   └── mavsdk_client.py
│   ├── main.py                 # Entry point da aplicação
│   └── settings.py             # Configurações de ambiente
└── Dockerfile                  # Configuração para container Docker
└── render.yaml                 # Configuração para deploy no Render
└── requirements.txt            # Dependências do projeto