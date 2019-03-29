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
$("#year-slider").slider({
    orientation: "vertical",
    min: 1920, // #TODO : Get this from the database
    max: 2019, // #TODO : Get this from the database
    slide: function(event, ui) {
        $("#year").val(ui.value)
    }
})

$("#year").val($("#year-slider").slider("value"))

function displayData(data) {
    $("#restAddLoading").removeClass("hidden")
    let extent = ol.extent.createEmpty()

    let sites = data.result

    sites = sites.map((site) => {
        return {
            type: "Feature",
            geometry: {
                type: "Point",
                coordinates: ol.proj.transform(
                    [parseFloat(site.long), parseFloat(site.lat)],
                    "EPSG:4326",
                    "EPSG:3857"
                )
            },
            properties: {
                name: site.name,
                id: site.stationID
            }
        }
    })

    let sitesGeoJSON = {
        type: "FeatureCollection",
        crs: {
            type: "name",
            properties: {
                name: "EPSG:3857"
            }
        },
        features: sites
    }

    const vectorSource = new ol.source.Vector({
        features: new ol.format.GeoJSON().readFeatures(sitesGeoJSON)
    })

    const vectorLayer = new ol.layer.Vector({
        source: vectorSource,
        style: featureStyle()
    })

    map.addLayer(vectorLayer)
    ol.extent.extend(extent, vectorSource.getExtent())

    vectorLayer.set("selectable", true)

    if (sites.length) {
        map.getView().fit(extent, map.getSize())
        map.updateSize()
    }
    $("#restAddLoading").addClass("hidden")
}

function perform_search() {
    let year = $("#year").val()
    let variables = $("#cont_selector").select2("data")

    variables = variables.map((variable) => variable.id)
    let url = `./get_points/?year=${year}&variables=${variables.join(",")}`

    $.ajax({
        url: encodeURI(url),
        success: displayData,
        error: function(err) {
            console.log(err)
        },
        dataType: "json"
    })
}

function featureStyle() {
    var style = new ol.style.Style({
        image: new ol.style.Circle({
            radius: 6,
            stroke: new ol.style.Stroke({
                color: "white",
                width: 1
            }),
            fill: new ol.style.Fill({
                color: `#${(((1 << 24) * Math.random()) | 0).toString(16)}`
            })
        })
    })
    return style
}
