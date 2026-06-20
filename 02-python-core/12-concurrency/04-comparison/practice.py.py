tasks = {
    "API Calls": "ThreadPoolExecutor",
    "Machine Learning": "ProcessPoolExecutor",
    "Web Scraping": "ThreadPoolExecutor",
    "Image Processing": "ProcessPoolExecutor"
}


for task, method in tasks.items():
    print(
        f"{task} -> {method}"
    )