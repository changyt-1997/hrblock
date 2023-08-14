from core.error_info import NotDataException
from ins.complete_ins import main


if __name__ == '__main__':
    while True:
        try:
            main()
        except NotDataException:
            break
        except Exception:
            pass
