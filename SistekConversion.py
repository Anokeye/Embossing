def convert_to_sistek(list_of_euronet_lines):
    """Accepts the contents of the Euronet file and returns Sistek Records """

    sistek_records_list = []
    euronet_record = []
    file_header = "Card_Number,Exp_Date,Customer_Name,Offset,ISO_Name"
    end_of_record_marker = "#END#"

    sistek_records_list.append(file_header)

    for line in list_of_euronet_lines:
        euronet_record.append(line)
        if end_of_record_marker in line:
            sistek_record = make_sistek_record(euronet_record)
            sistek_records_list.append(sistek_record)
            euronet_record.clear()
            euronet_record.append(line)

    return sistek_records_list


def make_sistek_record(euronet_record):
    card_number = get_card_number(euronet_record[0])
    expiry_date = get_expiry_date(euronet_record[1])
    full_name = get_full_name(euronet_record[2])
    offset = "0000"
    delimeter = ","
    iso_name = get_iso_name(euronet_record[5])
    record = [card_number, expiry_date, full_name, offset, iso_name]

    sistek_record = delimeter.join(record)

    return sistek_record


def get_iso_name(input_line):
    delimeter = '^'
    start_of_name = input_line.index(delimeter) + 1
    end_of_name = input_line.index(delimeter, start_of_name)

    return input_line[start_of_name:end_of_name]


def get_full_name(input_line):
    return input_line.strip()


def get_expiry_date(input_line):
    return input_line[0:8]


def get_card_number(input_line):
    card_length = 16
    card_delimeter = '$'
    start_of_card = input_line.index(card_delimeter) + 1
    card_number = input_line[start_of_card:start_of_card + card_length]

    return card_number