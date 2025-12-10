// Smooth Scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth'
      });
    }
  });
});

// Toggle visibility of subcategory lists
document.querySelectorAll('.toggle-section').forEach(btn => {
  btn.addEventListener('click', () => {
    const targetId = btn.dataset.target;
    const content = document.getElementById(targetId);
    if (content) {
      content.classList.toggle('hidden');
    }
  });
});

// randomiser page
// Show/hide category dropdown depending on choice_type
const countryRadio = document.querySelector('input[value="country"]');
const recipeRadio = document.querySelector('input[value="recipe"]');
const categorySelect = document.getElementById('category-select');

function toggleCategory() {
    categorySelect.style.display = recipeRadio.checked ? "block" : "none";
}

countryRadio.addEventListener("change", toggleCategory);
recipeRadio.addEventListener("change", toggleCategory);
toggleCategory();