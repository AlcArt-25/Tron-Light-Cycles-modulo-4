# 🏍️ Tron Light Cycles - Arcade Edition

Juego de motos de luz estilo **TRON** para dos jugadores, desarrollado utilizando el **Arcade Machine SDK**. Este proyecto forma parte del trabajo integrador para la materia *Taller de Objetos y Abstracción de Datos*.

---

## 🎮 Características

* **Dos modos de juego:** * *Clásico:* La experiencia pura de TRON.
    * *Arcade:* Incluye obstáculos dinámicos y estela desvaneciente.
* **Personalización:** Controles configurables para ambos jugadores.
* **Ambiente Sonoro:** Música dinámica (aleatoria en menús, dos pistas distintas en partida) y efectos de sonido para colisiones, botones y Game Over.
* **Estética Visual:** Interfaz retro con sprites detallados y efectos de neón.

---

## 📋 Requisitos

Asegúrate de tener instalado lo siguiente antes de ejecutar el juego:

* **Python:** 3.11 o superior
* **Pygame:** 2.6.0 o superior
* **Arcade Machine SDK**

---

## 🚀 Instalación Rápida

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/tron-light-cycles.git](https://github.com/tu-usuario/tron-light-cycles.git)
   cd tron-light-cycles
   exit
   
2. **Instalacion de dependencias**
    ```bash
    pip install -r requirements.txt

3. **Ejecutar el juego**
   ```bash
   python game.py
[!NOTE]

El juego es totalmente compatible para ejecutarse dentro del ecosistema de la máquina arcade principal del SDK.

🎯 Cómo Jugar
El objetivo es sobrevivir más tiempo que tu oponente. Evita chocar con las paredes, tu propia estela, la del rival y los obstáculos del modo arcade.

Jugador 1 
W A S D

Jugador 2
↑ ↓ ← →

Pausa,P
Debug Mode,F3

📁 Estructura del Proyecto
tron_game/
├── assets/          # Imágenes, sonidos y fuentes tipográficas
├── states/           # Gestión de estados (menú, partida, créditos)
├── game.py           # Punto de entrada principal
├── player.py         # Lógica y comportamiento de las motos
├── settings.py       # Constantes y configuraciones globales
└── ...

👥 Créditos - Grupo 4
Victor Alcala
Ricardo Trevison

TOAD sec: 20


<div align="center">
