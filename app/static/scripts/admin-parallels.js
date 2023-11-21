
let action = 'upload';
openModal = (edit, parallelId) => {
    if (edit) {
        fetch(`/get_parallel/${parallelId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("parallel").value = data.parallel;
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
    for(input of inputs) {
        if (input.value == '') {
            input.style.outline = "0.2rem solid #c00";
            return true;
        } else input.style = "";
    }
    return false;
}


document.querySelector(".btn-add").addEventListener("click", (e)=> {
    document.getElementById("title_modal").innerHTML = "Agregar Paralelo";
    document.getElementById("btn_modal").value = "Subir información"
    action = 'upload';
    openModal();
})
btnsEdit = (id)=> {
    document.getElementById("title_modal").innerHTML = "Actualizar Paralelo";
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
    const parallelData = new FormData(document.getElementById("add-info-form"))
    if (action == 'upload') {
        fetch('/add_parallel', {
            method: 'POST',
            body: parallelData
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
        fetch(`/edit_parallel/${action}`, {
            method: 'PUT',
            body: parallelData
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

deleteParallel = (id_parallel) => {
    if (!confirm("¿Está seguro que sea eliminar esta materia?")) {
        return;
    }
    fetch(`/delete_parallel/${id_parallel}`, {
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