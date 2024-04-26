import queue
import time
import random

# Створення черги для заявок
request_queue = queue.Queue()

def generate_request():
    """Генерує унікальну заявку та додає її до черги."""
    request_id = random.randint(1000, 9999)
    request_queue.put(request_id)
    print(f"Заявка {request_id} додана до черги.")

def process_request():
    """Обробляє першу заявку у черзі, якщо вона існує."""
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Заявка {request_id} оброблена.")
    else:
        print("Черга пуста. Немає заявок для обробки.")

def main():
    try:
        while True:
            generate_request()
            time.sleep(1)  
            process_request()
            time.sleep(1) 
    except KeyboardInterrupt:
        print("Програма зупинена користувачем.")


if __name__ == '__main__':
    main()
