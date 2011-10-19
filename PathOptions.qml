import QtQuick 1.0

Column {
    id: root

    property alias cityName: cityLabel.text

    signal backPressed()
    signal gotoMap()

    spacing: 5

    Item {
        width: parent.width; height: 50
        Text {
            id: cityLabel
            anchors.left: parent.left
        }

        Link {
            anchors.right: parent.right
            width: 200; height: parent.height

            text: "Ver mais cidades"

            onClicked: root.backPressed();
        }
    }

    Text {
        text: "Origem:"
    }

    TextField { }

    Text {
        text: "Destino:"
    }

    TextField { }

    Button {
        anchors.horizontalCenter: parent.horizontalCenter
        text: "Calcular Tarifa"
        onClicked: parent.gotoMap()
    }
}