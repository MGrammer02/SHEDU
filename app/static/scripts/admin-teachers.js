
let action = 'upload';
openModal = (edit, teacherId) => {
    if (edit) {
        fetch(`/get_teacher/${teacherId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("firstName").value = data.first_name;
            document.getElementById("secondName").value = data.second_name;
            document.getElementById("firstLastName").value = data.first_lastname;
            document.getElementById("secondLastName").value = data.second_lastname;
            document.getElementById("hours").value = data.work_hours;
            document.getElementById("gender").value = data.gender_id;
            document.getElementById("salutation").value = data.salutation_id;
        })
        .catch(error => {
            closeModal();
            alert(error['error'])
        });
    }
    document.querySelector(".modal-container").classList.remove("closed");
}
closeModal = () => {
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
    document.getElementById("title_modal").innerHTML = "Agregar Docente";
    document.getElementById("btn_modal").value = "Subir información"
    action = 'upload';
    openModal();
})
btnsEdit = (id)=> {
    document.getElementById("title_modal").innerHTML = "Actualizar Docente";
    document.getElementById("btn_modal").value = "Actualizar"
    action = id;
    openModal(true, id);
}
document.querySelector(".icon-tabler-x").addEventListener("click", ()=>{
    closeModal();
})

let btnUpload = document.getElementById("btn_modal");
btnUpload.addEventListener("click", (e)=>{
    e.preventDefault();
    if (validateForm()) {
        return;
    };
    const teacherData = new FormData(document.getElementById("add-info-form"))
    if (action == 'upload') {
        fetch('/add_teacher', {
            method: 'POST',
            body: teacherData
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
    } else {
        fetch(`/edit_teacher/${action}`, {
            method: 'PUT',
            body: teacherData
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
    }
})

deleteTeacher = (id_teacher) => {
    if (!confirm("¿Está seguro que sea eliminar este docente?")) {
        return;
    }
    fetch(`/delete_teacher/${id_teacher}`, {
        method: 'DELETE',
      })
      .then(response => response.json())
      .then(data => {
        // Manejar la respuesta del servidor si es necesario
        alert(data['message']);
        window.location.reload();
      })
      .catch(error => alert(error['error']));
      closeModal();
}