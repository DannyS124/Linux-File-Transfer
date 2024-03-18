import os
import shutil

def transfer_files(source_folder, destination_folder, transfer_type):
    file_count = 0
    extensions = []

    if transfer_type == 1:  # Photos only
        extensions = ['.jpg', '.jpeg', '.png']
    elif transfer_type == 2:  # Videos only
        extensions = ['.mp4', '.avi', '.mov']
    else:  # Both photos and videos
        extensions = ['.jpg', '.jpeg', '.png', '.mp4', '.avi', '.mov']

    total_files = sum(len(files) for _, _, files in os.walk(source_folder))

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_folder, file)

                shutil.copy2(source_file, destination_file)
                file_count += 1

                progress = (file_count / total_files) * 100
                print(f"\rProgress: {progress:.2f}%  ", end='', flush=True)

    print("\nTransfer Complete.")
    print(f"{file_count} files transferred.")

def main():
    print("Welcome to File Transfer!")

    print("\nSelect Transfer Type:")
    print("1. Photos")
    print("2. Videos")
    print("3. Both")
    transfer_type = int(input("Enter your choice (1/2/3): "))

    source_folder = input("Enter the source folder: ")
    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        return

    destination_folder = input("Enter the destination folder: ")
    if not os.path.exists(destination_folder):
        print("Destination folder does not exist.")
        return

    transfer_files(source_folder, destination_folder, transfer_type)

if __name__ == "__main__":
    main()
