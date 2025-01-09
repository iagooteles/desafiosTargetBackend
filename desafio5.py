# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(texto):
    invertida = ""

    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]

    print(f"Texto original: {texto}")
    print(f"Texto invertido: {invertida}")

inverter_string("Fortaleza é uma cidade linda")
