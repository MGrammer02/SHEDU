
sectionTeachers = document.getElementById("adm-teachers");
sectionSubjects = document.getElementById("adm-subjects");
sectionCourses = document.getElementById("adm-courses");
sectionParallels = document.getElementById("adm-parallels");
sectionSheduls = document.getElementById("adm-sheduls");
sectionUsers = document.getElementById("adm-users");
sectionSalutations = document.getElementById("adm-salutations");
sectionCoursesSubjects = document.getElementById("adm-courses-subjects");
sectionConfigSheduls = document.getElementById("config-sheduls");
configSheduls = document.getElementById("conf-sheduls");

createSheduls = document.getElementById("create-sheduls");


createSheduls.addEventListener("click", ()=>{
    window.location.href = "/create-sheduls";
})
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
sectionUsers.addEventListener("click", ()=>{
    window.location.href = "admin-users";
});
sectionCoursesSubjects.addEventListener("click", ()=>{
    window.location.href = "admin-courses-subjects";
});
sectionConfigSheduls.addEventListener("click", ()=>{
    window.location.href = "config-sheduls";
});
configSheduls.addEventListener("click", ()=>{
    window.location.href = "config-sheduls";
});