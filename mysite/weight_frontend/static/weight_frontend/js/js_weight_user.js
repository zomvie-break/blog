const baseEndPoint = `${window.location.protocol}//${window.location.host}/api/`;

const weightContainer = document.getElementById("list-weight");
const weightForm = document.getElementById("form-weight");
const csrftoken = Cookies.get("csrftoken");
// variable to let us know if the item is to be editted.
var activeItem = false;

if (weightForm) {
    weightForm.addEventListener("submit", handleWeightForm);
    handleDateInput();
}

if (weightContainer) {
    handleWeightContainer();
}

function handleWeightContainer() {
    let endPoint = `${baseEndPoint}weight/`
    var options = {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        }
    }
    fetch(endPoint, options)
        .then(response => {
            return response.json();
        })
        .then(data => {
            writeToWeightList(data, "mass");
            createChartJS(data)
        })
}

function handleWeightForm(event) {
    event.preventDefault();
    let endPoint = `${baseEndPoint}weight/`
    // handleDateInput(); // set input date to todays
    // get form element from document
    var formData = new FormData(weightForm);
    // output as an object
    // console.log("object.fromEntries:", Object.fromEntries(formData));
    // create a dictionary type object from the form element
    var formProps = Object.fromEntries(formData);

    if (activeItem) {
        handleWeightUpdate();
        handleDateInput();
    } else {
        var options = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": formProps.csrfmiddlewaretoken,
            },
            body: JSON.stringify({
                mass: formProps.mass,
                created: formProps.created,
            })
        }
        fetch(endPoint, options)
            .then(function (response) {
                handleWeightContainer();
            })
    }

}

function writeToWeightList(data, key) {

    // select the container in the document
    let ul0 = document.getElementById("list-weight");
    ul0.remove();

    let ul = document.createElement("ul");
    ul.setAttribute("id", "list-weight");
    

    // iterate over the data, up to dataToPrint times
    let dataToPrint = 5;
    if (dataToPrint > data.length) {
        dataToPrint = data.length;
    }
    // write a small description to the p element before listing
    addListDescription(dataToPrint);


    for (let index = 0; index < dataToPrint ; index++) {

        // create an element li and add the mass to it.
        let li = document.createElement("li");
        li.innerHTML = data[index][key] + "kg - " + data[index].created.slice(0, 10) + "\t";

        // primary key of the weight object.
        // useful for editing and deleting endpoints
        let pk = data[index]["pk"];

        // create a span element to handle update of the weight object
        let span_delete = document.createElement("span");
        span_delete.innerHTML = "&#10539;";
        span_delete.addEventListener("click", function () {
            handleWeightDelete(pk);
        });


        // create a span element to handle update of the weight object
        let span_update = document.createElement("span");
        span_update.innerHTML = "&#9998;";

        span_update.addEventListener("click", function () {
            toBeUpdated(pk);
        });

        // append the span items to the li item and then
        // append the li item to the ul item in document
        li.appendChild(span_delete);
        li.appendChild(span_update);
        ul.appendChild(li);
    }
    // append to parent div#list-weight-container
    document.getElementById("list-weight-container").appendChild(ul);

    // clear input field
    var formMass = document.getElementById("form-mass");
    formMass.value = '';
}

function handleWeightDelete(pk) {
    const destroyEndPoint = `${baseEndPoint}weight/${pk}/delete/`;

    var options = {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken,
        }
    }
    fetch(destroyEndPoint, options)
        .then(function (response) {
            handleWeightContainer();
        })
        .catch(err => console.log(err));
}

async function handleWeightDetail(pk) {
    
    var detailEndPoint = `${baseEndPoint}weight/${pk}/`
    var options = {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        }
    }
    try {
        const response = await fetch(detailEndPoint, options);

        const weight = await response.json();
        return weight
    } catch(err){
        console.log(err)
    }
}

async function toBeUpdated(pk) {
    // I'm calling the detail function here because I can!
    const weight = await handleWeightDetail(pk);
    var formMass = document.getElementById("form-mass");
    var formCreated = document.getElementById("form-created");

    // set the form inputs to the values of the get request
    formMass.value = weight.mass;
    formCreated.value = weight.created.slice(0,10);

    // set the activeItem to the current primary key of the item to be updated
    activeItem = pk;

}

function handleWeightUpdate() {
    var formData = new FormData(weightForm);
    // output as an object
    // console.log("object.fromEntries:", Object.fromEntries(formData));
    var formProps = Object.fromEntries(formData);

    var updateEndPoint = `${baseEndPoint}weight/${activeItem}/update/`

    var options = {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": formProps.csrfmiddlewaretoken,
        },
        body: JSON.stringify({
            mass: formProps.mass,
            created: formProps.created,
        })
    }

    activeItem = false;

    fetch(updateEndPoint, options)
        .then(function (response) {
            handleWeightContainer();
            return response.json();
        })
        .catch(err => {
            console.log("err", err);
        })
}

function addListDescription(nItems) {
    p = document.getElementById("p-list-weight");
    p.innerHTML = `Here are your last ${nItems} item(s).`;
}

function handleDateInput(item = null) {
    d = document.getElementById("form-created");
    if (!item) {
        var date = new Date();

        var day = date.getDate();
        var month = date.getMonth() + 1;
        var year = date.getFullYear();

        if (month < 10) month = "0" + month;
        if (day < 10) day = "0" + day;

        var today = year + "-" + month + "-" + day;

        d.value = today;
    } else {
        if (item) {
            d.value = item.created;
        }
    }



}

function createChartJS(data) {
    // selecting the canvas to delete it and reappend it
    let ctx0 = document.getElementById("weight-canvas");
    ctx0.remove();

    let ctx = document.createElement("canvas");
    ctx.setAttribute("id", "weight-canvas");

    document.getElementById("chart-container").appendChild(ctx);

    data = data.sort((a,b) => (a.created > b.created) ? 1: -1)

    // let's get the mass and dates from the data
    let masses = data.map(function (point) {
        return point.mass;
    });
    let date_values = data.map(function (point) {
        return point.created.slice(0, 10);
    });


    
    // need the spread operator (...) to pass the array as arguments
    let temp_min = Math.min(...masses) - 1
    let temp_max = Math.max(...masses) + 1

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: date_values,
            datasets: [{
                label: 'kgs',
                data: masses,
                borderWidth: 1,
                pointStyle: 'circle',
                pointRadius: 2,
                pointHoverRadius: 3
            }]
        },
        options: {
            scales: {
                y: {
                    suggestedMin: temp_min,
                    suggestedMax: temp_max,
                    title: {
                        display: true,
                        text: "Mass [kg]"
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: "Date"
                    },
                    type: "time",
                    time: {
                        // unit: 'day',
                        // tooltipFormat: 'MMM DD',
                        displayFormats: {
                            day: 'yyyy MMM dd'
                        }
                        // min: "2023-03-13",
                    }
                }
            }
        }
    })
}
