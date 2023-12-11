
let action = 'upload';
openModal = (modal, edit) => {
    if (edit) {
        fetch(`/get_shedul_config`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("startWeek").value = data.start_week;
            document.getElementById("endWeek").value = data.end_week;
            document.getElementById("hours").value = data.hours;
            document.getElementById("hoursDuration").value = data.hours_duration;
            document.getElementById("breaks").value = data.breaks;
            document.getElementById("breakDuration").value = data.breaks_duration;
            document.getElementById("breakHours").value = data.breaks_hours;
            document.getElementById("startTime").value = data.start_time;
        })
        .catch(error => {
            closeModal();
            alert(error)
        });
    }
    modal.classList.remove("closed");
}
closeModal = () => {
    document.querySelector(".modal-container").classList.add("closed");
    document.querySelector("#add-info-form").reset();
    if (document.getElementById("breaks-selector")) {document.getElementById("breaks-selector").innerHTML = '';}
}
validateForm = (form) => {
    let inputs = form.querySelectorAll("input");
    for(input of inputs) {
        if (input.value == '') {
            input.style.outline = "0.2rem solid #c00";
            return true;
        } else input.style = "";
    }
    if (document.getElementById("hours").value < 1) {
        document.getElementById("hours").style.outline = "0.2rem solid #c00";
        return true;
    } else document.getElementById("hours").style.outline = "";

    if (document.getElementById("hoursDuration").value < 1) {
        document.getElementById("hoursDuration").style.outline = "0.2rem solid #c00";
        return false;
    } else document.getElementById("hoursDuration").style.outline = "";

    if (document.getElementById("hoursDuration").value < 1) {
        document.getElementById("hoursDuration").style.outline = "0.2rem solid #c00";
        return true;
    } else document.getElementById("hoursDuration").style.outline = "";

    if (document.getElementById("breaks").value < 1) {
        document.getElementById("breaks").style.outline = "0.2rem solid #c00";
        return true;
    } else document.getElementById("breaks").style.outline = "";

    if (document.getElementById("breakDuration").value < 1) {
        document.getElementById("breakDuration").style.outline = "0.2rem solid #c00";
        return true;
    } else document.getElementById("breakDuration").style.outline = "";

    breakHoursArray = document.getElementById("breakHours").value.split(';');
    for (breakHour of breakHoursArray) {
        if(parseInt(breakHour) == NaN) {
            document.getElementById("breakHours").style.outline = "0.2rem solid #c00";
            return true;
        } 
        else document.getElementById("breakHours").style.outline = "";
    }
    return false;
}

document.querySelector(".btn-add").addEventListener("click", (e)=> {
    document.getElementById("title_modal").innerHTML = "Configuración de Horarios";
    document.getElementById("btn_modal").value = "Subir información"
    action = 'upload';
    openModal(document.querySelector(".modal-container"), true);
})

document.querySelector(".icon-tabler-x").addEventListener("click", ()=>{
    closeModal();
})

let btnUpload = document.getElementById("btn_modal");
btnUpload.addEventListener("click", (e)=>{
    e.preventDefault();
    if (validateForm(document.querySelector("#add-info-form"))) {
        return;
    };
    const configData = new FormData(document.getElementById("add-info-form"))
    fetch(`/edit_shedul_config`, {
        method: 'PUT',
        body: configData
      })
      .then(response => response.json())
      .then(data => {
        // Manejar la respuesta del servidor si es necesario
        alert(data['message']);
        closeModal();
        window.location.reload();
      })
      .catch(error => alert(error['error']));
      closeModal();
})

viewPreview = () => {
    if (validateForm(document.getElementById("add-info-form"))) {
        return;
    };
    const configData = new FormData(document.getElementById("add-info-form"))
    fetch(`/preview-config-sheduls`, {
        method: 'POST',
        body: configData
      })
      .then(response => response.json())
      .then(data => {
        console.log(data)
        // Manejar la respuesta del servidor si es necesario
        table = document.createElement("DIV");
        table.innerHTML = `<div id="breaks-selector">
        <table id="breaks-selector-table" style="margin: 1rem auto" class="txt-c">
        </table>
        </div>`;
        document.querySelector(".big-modal").append(table);
        document.getElementById("breaks-selector-table").innerHTML = `<thead id="breaks-selector-head"></thead>
        <tbody  id="breaks-selector-body"></tbody>`
        days = `<tr><th>Hora</th>`;
        for (day of data.days) {
            days += `<th>${day}</th>`;
        }
        document.getElementById("breaks-selector-head").innerHTML = `${days}</tr>`;
        rows = ``;
        for (i = 0; i < (parseInt(document.getElementById("hours").value) + parseInt(document.getElementById("breaks").value)); i++) {
            if (data.breaks.includes(i)) {
                rows += `<tr class="break-hour"><td><b>${data.times[i]}</b></td>`
                for(j in data.days) {
                    rows += `<td><b>Receso</b></td>`
                }
                rows += '</tr>'
            } else {
                rows += `<tr><td>${data.times[i]}</td>`
                for(j in data.days) {
                    rows += `<td>Clase</td>`
                }
                rows += '</tr>'
            }
        }
        rows += `<tr><td><b>${data.times[data.times.length - 1]}<b></td>`;
        for (j in data.days) {
            rows += `<td><b>Salida</b></td>`;
        }
        document.getElementById("breaks-selector-body").innerHTML = `${rows}</tr>`;
      })
      .catch(error => alert(error));
      
}
