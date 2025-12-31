import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(BASE_DIR, "app.log")

def check_log():
    error_cnt = 0
    info_cnt = 0
    warn_cnt = 0
    log_summary = {}
    try:
        with open(log_path,'r') as file:
            for line in file:
                if 'error' in line.lower():
                    error_cnt += 1
                if 'info' in line.lower():
                    info_cnt += 1
                if 'warning' in line.lower():
                    warn_cnt += 1
    except:
        print("error occured while opening file")
    log_summary['ERROR'] = error_cnt
    log_summary['WARNING'] = warn_cnt
    log_summary['INFO'] = info_cnt
    return log_summary