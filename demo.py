import face_recognition
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
import os

from PIL import Image, ImageDraw


image_with_faces = face_recognition.load_image_file ('groupdata/group.png')


# boxes to faces
face_locations = face_recognition.face_locations(image_with_faces)
print(face_locations)

# no.of faces in img
print('found {} faces'.format(len(face_locations)))

# add grid to the faces
fig, ax = plt.subplots()
ax.imshow(image_with_faces)
ax.grid()
ax.add_patch(matplotlib.patches.Rectangle((415, 325), 105, 125, edgecolor='r', facecolor='none'))

fig.savefig('groupdata/group1_grid.png')


# save the img
for i, (top, right, bottom, left) in enumerate(face_locations):
    print(i+1,top,right,bottom,left)
    face_array = image_with_faces[top:bottom, left:right]
    face_images = Image.fromarray(face_array)
    face_images.save('{}{}{}'.format('sep_images/Student',i+1,'.jpg'))


images = os.listdir('images')

images = ['Priyanka.jpg', 'Swati.jpg', 'aruna.jpg', 'Shagun.jpg', 'Nima.jpg', 'Ashvarya.jpg', 'sukhada.jpg', 'seema.jpg', 'madhura.jpg', 'medha.jpg', 'samiksha.jpg', 'mugdha.jpg', 'Janhavi.jpg']
print('-----------------------------------------------------------------------------')

#first
print('check for 1st student')

# load your image
image_to_be_matched = face_recognition.load_image_file('sep_images/Student1.jpg')

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
            "Janhavi"

        ]

        # load test img to find faces in
        test_images = face_recognition.load_image_file('./images/Janhavi.jpg')

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

        known_image = face_recognition.load_image_file('images/Janhavi.jpg')
        biden_encoding = face_recognition.face_encodings(known_image)[0]

#second
# load your image
image_to_be_matched = face_recognition.load_image_file('sep_images/Student2.jpg')
print('-----------------------------------------------------------------------------')
print('checking for student2')
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
            "samiksha"

        ]

        # load test img to find faces in
        test_images = face_recognition.load_image_file('./images/samiksha.jpg')

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

        known_image = face_recognition.load_image_file('images/samiksha.jpg')
        biden_encoding = face_recognition.face_encodings(known_image)[0]


#Third
# load your image
image_to_be_matched = face_recognition.load_image_file('images/aruna.jpg')
print('-----------------------------------------------------------------------------')
print('checking for student3')
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
            "Aruna"

        ]

        # load test img to find faces in
        test_images = face_recognition.load_image_file('./images/aruna.jpg')

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

        known_image = face_recognition.load_image_file('images/aruna.jpg')
        biden_encoding = face_recognition.face_encodings(known_image)[0]

#fourth
# load your image
image_to_be_matched = face_recognition.load_image_file('sep_images/Student4.jpg')
print('-----------------------------------------------------------------------------')
print('checking for student4')
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
            "sukhada"

        ]

        # load test img to find faces in
        test_images = face_recognition.load_image_file('./images/sukhada.jpg')

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

        known_image = face_recognition.load_image_file('images/sukhada.jpg')
        biden_encoding = face_recognition.face_encodings(known_image)[0]




'''
import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", password="manchurian")

print(mydb)

if (mydb):
    print("connection succesful")
else:
    print("connection unsuccesfull")

'''
print('-----------------------------------------------------------------------------')
print('Attendance Record..')
import pandas as pd

data = [{
    'NAME': 'Priyanka',
    'ROLL_NO.': 1,
    'STATUS': 'ABSENT'
    },

   {
    'NAME': 'Swati',
    'ROLL_NO.': 2,
    'STATUS': 'ABSENT'
    },
{
    'NAME': 'Aruna',
    'ROLL_NO.': 3,
    'STATUS': 'PRESENT'
    },
{
    'NAME': 'Shagun',
    'ROLL_NO.': 4,
    'STATUS': 'ABSENT'
    },
{
    'NAME': 'Nima',
    'ROLL_NO.': 5,
    'STATUS': 'ABSENT'
    },
{
    'NAME': 'Aishwarya',
    'ROLL_NO.': 6,
    'STATUS': 'ABSENT'
    },
{
    'NAME': 'Sukhada',
    'ROLL_NO.': 7,
    'STATUS': 'PRESENT'
    },
{
    'NAME': 'Seema',
    'ROLL_NO.': 8,
    'STATUS': 'ABSENT'
    },
{
    'NAME': 'Madhura',
    'ROLL_NO.': 9,
    'STATUS': 'ABSENT'
    },
{
    'NAME': 'Medha',
    'ROLL_NO.': 10,
    'STATUS': 'ABSENT'
    },
{
    'NAME': 'Samiksha',
    'ROLL_NO.': 11,
    'STATUS': 'PRESENT'
    },
{
    'NAME': 'Mugdha',
    'ROLL_NO.': 12,
    'STATUS': 'ABSENT'
    },
{
    'NAME': 'Janhavi',
    'ROLL_NO.': 13,
    'STATUS': 'PRESENT'
    },
]

raw_data = {'NAMES': ['Priyanka', 'Swati', 'Aruna', 'Shagun', 'Nima', 'Aishwarya', 'Sukhada', 'Seema', 'Madhura', 'Medha', 'Samiksha', 'Mugdha', 'Janhavi'],
            'ROLL_NO.': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            'STATUS': ['ABSENT', 'ABSENT', 'PRESENT', 'ABSENT', 'ABSENT', 'ABSENT', 'PRESENT', 'ABSENT', 'ABSENT', 'ABSENT', 'PRESENT', 'ABSENT', 'PRESENT']}

df = pd.DataFrame(raw_data, columns = ['NAMES', 'ROLL_NO.', 'STATUS'])
print(df)
'''
color = [(1, .4, .4), (.5, .3, 1)]
plt.pie(df['STATUS'],
        labels=df['ABSENT', 'PRESENT'],
        colors=color,
        autopct='%1.1f%%')

plt.show()
'''