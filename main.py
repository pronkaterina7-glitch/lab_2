import matplotlib.pyplot as plt


def visualize_dataset(file_path, output_image="result.png"):
  x_coords = []
  y_coords = []

  # 1. Зчитування датасету з файлу
  with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
      line = line.strip()
      if line:
        # Підтримуємо пробіли, коми, табуляцію
        parts = line.replace(",", " ").split()
        if len(parts) >= 2:
          x_coords.append(int(parts[0]))
          y_coords.append(int(parts[1]))

  # 2. Встановлення розмірів полотна (canvas size) 960х540 пкс
  # При DPI = 100 розмір у дюймах дорівнює 9.6 x 5.4 (9.6 * 100 = 960, 5.4 * 100 = 540)
  fig, ax = plt.subplots(figsize=(9.6, 5.4), dpi=100)

  # 3. Відображення точок за заданими координатами
  ax.scatter(x_coords, y_coords, s=2, c="black", marker=".")

  # Встановлення меж відповідно до розміру полотна (0,0 у нижньому лівому куті)
  ax.set_xlim(0, 960)
  ax.set_ylim(0, 540)

  # Прибираємо рамки та зайві відступи для отримання чистого полотна
  ax.set_axis_off()
  plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)

  # 4. Виведення результату у графічний формат (PNG)
  plt.savefig(
      output_image, dpi=100, bbox_inches="tight", pad_inches=0, format="png"
  )
  plt.close()
  print(
      f"Успішно! Згенеровано файл зображення '{output_image}' з полотном"
      " 960x540 пкс."
  )


if __name__ == "__main__":
  visualize_dataset("DS1.txt", "result_km_51fpm_101.png")
