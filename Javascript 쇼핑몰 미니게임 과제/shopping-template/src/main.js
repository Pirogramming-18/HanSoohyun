
// Fetch the items from the JSON file 
function loadItems() {
    return fetch('data/data.jason')
        .then(response => response.json())
        .then(json => json.items);
}

// main
loadItems()
    .then(items=> {
        console.log(items);
            //displayItems(items);
            //setEventlistners(items)
    })
    .catch(console.log)
