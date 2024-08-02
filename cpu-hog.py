import multiprocessing

def cpu_intensive_task():
    while True:
        result = sum(i * i for i in range(100000))

if __name__ == "__main__":
    # 獲取 CPU 核心數
    num_cpus = multiprocessing.cpu_count()
    
    # 創建多個進程來佔用所有 CPU 核心
    processes = []
    for _ in range(num_cpus):
        p = multiprocessing.Process(target=cpu_intensive_task)
        processes.append(p)
        p.start()
    
    # 等待所有進程完成
    for p in processes:
        p.join()
