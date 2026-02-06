import time
import cv2
import numpy as np
import mss
import pygetwindow as gw
import threading
import ctypes
from pynput import keyboard

def move_mouse_relative(dx, dy):
    ctypes.windll.user32.mouse_event(0x0001, int(dx), int(dy), 0, 0)

def quick_shot():
    ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
    time.sleep(0.01)
    ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)

running = True
last_shot_time = 0
SHOT_DELAY = 0.03
SCAN_FOV = 320
GREEN = "\033[32m"
RESET = "\033[0m"

def on_press(key):
    global running
    try:
        if key == keyboard.Key.esc:
            running = False
            print("" + "-"*18)
            print(f"{GREEN}AIMBOT ОСТАНОВЛЕН!{RESET}")
            print("-"*18)
            return False
    except AttributeError:
        pass

def start_bot():
    global running, last_shot_time
    import os
    os.system('')

    GREEN = "\033[32m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    LOWER_BODY = np.array([0, 0, 0])
    UPPER_BODY = np.array([0, 0, 0])
    mode = "single"

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(GREEN + """
  /$$$$$$   /$$$$$$          /$$        /$$$$$$         /$$$$$$  /$$               /$$                   /$$    
 /$$__  $$ /$$__  $$       /$$$$       /$$__  $$       /$$__  $$|__/              | $$                  | $$    
| $$  \__/| $$  \__/      |_  $$      | $$  \__/      | $$  \ $$ /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$  /$$$$$$  
| $$      |  $$$$$$         | $$      | $$$$$$$       | $$$$$$$$| $$| $$_  $$_  $$| $$__  $$ /$$__  $$|_  $$_/  
| $$       \____  $$        | $$      | $$__  $$      | $$__  $$| $$| $$ \ $$ \ $$| $$  \ $$| $$  \ $$  | $$    
| $$    $$ /$$  \ $$        | $$      | $$  \ $$      | $$  | $$| $$| $$ | $$ | $$| $$  | $$| $$  | $$  | $$ /$$
|  $$$$$$/|  $$$$$$/       /$$$$$$ /$$|  $$$$$$/      | $$  | $$| $$| $$ | $$ | $$| $$$$$$$/|  $$$$$$/  |  $$$$/
 \______/  \______/       |______/|__/ \______/       |__/  |__/|__/|__/ |__/ |__/|_______/  \______/    \___/  
--------------------------------------------- by 4elik123 ----------------------------------------------------    
""" + RESET)
        print(f"{YELLOW}ГЛАВНОЕ МЕНЮ:{RESET}")
        print("1. Запустить Аимбот")
        print("2. Информация о Аимботе")

        main_choice = input("\nВыбор: ")

        if main_choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')

            print(GREEN + """
  /$$$$$$   /$$$$$$          /$$        /$$$$$$         /$$$$$$  /$$               /$$                   /$$    
 /$$__  $$ /$$__  $$       /$$$$       /$$__  $$       /$$__  $$|__/              | $$                  | $$    
| $$  \__/| $$  \__/      |_  $$      | $$  \__/      | $$  \ $$ /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$  /$$$$$$  
| $$      |  $$$$$$         | $$      | $$$$$$$       | $$$$$$$$| $$| $$_  $$_  $$| $$__  $$ /$$__  $$|_  $$_/  
| $$       \____  $$        | $$      | $$__  $$      | $$__  $$| $$| $$ \ $$ \ $$| $$  \ $$| $$  \ $$  | $$    
| $$    $$ /$$  \ $$        | $$      | $$  \ $$      | $$  | $$| $$| $$ | $$ | $$| $$  | $$| $$  | $$  | $$ /$$
|  $$$$$$/|  $$$$$$/       /$$$$$$ /$$|  $$$$$$/      | $$  | $$| $$| $$ | $$ | $$| $$$$$$$/|  $$$$$$/  |  $$$$/
 \______/  \______/       |______/|__/ \______/       |__/  |__/|__/|__/ |__/ |__/|_______/  \______/    \___/  
--------------------------------------------- by 4elik123 ----------------------------------------------------
""" + RESET)

            print(f"{YELLOW}--- Запустить Аимбот ---{RESET}")
            print("За какую команду вы играете?")
            print(f"1. {RED}Т{RESET}")
            print(f"2. {BLUE}КТ{RESET}")
            print(f"3. {YELLOW}Deathmatch{RESET}")
            choice = input("Выбор: ")

            if choice == "1":
                print(f"Ваш выбор: {RED}1 (Террористы){RESET}")
                LOWER_BODY = np.array([100, 160, 50])
                UPPER_BODY = np.array([140, 255, 255])
                break

            elif choice == "2":
                print(f"Ваш выбор: {BLUE}2 (Контр-Террористы){RESET}")
                LOWER_BODY = np.array([0, 160, 50])
                UPPER_BODY = np.array([10, 255, 255])
                break
            
            elif choice == "3":
                print(f"Ваш выбор: {YELLOW}3 (Огонь по всем){RESET}")
                mode = "all"
                break

        elif main_choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')

            print(GREEN + """
  /$$$$$$   /$$$$$$          /$$        /$$$$$$         /$$$$$$  /$$               /$$                   /$$    
 /$$__  $$ /$$__  $$       /$$$$       /$$__  $$       /$$__  $$|__/              | $$                  | $$    
| $$  \__/| $$  \__/      |_  $$      | $$  \__/      | $$  \ $$ /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$  /$$$$$$  
| $$      |  $$$$$$         | $$      | $$$$$$$       | $$$$$$$$| $$| $$_  $$_  $$| $$__  $$ /$$__  $$|_  $$_/  
| $$       \____  $$        | $$      | $$__  $$      | $$__  $$| $$| $$ \ $$ \ $$| $$  \ $$| $$  \ $$  | $$    
| $$    $$ /$$  \ $$        | $$      | $$  \ $$      | $$  | $$| $$| $$ | $$ | $$| $$  | $$| $$  | $$  | $$ /$$
|  $$$$$$/|  $$$$$$/       /$$$$$$ /$$|  $$$$$$/      | $$  | $$| $$| $$ | $$ | $$| $$$$$$$/|  $$$$$$/  |  $$$$/
 \______/  \______/       |______/|__/ \______/       |__/  |__/|__/|__/ |__/ |__/|_______/  \______/    \___/  
--------------------------------------------- by 4elik123 ----------------------------------------------------
""" + RESET)

            print(f"\n{YELLOW}--- ИНФОРМАЦИЯ О АИМБОТЕ ---{RESET}")
            print(f"• {GREEN}Название:{RESET} CS 1.6 Aimbot.")
            print(f"• {GREEN}Версия:{RESET} 2.0")
            print(f"• {GREEN}Автор:{RESET} 4elik123")
            print(f"• {GREEN}Дата выпуска обновленния:{RESET} 05.02.2026")
            print(f"\n{YELLOW}--- ФУНКЦИИ АИМБОТА ---{RESET}")
            print(f"• {GREEN}Авто-наводка:{RESET} Ищет зеленый цвет головы и проверяет цвет формы.")
            print(f"• {GREEN}Темное видение:{RESET} Встроена гамма-коррекция для темных углов.")
            print(f"• {GREEN}Скорость:{RESET} Обработка кадра занимает около 1-5 мс.")
            print(f"• {GREEN}Управление:{RESET} Нажми 'Escape' для остановки.")
            print(f"\n{YELLOW}--- ЧТО НОВОГО ДОБАВЛЕННО ---{RESET}")
            print(f"• {GREEN}Темное видение:{RESET} Встроена гамма-коррекция для темных углов.")
            print(f"• {GREEN}Главное меню:{RESET} Добавленно главное меню вы можете запустить чит или посмотреть информацию.")
            print(f"• {GREEN}Скорость:{RESET} теперь аимбот быстрее обноружывает противника.")
            print(f"• {GREEN}Режим Deathmatch:{RESET} теперь  добавлен режим Deathmatch, если вы выбрали этот режим то аимбот будет стрелять по всем. Отличный режим для CSDM серверов.")
            print(f"• {GREEN}Счетчик Fps:{RESET} в окне там где видно как видит аимбот игру, слева в вверхнем углу есть счетчик кадров в секунду.")
            input("\nНажми Enter, чтобы вернуться в меню...")
        else:
            print(f"{RED}Ошибка! Выбери 1 или 2.{RESET}")
            time.sleep(1)

    win_titles = ["Counter-Strike", "Counter-Strike 1.6", "Counter Strike", "CS 1.6"]
    win = next((gw.getWindowsWithTitle(t)[0] for t in win_titles if gw.getWindowsWithTitle(t)), None)

    if not win:
        print("Окно игры не найдено!"); return

    print("\nПриготовьтесь, Aimbot запускается...")
    for i in range(3, 0, -1):
        print(f"Запуск через: {i}")
        time.sleep(1)
    print("" + "-"*46)
    print(f"{GREEN}AIMBOT АКТИВИРОВАН! Нажмите Escape для выхода.{RESET}")
    print("-"*46)

    keyboard.Listener(on_press=on_press).start()

    LOWER_GREEN = np.array([45, 170, 80])
    UPPER_GREEN = np.array([75, 255, 255])

    if choice == "1":
        LOWER_BODY = np.array([100, 160, 50])
        UPPER_BODY = np.array([140, 255, 255])

    elif choice == "2":
        LOWER_BODY = np.array([0, 160, 50])
        UPPER_BODY = np.array([10, 255, 255])

    with mss.mss() as sct:
        prev_frame_time = 0
        while running:
            sw, sh = win.width, win.height
            cx, cy = sw // 2, sh // 2

            monitor = {
                "top": win.top + cy - SCAN_FOV // 2,
                "left": win.left + cx - SCAN_FOV // 2,
                "width": SCAN_FOV,
                "height": SCAN_FOV
            }

            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            gamma = 1.5
            invGamma = 1.0 / gamma
            table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
            frame = cv2.LUT(frame, table)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(hsv, LOWER_GREEN, UPPER_GREEN)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            best_target = None
            min_dist = float('inf')

            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > 3:
                    x, y, w, h = cv2.boundingRect(cnt)
                    if w > h * 1.3: continue
                    if y > (SCAN_FOV * 0.8): continue

                    M = cv2.moments(cnt)
                    if M["m00"] != 0:
                        hx, hy = int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])

                        check_h = int(h * 5)
                        check_zone = hsv[hy:min(hy+check_h, SCAN_FOV), max(0, hx-w):min(SCAN_FOV, hx+w)]
                        if check_zone.size > 0:
                            if mode == "all":
                                m_red = cv2.inRange(check_zone, np.array([0, 160, 50]), np.array([10, 255, 255]))
                                m_blue = cv2.inRange(check_zone, np.array([100, 160, 50]), np.array([140, 255, 255]))
                                target_valid = (cv2.countNonZero(m_red) + cv2.countNonZero(m_blue)) > (area * 1.5)
                            else:
                                body_mask = cv2.inRange(check_zone, LOWER_BODY, UPPER_BODY)
                                target_valid = cv2.countNonZero(body_mask) > (area * 2.5)
                                
                            if target_valid:
                                dist = np.sqrt((hx - SCAN_FOV//2)**2 + (hy - SCAN_FOV//2)**2)
                                if dist < min_dist:
                                    min_dist = dist
                                    best_target = (hx, hy, h)
            if best_target:
                tx, ty, th = best_target
                dx = tx - (SCAN_FOV // 2)
                dy = (ty - int(th * 0.45)) - (SCAN_FOV // 2)

                move_mouse_relative(dx * 0.75, dy * 0.75)

                if time.time() - last_shot_time >= SHOT_DELAY:
                    quick_shot()
                    last_shot_time = time.time()

            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            frame = cv2.LUT(frame, table)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            new_frame_time = time.time()
            fps = 1 / (new_frame_time - prev_frame_time) if (new_frame_time - prev_frame_time) > 0 else 0
            prev_frame_time = new_frame_time
            fps_int = int(fps)
            fps_color = (0, 255, 0) if fps_int >= 25 else (0, 0, 255)
            cv2.putText(frame, f"Fps {fps_int}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, fps_color, 2)

            mask = cv2.inRange(hsv, LOWER_GREEN, UPPER_GREEN)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            best_target = None
            min_dist = float('inf')

            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > 1.5:
                    x, y, w, h = cv2.boundingRect(cnt)

                    if w > h * 1.1: continue

                    M = cv2.moments(cnt)
                    if M["m00"] != 0:
                        hx, hy = int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])

                        check_h = int(h * 4)
                        check_zone = hsv[hy:min(hy+check_h, SCAN_FOV), max(0, hx-w):min(SCAN_FOV, hx+w)]

                        if check_zone.size > 0:
                            body_mask = cv2.inRange(check_zone, LOWER_BODY, UPPER_BODY)
                            if cv2.countNonZero(body_mask) > (area * 1.2):
                                dist = np.sqrt((hx - SCAN_FOV//2)**2 + (hy - SCAN_FOV//2)**2)
                                if dist < min_dist:
                                    min_dist = dist
                                    best_target = (hx, hy, h)

            cv2.imshow("CS 1.6 Aimbot Vision", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_bot()