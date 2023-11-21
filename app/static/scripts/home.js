
sectionTeachers = document.getElementById("adm-teachers");
sectionSubjects = document.getElementById("adm-subjects");
sectionCourses = document.getElementById("adm-courses");
sectionParallels = document.getElementById("adm-parallels");
sectionSheduls = document.getElementById("adm-sheduls");
sectionUsers = document.getElementById("adm-users");
sectionSalutations = document.getElementById("adm-salutations");

sectionTeachers.addEventListener("click", ()=>{
    window.location.href = "/admin-teachers";
});
sectionSubjects.addEventListener("click", ()=>{
    window.location.href = "admin-subjects";
});
sectionCourses.addEventListener("click", ()=>{
    window.location.href = "admin-courses";
});
sectionParallels.addEventListener("click", ()=>{
    window.location.href = "admin-parallels";
});
sectionSheduls.addEventListener("click", ()=>{
    window.location.href = "admin-sheduls";
});
sectionUsers.addEventListener("click", ()=>{
    window.location.href = "admin-users";
})
sectionSalutations.addEventListener("click", ()=>{
    window.location.href = "admin-salutations";
});