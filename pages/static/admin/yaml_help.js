document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".help").forEach(help => {
    const toggle = document.createElement("a");
    toggle.href = "#";
    toggle.textContent = "▶ show formatting help";
    toggle.style.display = "block";
    toggle.style.marginBottom = "4px";

    toggle.addEventListener("click", e => {
      e.preventDefault();
      help.classList.toggle("open");
      toggle.textContent = help.classList.contains("open")
        ? "▼ hide formatting help"
        : "▶ show formatting help";
    });

    help.parentNode.insertBefore(toggle, help);
  });
});

