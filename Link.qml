import QtQuick 1.0

Text {
    signal clicked()

    // anchors.right: parent.right
    // width: 200; height: parent.height

    color: mouse.pressed ? "white" : "black"

    MouseArea {
        id: mouse
        anchors.fill: parent
        onClicked: parent.clicked();
    }
}