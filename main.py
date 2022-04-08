import PySimpleGUI as sg
import cv2 as cv

textFrame = 0
cameraFrame = 1
CAMERA_0, CAMERA_1 = 0, 1


def create_window():
    return sg.Window("", [
        [sg.Text("Faces tracked: 0", key=textFrame)],
        [sg.Image(key=cameraFrame)]
    ])


def camera_not_detected(window, camera):
    window[textFrame].update("No webcam #{} input detected!".format(camera))


def camera_detected(window):
    window[textFrame].update("Webcam detected!")
    imgbytes = cv.imencode(".png", frame)[1].tobytes()
    window[cameraFrame].update(data=imgbytes)


if __name__ == '__main__':
    camera = CAMERA_0  # To select different webcams
    window = create_window()
    video = cv.VideoCapture(camera)

    while True:
        event, _ = window.read(timeout=0)
        if event == sg.WIN_CLOSED:
            break

        isCameraRead, frame = video.read()
        if isCameraRead:
            camera_detected(window)
        else:
            camera_not_detected(window, camera)

    print("App closed!")
    window.close()
