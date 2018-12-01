import face_recognition
from PIL import Image, ImageDraw


modiji_image = face_recognition.load_image_file("Modiji.jpeg")
modiji_face_encoding = face_recognition.face_encodings(modiji_image)[0]

putin_image = face_recognition.load_image_file("Putin.jpeg")
putin_face_encoding = face_recognition.face_encodings(putin_image)[0]

trump_image = face_recognition.load_image_file("Trump.jpg")
trump_face_encoding = face_recognition.face_encodings(trump_image)[0]

necil_image = face_recognition.load_image_file("Necil.jpg")
necil_face_encoding = face_recognition.face_encodings(necil_image)[0]

tom_image = face_recognition.load_image_file("Tom.jpg")
tom_face_encoding = face_recognition.face_encodings(tom_image)[0]

radhika_image = face_recognition.load_image_file("Radhika.jpg")
radhika_face_encoding = face_recognition.face_encodings(radhika_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    modiji_face_encoding,
    putin_face_encoding,
    trump_face_encoding,
    necil_face_encoding,
    tom_face_encoding,
    radhika_face_encoding
]
known_face_names = [
    "Narendra Modi",
    "Vladimir Putin",
    "Donald Trump",
    "Necil Dabre",
    "Thomas Cruise",
    "Radhika Vartak"
]
unknown_image = face_recognition.load_image_file("r3.jpg") #filename with its directory

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

pil_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(pil_image)
pil_image1 = Image.fromarray(unknown_image)
draw1=ImageDraw.Draw(pil_image1)


for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
    draw1.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


del draw,draw1
#pil_image1.show()
pil_image.show()


