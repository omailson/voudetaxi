import QtQuick 1.0

Column {
    id: column

    signal citySelected(string city);

    height: childrenRect.height

    Repeater {
        id: list

        model: CityListModel { }

        delegate: CityItem {
            width: column.width
            height: 40
            city: cityName
            onClicked: {
                citySelected(cityName);

            }
        }
    }
}