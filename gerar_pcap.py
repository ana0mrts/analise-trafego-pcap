from scapy.all import IP, TCP, Raw, wrpcap
import random

pacotes = []
ip_atacante = "192.168.1.105"
ip_vitima = "10.0.0.15"

print("Gerando o scan de portas...")

for porta in range(1, 101):
    porta_origem = random.randint(1024, 65535)
    p_syn = IP(src=ip_atacante, dst=ip_vitima) / TCP(sport=porta_origem, dport=porta, flags="S")
    pacotes.append(p_syn)
    
    if porta == 22 or porta == 80:
        p_resposta = IP(src=ip_vitima, dst=ip_atacante) / TCP(sport=porta, dport=porta_origem, flags="SA")
    else:
        p_resposta = IP(src=ip_vitima, dst=ip_atacante) / TCP(sport=porta, dport=porta_origem, flags="RA")
    
    pacotes.append(p_resposta)

print("Gerando o ataque no SSH...")

for i in range(50):
    porta_origem = random.randint(1024, 65535)
    p1 = IP(src=ip_atacante, dst=ip_vitima) / TCP(sport=porta_origem, dport=22, flags="S")
    p2 = IP(src=ip_vitima, dst=ip_atacante) / TCP(sport=22, dport=porta_origem, flags="SA")
    p3 = IP(src=ip_atacante, dst=ip_vitima) / TCP(sport=porta_origem, dport=22, flags="A")
    p_dados = IP(src=ip_atacante, dst=ip_vitima) / TCP(sport=porta_origem, dport=22, flags="PA") / Raw(load="Failed password for root")
    
    pacotes.append(p1)
    pacotes.append(p2)
    pacotes.append(p3)
    pacotes.append(p_dados)

wrpcap("meu_teste_ataque.pcap", pacotes)
print("Pronto! Arquivo meu_teste_ataque.pcap criado.")