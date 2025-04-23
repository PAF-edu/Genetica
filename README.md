# 🧬 Genetic Simulator

Simulazione didattica di ereditarietà poligenica, per esplorare la **variazione genetica** e la **regressione verso la media** attraverso un modello semplificato.

## 📚 Descrizione

Questa applicazione simula l'altezza dei figli (progenie) in base ai genotipi di due genitori. Ogni genotipo è costituito da una combinazione di geni con effetto codominante. La simulazione include la **variabilità casuale** (rumore), per rappresentare anche fattori ambientali o non-genetici.

## ⚙️ Come funziona

- Ogni gene può essere **omozigote dominante**, **eterozigote** o **omozigote recessivo**.
- L'effetto sul fenotipo (altezza) è:
  - `+5 cm ± 2` se eterozigote
  - `+10 cm ± 2` se omozigote dominante
  - `0 cm ± 2` se omozigote recessivo
- Il programma simula 100 figli per ciascuna coppia parentale.

## 📊 Output

Il programma stampa:

- Altezza simulata dei genitori (valore massimo o minimo su 100 simulazioni)
- Media, minimo e massimo dell'altezza nella progenie
