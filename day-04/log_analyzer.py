import json

def check_log(filename):
    error_cnt = 0
    info_cnt = 0
    warn_cnt = 0
    log_summary = {}
    try:
        with open(filename,'r') as file:
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

def write_data_to_file(data):
    try:
        with open("log_summary.json", "w") as f:
            json.dump(data, f, indent=4)
        return True 
    except:
        print("Error Occured while writting data to file")
        return False
     
data = check_log("app.log")
write_data_to_file(data)