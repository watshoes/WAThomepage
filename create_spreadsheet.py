import boto3
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pprint import pprint

from googleapiclient import discovery
s3 = boto3.resource("s3")
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
#https://docs.google.com/spreadsheets/d/1sMXpRIQhO1_COatlez0RTvaioIqXD5TM5NCMOTDIqLQ/edit?usp=sharing
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1sMXpRIQhO1_COatlez0RTvaioIqXD5TM5NCMOTDIqLQ'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'
class Spreadsheet(object):
    entries = {}
    count = 1
    def add_values(self,values):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('sheets', 'v4', http=creds.authorize(Http()))



        # The ID of the spreadsheet to update.
        spreadsheet_id = '1sMXpRIQhO1_COatlez0RTvaioIqXD5TM5NCMOTDIqLQ'  # TODO: Update placeholder value.

        # The A1 notation of a range to search for a logical table of data.
        # Values will be appended after the last row of the table.
        range_ = 'Sheet1!A1:B2:C3:D4'  # TODO: Update placeholder value.

        # How the input data should be interpreted.
        value_input_option = 'RAW'  # TODO: Update placeholder value.

        # How the input data should be inserted.
        insert_data_option = 'INSERT_ROWS'  # TODO: Update placeholder value.
        vals = []
        vals.append(values['name1'])
        vals.append(values['email1'])
        vals.append(values['gender'])
        vals.append(values['FavoriteShoe'])
        value_range_body = {
            # TODO: Add desired entries to the request body.
            "values" : [vals]
        }

        request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
        response = request.execute()

        # TODO: Change code below to process the `response` dict:
        pprint(response)
        # with open("beta_testers.txt",'a+') as data:
        #     entry = values['name1'], values['email1'],values['gender'],values['FavoriteShoe']
        #     self.entries[self.count] = entry
        #     print(self.entries)
        #     data.write("\nentry {}: {}".format(self.count,self.entries[self.count]))
        #     self.count += 1
        # s3.meta.client.upload_file('beta_testers.txt', 'visionprocessing', 'beta_testers.txt')
        # print("operation complete")
