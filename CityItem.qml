import QtQuick 1.0

Item {
    property alias city: cityLabel.text

    Rectangle {
        anchors.fill: parent
        color: "white"
        opacity: 0.4
        visible: mouse.pressed
    }

    Text {
        id: cityLabel
        anchors {
            verticalCenter: parent.verticalCenter
            left: parent.left
        }
        font.pixelSize: 20
    }

    Rectangle {
        height: 2
        color: "black"
        anchors {
            top: cityLabel.bottom
            left: parent.left
            right: parent.right
            margins: 10
        }
    }

    MouseArea {
        id: mouse
        anchors.fill: parent
    }
}