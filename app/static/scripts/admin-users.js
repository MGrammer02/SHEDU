
let action = 'upload';
openModal = (edit, userId) => {
    if (edit) {
        fetch(`/get_user/${userId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("teacher").setAttribute("disabled", "");
            user = document.createElement("OPTION");
            user.value = userId;
            user.text = data.teacher;
            user.id = "editOption";
            document.getElementById("teacher").appendChild(user);
            document.getElementById("teacher").value = data.teacher_id;
            document.getElementById("user").value = data.user;
            document.getElementById("password").value = data.password;
            document.getElementById("admin").checked = data.admin;
        })
        .catch(error => {
            closeModal();
            console.log(error)
            alert(error.error)
        });
    }
    document.querySelector(".modal-container").classList.remove("closed");
}
closeModal = () => {
    if (document.getElementById("editOption")) {
        document.getElementById("teacher").removeAttribute("disabled");
        editOption.outerHTML = "";
    }
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
    if (document.getElementById("password").value != document.getElementById("confirm_password").value) {
        alert("Las contraseñas no coinciden >:I");
        document.getElementById("password").style.outline = "0.2rem solid #c00";
        document.getElementById("confirm_password").style.outline = "0.2rem solid #c00";
        return true;
    } else {
        document.getElementById("password").style.outline = "";
        document.getElementById("confirm_password").style.outline = "";
    }
    if (document.getElementById("password").value.length < 8) {
        alert("La contraseña debe tener mínimo 8 carácteres :c");
        document.getElementById("password").style.outline = "0.2rem solid #c00";
        return true;
    }
    if (document.getElementById("password").value.length > 15) {
        alert("La contraseña no debe contener más de 15 carácteres >:I. No se pase de seguro");
        document.getElementById("password").style.outline = "0.2rem solid #c00";
        return true;
    }
    return false;
}


document.querySelector(".btn-add").addEventListener("click", (e)=> {
    document.getElementById("title_modal").innerHTML = "Agregar Usuario";
    document.getElementById("btn_modal").value = "Subir información"
    action = 'upload';
    openModal();
})
btnsEdit = (id)=> {
    document.getElementById("title_modal").innerHTML = "Actualizar Usuario";
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
    const userData = new FormData(document.getElementById("add-info-form"));
    userData.admin = document.getElementById("admin").checked
    if (action == 'upload') {
        fetch('/add_user', {
            method: 'POST',
            body: userData
          })
          .then(response => response.json())
          .then(data => {
            // Manejar la respuesta del servidor si es necesario
            alert(data['message']);
            closeModal();
            window.location.reload();
          })
          .catch(error => alert(error.error));
          closeModal();
    } else {
        fetch(`/edit_user/${action}`, {
            method: 'PUT',
            body: userData
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

deleteUser = (id_user) => {
    if (!confirm("¿Está seguro que sea eliminar este usuario?")) {
        return;
    }
    fetch(`/delete_user/${id_user}`, {
        method: 'DELETE',
      })
      .then(response => response.json())
      .then(data => {
        // Manejar la respuesta del servidor si es necesario
        alert(data['message']);
        window.location.reload();
        })
      .catch(error => {
        alert(error['error'])
        });
        if(!(error['error'] == 'userexists')) closeModal();
}

function showPasswords() {
    document.querySelector(".btn-show-pwd").setAttribute("onclick", "hidePasswords()");
    document.querySelector(".icon-tabler-eye-closed").outerHTML = `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-eye" width="28" height="28" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
    <path d="M10 12a2 2 0 1 0 4 0a2 2 0 0 0 -4 0" />
    <path d="M21 12c-2.4 4 -5.4 6 -9 6c-3.6 0 -6.6 -2 -9 -6c2.4 -4 5.4 -6 9 -6c3.6 0 6.6 2 9 6" />
    </svg>`;
    document.getElementById("password").type = "text";
    document.getElementById("confirm_password").type = "text";
    document.getElementById("btn-show-pwd__span").textContent = "Ocultar contraseñas";
}
function hidePasswords() {
    document.querySelector(".btn-show-pwd").setAttribute("onclick", "showPasswords()");
    document.querySelector(".icon-tabler-eye").outerHTML = `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-eye-closed" width="28" height="28" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
    <path d="M21 9c-2.4 2.667 -5.4 4 -9 4c-3.6 0 -6.6 -1.333 -9 -4" />
    <path d="M3 15l2.5 -3.8" />
    <path d="M21 14.976l-2.492 -3.776" />
    <path d="M9 17l.5 -4" />
    <path d="M15 17l-.5 -4" />
    </svg>`;
    document.getElementById("password").type = "password";
    document.getElementById("confirm_password").type = "password";
    document.getElementById("btn-show-pwd__span").textContent = "Ver contraseñas";
}