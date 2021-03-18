import datetime


def choose_template_option(template_1, template_2):
    today = datetime.date.today()
    start_of_current_year = datetime.date(today.year, 1, 1)

    day_of_year = (today - start_of_current_year).days
    if day_of_year % 2 == 0:
        return template_1
    else:
        return template_2
