import PySimpleGUI as sg
import cv2 as cv

textFrame = 0
cameraFrame = 1
CAMERA_0, CAMERA_1 = 0, 1
GREEN = (0, 255, 0)


def create_window():
    sg.theme('Topanga')
    return sg.Window("", [
        [sg.Text("Face tracker",
                 key=textFrame,
                 font=('Any 15'),
                 justification='center',
                 expand_x=True)],
        [sg.Image(key=cameraFrame)]
    ])


def camera_not_detected(window, camera):
    window[textFrame].update("No webcam #{} input detected!".format(camera))


def camera_detected(window, frame, cascade):
    faces = drawFaces(frame, cascade)

    imgbytes = cv.imencode(".png", frame)[1].tobytes()
    window[cameraFrame].update(data=imgbytes)

    facesDetected = len(faces)
    window[textFrame].update("Faces tracked: {}".format(facesDetected))


def drawFaces(frame, cascade):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray,
                                     scaleFactor=1.2,
                                     minNeighbors=3,
                                     flags=0,
                                     minSize=(30, 30))
    for (start, top, width, height) in faces:
        end = start + width
        bottom = top + height
        cv.rectangle(frame, (start, top), (end, bottom), GREEN, 1)
    return faces


if __name__ == '__main__':
    window = create_window()

    cameraNumber = CAMERA_0  # To select different webcams
    video = cv.VideoCapture(cameraNumber)

    frontFaceCascade = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    while True:
        event, _ = window.read(timeout=0)
        if event == sg.WIN_CLOSED:
            break

        isCameraRead, frame = video.read()
        if isCameraRead:
            camera_detected(window, frame, frontFaceCascade)
        else:
            camera_not_detected(window, cameraNumber)

    print("App closed!")
    window.close()
