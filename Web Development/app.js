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

// ---------- Projects: filters + show more ----------
const filterBtns = document.querySelectorAll(".filter-btn");
const projects = document.querySelectorAll(".portfolio-item");
const showMoreBtn = document.getElementById("show-more");
const VISIBLE_COUNT = 3;          // how many projects show before "Show more"

let currentFilter = "all";
let expanded = false;

// does this project belong to the selected category?
function matchesFilter(item) {
  return currentFilter === "all" || item.dataset.category.split(" ").includes(currentFilter);
}

function updateProjects() {
  let shown = 0;
  let totalMatches = 0;

  projects.forEach((item) => {
    if (matchesFilter(item)) {
      totalMatches++;
      if (expanded || shown < VISIBLE_COUNT) {
        item.classList.remove("hidden");
        shown++;
      } else {
        item.classList.add("hidden");
      }
    } else {
      item.classList.add("hidden");
    }
  });

  // only show the button if there are more than 3 matching projects
  showMoreBtn.style.display = totalMatches > VISIBLE_COUNT ? "" : "none";

  // switch the button text and arrow
  showMoreBtn.querySelector(".btn-text").textContent = expanded ? "Show less" : "Show more projects";
  showMoreBtn.querySelector(".btn-icon i").className = expanded ? "fa-solid fa-arrow-up" : "fa-solid fa-arrow-down";
}

// clicking a filter button
filterBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelector(".filter-btn.active").classList.remove("active");
    btn.classList.add("active");
    currentFilter = btn.dataset.filter;
    expanded = false;             // collapse again when switching category
    updateProjects();
  });
});

// clicking "Show more" / "Show less"
showMoreBtn.addEventListener("click", () => {
  expanded = !expanded;           // flip between true and false
  updateProjects();

  // when collapsing, scroll back up to the projects
  if (!expanded) {
    document.getElementById("portfolio").scrollIntoView({ behavior: "smooth" });
  }
});

updateProjects();                 // set the starting state
// ---------- Blog: show more ----------
const blogCards = document.querySelectorAll(".blog-card");
const blogMoreBtn = document.getElementById("blog-more");
let blogExpanded = false;

function updateBlog() {
  // hide every card after the first 3, unless expanded
  blogCards.forEach((card, index) => {
    card.classList.toggle("hidden", !blogExpanded && index >= VISIBLE_COUNT);
  });

  // only show the button if there are more than 3 posts
  blogMoreBtn.style.display = blogCards.length > VISIBLE_COUNT ? "" : "none";

  // switch the button text and arrow
  blogMoreBtn.querySelector(".btn-text").textContent = blogExpanded ? "Show less" : "Show more articles";
  blogMoreBtn.querySelector(".btn-icon i").className = blogExpanded ? "fa-solid fa-arrow-up" : "fa-solid fa-arrow-down";
}

blogMoreBtn.addEventListener("click", () => {
  blogExpanded = !blogExpanded;
  updateBlog();

  // when collapsing, scroll back up to the blog
  if (!blogExpanded) {
    document.getElementById("blog").scrollIntoView({ behavior: "smooth" });
  }
});

updateBlog();   // set the starting state