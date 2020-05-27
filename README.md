# RGBA - English

Convert colors beetwen Decimal, Hexadecimal and Zero-one

---
# RGBA - Português
Converter cores entre Decimal, Hexadecimal e Zero-um

---
## Parametros 
1. Para `decimal()` e `zero_One()`
    1.1 R = Vermelho
    1.2 G = Verde
    1.3 B = Azul
    1.4 A = Opacidade
    1.5 RHZ = Qual a conversão a ser feita 1-3
2. Para `hexadecimal()`
    1.1 H = string '#000000'
    2.2 RHZ = Conversão 1-3
##
---
## Exemplo

Código `var = decimal(255, 255, 255, a=1, rhz=2)`
Retornará a conversão de RGB(255, 255, 255) para Hexadecimal no formato `'#FFFFFF'` e armazenará em `var`

o mesmo se pode fazer com as outras funções
---
## Funções
---
decimal               | hexadecimal        | zero_one
---                   |---                 |---
RHZ = 1 = hexadecimal | RHZ = 1 = decimal  | RHZ = 1 = decimal
RHZ = 2 = zero_one    | RHZ = 2 = zero_one | RHZ = 2 = hexadecimal





