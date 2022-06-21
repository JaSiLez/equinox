const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

const map = L.map('map')

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: attribution}).addTo(map);
const geodata = JSON.parse(document.getElementById('geodata').textContent);

L.Marker.prototype.options.icon = L.icon({
    iconUrl: "/static/reporting/img/sort_desc.png",
    iconSize: [11, 10],
    iconAnchor: [5, 5]
});

let feature = L.geoJSON(geodata).bindPopup(function (layer) {
}).addTo(map);

function onEachFeature(feature, layer) {
    if (feature.properties && feature.properties.nuts_id) {
        layer.bindPopup(feature.properties.nuts_id);
    }
}

L.geoJSON(geodata, {
    onEachFeature: onEachFeature
}).addTo(map);

map.fitBounds(feature.getBounds(), {padding: [100, 100]});
