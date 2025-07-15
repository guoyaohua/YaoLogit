"""
Multiprocessing example for YaoLogit

This example demonstrates how YaoLogit ensures consistent logging
across multiple processes and subprocesses.
"""

import multiprocessing
import time
import random
from yaologit import get_logger

def worker_function(worker_id, num_tasks):
    """Worker function that performs some tasks and logs progress"""
    # Each process will use the same logger instance
    logger = get_logger("multiprocess_app", log_dir="./mp_logs")
    
    logger.info(f"Worker {worker_id} started", pid=multiprocessing.current_process().pid)
    
    for i in range(num_tasks):
        # Simulate some work
        time.sleep(random.uniform(0.1, 0.5))
        
        # Log progress
        logger.debug(f"Worker {worker_id} processing task {i+1}/{num_tasks}")
        
        # Simulate occasional warnings or errors
        if random.random() < 0.2:
            logger.warning(f"Worker {worker_id} encountered a minor issue in task {i+1}")
        
        if random.random() < 0.1:
            logger.error(f"Worker {worker_id} encountered an error in task {i+1}", 
                        error_code=random.randint(100, 999))
    
    logger.success(f"Worker {worker_id} completed all tasks")

def subprocess_task():
    """Function to be run in a subprocess"""
    logger = get_logger("multiprocess_app", log_dir="./mp_logs")
    logger.info("Subprocess started", pid=multiprocessing.current_process().pid)
    
    # Simulate some work
    time.sleep(1)
    
    logger.info("Subprocess completed")

def main():
    # Initialize logger in main process
    logger = get_logger("multiprocess_app", log_dir="./mp_logs", 
                       rotation="100 MB", retention="7 days")
    
    logger.info("=== Multiprocessing Example Started ===")
    logger.info(f"Main process PID: {multiprocessing.current_process().pid}")
    
    # Number of worker processes
    num_workers = 4
    num_tasks_per_worker = 5
    
    # Create and start worker processes
    processes = []
    for i in range(num_workers):
        p = multiprocessing.Process(
            target=worker_function, 
            args=(i, num_tasks_per_worker)
        )
        p.start()
        processes.append(p)
        logger.info(f"Started worker process {i}")
    
    # Also create a subprocess using a different method
    subprocess = multiprocessing.Process(target=subprocess_task)
    subprocess.start()
    logger.info("Started subprocess")
    
    # Wait for all processes to complete
    for i, p in enumerate(processes):
        p.join()
        logger.info(f"Worker process {i} finished")
    
    subprocess.join()
    logger.info("Subprocess finished")
    
    logger.success("=== All processes completed successfully ===")
    
    # Demonstrate that all logs went to the same files
    print("\nAll processes logged to the same files in ./mp_logs/")
    print("Check the log files to see interleaved messages from different processes.")

if __name__ == "__main__":
    # Required for Windows
    multiprocessing.freeze_support()
    main()