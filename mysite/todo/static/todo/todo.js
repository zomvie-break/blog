/*
This js file is to add funcitonality to the todo app.
Check that the URLS are correctly set up according to the server.
*/


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

var activeItem = null
var list_snapshot = []

buildList()

function buildList() {
    var wrapper = document.getElementById('list-wrapper')
    // wrapper.innerHTML=''

    var url = '/todo/api/task-list/'

    fetch(url)
        .then((resp) => resp.json())
        .then(function (data) {
            console.log('Data:', data)

            var list = data
            for (var i in list) {
                try {
                    document.getElementById(`data-row-${i}`).remove()
                } catch (error) {
                    console.log('That item does not exist', i)
                }


                var title = `<span class="title">${list[i].title}</span>`
                if (list[i].completed) {
                    title = `<span class="title"><s>${list[i].title}</s></span>`
                }
                var item = `
        <div id="data-row-${i}" class="task-wrapper flex-wrapper">
            <div style="flex: 7">
                ${title}
            </div>
            <div style="flex: 1">
                <button class="btn btn-sm btn-outline-info edit">Edit</button>
            </div>
            <div style="flex: 1">
                <button class="btn btn-sm btn-outline-dark delete">-</button>
            </div>
        </div>
        `
                wrapper.innerHTML += item
            }

            if (list_snapshot.length > list.length) {
                for (let i = list.length; i < list_snapshot.length; i++) {
                    document.getElementById(`data-row-${i}`).remove()
                }
            }
            list_snapshot = list
            for (var i in list) {
                var editBtn = document.getElementsByClassName('edit')[i]
                var title = document.getElementsByClassName('title')[i]
                var deleteBtn = document.getElementsByClassName('delete')[i]

                editBtn.addEventListener('click', (function (item) {
                    return function () {
                        editItem(item)
                    }
                })(list[i]))

                deleteBtn.addEventListener('click', (function (item) {
                    return function () {
                        deleteItem(item)
                    }
                })(list[i]))

                title.addEventListener('click', (function (item) {
                    return function () {
                        strikeUnstrike(item)
                    }
                })(list[i]))

            }
        })
}

var form = document.getElementById('form-wrapper')
form.addEventListener('submit', function (e) {
    e.preventDefault()
    console.log('Form submitted')
    var url = '/todo/api/task-create/'
    var title = document.getElementById('title').value
    if (activeItem != null) {
        var url = `/todo/api/task-update/${activeItem.id}/`
        activeItem = null
    }

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        mode: 'same-origin',
        body: JSON.stringify({
            'title': title
        }),
    }).then(function (response) {
        buildList()
        document.getElementById('form').reset()
    })
})

function editItem(item) {
    console.log('item clicked', item)
    activeItem = item
    // setting the form text to the activeItem's title
    document.getElementById('title').value = activeItem.title
}

function deleteItem(item) {
    console.log('delete clicked', item.id)
    var url = `/todo/api/task-delete/${item.id}/`
    fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        mode: 'same-origin',
    }).then((response) => {
        buildList()
    })
}

function strikeUnstrike(item) {
    console.log('strike clicked')
    item.completed = !item.completed

    var url = `/todo/api/task-update/${item.id}/`
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        mode: 'same-origin',
        body: JSON.stringify({
            'title': item.title,
            'completed': item.completed
        })
    }).then((response) => {
        buildList()
    })
}