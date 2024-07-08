document.addEventListener("DOMContentLoaded", function() {
    var menuBtn = document.getElementById("menu-btn");
    var mobileMenu = document.getElementById("mobile-menu");
    var sidebarBackdrop = document.getElementById("sidebar-backdrop");
    var homeBtn = document.getElementById("sidebar-home");

    if (menuBtn && mobileMenu && sidebarBackdrop) {
        menuBtn.addEventListener("click", function() {
            mobileMenu.classList.toggle("visible");
            sidebarBackdrop.classList.toggle("visible");
        });

        sidebarBackdrop.addEventListener("click", function() {
            mobileMenu.classList.remove("visible");
            sidebarBackdrop.classList.remove("visible");
        });

        if (homeBtn) {
            homeBtn.addEventListener("click", function() {
                window.location.href = "{% url 'index' %}";
            });
        }
    }
});
