# WiSense Architecture

## Objetivo

O WiSense é uma plataforma experimental para pesquisa em Wi-Fi Sensing.

O projeto busca detectar alterações no ambiente utilizando variações da intensidade do sinal Wi-Fi (RSSI), inicialmente por meio de simulação e futuramente utilizando captura real de dados.

---

# Fluxo do Sistema

Signal Simulator
        │
        ▼
Signal Sample
        │
        ├────────► CSV Exporter
        │
        ├────────► Dashboard
        │
        └────────► Detector

---

# Módulos

## simulation

Responsável por gerar amostras artificiais de RSSI.

---

## models

Representa os objetos do sistema.

Atualmente:

- SignalSample

---

## detector

Algoritmos de detecção de movimento.

Inicialmente:

- ThresholdDetector

No futuro:

- Machine Learning Detector

---

## dashboard

Visualização em tempo real.

---

## exporters

Exportação para CSV.

---

## Futuro

- Captura real do Wi-Fi
- Banco de dados
- API REST
- Dashboard Web
- Inteligência Artificial