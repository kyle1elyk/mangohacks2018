import boto3
import json
import numpy as np
import time

##image capture and preprocess with opencv
##time.sleep(4)
##cap = cv2.VideoCapture(1)
##ret, img = cap.read()
##cv2.imwrite('capture.png',img)
##cap.release()
##time.sleep(4)

s3 = boto3.resource('s3')

##for bucket in s3.buckets.all():
##    print(bucket.name)

##name of the source file	
sourceFile='capture.jpg'

data = open(sourceFile, 'rb')
s3.Bucket('fitmangohacks').put_object(Key=sourceFile, Body=data)


bucket='fitmangohacks'
##targetFile='cody.jpg'

targetFiles = ['muntaser.jpg', 'cody.jpg', 'gabby.jpg', 'jake.jpg', 'kyle.jpg']

client=boto3.client('rekognition')

found = 0
for target in targetFiles:

    response=client.compare_faces(SimilarityThreshold=70, SourceImage={'S3Object':{'Bucket':bucket,'Name':sourceFile}}, TargetImage={'S3Object':{'Bucket':bucket,'Name':target}})

    for faceMatch in response['FaceMatches']:
            position = faceMatch['Face']['BoundingBox']
            confidence = str(faceMatch['Face']['Confidence'])
##            print('The face at ' +
##                       str(position['Left']) + ' ' +
##                       str(position['Top']) +
##                       ' matches with ' + confidence + '% confidence')
##            print('\n recognized file is ' + target)
            print(json.dumps({"match": target, "confidence": confidence}, sort_keys=False))
            found = 1
            break
    if found==1:
        break


if found==0:
    print(json.dumps({"match": "none", "confidence": 0}, sort_keys=False))
  
		   

		   
obj = s3.Object("fitmangohacks", sourceFile)
obj.delete()
