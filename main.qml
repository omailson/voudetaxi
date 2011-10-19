import QtQuick 1.0

Rectangle {
    id: root

    color: "#EBB701"
    width: 360 ; height: 640

    state: "home"

    states: [
        State {
            name: "home"
            PropertyChanges { target: flickable; contentX: 0 }
        },
        State {
            name: "map"
            PropertyChanges { target: flickable; contentX: root.width }
        }
    ]

    Header {
        id: header
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
        }
        height: 50
    }

    Flickable {
        id: flickable

        anchors {
            top: header.bottom
            left: parent.left
            right: parent.right
        }

        contentWidth: width
        contentHeight: childrenRect.height
        flickableDirection: Flickable.VerticalFlick

        Behavior on contentX {
            NumberAnimation { duration: 300; easing.type: Easing.OutQuad }
        }

        Row {
            CityList {
                width: root.width
                onCitySelected: {
                    root.state = "map";
                }
            }
        }
    }
}