import kairos_face

kairos_face.settings.app_id = "cd7690fd"
kairos_face.settings.app_key = "32df39bf4f4e7d9882a9e6e9154ceaca"
kairos_face.enroll_face(url='https://www.biography.com/.image/c_fill,cs_srgb,dpr_1.0,g_face,h_300,q_80,w_300/MTE4MDAzNDEwNzg5ODI4MTEw/barack-obama-12782369-1-402.jpg', subject_id='subject1', gallery_name='a-gallery')


galleries_list = kairos_face.get_galleries_names_list()


print(galleries_list)
