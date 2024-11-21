import requests # type: ignore
import sys

tasks = []  # Lista global para almacenar las tareas

def authenticate(username, password):
    url = f"https://httpbin.org/basic-auth/{username}/{password}"
    response = requests.get(url, auth=(username, password))
    return response.status_code == 200

def add_task():
    title = input("Ingrese el título de la tarea: ")
    tasks.append({"title": title, "status": "pendiente"})
    print(f"Tarea '{title}' agregada.")

def list_tasks():
    if not tasks:
        print("No hay tareas registradas.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['title']} [{task['status']}]")

def delete_task():
    title = input("Ingrese el título de la tarea a eliminar: ")
    for task in tasks:
        if task["title"] == title:
            tasks.remove(task)
            print(f"Tarea '{title}' eliminada.")
            return
    print(f"Tarea '{title}' no encontrada.")

def task_manager():
    while True:
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        choice = input("Elija una opción (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def main():
    print("Bienvenido al sistema de gestión de tareas")

    attempts = 0
    while attempts < 3:
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        if authenticate(username, password):
            print("Autenticación exitosa.")
            task_manager()
            break
        else:
            print("Credenciales incorrectas. Inténtelo nuevamente.")
            attempts += 1

    if attempts == 3:
        print("Error: Ha excedido el número de intentos. Saliendo del programa.")

if __name__ == "__main__":
    main()
