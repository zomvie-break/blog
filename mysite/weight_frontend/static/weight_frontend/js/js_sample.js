const weightContainer = document.getElementById("weight-container")
const baseEndpoint = `${window.location.protocol}//${window.location.host}/api`
var weight_values = []

if (weightContainer) {
    getWeightList()
}


function getFetchOptions() {
    return {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    }
}

function writeToContainer(container, data) {
    container.innerHTML = ""
    if (container) {

        // printing the latest n points
        let dataToPrint = 3
        if (dataToPrint < data.length){
            for (let index = 0; index < dataToPrint; index++) {
                let li = document.createElement('li')
                // print the mass and date of the data point
                li.innerHTML = `${data[index].mass} kgs - ${data[index].created.slice(0,10)}` 
                container.appendChild(li)
            }
        } else {
            let li = document.createElement('li')
            li.innerHTML = "not enough data poinst :("
            container.appendChild(li)        }
    }
}

function getWeightList() {
    const endpoint = `${baseEndpoint}/weight/sample`
    const options = getFetchOptions()

    fetch(endpoint, options)
        .then(response => {
            return response.json()
        })
        .then(data => {
            // write to html
            writeToContainer(weightContainer, data)

            // get the masses and created attributes from the Weight model
            let masses = data.map(x => (x.mass))
            let date_values = data.map(x => (x.created))
            
            // format the dates the way we want using regex
            const myReg = /(\d{4})-(\d{2})-(\d{2})/
            var temp = []
            for (let index = 0; index < date_values.length; index++) {
                // this is the regex being executed, returns an array with the groups
                var results = myReg.exec(date_values[index])
                var newString = results[1] + '-' + results[2] + '-' + results[3]
                temp.push(newString)
            }

            date_values = temp

            // create the chart
            createChartJS(masses, date_values)
        })
}

function createChartJS(masses, date_values) {
    const ctx = document.getElementById("weight-canvas");
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
                    min: "2023-03-13",
                }
            }
        }
    });
}