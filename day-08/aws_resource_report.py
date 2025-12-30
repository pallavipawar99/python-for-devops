import boto3
import boto3.session
import json

class AWS_Connection:
    def __init__(self,service):
        self.client = boto3.client(service)
        self.service = service

    def show_data(self):
        if self.service == 's3':
            for i in self.client.list_buckets()['Buckets']:
                print(i['Name'])
            return self.client.list_buckets()['Buckets']
        elif self.service == 'ec2':
            ec2_list = []
            response = self.client.describe_instances()
            for r in response["Reservations"]:
                for t in r["Instances"]:
                    for v in t["Tags"]:
                        ec2_list.append(v['Value'])
            print(ec2_list)
            return ec2_list

    def write_data(self):
        data = self.show_data()
        with open('aws_report.json','w+') as file:
            json.dump(data,file,default=str, indent=4)

    def upload_to_bucket(self):
        self.client.upload_file('aws_report.json', 'pallavi-devops', 'hello2.txt')
        print("file uploaded to s3 successfully")

def main():
    service_input = input("Enter server which u want to connect ")
    obj = AWS_Connection(service_input)
    datashow_input = input("Do u want to show data y/n")
    if datashow_input == 'y':
        obj.show_data()
    datawrite_input = input("Do u want to save data to file y/n")
    if datawrite_input == 'y':
        obj.write_data()
        
    # obj.upload_to_bucket()
    # if user_input == 'EC2':


if __name__ == "__main__":
    main()