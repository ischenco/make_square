import os
from PIL import Image, ImageOps

def make_square(image_path, output_path, fill_color=(255, 255, 255)):
    try:
        # Открываем изображение
        image = Image.open(image_path)
        
        # Получаем размеры изображения
        width, height = image.size
        
        # Определяем размер для нового квадратного изображения
        new_size = max(width, height)
        
        # Добавляем поля для создания квадратного изображения
        new_image = ImageOps.expand(image, 
                                    border=((new_size - width) // 2, 
                                            (new_size - height) // 2), 
                                    fill=fill_color)
        
        # Преобразуем изображение в режим RGB, если оно в RGBA
        if new_image.mode == 'RGBA':
            new_image = new_image.convert('RGB')
        
        # Сохраняем новое изображение
        new_image.save(output_path)
        print(f"Изображение {image_path} успешно сохранено как {output_path}.")
    
    except PermissionError:
        print(f"Ошибка разрешений при обработке файла {image_path}. Пожалуйста, проверьте права доступа.")
    except FileNotFoundError:
        print(f"Файл {image_path} не найден. Пожалуйста, проверьте путь к файлу.")
    except Exception as e:
        print(f"Произошла ошибка при обработке файла {image_path}: {e}")

def process_images_in_folder(input_folder, output_folder, fill_color=(255, 255, 255)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            make_square(input_path, output_path, fill_color)

# Пример использования
input_folder = 'D:\\Pt\\image_resize\\input_images'
output_folder = 'D:\\Pt\\image_resize\\output_images'
process_images_in_folder(input_folder, output_folder)
