from ins.is_valid_ins import main
from core.error_info import NotDataException, InsTryAgenException


if __name__ == '__main__':
    while True:
        try:
            main()
        except NotDataException:
            print("筛选完毕")
            break
        except InsTryAgenException:
            pass

