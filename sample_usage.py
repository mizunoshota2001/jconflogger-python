from jconflogger import getLogger


def main():
    logger = getLogger(__name__)

    logger.debug("これはデバッグメッセージです。")
    logger.info("これは情報メッセージです。")
    logger.warning("これは警告メッセージです。")
    logger.error("これはエラーメッセージです。")
    logger.critical("これは重大なエラーメッセージです。")


if __name__ == "__main__":
    main()
