# import the libraries
import os
import face_recognition

from PIL import Image, ImageDraw


import matplotlib
import matplotlib.pyplot as plt
from PIL import Image




# make a list of all the available images
images = os.listdir('images')

images = ['Priyanka.jpg', 'Swati.jpg', 'Shagun.jpg', 'Nima.jpg', 'Ashvarya.jpg', 'sukhada.jpg', 'seema.jpg', 'madhura.jpg', 'medha.jpg', 'mugdha.jpg']

# load your image
image_to_be_matched = face_recognition.load_image_file('Mugdha1.jpg')

# encoded the loaded image into a feature vector

image_to_be_matched_encoded = face_recognition.face_encodings(

    image_to_be_matched)[0]

# iterate over each image
for image in images:
    # load the image
    current_image = face_recognition.load_image_file("images/" + image)

# encode the loaded image into a feature vector
    current_image_encoded = face_recognition.face_encodings(current_image)[0]

    # match your image with the image and check if it matches
    result = face_recognition.compare_faces(
        [image_to_be_matched_encoded], current_image_encoded, 0.5)

 # check if it was a match
    if result[0] == True:
        print( "Matched: " + image)
        # create array of encodings and their names
        known_face_encodings = [
            biden_encoding

        ]

        known_face_names = [
            "Mugdha"

        ]

        # load test img to find faces in
        test_images = face_recognition.load_image_file('./images/mugdha.jpg')

        # find faces in test img
        face_locations = face_recognition.face_locations(test_images)
        face_encodings = face_recognition.face_encodings(test_images, face_locations)

        # converts to pil formates
        pil_image = Image.fromarray(test_images)

        # create a ImageDraw instance
        draw = ImageDraw.Draw(pil_image)

        # loop through test img
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "unknown person"

            # if match
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

                # draw box
                draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

                # draw label
                text_width, text_height = draw.textsize(name)
                draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0), outline=(0, 0, 0))
                draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

                # del draw

                # display
                pil_image.show()
    else:
        print("Not matched: " + image)

        known_image = face_recognition.load_image_file('images/mugdha.jpg')
        biden_encoding = face_recognition.face_encodings(known_image)[0]




image_with_faces = face_recognition.load_image_file ('images/mugdha.jpg')

# boxes to faces
face_locations = face_recognition.face_locations(image_with_faces)
#print(face_locations)

# no.of faces in img
print('found {} faces which is match with the test image, And the co-ordinates are '.format(len(face_locations)))

# add grid to the faces
fig, ax = plt.subplots()
ax.imshow(image_with_faces)
ax.grid()
ax.add_patch(matplotlib.patches.Rectangle((415, 325), 105, 125, edgecolor='r', facecolor='none'))
fig.savefig('images/grid.png')

# save the img
for i, (top, right, bottom, left) in enumerate(face_locations):
    print(i+1,top,right,bottom,left)
    face_array = image_with_faces[top:bottom, left:right]
    face_images = Image.fromarray(face_array)



import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", password="manchurian")

print(mydb)

if (mydb):
    print("connection succesful")
else:
    print("connection unsuccesfull")

