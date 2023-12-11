
let action = 'upload';
openModal = (modal, edit, subjectId) => {
    if (edit) {
        fetch(`/get_subject/${subjectId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("subject").value = data.subject;
        })
        .catch(error => {
            closeModal(document.querySelector(".modal-container"), document.getElementById("add-info-form"));
            alert(error)
        });
    }
    modal.classList.remove("closed");
}
closeModal = (modal, form) => {
    modal.classList.add("closed");
    form.reset();
}
validateForm = (formToValidate) => {
    let inputs = formToValidate.querySelectorAll("input");
    for(input of inputs) {
        if (input.value == '') {
            input.style.outline = "0.2rem solid #c00";
            return true;
        } else input.style = "";
    }
    return false;
}


document.querySelector(".btn-add").addEventListener("click", (e)=> {
    document.getElementById("title_modal").innerHTML = "Agregar Materia";
    document.getElementById("btn_modal").value = "Subir información"
    action = 'upload';
    openModal(document.querySelector(".modal-container"));
});

btnsEdit = (id)=> {
    document.getElementById("title_modal").innerHTML = "Actualizar Materia";
    document.getElementById("btn_modal").value = "Actualizar"
    action = id;
    openModal(document.querySelector(".modal-container"), true, id);
}

document.querySelector(".icon-tabler-x").addEventListener("click", ()=>{
    closeModal(document.querySelector(".modal-container"), document.getElementById("add-info-form"));
});
document.querySelector(".icon-tabler-x-asign").addEventListener("click", ()=>{
    closeModal(document.querySelector(".modal-asign-container"), document.getElementById("asign-info-form"));
});

let btnUpload = document.getElementById("btn_modal");
btnUpload.addEventListener("click", (e)=>{
    e.preventDefault();
    if (validateForm(document.getElementById("add-info-form"))) {
        return;
    };
    const subjectData = new FormData(document.getElementById("add-info-form"))
    if (action == 'upload') {
        fetch('/add_subject', {
            method: 'POST',
            body: subjectData
          })
          .then(response => response.json())
          .then(data => {
            // Manejar la respuesta del servidor si es necesario
            alert(data['message']);
            closeModal(document.querySelector(".modal-container"), document.getElementById("add-info-form"));
            window.location.reload();
          })
          .catch(error => alert(error['error']));
          closeModal(document.querySelector(".modal-container"), document.getElementById("add-info-form"));
    } else if (action == 'asign') {

    } else {
        fetch(`/edit_subject/${action}`, {
            method: 'PUT',
            body: subjectData
          })
          .then(response => response.json())
          .then(data => {
            // Manejar la respuesta del servidor si es necesario
            alert(data['message']);
            closeModal(document.querySelector(".modal-container"), document.getElementById("add-info-form"));
            window.location.reload();
          })
          .catch(error => alert(error['error']));
          closeModal(document.querySelector(".modal-container"), document.getElementById("add-info-form"));
    }
})

deleteSubject = (id_subject) => {
    if (!confirm("¿Está seguro que sea eliminar esta materia?")) {
        return;
    }
    fetch(`/delete_subject/${id_subject}`, {
        method: 'DELETE',
      })
      .then(response => response.json())
      .then(data => {
        // Manejar la respuesta del servidor si es necesario
        alert(data['message']);
        window.location.reload();
      })
      .catch(error => alert(error['error']));
      closeModal(document.querySelector(".modal-container"), document.getElementById("add-info-form"));
}
