# 🎮 Project 2 — Minesweeper Game (Functional Programming)

**Author:** Filippo da Costa Bortoli  
**IST ID:** ist1106103  
**Email:** filippo.bortoli@tecnico.ulisboa.pt  
**Date:** 10/11/2022  

---

## 🧠 Overview

This project is a complete implementation of the **Minesweeper** game in Python, written in a functional programming style.  
It introduces **custom data abstractions**, **pseudorandom number generation**, and **recursive field logic** — all without using external libraries.

---

## ⚙️ Main Features

| Component | Description |
|------------|-------------|
| **Xorshift RNG** | A deterministic pseudo-random number generator (32/64-bit). |
| **Coordinates** | Representation and validation of board positions (e.g., `"B07"`). |
| **Parcels (Cells)** | Data abstraction for field cells (hidden, marked, clean, mined). |
| **Field (Board)** | Dictionary mapping coordinates to parcel states. |
| **Game Logic** | Includes mine placement, recursive reveal, and victory detection. |

---

## 🧩 Core Modules

### 1️⃣ Random Number Generator — Xorshift

Implements a 32-bit or 64-bit **Xorshift generator** for reproducible randomness.

| Function | Description |
|-----------|-------------|
| `cria_gerador(bits, seed)` | Creates a generator with a given bit size and seed. |
| `atualiza_estado(g)` | Updates the generator state. |
| `gera_numero_aleatorio(g, n)` | Generates a random integer in `[1, n]`. |
| `gera_carater_aleatorio(g, c)` | Generates a random uppercase letter between `'A'` and `c`. |

---

### 2️⃣ Coordinates

Encapsulates grid positions using tuples `(column, row)` and ensures valid range.

| Function | Description |
|-----------|-------------|
| `cria_coordenada(col, l)` | Creates a coordinate. |
| `obtem_coordenadas_vizinhas(c)` | Returns valid neighboring coordinates. |
| `coordenada_para_str(c)` | Converts a coordinate to a string format (`"B07"`). |
| `str_para_coordenada(s)` | Parses a string back into a coordinate. |

---

### 3️⃣ Parcels (Cells)

Represents the state of each cell — **hidden**, **clean**, or **marked** — and whether it contains a mine.

| Function | Description |
|-----------|-------------|
| `cria_parcela()` | Creates a new parcel. |
| `marca_parcela(p)` | Marks a parcel with a flag. |
| `limpa_parcela(p)` | Reveals (cleans) a parcel. |
| `esconde_mina(p)` | Places a mine in a parcel. |
| `parcela_para_str(p)` | Converts parcel state into a display character. |

---

### 4️⃣ Field (Board)

A dictionary mapping coordinates → parcel objects.  
Implements field creation, mine placement, and string rendering.

| Function | Description |
|-----------|-------------|
| `cria_campo(col, l)` | Builds a new empty minefield. |
| `coloca_minas(m, c, g, n)` | Places `n` mines randomly, excluding coordinate `c`. |
| `campo_para_str(m)` | Renders the current game board as ASCII text. |
| `obtem_numero_minas_vizinhas(m, c)` | Counts mines adjacent to a coordinate. |

---

### 5️⃣ Game Logic

Implements the actual **Minesweeper** gameplay loop.

| Function | Description |
|-----------|-------------|
| `minas(c, l, n, d, s)` | Main entry point to start the game. |
| `turno_jogador(m)` | Handles user turn and actions (`L` to clean, `M` to mark). |
| `limpa_campo(m, c)` | Recursively cleans connected safe parcels. |
| `jogo_ganho(m)` | Checks if all safe cells have been revealed. |

---

## 🕹️ Example Usage

```python
>>> minas('C', 3, 2, 32, 123)
   [Bandeiras 0/2]
   ABC
  +---+
01|###|
02|###|
03|###|
  +---+
Escolha uma coordenada:A01
Escolha uma ação, [L]impar ou [M]arcar:L
...
