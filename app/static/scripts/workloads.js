
let action = 'upload';
openModal = (edit, courseId, subjectId) => {
    if (edit) {
        fetch(`/get_workload/${courseId}&${subjectId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("subject").setAttribute("disabled", "");
            subject = document.createElement("OPTION");
            subject.value = subjectId;
            subject.text = data.subject;
            subject.id = "editOption";
            document.getElementById("subject").appendChild(subject);
            document.getElementById("subject").value = subjectId;
            document.getElementById("teacher").value = data.teacher;
            document.getElementById("hours").value = data.hours;
        })
        .catch(error => {
            closeModal();
            alert(error)
        });
    }
    document.querySelector(".modal-container").classList.remove("closed");
}
closeModal = () => {
    if (document.getElementById("editOption")) {
        document.getElementById("subject").removeAttribute("disabled");
        editOption.outerHTML = "";
    }
    document.querySelector(".modal-container").classList.add("closed");
    document.querySelector("#add-info-form").reset();
}
validateForm = () => {
    let inputs = document.querySelectorAll("input");
    let selects = document.querySelectorAll("select");
    for(input of inputs) {
        if (input.value == '') {
            input.style.outline = "0.2rem solid #c00";
            return true;
        } else input.style = "";
    }
    for(select of selects) {
        if (select.value == '') {
            select.style.outline = "0.2rem solid #c00";
            return true;
        } else select.style = "";
    }
    return false;
}

document.querySelector(".btn-add").addEventListener("click", (e)=> {
    document.getElementById("title_modal").innerHTML = "Agregar Carga Horaria";
    document.getElementById("btn_modal").value = "Subir información";
    action = 'upload';
    openModal();
})
btnsEdit = (courseId, subjectId)=> {
    document.getElementById("title_modal").innerHTML = "Actualizar Carga Horaria";
    document.getElementById("btn_modal").value = "Actualizar";
    action = [courseId, subjectId];
    openModal(true, courseId, subjectId);
}
document.querySelector(".icon-tabler-x").addEventListener("click", ()=>{
    closeModal();
})
document.querySelector(".icon-tabler-x-asign").addEventListener("click", ()=>{
    document.querySelector(".modal-asign-container").classList.add("closed");
    document.getElementById("asign-info").innerHTML = ''
})

let btnUpload = document.getElementById("btn_modal");
btnUpload.addEventListener("click", (e)=>{
    e.preventDefault();
    if (validateForm()) {
        return;
    };
    const courseData = new FormData(document.getElementById("add-info-form"))
    if (action == 'upload') {
        fetch('/add_workload', {
            method: 'POST',
            body: courseData
          })
          .then(response => response.json())
          .then(data => {
            // Manejar la respuesta del servidor si es necesario
            alert(data['message']);
            closeModal();
            window.location.reload();
          })
          .catch(error => alert(error));
          closeModal();
    } else {
        fetch(`/edit_workload/${action[0]}&${action[1]}`, {
            method: 'PUT',
            body: courseData
          })
          .then(response => response.json())
          .then(data => {
            // Manejar la respuesta del servidor si es necesario
            alert(data['message']);
            closeModal();
            window.location.reload();
          })
          .catch(error => alert(error));
          closeModal();
    }
})

deleteCourseSubject = (courseId, subjectId) => {
    if (!confirm("¿Está seguro que sea eliminar esta carga horaria?")) {
        return;
    }
    fetch(`/delete_workload/${courseId}&${subjectId}`, {
        method: 'DELETE',
      })
      .then(response => response.json())
      .then(data => {
        // Manejar la respuesta del servidor si es necesario
        alert(data['message']);
        window.location.reload();
      })
      .catch(error => alert(error));
      closeModal();
}

verifyWorkloads = (courseId)=> {
    fetch(`/verify_workloads/${courseId}`)
        .then(response => response.json())
        .then(data => {
            document.querySelector(".modal-asign-container").classList.remove("closed");
            if (data.error != undefined) {
                document.getElementById("asign-info").innerHTML = `<span style="color:#d00;font-size:1.8rem;margin:auto">${data.error}</span>`;
                return;
            } else {
                document.getElementById("asign-info").innerHTML = `<span style="color:#0d0;font-size:1.8rem;margin:auto">${data.message}</span>`;
                return;
            }
        })
        .catch(error => {
            closeModal();
            alert(error)
        });
}

