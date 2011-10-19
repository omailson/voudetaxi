import QtQuick 1.0

Rectangle {
    property alias text: label.text
    signal clicked()

    color: mouse.pressed ? "grey" : "white"
    radius: 5

    width: 200
    height: 30

    MouseArea {
        id: mouse
        anchors.fill: parent
        onClicked: parent.clicked()
    }

    Text {
        id: label
        anchors.centerIn: parent
    }
}