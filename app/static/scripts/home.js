
sectionTeachers = document.getElementById("adm-teachers");
sectionSubjects = document.getElementById("adm-subjects");
sectionCourses = document.getElementById("adm-courses");
sectionSheduls = document.getElementById("adm-sheduls");

sectionTeachers.addEventListener("click", ()=>{
    window.location.replace("admin-teachers");
})
sectionSubjects.addEventListener("click", ()=>{
    window.location.replace("admin-subjects")
})
sectionCourses.addEventListener("click", ()=>{
    window.location.replace("admin-courses");
})
sectionSheduls.addEventListener("click", ()=>{
    window.location.replace("admin-sheduls");
})