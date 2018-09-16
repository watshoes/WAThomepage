import boto3
s3 = boto3.resource("s3")

class Spreadsheet(object):
    entries = {}
    count = 1
    def add_values(self,values):
        with open("beta_testers.txt",'a+') as data:
            entry = values['name1'], values['email1'],values['gender'],values['FavoriteShoe']
            self.entries[self.count] = entry
            print(self.entries)
            data.write("\nentry {}: {}".format(self.count,self.entries[self.count]))
            self.count += 1
        s3.meta.client.upload_file('beta_testers.txt', 'visionprocessing', 'beta_testers.txt')
        print("operation complete")
