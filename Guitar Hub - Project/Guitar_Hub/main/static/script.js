//Smooth fade-in for sections
document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll(".section");

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
            }
        });
    } , { threshold: 0.2 });

    sections.forEach(sec => {
        sec.style.opacity = "0";
        sec.style.transform = "translateY(20px)";
        sec.style.transition = "0.6s ease";
        observer.observe(sec);
    });
});

//Small hover animation for nav links
document.querySelectorAll("nav a").forEach(link => {
    link.addEventListener("mouseenter", () => {
        link.style.letterSpacing = "1px";
    });
    link.addEventListener("mouseleave", () => {
        link.style.letterSpacing = "0px";
    });
});