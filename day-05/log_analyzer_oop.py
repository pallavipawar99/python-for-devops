import json

class LogAnalyzer:
    
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_summary = {}
    def check_log(self):
        error_cnt = 0
        info_cnt = 0
        warn_cnt = 0
        try:
            with open(self.filename,'r') as file:
                for line in file:
                    if 'error' in line.lower():
                        error_cnt += 1
                    if 'info' in line.lower():
                        info_cnt += 1
                    if 'warning' in line.lower():
                        warn_cnt += 1
        except:
            print("error occured while opening file")
        self.log_summary['ERROR'] = error_cnt
        self.log_summary['WARNING'] = warn_cnt
        self.log_summary['INFO'] = info_cnt
        return self.log_summary

    def write_data_to_file(data,filename):
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
            return True 
        except:
            print("Error Occured while writting data to file")
            return False
        
def main():
    analyzer = LogAnalyzer("app.log")
    data = analyzer.check_log()
    print(data)
    result = analyzer.write_data_to_file(data,"log_summary.json")

    print("Log Analysis Summary:")
    for level, count in result.items():
        print(f"{level}: {count}")


if __name__ == "__main__":
    main()
