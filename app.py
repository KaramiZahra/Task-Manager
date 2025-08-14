import json
import os
from pathlib import Path

FILE_TODO = Path('todo.json')

tasks_list = []


def load_tasks():
    if os.path.exists(FILE_TODO):
        with open(FILE_TODO, "r") as tf:
            try:
                tasks_list.extend(json.load(tf))
            except json.JSONDecodeError:
                tasks_list.clear()
    else:
        FILE_TODO.touch()
        tasks_list.clear()
    return tasks_list


load_tasks()


def show_tasks():
    if tasks_list:
        for task in tasks_list:
            print(
                f"{task['id']}.{task['name']} {'✓' if task['status'] else '✗'}")
    else:
        print('You have no tasks.')


def add_task():
    user_task = input('Enter your task: ').strip()
    if user_task:
        new_task = {'id': len(tasks_list) + 1,
                    'name': user_task, 'status': False}
        tasks_list.append(new_task)
        print('Task successfully added.')
    else:
        print('Task can\'t be empty.')


def reassign_task_ids():
    for index, task in enumerate(tasks_list, start=1):
        task['id'] = index


def delete_task():
    show_tasks()
    try:
        rm_task = int(input('Enter task number to delete: '))
    except ValueError:
        print("Task doesn't exist.")
        return

    for index, task in enumerate(tasks_list):
        if task['id'] == rm_task:
            del tasks_list[index]
            print('Task successfully deleted.')
            reassign_task_ids()
            break
    else:
        print("Task doesn't exist.")


def change_status():
    show_tasks()
    try:
        change_task = int(input('Enter task number to change: '))
    except ValueError:
        print("Task doesn't exist.")
        return

    for index, task in enumerate(tasks_list):
        if task['id'] == change_task:
            tasks_list[index]['status'] = not tasks_list[index]['status']
            print('Status successfully changed.')
            break
    else:
        print("Task doesn't exist.")


def save_tasks():
    with open(FILE_TODO, 'w') as tf:
        json.dump(tasks_list, tf, indent=4)


def menu():
    flag = True
    while flag:
        print('\n---To Do List Menu---\n')
        print('1.Show Tasks')
        print('2.Add Tasks')
        print('3.Remove Tasks')
        print('4.Change Tasks')
        print('5.Exit and Save \n')

        user_input = input('Choose an option (1-5): ')

        if user_input == '1':
            show_tasks()
        elif user_input == '2':
            add_task()
        elif user_input == '3':
            delete_task()
        elif user_input == '4':
            change_status()
        elif user_input == '5':
            save_tasks()
            flag = False
        else:
            print('Enter a valid number.')


menu()
