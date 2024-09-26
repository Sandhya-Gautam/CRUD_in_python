const create_data = document.getElementById('create');
const update_data = document.getElementById("update");
const delete_data = document.getElementById("delete");
const create_form = document.getElementById("create_form");
const update_form = document.getElementById("update_form");
const delete_form = document.getElementById("delete_form");
function form_display(event) {
    console.log(clicked)
    if (clicked == create_data) {
        create_form.style.display = "block";
        update_form.style.display = "none";
        delete_form.style.display = "none";
    }
    if (clicked == update_data) {
        update_form.style.display = "block";
        delete_form.style.display = "none";
        create_form.style.display = "none";
    }
    if (clicked == delete_data) {
        delete_form.style.display = "block";
        update_form.style.display = "none";
        create_form.style.display = "none";
    }
}



function create_action(event) {
    const dbname = document.getElementById("dbname");
    data = { "name": dbname.value }
    const apiUrl = 'http://127.0.0.1:8000/create/'
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => {
            const display=document.getElementById("output")
            display.innerHTML=response.json();
        })
    read()

}

function update_action(event) {
    const dbname = document.getElementById("dbname");
    const key = document.getElementById("key");
    const value= document.getElementById("value")
    data = { "name": dbname.value,
        "key":key.value,
        "value":value.value
     }
    const apiUrl = 'http://127.0.0.1:8000/update/'
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => {
            const display=document.getElementById("output")
            display.innerHTML=response.json();
        })
}

function delete_action(event) {
    const dbname = document.getElementById("dbname");
    const key = document.getElementById("key");
    const value= document.getElementById("value")
    data = { "name": dbname.value,
        "key":key.value,
        "value":value.value
     }
    const apiUrl = 'http://127.0.0.1:8000/delete/'
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => {
            const display=document.getElementById("output")
            display.innerHTML=response.json();
        })
}

function read() {
     const apiUrl = 'http://127.0.0.1:8000/get_databases/'
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => {
            const record= document.getElementsByClassName("databases")
            for(i in response){
                
            }
        })
}