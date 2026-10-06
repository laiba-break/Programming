const sections = document.querySelectorAll(".section");
const navBtns = document.querySelectorAll(".control");

// 1. Click a button → smoothly scroll to its section
navBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    const target = document.getElementById(btn.dataset.id);
    target.scrollIntoView({ behavior: "smooth" });
  });
});

// 2. While scrolling → fade in sections and highlight the matching button
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");

        navBtns.forEach((btn) => {
          btn.classList.toggle("active-btn", btn.dataset.id === entry.target.id);
        });
      }
    });
  },
  // a section counts as "current" when it crosses the middle of the screen
  { rootMargin: "-45% 0px -50% 0px" }
);

sections.forEach((section) => observer.observe(section));