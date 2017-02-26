import kairos_face
import json

kairos_face.settings.app_id = "cd7690fd"
kairos_face.settings.app_key = "32df39bf4f4e7d9882a9e6e9154ceaca"


recognized_faces = kairos_face.recognize_face(url='http://stanlemmens.nl/wp/wp-content/uploads/2014/07/bill-gates-wealthiest-person.jpg', gallery_name='a-gallery')


print(json.dumps(recognized_faces, sort_keys=True, indent=4))

print(recognized_faces["images"][0]["candidates"][0]["confidence"]*100)
