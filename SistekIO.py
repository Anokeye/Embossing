import datetime
import os


def read_euronet_file():
    euronet_file = get_euronet_file()
    euronet_file_lines = []
    try:
        with open(euronet_file, encoding='ansi', mode='r') as f:
            euronet_file_lines = f.readlines()
    except:
        print(f"Error processing file {euronet_file}")
        quit()

    return euronet_file_lines


def write_backup_file(sistek_list):
    backup_file = get_backup_file()
    write_file(backup_file, sistek_list)


def write_sistek_file(sistek_list):
    sistek_file = get_sistek_file()
    write_file(sistek_file, sistek_list)


def write_file(file_name, file_data):
    with open(file_name, "w") as f:
        for line in file_data:
            f.write(line + '\n')


def get_euronet_file():
    current_directory = os.path.dirname(__file__)
    input_file = current_directory + "\\emc001vd1"
    return input_file


def get_sistek_file():
    current_directory = os.path.dirname(__file__)
    output_file = current_directory + '\\cards.txt'
    return output_file


def get_backup_file():
    current_directory = os.path.dirname(__file__)
    today_date = datetime.datetime.today()
    backup_directory = f'{current_directory}\\backup'

    if not os.path.isdir(backup_directory):
        os.mkdir(backup_directory)

    file_name = f"{today_date.year}{today_date.month:02d}{today_date.day:02d}_{today_date.hour:02d}" \
                f"{today_date.minute:02d}{today_date.second:02d}.stk "
    return f"{backup_directory}\\{file_name}"