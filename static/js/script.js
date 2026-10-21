/* =========================================================
   Grunge-style Portfolio — vanilla JavaScript
   ========================================================= */
(function () {
  "use strict";

  /* ---------- Barcodes ---------- */
  // Turns any text into a deterministic barcode-like SVG.
  function makeBarcode(el) {
    var text = el.getAttribute("data-barcode") || "NISHAN";
    var seed = 0;
    for (var i = 0; i < text.length; i++) seed = (seed * 31 + text.charCodeAt(i)) >>> 0;
    function rand() {
      seed = (seed * 1664525 + 1013904223) >>> 0;
      return seed / 4294967296;
    }
    var bars = "";
    var x = 0;
    var width = 136;
    while (x < width) {
      var w = 1 + Math.floor(rand() * 3);
      var gap = 1 + Math.floor(rand() * 2);
      if (x + w > width) break;
      bars += '<rect x="' + x + '" y="0" width="' + w + '" height="28"/>';
      x += w + gap;
    }
    el.innerHTML =
      '<svg viewBox="0 0 ' + width + ' 28" preserveAspectRatio="none" fill="currentColor" aria-hidden="true">' +
      bars + "</svg><small>" + text + "</small>";
  }
  document.querySelectorAll("[data-barcode]").forEach(makeBarcode);

  /* ---------- Accordion ---------- */
  document.querySelectorAll(".acc-item").forEach(function (item) {
    var head = item.querySelector(".acc-head");
    if (!head) return;
    head.setAttribute("aria-expanded", item.classList.contains("open") ? "true" : "false");
    head.addEventListener("click", function () {
      var group = item.closest("[data-accordion]");
      var willOpen = !item.classList.contains("open");
      if (group && group.getAttribute("data-accordion") === "single") {
        group.querySelectorAll(".acc-item.open").forEach(function (other) {
          other.classList.remove("open");
          other.querySelector(".acc-head").setAttribute("aria-expanded", "false");
        });
      }
      item.classList.toggle("open", willOpen);
      head.setAttribute("aria-expanded", willOpen ? "true" : "false");
    });
  });

  /* ---------- Active nav link ---------- */
  var page = (location.pathname.split("/").pop() || "index.html").toLowerCase();
  document.querySelectorAll(".nav a").forEach(function (a) {
    var href = (a.getAttribute("href") || "").toLowerCase();
    if (href === page || (page === "" && href === "index.html")) {
      a.setAttribute("aria-current", "page");
    }
  });

  /* ---------- Mobile menu ---------- */
  var nav = document.querySelector(".nav");
  var toggle = document.querySelector(".nav-toggle");
  if (nav && toggle) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.textContent = open ? "Close" : "Menu";
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    nav.querySelectorAll("ul a").forEach(function (a) {
      a.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.textContent = "Menu";
        document.body.style.overflow = "";
      });
    });
  }

  /* ---------- Scroll reveal ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  
})();
