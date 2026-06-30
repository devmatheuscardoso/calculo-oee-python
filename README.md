# 📊 Calculadora de OEE em Python

Um terminal interativo simples e direto desenvolvido em Python para automatizar o cálculo do **OEE (Eficiência Global do Equipamento)** em turnos de produção industrial.

O objetivo deste projeto foi traduzir as métricas de negócio do chão de fábrica para uma lógica de programação limpa, facilitando a tomada de decisão rápida.

## ⚙️ Como Funciona?

O script solicita 5 dados básicos do turno:
1. Tempo total planejado (minutos)
2. Tempo de paradas/falhas (minutos)
3. Meta de produção (peças)
4. Total de peças produzidas (boas + ruins)
5. Quantidade de refugos (peças rejeitadas)

Com isso, ele processa e entrega os 3 pilares do OEE:
* **Disponibilidade** ⏱️
* **Performance** 🚀
* **Qualidade** 🛡️

E gera o **OEE Global do Turno** formatado na tela.

## 🚀 Como Executar

Você só precisa ter o Python instalado na sua máquina (não requer nenhuma biblioteca externa).

1. Baixe o arquivo `main.py`
2. Abra o terminal na pasta do arquivo e execute:
```bash
python main.py
