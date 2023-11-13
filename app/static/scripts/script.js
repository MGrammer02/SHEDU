cursos = {
    "c1": "Noveno A",
    "c2": "Noveno B",
    "c3": "Decimo A",
    "c4": "Decimo B",
    "c5": "Primero T",
    "c6": "Primero C",
    "c7": "Segundo T",
    "c8": "Segundo C",
    "c9": "Tercero T",
    "c10": "Tercero C"
}
docentes = {
    "01": "José Pinargote",
    "02": "Israel Chumi",
    "03": " Laura Sánchez",
    "04": "Juana Quevedo",
    "05": "Hugo Moncayo",
    "06": "Bryan Vera",
    "07": "Ramon Contreras",
    "08": "William Burgos"
}

materias = {
    "m1": ["Matematicas", "José Pinargote"],
    "m2": ["Lengua y Literatura", "Juana Quevedo"],
    "m3": ["Química", "Hugo Moncayo"],
    "m4": ["Biología", "Hugo Moncayo"],
    "m5": ["Física", "José Pinargote"],
    "m6": ["Emprendimiento y Gestión", "Juana Quevedo"],
    "m7": ["Programación", "Israel Chumi"],
    "m8": ["Diseño Web", "Israel Chumi"],
    "m9": ["Ofimática", "Israel Chumi"],
    "m10": ["Soporte Técnico", "Israel Chumi"],
    "m11": ["Ciencias Naturales", "Yolanda Caicedo"],
    "m12": ["Estudios Sociales", "Yolanda Caicedo"],
    "m13": ["Computación", "Jenny Corral"],
    "m14": ["Historia", "Laura Sánchez"],
    "m15": ["Psicología", "Carla Duarte"]
}

curso_materias = {
    "c1": [[materias["m1"][0], 6], [materias["m2"][0], 8], [materias["m11"][0], 9], [materias["m12"][0], 8], [materias["m13"][0], 9]],
    "c2": [[materias["m1"][0], 6], [materias["m2"][0], 8], [materias["m11"][0], 9], [materias["m12"][0], 8], [materias["m13"][0], 9]],
    "c3": [[materias["m1"][0], 6], [materias["m2"][0], 8], [materias["m11"][0], 9], [materias["m12"][0], 8], [materias["m13"][0], 9]],
    "c4": [[materias["m1"][0], 6], [materias["m2"][0], 8], [materias["m11"][0], 9], [materias["m12"][0], 8], [materias["m13"][0], 9]],
    "c5": [[materias["m1"][0], 3], [materias["m2"][0], 5], [materias["m3"][0], 5], [materias["m4"][0], 10], [materias["m5"][0], 10], [materias["m14"][0], 5], [materias["m7"][0], 2]],
    "c6": [[materias["m1"][0], 3], [materias["m2"][0], 5], [materias["m3"][0], 5], [materias["m4"][0], 10], [materias["m5"][0], 10], [materias["m14"][0], 5], [materias["m7"][0], 2]],
    "c7": [[materias["m1"][0], 3], [materias["m2"][0], 5], [materias["m3"][0], 5], [materias["m4"][0], 10], [materias["m5"][0], 10], [materias["m14"][0], 5], [materias["m15"][0], 2]],
    "c8": [[materias["m1"][0], 3], [materias["m2"][0], 5], [materias["m3"][0], 5], [materias["m4"][0], 10], [materias["m5"][0], 10], [materias["m14"][0], 5], [materias["m15"][0], 2]]
}

curso_docente = {
    "c1": [],
    "c2": [],
    "c3": [],
    "c4": [],
    "c5": [],
    "c6": []
}


var data = [];
for (i = 0; i < cursos.length; i++) {
    indexDict = `c${i + 1}`;
    for (subjet of materias_curso) {
        
    }
    let dictMateriaCurso = {
        
    }
    data[i] = [4, 4, 4, 4];
}

list_cursos = "<ol>";
for (const course in cursos) {
    curso = cursos[course];
    list_cursos += "<li>" + curso + "</li>";
}
list_materias = "<ol>";
for (const subject in materias) {
    materia = materias[subject];
    list_materias += "<li>" + materia + "</li>";
}

document.body.innerHTML += list_cursos + "</ol>";

document.body.innerHTML += list_materias + "</ol>";
let days = {
    "monday": [],

}
let dayHours = 8;
let daysWeek = 5;
for (course_id in cursos) {
    for(day in days) {
        for(let i = 0; i <= dayHours; i++) {
            let subject_random = Math.random() * (materias_curso[course_id].length + 1 - 0);
            days[day][i] = [materias_curso[subject_random], ];
            materias_curso[course][1] -= 1;
        }
    }

}
Math.random() * (max - min) + min;

let row_courses = ""

let tableString = `<table><tr><td></td>${row_courses}</tr></table>`