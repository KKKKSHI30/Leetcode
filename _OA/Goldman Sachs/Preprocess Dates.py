# 题目: https://www.1point3acres.com/bbs/thread-1010797-1-1.html
def preprocessDate(dates):
    month_mapping = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12"
    }

    processed_dates = []
    for date in dates:
        parts = date.split()
        day = parts[0][:-2].zfill(2)
        month = month_mapping[parts[1]]
        year = parts[2]
        processed_date = f"{year}-{month}-{day}"
        processed_dates.append(processed_date)

    return processed_dates

# Example usage
input_dates = ["1st Mar 1974", "22nd Jan 2013", "7th Apr 1904"]
processed_dates = preprocessDate(input_dates)
print(processed_dates)
