import xmlrpc.client
import os

MENU = \
"""
Bem-vindo ao sistema de notas 2000.
As possíveis operações são:
rg - cadastrar nota(matricula, disciplina, nota)
gg - bucar nota(matricula, disciplina)
ga - buscar notas(matricula)
ac - consultar cr(matricula)
"""

def command_handler(operations, command):
    split_message = command.split(sep=" ")
    return operations[split_message[0]](*split_message[1:])


with xmlrpc.client.ServerProxy("http://localhost:9001/") as proxy:
    operations = {}
    operations["rg"] = proxy.register_grade
    operations["gg"] = proxy.get_grade
    operations["ga"] = proxy.get_all_grades
    operations["ac"] = proxy.get_ac
    
    print(MENU)
    
    while(1):
        if os.name in ('nt', 'dos'):
            os.system('cls')
        else: 
            os.system('clear')

        print(MENU)
        
        command = input()
        
        rtn = command_handler(operations, command)
        print(rtn)
        input()