import face_recognition
import cv2

#Load a photo
my_photo = face_recognition.load_image_file("myphoto.jpg")
know_face_encoding = face_recognition.face_encodings(myphoto)[0]

#Start Webcam
video_capture = cv2.VideoCapture(0)

while True:
    #Capture a frame from the video/camera
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    
    #Delect face locations and encodings in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    #If face is detected or capture
    if face_encoding:
        print("Detecting face...")
        
        #Check if the detected face maches the photo face
        matches = face_recognition.compare_faces([know_face_encoding], face_encodings[0])
        
        if maches[0]:
            print("Face recognized!")
        else:
            print("Fake person!")
            
    #Display the Video feed
    cv2.imshow('Video',frame)
    
    #How to exit or quit from the aPP
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break
    
#Release webcam and close window
video_capture.release()
cv2.destroyAllwindow()