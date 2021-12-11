import xmlrpc.client
import os

MENU = \
"""
Bem-vindo ao sistema de notas 2000.
As possíveis operações são:
cn - cadastrar nota(matricula, disciplina, nota)
bn - bucar nota(matricula, disciplina)
bs - buscar notas(matricula)
cr - consultar cr(matricula)
"""

def command_handler(operations, command):
    split_message = command.split(sep=" ")
    return operations[split_message[0]](*split_message[1:])


with xmlrpc.client.ServerProxy("http://localhost:9001/") as proxy:
    operations = {}
    operations["cn"] = proxy.register_grade
    operations["bn"] = proxy.get_grade
    operations["bs"] = proxy.get_all_grades
    operations["cr"] = proxy.get_ac
    
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