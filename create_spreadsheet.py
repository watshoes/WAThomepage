import boto3
s3 = boto3.resource("s3")

class Spreadsheet(object):
    entries = {}
    count = 1
    def add_values(self,values):
        with open("beta_testers.txt",'w+') as data:
            entry = values['name1'], values['email1'],values['gender'],values['FavoriteShoe']
            self.entries[self.count] = entry
            data.write("\nentry {}: {}".format(self.count,entries[self.count]))
            self.count += 1
            print(data.read())
            s3.meta.client.upload_file('beta_testers.txt', 'visionprocessing', 'beta_testers.txt')
            print("operation complete")
