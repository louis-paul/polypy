import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.0
import QtQuick.Window 2.2

ApplicationWindow {
    title: qsTr("PolyPy")
    width: 428
    height: 365

    FileDialog {
        id: fileDialog
        title: "Please choose a file to transform"
        onAccepted: {
            image.source = fileDialog.fileUrl;
        }
    }

    Button {
        x: 10
        y: 328
        width: 205
        height: 26
        text: qsTr("Open an image")
        onClicked: {
            fileDialog.open()
        }
    }

    Rectangle {
        id: imageBorder
        x: 13
        y: 12
        width: 401
        height: 254
        color: "#00000000"
        border.width: 1
    }

    Image {
        id: image
        x: 14
        y: 13
        z: 1
        width: 400
        height: 253
        antialiasing: true
        fillMode: Image.PreserveAspectFit
    }

    Text {
        id: triangleCountLabel
        x: 14
        y: 276
        text: qsTr("Triangle count")
        font.pixelSize: 12
    }

    TextField {
        id: triangleCountInput
        x: 101
        y: 272
        width: 55
        height: 22
        text: triangleCountSlider.value.toFixed(2) * 2500
        validator: IntValidator{bottom: 0; top: 2500;}
    }

    Slider {
        id: triangleCountSlider
        x: 162
        y: 273
        width: 252
        height: 22
        value: 0.06
    }

    Text {
        id: edgeRatioLabel
        x: 14
        y: 304
        text: qsTr("Edge ratio")
        font.pixelSize: 12
    }

    TextField {
        id: edgeRatioInput
        x: 101
        y: 300
        width: 55
        height: 22
        text: edgeRatioSlider.value.toFixed(2)/10 + 0.9
        validator: RegExpValidator{regExp: /0\.9[0-9][0-9]?/;}
    }

    Slider {
        id: edgeRatioSlider
        x: 162
        y: 301
        width: 252
        height: 22
        value: 0.8
    }

    Button {
        id: generateButton
        x: 214
        y: 328
        width: 205
        height: 26
        text: qsTr("Generate")
    }
}
