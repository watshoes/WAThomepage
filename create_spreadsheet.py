import boto3
s3 = boto3.resource("s3")

class Spreadsheet(object):

    def add_values(self,values):
        with open("beta_testers.txt",'a') as data:
            entry = values['name1'], values['email1'],values['gender'],values['FavoriteShoe']
            data.write("\nentry: {}".format( entry))
            s3.meta.client.upload_file('/tmp/beta_testers.txt', 'visionprocessing', 'beta_testers.txt')
            print("operation complete")
