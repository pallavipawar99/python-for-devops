import json
import argparse

def check_log(filename,level=None):
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
    
    return log_summary,level

def write_data_to_file(data,outfile,level=None):
    try:
        if level != None:
            data = {
                level:data[level]
            }
        with open(outfile, "w") as f:
            json.dump(data, f, indent=4)
        return True 
    except:
        print("Error Occured while writting data to file")
        return False
     

parser = argparse.ArgumentParser(description="Log Analyzer CLI Tool")
parser.add_argument("--file", required=True, help="Path to log file")
parser.add_argument("--out", required=True, help="Output summary file")
parser.add_argument("--level", help="Log level filter (INFO, WARNING, ERROR)")
args = parser.parse_args()
data,level = check_log(args.file,args.level)
write_data_to_file(data,args.out,level)
if level != None:

    print(f"{level} : {data[level]}")
else:
    print(f"{data}")