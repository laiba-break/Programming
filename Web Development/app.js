const sections = document.querySelectorAll(".section");
const sectBtns = document.querySelectorAll(".control");
const allSections = document.querySelector(".main-content");

function pageTransitions() {
  // 1. Highlight the clicked button
  sectBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelector(".active-btn").classList.remove("active-btn");
      btn.classList.add("active-btn");
    });
  });

  allSections.addEventListener("click", (e) => {
    const id = e.target.dataset.id;
    if (id) {
      sections.forEach((section) => section.classList.remove("active"));
      document.getElementById(id).classList.add("active");
    }
  })

}

pageTransitions();