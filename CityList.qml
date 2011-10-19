import QtQuick 1.0

Rectangle {
    id: root

    color: "#EBB701"
    width: 360 ; height: 640

    Flickable {
        anchors.fill: parent
        contentWidth: width
        contentHeight: childrenRect.height

        Image {
            id: header
            anchors {
                top: parent.top
                topMargin: 20
                horizontalCenter: parent.horizontalCenter
            }
            source: "logo.gif"
        }

        Column {
            id: column

            anchors {
                top: header.bottom
                left: parent.left
                right: parent.right
                margins: 20
            }
            height: childrenRect.height

            spacing: 5

            Repeater {
                id: list

                model: CityListModel { }

                delegate: CityItem {
                    width: column.width
                    height: 40
                    city: cityName
                }
            }
        }
    }
}