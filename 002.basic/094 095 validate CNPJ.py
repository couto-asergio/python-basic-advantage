"""
094 and 095 - Validate CNPJ
"""
import cnpj_old

cnpj1 = '04.OOP.252.011/0001-10'

if cnpj1.valida(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')