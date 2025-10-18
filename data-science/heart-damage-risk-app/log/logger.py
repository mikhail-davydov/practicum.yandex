import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    # Настраиваем формат вывода логов
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s]: %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    return logger
