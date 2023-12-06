import logging

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    a = 0
    while True:
        a += 1
        logger.info("ХЗАРАБОТАЛО")
        print(f"{a}")