# HydroAlert AI

Sistema academico de alerta preditivo de inundacoes urbanas com IoT, NoSQL, Data Science, BI e IA.

## Etapa 1 - Simulacao de sensores

Nesta etapa o projeto gera telemetria hidrometeorologica simulada para Goiania/GO.

Os sensores virtuais produzem:

- chuva em mm;
- nivel da agua em metros;
- variacao do nivel;
- tendencia;
- cotas de atencao, alerta e critica;
- classificacao de risco;
- data/hora;
- localizacao simulada;
- status do sensor.

Os dados sao gravados em `data/telemetria.jsonl`.

> Importante: os pontos, coordenadas e medicoes desta etapa sao simulados e servem apenas para fins academicos.

## Requisitos

- Windows 10/11
- Python 3.10 ou superior
- Visual Studio Code
- Extensao Python da Microsoft para o VS Code

## Como executar no VS Code

### 1. Clonar a branch do projeto

```bash
git clone -b hydroalert-ai https://github.com/Abnerrum/Projeto_Integrador01.git
```

### 2. Entrar na pasta

```bash
cd Projeto_Integrador01/HydroAlert-AI
```

### 3. Criar ambiente virtual

No PowerShell do VS Code:

```powershell
python -m venv .venv
```

### 4. Ativar ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativacao, use o Prompt de Comando do VS Code:

```cmd
.venv\Scripts\activate.bat
```

### 5. Instalar dependencias

A Etapa 1 nao usa bibliotecas externas, mas o comando pode ser executado normalmente:

```bash
pip install -r requirements.txt
```

### 6. Executar 10 ciclos de teste

```bash
python -m iot.sensor_simulator --ciclos 10
```

### 7. Executar continuamente

```bash
python -m iot.sensor_simulator
```

Para parar, pressione `Ctrl + C`.

## Execucao rapida no Windows

Tambem e possivel executar:

```text
run_etapa1.bat
```

O arquivo realiza 10 ciclos de simulacao.

## Exemplo de saida

```text
GYN-SIM-001 | Chuva: 8.42 mm | Nivel: 1.153 m | Tendencia: SUBINDO | Risco: BAIXO
GYN-SIM-002 | Chuva: 0.00 mm | Nivel: 0.987 m | Tendencia: DIMINUINDO | Risco: BAIXO
GYN-SIM-003 | Chuva: 21.60 mm | Nivel: 1.402 m | Tendencia: SUBINDO_RAPIDAMENTE | Risco: BAIXO
```

## Estrutura atual

```text
HydroAlert-AI/
├── data/
│   └── .gitkeep
├── iot/
│   ├── __init__.py
│   ├── config.py
│   └── sensor_simulator.py
├── .gitignore
├── requirements.txt
├── run_etapa1.bat
└── README.md
```

## Proxima etapa

A Etapa 2 adicionara:

- Eclipse Mosquitto;
- protocolo MQTT;
- Paho MQTT;
- publisher dos sensores;
- subscriber para validar o recebimento da telemetria.
