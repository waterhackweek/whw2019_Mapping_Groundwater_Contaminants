let map
let layers

let base_layer = new ol.layer.Tile({
    source: new ol.source.BingMaps({
        key:
            "eLVu8tDRPeQqmBlKAjcw~82nOqZJe2EpKmqd-kQrSmg~AocUZ43djJ-hMBHQdYDyMbT-Enfsk0mtUIGws1WeDuOvjY4EXCH-9OK3edNLDgkc",
        imagerySet: "Road"
    })
})

layers = [base_layer]

map = new ol.Map({
    controls: ol.control.defaults().extend([new ol.control.OverviewMap()]),
    target: "map",
    view: new ol.View({
        center: ol.proj.fromLonLat([-119.4179, 36.7783]),
        zoom: 6,
        minZoom: 2,
        maxZoom: 18
    }),
    layers: layers
})
