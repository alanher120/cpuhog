import multiprocessing
import time

def cpu_intensive_task(duration):
    start_time = time.time()
    # 執行大量計算來模擬高 CPU 使用率
    while time.time() - start_time < duration:
        result = sum(i * i for i in range(100000))

if __name__ == "__main__":
    # 設定運行時間（秒）
    duration = 10

    # 獲取 CPU 核心數
    num_cpus = multiprocessing.cpu_count()
    
    # 創建多個進程來佔用所有 CPU 核心
    processes = []
    for _ in range(num_cpus):
        p = multiprocessing.Process(target=cpu_intensive_task, args=(duration,))
        processes.append(p)
        p.start()
    
    # 等待所有進程完成
    for p in processes:
        p.join()
