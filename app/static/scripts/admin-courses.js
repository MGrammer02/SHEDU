
let action = 'upload';
openModal = (edit, courseId) => {
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
    document.getElementById("title_modal").innerHTML = "Agregar Curso";
    document.getElementById("btn_modal").value = "Subir información"
    action = 'upload';
    openModal();
})
btnsEdit = (id)=> {
    document.getElementById("title_modal").innerHTML = "Actualizar Curso";
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
    const courseData = new FormData(document.getElementById("add-info-form"))
    if (action == 'upload') {
        fetch('/add_course', {
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
          .catch(error => alert(error['error']));
          closeModal();
    } else {
        fetch(`/edit_course/${action}`, {
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
          .catch(error => alert(error['error']));
          closeModal();
    }
})

deleteCourse = (id_course) => {
    if (!confirm("¿Está seguro que sea eliminar este docente?")) {
        return;
    }
    fetch(`/delete_course/${id_course}`, {
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