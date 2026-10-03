/* ==========================================================================
   Lumina — núcleo: rolagem suave, navegação, menu, componentes e formulários
   ========================================================================== */

(function () {
  "use strict";

  const root = document.documentElement;
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const hasGsap = typeof window.gsap !== "undefined";

  if (!hasGsap || reduceMotion) root.classList.add("no-gsap");

  const LUMINA = {
    reduceMotion,
    lenis: null,
    ready: false,
  };
  window.LUMINA = LUMINA;

  /* --- Utilidades -------------------------------------------------------- */
  const $ = (selector, scope) => (scope || document).querySelector(selector);
  const $$ = (selector, scope) => Array.from((scope || document).querySelectorAll(selector));
  const clamp = (value, min, max) => Math.min(Math.max(value, min), max);
  const lerp = (a, b, t) => a + (b - a) * t;
  LUMINA.$ = $;
  LUMINA.$$ = $$;

  function lockScroll(locked) {
    if (LUMINA.lenis) {
      locked ? LUMINA.lenis.stop() : LUMINA.lenis.start();
    }
    document.body.classList.toggle("is-locked", locked);
  }
  LUMINA.lockScroll = lockScroll;

  /* --- Rolagem suave (Lenis) -------------------------------------------- */
  function initSmoothScroll() {
    if (reduceMotion || typeof window.Lenis === "undefined") return;

    const lenis = new window.Lenis({
      duration: 1.15,
      lerp: 0.09,
      smoothWheel: true,
      wheelMultiplier: 1,
      touchMultiplier: 1.6,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    });

    if (hasGsap && window.ScrollTrigger) {
      lenis.on("scroll", window.ScrollTrigger.update);
      window.gsap.ticker.add((time) => lenis.raf(time * 1000));
      window.gsap.ticker.lagSmoothing(0);
    } else {
      const raf = (time) => {
        lenis.raf(time);
        requestAnimationFrame(raf);
      };
      requestAnimationFrame(raf);
    }

    LUMINA.lenis = lenis;

    // Rolagem suave para links internos
    $$('a[href^="#"], a[href*="/#"]').forEach((link) => {
      link.addEventListener("click", (event) => {
        const hash = link.getAttribute("href");
        if (!hash || hash === "#") return;
        const targetId = hash.includes("/#") ? hash.split("#")[1] : hash.slice(1);
        const target = document.getElementById(targetId);
        if (!target) return;
        event.preventDefault();
        const headerOffset = parseFloat(
          getComputedStyle(root).getPropertyValue("--header-h")
        ) || 84;
        lenis.scrollTo(target, { offset: -headerOffset, duration: 1.4 });
      });
    });
  }

  /* --- Preloader --------------------------------------------------------- */
  function initPreloader() {
    const preloader = $(".preloader");
    const counter = $(".preloader__counter", preloader);
    const bar = $(".preloader__bar span", preloader);

    const finish = () => {
      if (LUMINA.ready) return;
      LUMINA.ready = true;
      document.dispatchEvent(new CustomEvent("lumina:ready"));
    };

    if (!preloader) {
      finish();
      return;
    }

    document.body.classList.add("is-locked");

    if (!hasGsap || reduceMotion) {
      preloader.remove();
      document.body.classList.remove("is-locked");
      finish();
      return;
    }

    const { gsap } = window;
    const value = { current: 0 };

    const tl = gsap.timeline({
      onComplete: () => {
        preloader.remove();
        document.body.classList.remove("is-locked");
        finish();
      },
    });

    tl.from(".preloader__mark path, .preloader__mark circle", {
      strokeDashoffset: 0,
      duration: 1.4,
      ease: "power2.inOut",
      stagger: 0.08,
    })
      .to(".preloader__wordmark", { opacity: 1, y: 0, duration: 0.6 }, "-=0.9")
      .to(
        value,
        {
          current: 100,
          duration: 1.5,
          ease: "power2.inOut",
          onUpdate: () => {
            const shown = Math.round(value.current);
            if (counter) counter.textContent = String(shown).padStart(3, "0");
            if (bar) bar.style.transform = `scaleX(${value.current / 100})`;
          },
        },
        "-=0.5"
      )
      .to(".preloader__inner", { opacity: 0, y: -18, duration: 0.5 }, "-=0.15")
      .to(".preloader", {
        clipPath: "inset(0% 0% 100% 0%)",
        duration: 0.9,
        ease: "power4.inOut",
      })
      .to(".preloader__panel", { scaleY: 0, duration: 0.9, ease: "power4.inOut" }, "<");
  }

  /* --- Cabeçalho e progresso -------------------------------------------- */
  function initHeader() {
    const header = $(".header");
    const progress = $(".scroll-progress span");
    if (!header) return;

    let ticking = false;
    const update = () => {
      const y = window.scrollY;
      header.classList.toggle("is-scrolled", y > 40);

      const toTop = $(".to-top");
      if (toTop) toTop.classList.toggle("is-visible", y > window.innerHeight * 0.9);

      if (progress) {
        const max = document.body.scrollHeight - window.innerHeight;
        progress.style.transform = `scaleX(${max > 0 ? clamp(y / max, 0, 1) : 0})`;
      }
      ticking = false;
    };

    window.addEventListener(
      "scroll",
      () => {
        if (!ticking) {
          requestAnimationFrame(update);
          ticking = true;
        }
      },
      { passive: true }
    );
    update();

    // Marca o link de navegação ativo
    const links = $$(".header__link");
    const sections = links
      .map((link) => {
        const hash = link.getAttribute("href");
        if (!hash) return null;
        const id = hash.includes("#") ? hash.split("#")[1] : "";
        const section = id ? document.getElementById(id) : null;
        return section ? { link, section } : null;
      })
      .filter(Boolean);

    if (sections.length && window.IntersectionObserver) {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            links.forEach((link) => link.classList.remove("is-active"));
            const match = sections.find((item) => item.section === entry.target);
            if (match) match.link.classList.add("is-active");
          });
        },
        { rootMargin: "-45% 0px -50% 0px" }
      );
      sections.forEach((item) => observer.observe(item.section));
    }
  }

  /* --- Menu mobile ------------------------------------------------------- */
  function initMenu() {
    const toggle = $(".menu-toggle");
    const menu = $(".mobile-menu");
    if (!toggle || !menu) return;

    const links = $$(".mobile-menu__link", menu);
    if (hasGsap && !reduceMotion) {
      window.gsap.set(links, { opacity: 0, y: 28 });
    }

    const setOpen = (open) => {
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
      menu.classList.toggle("is-open", open);
      document.querySelector(".header").classList.toggle("is-menu-open", open);
      lockScroll(open);

      if (open && hasGsap && !reduceMotion) {
        window.gsap.to(links, {
          opacity: 1,
          y: 0,
          duration: 0.75,
          ease: "power3.out",
          stagger: 0.07,
          delay: 0.18,
        });
      }
    };

    toggle.addEventListener("click", () => {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });

    $$('a[href]', menu).forEach((link) => link.addEventListener("click", () => setOpen(false)));

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setOpen(false);
        toggle.focus();
      }
    });
  }

  /* --- Acordeão de perguntas -------------------------------------------- */
  function initFaq() {
    $$(".faq__trigger").forEach((trigger) => {
      trigger.addEventListener("click", () => {
        const item = trigger.closest(".faq__item");
        const isOpen = item.classList.contains("is-open");

        $$(".faq__item.is-open").forEach((open) => {
          if (open !== item) {
            open.classList.remove("is-open");
            open.querySelector(".faq__trigger").setAttribute("aria-expanded", "false");
          }
        });

        item.classList.toggle("is-open", !isOpen);
        trigger.setAttribute("aria-expanded", String(!isOpen));
      });
    });
  }

  /* --- Lightbox da galeria ---------------------------------------------- */
  function initLightbox() {
    const items = $$("[data-lightbox]");
    const lightbox = $(".lightbox");
    if (!items.length || !lightbox) return;

    const image = $(".lightbox__figure img", lightbox);
    const caption = $(".lightbox__caption", lightbox);
    let index = 0;

    const show = (next) => {
      index = (next + items.length) % items.length;
      const item = items[index];
      image.src = item.dataset.lightbox;
      image.alt = item.dataset.alt || "";
      caption.textContent = `${String(index + 1).padStart(2, "0")} / ${String(
        items.length
      ).padStart(2, "0")} — ${item.dataset.caption || ""}`;
    };

    const open = (next) => {
      show(next);
      lightbox.classList.add("is-open");
      lockScroll(true);
      $(".lightbox__close", lightbox).focus();
    };

    const close = () => {
      lightbox.classList.remove("is-open");
      lockScroll(false);
    };

    items.forEach((item, i) => item.addEventListener("click", () => open(i)));
    $(".lightbox__close", lightbox).addEventListener("click", close);
    $(".lightbox__nav--prev", lightbox).addEventListener("click", () => show(index - 1));
    $(".lightbox__nav--next", lightbox).addEventListener("click", () => show(index + 1));
    lightbox.addEventListener("click", (event) => {
      if (event.target === lightbox) close();
    });
    document.addEventListener("keydown", (event) => {
      if (!lightbox.classList.contains("is-open")) return;
      if (event.key === "Escape") close();
      if (event.key === "ArrowLeft") show(index - 1);
      if (event.key === "ArrowRight") show(index + 1);
    });
  }

  /* --- Carrossel de depoimentos ----------------------------------------- */
  function initCarousel() {
    $$("[data-carousel]").forEach((carousel) => {
      const track = $("[data-carousel-track]", carousel);
      const progress = $("[data-carousel-progress]", carousel);
      if (!track) return;

      const updateProgress = () => {
        const max = track.scrollWidth - track.clientWidth;
        const ratio = max > 0 ? track.scrollLeft / max : 0;
        if (progress) progress.style.setProperty("--progress", `${0.15 + ratio * 0.85}`);
      };

      const scrollByCard = (direction) => {
        const card = track.firstElementChild;
        const step = card ? card.getBoundingClientRect().width + 16 : track.clientWidth * 0.7;
        track.scrollBy({ left: step * direction, behavior: "smooth" });
      };

      $("[data-carousel-prev]", carousel)?.addEventListener("click", () => scrollByCard(-1));
      $("[data-carousel-next]", carousel)?.addEventListener("click", () => scrollByCard(1));
      track.addEventListener("scroll", updateProgress, { passive: true });
      window.addEventListener("resize", updateProgress);
      updateProgress();
    });
  }

  /* --- Cursor customizado ------------------------------------------------ */
  function initCursor() {
    if (reduceMotion || !hasGsap) return;
    if (!window.matchMedia("(hover: hover) and (pointer: fine)").matches) return;

    const dot = $(".cursor-dot");
    const ring = $(".cursor-ring");
    const label = $(".cursor-ring span");
    if (!dot || !ring) return;

    const { gsap } = window;
    const dotX = gsap.quickTo(dot, "x", { duration: 0.16, ease: "power3" });
    const dotY = gsap.quickTo(dot, "y", { duration: 0.16, ease: "power3" });
    const ringX = gsap.quickTo(ring, "x", { duration: 0.42, ease: "power3" });
    const ringY = gsap.quickTo(ring, "y", { duration: 0.42, ease: "power3" });

    let cursorX = -100;
    let cursorY = -100;
    let ringXPos = -100;
    let ringYPos = -100;
    let raf = null;

    const render = () => {
      ringXPos = lerp(ringXPos, cursorX, 0.16);
      ringYPos = lerp(ringYPos, cursorY, 0.16);
      ringX(ringXPos);
      ringY(ringYPos);
      raf = requestAnimationFrame(render);
    };

    window.addEventListener(
      "pointermove",
      (event) => {
        cursorX = event.clientX;
        cursorY = event.clientY;
        dotX(event.clientX);
        dotY(event.clientY);
        if (!raf) raf = requestAnimationFrame(render);
        if (!dot.classList.contains("is-ready")) {
          dot.classList.add("is-ready");
          ring.classList.add("is-ready");
        }
      },
      { passive: true }
    );

    document.addEventListener("pointerover", (event) => {
      const target = event.target.closest(
        "a, button, [role='button'], .gallery-grid__item, .service-card, .team-card"
      );
      if (!target) return;
      ring.classList.add("is-hover");
      const custom = target.dataset.cursor;
      if (label) label.textContent = custom || "";
    });

    document.addEventListener("pointerout", (event) => {
      const target = event.target.closest(
        "a, button, [role='button'], .gallery-grid__item, .service-card, .team-card"
      );
      if (!target) return;
      ring.classList.remove("is-hover");
    });

    document.addEventListener("mouseleave", () => {
      dot.classList.remove("is-ready");
      ring.classList.remove("is-ready");
    });
  }

  /* --- Botões magnéticos -------------------------------------------------- */
  function initMagnetic() {
    if (reduceMotion || !hasGsap) return;
    if (!window.matchMedia("(hover: hover) and (pointer: fine)").matches) return;

    const { gsap } = window;
    $$("[data-magnetic]").forEach((element) => {
      const strength = parseFloat(element.dataset.magnetic) || 0.28;

      element.addEventListener("pointermove", (event) => {
        const rect = element.getBoundingClientRect();
        const x = event.clientX - (rect.left + rect.width / 2);
        const y = event.clientY - (rect.top + rect.height / 2);
        gsap.to(element, { x: x * strength, y: y * strength, duration: 0.5, ease: "power3.out" });
      });

      element.addEventListener("pointerleave", () => {
        gsap.to(element, { x: 0, y: 0, duration: 0.75, ease: "elastic.out(1, 0.4)" });
      });
    });
  }

  /* --- Voltar ao topo ----------------------------------------------------- */
  function initToTop() {
    const button = $(".to-top");
    if (!button) return;
    button.addEventListener("click", () => {
      if (LUMINA.lenis) LUMINA.lenis.scrollTo(0, { duration: 1.6 });
      else window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* --- Formulário de agendamento ----------------------------------------- */
  function initForms() {
    const form = $("[data-form]");
    if (!form) return;

    const status = $("[data-form-status]", form);
    const submit = $("[data-form-submit]", form);

    const setStatus = (type, message) => {
      if (!status) return;
      status.className = `form-status form-status--${type} is-visible`;
      status.innerHTML = message;
    };

    const clearErrors = () => {
      $$(".field.has-error", form).forEach((field) => field.classList.remove("has-error"));
      if (status) status.classList.remove("is-visible");
    };

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      clearErrors();

      if (submit) {
        submit.disabled = true;
        submit.dataset.originalText = submit.textContent;
        submit.innerHTML = '<span class="loader-dots"><span></span><span></span><span></span></span>';
      }

      try {
        const response = await fetch(form.action, {
          method: "POST",
          body: new FormData(form),
          headers: { "X-Requested-With": "fetch" },
        });
        const data = await response.json();

        if (data.ok) {
          form.reset();
          setStatus("ok", `<strong>Recebido.</strong> ${data.mensagem}`);
          if (hasGsap) {
            window.gsap.fromTo(
              status,
              { y: 12, opacity: 0 },
              { y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }
            );
          }
          status.scrollIntoView({ behavior: "smooth", block: "center" });
        } else {
          Object.entries(data.erros || {}).forEach(([name, message]) => {
            const field = form.querySelector(`[name="${name}"]`)?.closest(".field");
            if (!field) return;
            field.classList.add("has-error");
            const error = field.querySelector(".field__error");
            if (error) error.textContent = message;
          });
          setStatus("error", "<strong>Quase lá.</strong> Confira os campos destacados e tente de novo.");
        }
      } catch (error) {
        setStatus(
          "error",
          "<strong>Ops.</strong> Não conseguimos enviar agora. Tente novamente ou ligue para (11) 4003-8922."
        );
      } finally {
        if (submit) {
          submit.disabled = false;
          submit.textContent = submit.dataset.originalText || "Enviar";
        }
      }
    });
  }

  /* --- Newsletter (demo) -------------------------------------------------- */
  function initNewsletter() {
    $$("[data-newsletter]").forEach((form) => {
      form.addEventListener("submit", (event) => {
        event.preventDefault();
        const input = form.querySelector("input");
        const button = form.querySelector("button");
        if (!input || !button) return;
        const original = button.textContent;
        button.textContent = "Pronto!";
        button.disabled = true;
        input.value = "";
        setTimeout(() => {
          button.textContent = original;
          button.disabled = false;
        }, 2600);
      });
    });
  }

  /* --- Bootstrap --------------------------------------------------------- */
  function boot() {
    initSmoothScroll();
    initHeader();
    initMenu();
    initFaq();
    initLightbox();
    initCarousel();
    initCursor();
    initMagnetic();
    initToTop();
    initForms();
    initNewsletter();
    initPreloader();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();