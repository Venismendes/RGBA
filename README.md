# RGBA - English

Convert colors beetwen Decimal, Hexadecimal and Zero-one

---
# RGBA - Português
Converter cores entre Decimal, Hexadecimal e Zero-um

---
## Parametros 
1. Para `decimal()` e `zero_One()`
    * R = Vermelho
    * G = Verde
    * B = Azul
    * A = Opacidade
    * RHZ = Qual a conversão a ser feita 1-3
2. Para `hexadecimal()`
    * H = string '#000000'
    * RHZ = Conversão 1-3

---
## Exemplos
Código `var = decimal(255, 255, 255, a=1, rhz=2)`
Retornará a conversão de RGBA(255, 255, 255, 1) para Hexadecimal `'#FFFFFF'` e armazenará em `var`.

Código `var = hexadecimal('#FFFfFf', rhz=1)`
retornará o valor RGBA(1, 1, 1, 1) e armazenará em `var`.

Código `zero_one(0.5, 0.5, 0.5, rhz=3)` mostra no terminal a conversão de RGBA(1, 1, 1, 1) para Decimal e Hexadecimal.

---
## Funções

decimal               | hexadecimal        | zero_one
---                   |---                 |---
RHZ = 1 = hexadecimal | RHZ = 1 = decimal  | RHZ = 1 = decimal
RHZ = 2 = zero_one    | RHZ = 2 = zero_one | RHZ = 2 = hexadecimal





