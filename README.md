## Fundamentos da programaçao

This repository contains proj1_FP.py — a collection of small utilities and exercises from the "Fundamentos da Programação" (Programming Fundamentals) course.

## Overview

proj1_FP.py implements the following groups of utilities:

1. Text formatting and justification
   - limpa_texto: cleans whitespace
   - corta_texto: splits text into a line respecting a maximum width without breaking words
   - insere_espacos: inserts spaces to expand a line to an exact width (distributes spaces left-to-right)
   - justifica_texto: fully justify a text into multiple lines of a given width (last line left-aligned)

2. Linear algebra / Jacobi method
   - produto_interno: computes the inner product of two vectors
   - verifica_convergencia: checks convergence of a candidate solution for Ax = c within a tolerance
   - retira_zeros_diagonal: attempts to remove zeros from the diagonal by swapping rows
   - eh_diagonal_dominante: tests whether a matrix is diagonally dominant
   - resolve_sistema: solves a linear system using the Jacobi iterative method with validation

3. Electoral system (D'Hondt method)
   - calcula_quocientes: computes vote quotients for each party up to number of seats
   - atribui_mandatos: assigns seats using the D'Hondt method
   - obtem_partidos: collects and sorts participating party names from election data
   - obtem_resultado_eleicoes: returns final election results aggregated across districts

The code and docstrings are mostly written in Portuguese.

---
