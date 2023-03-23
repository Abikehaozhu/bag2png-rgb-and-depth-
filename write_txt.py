import numpy as np

if __name__ == "__main__":
    file_path = "association.txt"
    with open(file_path, 'w') as file_object:
        for i in range(2400):
            file_object.write(f"{i} rgb/{i}.png {i} depth/{i}.png\n")
