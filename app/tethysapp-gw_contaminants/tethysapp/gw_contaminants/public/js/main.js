let map
let layers
let current_layer
let currentVectorLayer

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

init_events()

$("#year-slider").slider({
    min: 1920, // #TODO : Get this from the database
    max: 2019, // #TODO : Get this from the database
    slide: function(event, ui) {
        $("#year").val(ui.value)
        $("#custom-handle").text(ui.value)
    },
    create: function(event, ui) {
        $(this).slider("value", 2018)
        $("#custom-handle").text(2018)
    }
})

$("#year").change(function() {
    $("#year-slider").slider("value", $("#year").val())
    $("#custom-handle").text($("#year").val())
})

$("#year").val($("#year-slider").slider("value"))

function init_events() {
    //Only show the pointer for layers that aren't base layer, shapefile layer and the point/polygon feature layer
    map.on("pointermove", function(evt) {
        if (evt.dragging) {
            return
        }
        var pixel = map.getEventPixel(evt.originalEvent)
        var hit = map.forEachLayerAtPixel(pixel, function(layer) {
            if (layer != layers[0]) {
                current_layer = layer
                return true
            }
        })
        map.getTargetElement().style.cursor = hit ? "pointer" : ""
    })

    // display popup on click
    map.on("singleclick", function(evt) {
        if (map.getTargetElement().style.cursor == "pointer") {
            var feature = map.forEachFeatureAtPixel(
                evt.pixel,
                (feature, layer) => feature
            )

            if (feature) {
                var geometry = feature.getGeometry()
                var coord = geometry.getCoordinates()

                let variables = $("#cont_selector").select2("data")

                variables = variables.map((variable) => variable.id)

                let site_name = feature.get("name"),
                    site_id = feature.get("id"),
                    details_html =
                        `details/?sitename=${encodeURIComponent(site_name)}` +
                        `&siteid=${encodeURIComponent(site_id)}` +
                        `&variables=${encodeURIComponent(variables)}`

                $("#graph").modal("show")
                $("#main-chart").addClass("hidden")

                $("#view-file-loading").removeClass("hidden")
                $.ajax({
                    type: "GET",
                    url: details_html,
                    success: function(data) {
                        $("#view-file-loading").addClass("hidden")
                        $("#main-chart").removeClass("hidden")
                        $("#main-chart").html(data)
                    },
                    error: function(err) {
                        $("#view-file-loading").addClass("hidden")
                        console.log(err)
                        $("#info").html(
                            '<p class="alert alert-danger" style="text-align: center"><strong>An unknown error occurred</strong></p>'
                        )
                        $("#info").removeClass("hidden")

                        setTimeout(function() {
                            $("#info").addClass("hidden")
                        }, 5000)
                    }
                })
            } else {
            }
        }
    })
}

function displayData(data) {
    if (currentVectorLayer) {
        map.removeLayer(currentVectorLayer)
    }
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
    currentVectorLayer = vectorLayer

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
    $("#restAddLoading").removeClass("hidden")
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
