//-------------------------------------------
// nav bar js
(function () {
  const mainHeader = document.querySelector(".mainHeader");
  window.addEventListener("scroll", function () {
    const isScrlled = window.scrollY;
    if (isScrlled > 10) {
      mainHeader.classList.add("scrolled");
    } else {
      mainHeader.classList.remove("scrolled");
    }
  });
})();

// ------------------------------------------------
