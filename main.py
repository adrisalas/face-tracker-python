import PySimpleGUI as sg
import cv2

textFrame = 0
webcamFrame = 1


def createWindow():
    return sg.Window("", [
        [sg.Text("Faces tracked: 0", key=textFrame)],
        [sg.Image(key=webcamFrame)]
    ])


if __name__ == '__main__':
    window = createWindow()
    video = cv2.VideoCapture()

    while True:
        event, _ = window.read(timeout=0)
        if event == sg.WIN_CLOSED:
            break
        else:
            isCameraRead, image = video.read()
            if isCameraRead:
                window[textFrame].update("No webcam input detected!")
            else:
                window[textFrame].update("Webcam detected!")

    print("App closed!")
    window.close()
