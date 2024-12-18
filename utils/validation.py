def is_valid_date(date_str, format_str="%d-%m-%Y"):
    from datetime import datetime
    try:
        datetime.strptime(date_str, format_str)
        return True
    except ValueError:
        return False