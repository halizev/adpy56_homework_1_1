if __name__ == '__main__':
    import datetime
    from application.salary import calculate_salary
    from application.db.people import get_employees
    calculate_salary()
    get_employees()
    print(datetime.datetime.today())
