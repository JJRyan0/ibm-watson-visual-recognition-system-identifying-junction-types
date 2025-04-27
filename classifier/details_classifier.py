import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(VisualRecognitionV3.latest_version, api_key='ecccccccccccccccccc')

print(json.dumps(visual_recognition.get_classifier('Junctions_204132427'), indent=2))
