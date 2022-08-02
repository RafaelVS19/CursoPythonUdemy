"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""


def show_op(todo_list):
    print()
    if not todo_list:
        print('Lista de tarefas vazia!')
    else:
        print('Tarefas: ')
        for i in todo_list:
            print(f'-{i}')
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo_list):
    print()
    todo_list.append(input('Digite sua tarefa:\n'))
    print()


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite o número da opção:\n1.Adicionar tarefas 2.Listar tarefar 3.Desfazer 4.Refazer 5.Sair\n')

        if todo == '1':
            do_add(todo_list)
        elif todo == '2':
            show_op(todo_list)
            continue
        elif todo == '3':
            do_undo(todo_list, redo_list)
            continue
        elif todo == '4':
            do_redo(todo_list, redo_list)
            continue
        elif todo == '5':
            print('\nVoçê saiu!')
            break
        else:
            print('\nDigite apenas uma das opções mostradas!\n')
