import kairos_face
import json

kairos_face.settings.app_id = "cd7690fd"
kairos_face.settings.app_key = "32df39bf4f4e7d9882a9e6e9154ceaca"


name_list = kairos_face.get_gallery('a-gallery')["subject_ids"]
print(name_list)
top_five = [0]

for name in name_list:
    recognized_faces = kairos_face.verify_face(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/George_Hotz.jpg/200px-George_Hotz.jpg",subject_id = name ,gallery_name= "a-gallery")
    percent = recognized_faces["images"][0]["transaction"]["confidence"]*100
    top_five.append(percent)
    top_five.sort(reverse=True);
    if len(top_five) > 5:
        del(top_five[5])

print(top_five)


#image, subject_id, gallery_name,




#print(json.dumps(recognized_faces, sort_keys=True, indent=4))
#print(recognized_faces["images"][0]["transaction"]["confidence"]*100)
