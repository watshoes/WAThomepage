import boto3
import requests 

class UploadLambda:
    client = boto3.client("lambda")
    api_gateway_url = "https://7oc64d7ws4.execute-api.us-east-1.amazonaws.com/Stage1/SageMakerFunction"

    def upload(self,file):
        headers = {
            "Content-Type": "multipart/form-data"
        }
        shoe_recognition = requests.post(self.api_gateway_url,headers=headers,data=file)

        return  shoe_recognition.json()

