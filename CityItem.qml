import QtQuick 1.0

Item {
    id: item

    property alias city: cityLabel.text

    signal clicked()

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
        }
        font.pixelSize: 20
    }

    Rectangle {
        height: 2
        color: "black"
        anchors {
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }
    }

    MouseArea {
        id: mouse
        anchors.fill: parent
        onClicked: item.clicked()
    }
}