import json
from watson_developer_cloud import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import sys
import ibm_watson

authenticator = IAMAuthenticator(
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')  # here goes service api key

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXL'
)


def detect_image(file):
    file = 'path to file/'+file
    with open(file, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0.6',
            classifier_ids='DefaultCustomModel_422700449').get_result()
    #print(json.dumps(classes, indent=2))
    return classes
