import cv2
import datetime


def record_video():
    # Инициализация камеры
    cap = cv2.VideoCapture(5,cv2.CAP_DSHOW)

    # Проверка, открыта ли камера
    if not cap.isOpened():
        print("Ошибка: Не удалось открыть камеру")
        return

    # Получение разрешения камеры
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Создание имени файла с текущей датой и временем
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"video_{timestamp}.avi"

    # Определение кодека и создание VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 10  # 10 кадров в секунду
    out = cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height))

    print("Запись начата...")
    print("Нажмите 'S' для остановки записи")

    recording = True

    while recording:
        # Захват кадра
        ret, frame = cap.read()

        if not ret:
            print("Ошибка: Не удалось получить кадр")
            break

        # Запись кадра в видеофайл
        out.write(frame)

        # Отображение кадра (опционально)
        cv2.imshow('Recording - Press S to stop', frame)

        # Проверка нажатия клавиши
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s') or key == ord('S') or key == ord('ы') or key == ord('Ы'):
            recording = False

    # Освобождение ресурсов
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Запись завершена! Видео сохранено как: {filename}")


if __name__ == "__main__":
    record_video()