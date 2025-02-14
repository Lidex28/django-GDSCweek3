import logging

def setup_logging():
    logging.basicConfig(
        filename="script.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log_execution(message):
    logging.info(message)

if __name__ == "__main__":
    setup_logging()
    log_execution("Script execution started.")
    print("Logging system initialized. Check 'script.log' for details.")
