const sections = document.querySelectorAll(".section");
const sectBtns = document.querySelectorAll(".controls");
const sectBtn = document.querSelectorAll(".control");
const allSections = document.querSelectorAll(".main-content");

function PageTransitions(){
    //Button click active class
    for(let i =0; i<sectBtn.length;i++){
        sectBtn[i].addEventListener("click", () =>{
            let currentBtn = document.querySelectorAll(".active-btn");
            currentBtn[0].classList = currentBtn[0].classname.replace("active-btn", "");
            this.classNAme += " active-btn"
        })
    }

    }
}
PageTransitions();
