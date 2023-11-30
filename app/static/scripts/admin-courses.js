
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
    openModal(document.querySelector(".modal-container"));
})
btnsEdit = (id)=> {
    document.getElementById("title_modal").innerHTML = "Actualizar Curso";
    document.getElementById("btn_modal").value = "Actualizar"
    action = id;
    openModal(document.querySelector(".modal-container"), true, id);
}
document.querySelector(".icon-tabler-x").addEventListener("click", ()=>{
    closeModal();
})
document.querySelector(".icon-tabler-x-asign").addEventListener("click", ()=>{
    document.querySelector(".modal-asign-container").classList.add("closed");
    document.getElementById("asign-info").innerHTML = '';
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
    if (!confirm("¿Está seguro que sea eliminar este curso :o?")) {
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


adminWorkloads = (courseID) => {
    window.open(`/workloads/${courseID}`);
}

viewInfo = (courseId) => {
    openModal(document.querySelector(".modal-asign-container"));
    fetch(`/get_course/${courseId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("title_modal-asign").innerHTML =  `${data.contraction} ${data.parallel} | Materias:`;
        })
    document.querySelector(".btn-href").setAttribute("onclick", `adminWorkloads(${courseId})`);
    fetch(`/get_course-info/${courseId}`)
        .then(response => response.json())
        .then(data => {
            if (data.error != undefined) {
                document.getElementById("asign-info").innerHTML = `<span style="color:#d00;font-size:1.8rem;margin:auto">${data.error}</span>`;
                return;
            }
            block = document.createDocumentFragment("DIV");
            block.innerHTML = "";
            for (info of data.course_info) {
                block.innerHTML += `<div class="flex-aj-c flex-column"><span class="span-course">${info[0]}</span> <span class="span-subject">${info[1]}</span></div>`;
            }
            document.getElementById("asign-info").innerHTML = block.innerHTML;
        })
        .catch(error => {
            document.querySelector(".modal-asign-container").classList.add("closed");
            document.getElementById("asign-info").innerHTML = '';
            console.log(error);
            alert(error.error)
        });
}