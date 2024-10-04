import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task():
    task = input("Görev adı: ")
    date = input("Tarih (opsiyonel): ")
    task_entry = f"{task} | {date}" if date else task
    tasks = load_tasks()
    tasks.append(task_entry)
    save_tasks(tasks)
    print("Görev eklendi.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Henüz hiçbir görev yok.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def complete_task():
    tasks = load_tasks()
    if not tasks:
        print("Tamamlanacak görev yok.")
        return
    view_tasks()
    task_no = int(input("Tamamlanacak görevin numarası: "))
    if 0 < task_no <= len(tasks):
        tasks.pop(task_no - 1)
        save_tasks(tasks)
        print("Görev tamamlandı.")
    else:
        print("Geçersiz görev numarası.")

def main():
    while True:
        print("\nGörev Yönetim Uygulaması")
        print("1. Görev Ekle")
        print("2. Görevleri Görüntüle")
        print("3. Görev Tamamla")
        print("4. Çıkış")
        choice = input("Seçiminiz: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
