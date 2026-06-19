import threading
import time


def download_file(file_name):
    print(f"Downloading {file_name}...")
    time.sleep(3)
    print(f"{file_name} downloaded")


start_time = time.time()

t1 = threading.Thread(
    target=download_file,
    args=("file1.pdf",)
)

t2 = threading.Thread(
    target=download_file,
    args=("file2.pdf",)
)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()

print(
    f"Execution Time: {end_time - start_time:.2f} seconds"
)