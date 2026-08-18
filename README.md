# Lab de Análise de Tráfego: Identificando Port Scan e Brute Force com Scapy e TShark

Este repositório documenta um laboratório prático que montei para entender, na prática, como ataques de **reconhecimento (Port Scan)** e **força bruta (SSH)** se comportam na camada de rede, além de como extrair evidências usando ferramentas de linha de comando.
---
## Objetivo do Estudo
* Criar e manipular pacotes de rede usando **Python (`Scapy`)**.
* Analisar arquivos de captura `.pcap` via linha de comando com o **TShark**.
* Identificar padrões de comportamento malicioso (flags TCP, volume e portas).
---
## Tecnologias Utilizadas
* **Python 3** + biblioteca **Scapy** (para geração de tráfego)
* **TShark / Wireshark** (para inspeção de pacotes)
* **PowerShell / VS Code** (ambiente de execução)
---
## Passo a Passo do Laboratório

### 1. Geração do Arquivo PCAP
Escrevi o script `gerar_pcap.py` para simular dois cenários em uma captura única:
1. **Varredura de Portas (Port Scan):** Envio de pacotes TCP SYN sequenciais para as portas 1 a 100 da máquina alvo.
2. **Ataque no SSH:** Simulação de múltiplas tentativas de conexão e envio de payloads na porta 22/TCP.

Para rodar o script e gerar o arquivo de captura:
```powershell
python gerar_pcap.py
