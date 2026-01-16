import datetime
def log_error(error):
    LOG_PATH = "logs/errors.log"
    time = str(datetime.datetime.now())
    with open(LOG_PATH, mode='a', newline='') as err:
        err.write(f"{[time]} {error}\n")
