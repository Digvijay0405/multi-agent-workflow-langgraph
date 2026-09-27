const form = document.getElementById("agentForm");
const loader = document.getElementById("loader");

if(form){
    form.addEventListener("submit",()=>{
        loader.classList.remove("hidden");
    });
}

function copyWork(){
    const work = document.querySelector(".worker pre");

    if(work){
        navigator.clipboard.writeText(work.innerText);
        alert("Worker response copied!");
    }
}