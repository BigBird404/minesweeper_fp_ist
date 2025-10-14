# 🧩 Project 1 — Text Formatting, Elections, and Linear Systems

**Author:** Filippo da Costa Bortoli  
**IST ID:** ist1106103  
**Email:** filippo.bortoli@tecnico.ulisboa.pt  
**Date:** 27/10/2022  

---

## 🧠 Overview

This project implements three independent modules focusing on algorithmic reasoning and data manipulation:

1. **Text formatting and justification**  
2. **Election results simulation using the D’Hondt method**  
3. **Solving linear systems using the Jacobi iterative method**

All tasks are implemented **without external libraries**, using only base Python data structures such as tuples, lists, and dictionaries.

---

## 📂 Structure

| Module | Description |
|---------|-------------|
| `Ex1` | Text formatting and justification functions |
| `Ex2` | Election result processing (D’Hondt method) |
| `Ex3` | Linear system solver (Jacobi method) |

---

### 📝 1. Text Formatting

Implements functions to clean, wrap, and justify text to a fixed width.

| Function | Description |
|-----------|-------------|
| `limpa_texto(t)` | Removes extra spaces between words. |
| `corta_texto(t, width)` | Splits text into two parts based on the given width. |
| `insere_espacos(t, width)` | Adds spaces between words to fully justify text. |
| `justifica_texto(t, width)` | Fully justifies a block of text. |

**Example:**
```python
>>> justifica_texto("Instituto Superior Tecnico is a university", 20)
('Instituto Superior', 'Tecnico is a', 'university         ')
```


### 🗳️ 2. Elections — D’Hondt Method

Simulates an electoral seat distribution based on votes per district using the D’Hondt proportional representation system.


| Function | Description |
|-----------|-------------|
| `calcula_quocientes(info, seats)` | Calculates the D’Hondt quotients for each party. |
| `atribui_mandatos(info, seats)` | Allocates parliamentary seats according to quotients. |
| `obtem_partidos(info)` | Retrieves the list of parties. |
| `obtem_resultado_eleicoes(info)` | Returns the overall election result. |

**Example:**
```python
info = {
    "Lisboa": {"deputados": 3, "votos": {"A": 34000, "B": 28000, "C": 16000}},
    "Porto": {"deputados": 2, "votos": {"A": 30000, "B": 22000, "C": 17000}}
}

>>> obtem_resultado_eleicoes(info)
[('A', 3, 64000), ('B', 2, 50000), ('C', 0, 33000)]
```

### 🔢 3. Linear Systems — Jacobi Method
Numerical solver for linear systems of the form A * x = c, using the Jacobi iterative method.
Includes convergence checks and input validation.

| Function	| Description 
|-----------|-------------|
| `produto_interno(t1, t2)`	| Computes the inner product of two tuples.
| `retira_zeros_diagonal(A, c)`	| Rearranges matrix rows to avoid zeros on the diagonal.
| `eh_diagonal_dominante(A)`	| Checks if the matrix is diagonally dominant.
| `resolve_sistema(A, c, p)`	| Solves a system iteratively with precision p.

**Example:**
```python
A = ((10, 2, 1), (1, 5, 1), (2, 3, 10))
c = (7, -8, 6)

>>> resolve_sistema(A, c, 1e-5)
(0.5385, -1.6923, 0.7692)
```

## 🧪 Error Handling
All modules include strict validation.

## 🧱 Key Concepts
String and tuple manipulation
Dictionaries and sorting
Numerical algorithms
Input validation and error handling
Modular design and clean documentation
