
let action = 'upload';
openModal = (modal, edit, courseId) => {
    if (edit) {
        fetch(`/get_course/${courseId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("course").value = data.course;
            document.getElementById("contraction").value = data.contraction;
            document.getElementById("parallel").value = data.parallel_id;
            document.getElementById("tutor").value = data.tutor;
        })
        .catch(error => {
            closeModal();
            alert(error['error'])
        });
    }
    modal.classList.remove("closed");
}
closeModal = () => {
    document.querySelector(".modal-container").classList.add("closed");
    document.querySelector("#add-info-form").reset();
    document.getElementById("breaks-selector-table").innerHTML = '';
}
validateForm = (form) => {
    let inputs = form.querySelectorAll("input");
    for(input of inputs) {
        if (input.value == '') {
            input.style.outline = "0.2rem solid #c00";
            return true;
        } else input.style = "";
    }
    return false;
}

document.querySelector(".btn-add").addEventListener("click", (e)=> {
    document.getElementById("title_modal").innerHTML = "Configuración de Horarios";
    document.getElementById("btn_modal").value = "Subir información"
    action = 'upload';
    openModal(document.querySelector(".modal-container"));
})

document.querySelector(".icon-tabler-x").addEventListener("click", ()=>{
    closeModal();
})

let btnUpload = document.getElementById("btn_modal");
btnUpload.addEventListener("click", (e)=>{
    e.preventDefault();
    if (validateForm()) {
        return;
    };
    const configData = new FormData(document.getElementById("add-info-form"))
    fetch(`/edit_shedul-config`, {
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
