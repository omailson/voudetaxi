import QtQuick 1.0

Rectangle {
    property alias text: textInput.text

    width: 200
    height: 40

    radius: 5
    border {
        width: 1
        color: "black"
    }
    color: "white"

    TextInput {
        id: textInput
        anchors {
            verticalCenter: parent.verticalCenter
            left: parent.left
            right: parent.right
            leftMargin: 10
            rightMargin: 10
        }
    }
}