
// Fetch the items from the JSON file 
function loadItems() {
    return fetch('data/data.jason')
        .then(response => response.json())
        .then(json => json.items);
}

//  Update the list with the given items //
function displayItems(items) {
    const container = document.querySelector('.items');
    const html = items.map(item => createHTMLString(item));
    container.innerHTML = items.map(item => createHTMLString(item)).join('');

}

