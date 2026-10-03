/* ==========================================================================
   Lumina — camada de animação: GSAP + ScrollTrigger
   ========================================================================== */

(function () {
  "use strict";

  const { $, $$ } = window.LUMINA || {};
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!window.gsap || reduceMotion || !$) {
    document.documentElement.classList.add("no-gsap");
    return;
  }

  const gsap = window.gsap;
  const ScrollTrigger = window.ScrollTrigger;
  const CustomEase = window.CustomEase;

  gsap.registerPlugin(ScrollTrigger);

  if (CustomEase) {
    CustomEase.create("luminaOut", "M0,0 C0.16,1 0.3,1 1,1");
    CustomEase.create("luminaInOut", "M0,0 C0.65,0 0.35,1 1,1");
  }
  const EASE = CustomEase ? "luminaOut" : "power3.out";

  /* --- Quebra de texto --------------------------------------------------- */
  function splitWords(element) {
    if (!element || element.dataset.splitDone) return [];
    element.dataset.splitDone = "true";

    const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);

    nodes.forEach((node) => {
      const text = node.textContent;
      if (!text.trim()) return;
      const fragment = document.createDocumentFragment();
      text.split(/(\s+)/).forEach((chunk) => {
        if (!chunk) return;
        if (/^\s+$/.test(chunk)) {
          fragment.appendChild(document.createTextNode(" "));
          return;
        }
        const word = document.createElement("span");
        word.className = "word";
        const inner = document.createElement("span");
        inner.className = "word__inner";
        inner.textContent = chunk;
        word.appendChild(inner);
        fragment.appendChild(word);
      });
      node.parentNode.replaceChild(fragment, node);
    });

    return $$(".word__inner", element);
  }

  function splitLines(element) {
    // `splitWords` já registra `splitDone`; duplicar a guarda aqui fazia o
    // `splitLines` devolver sempre vazio e o título nunca era quebrado.
    if (!element) return [];
    const words = splitWords(element);
    if (!words.length) return [];
    element.dataset.splitDone = "true";

    const lines = [];
    let currentTop = null;
    let bucket = [];

    words.forEach((word) => {
      const top = Math.round(word.offsetTop);
      if (currentTop === null || Math.abs(top - currentTop) > 4) {
        if (bucket.length) lines.push(bucket);
        bucket = [];
        currentTop = top;
      }
      bucket.push(word);
    });
    if (bucket.length) lines.push(bucket);

    const wrappers = lines.map((bucketWords) => {
      const line = document.createElement("span");
      line.className = "line";
      const inner = document.createElement("span");
      inner.className = "line__inner";
      const text = bucketWords.map((w) => w.textContent).join(" ");
      inner.textContent = text;
      line.appendChild(inner);
      return line;
    });

    element.innerHTML = "";
    wrappers.forEach((line) => element.appendChild(line));
    return $$(".line__inner", element);
  }

  /* --- Entrada do hero --------------------------------------------------- */
  function heroIntro() {
    const hero = $(".hero");
    if (!hero) return;

    const items = $$("[data-hero-item]", hero);
    const mediaMain = $(".hero__media-main", hero);
    const mediaSide = $$(".hero__media-side", hero);
    const floaters = $$(".hero__floating", hero);
    const seal = $(".seal", hero);

    const tl = gsap.timeline({
      defaults: { ease: EASE, duration: 1 },
      delay: 0.15,
    });

    tl.to(items, { opacity: 1, y: 0, duration: 0.9, stagger: 0.09 }, 0.25);

    if (mediaMain) {
      tl.fromTo(
        mediaMain,
        { clipPath: "inset(0% 0% 100% 0%)", scale: 1.04 },
        { clipPath: "inset(0% 0% 0% 0%)", scale: 1, duration: 1.5 },
        0.2
      );
    }

    mediaSide.forEach((side, index) => {
      tl.fromTo(
        side,
        { clipPath: "inset(100% 0% 0% 0%)", scale: 1.06 },
        { clipPath: "inset(0% 0% 0% 0%)", scale: 1, duration: 1.3 },
        0.45 + index * 0.12
      );
    });

    floaters.forEach((floater, index) => {
      tl.fromTo(
        floater,
        { opacity: 0, y: 30, scale: 0.92 },
        { opacity: 1, y: 0, scale: 1, duration: 0.9 },
        0.85 + index * 0.14
      );
      gsap.to(floater, {
        y: index % 2 ? 16 : -16,
        duration: 2.6 + index * 0.4,
        repeat: -1,
        yoyo: true,
        ease: "sine.inOut",
        delay: index * 0.3,
      });
    });

    if (seal) {
      tl.fromTo(seal, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 1 }, 0.9);
    }

    // parallax suave do hero ao rolar
    gsap.to(".hero__inner", {
      yPercent: -8,
      ease: "none",
      scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: 0.6 },
    });

    gsap.to(".hero__bg", {
      yPercent: 12,
      ease: "none",
      scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: 0.8 },
    });
  }

  /* --- Revelações genéricas ---------------------------------------------- */
  function initReveals() {
    $$("[data-reveal]").forEach((element) => {
      if (element.closest(".hero")) return;
      const variant = element.dataset.reveal || "up";
      const clip = variant === "clip";

      gsap.to(element, {
        opacity: 1,
        x: 0,
        y: 0,
        scale: 1,
        duration: clip ? 1.35 : 1.05,
        ease: EASE,
        scrollTrigger: {
          trigger: element,
          start: "top 88%",
          once: true,
        },
        onStart: () => {
          if (!clip) return;
          gsap.fromTo(
            element,
            { clipPath: "inset(0% 0% 100% 0%)" },
            { clipPath: "inset(0% 0% 0% 0%)", duration: 1.35, ease: EASE }
          );
          const media = element.querySelector("img");
          if (media) gsap.fromTo(media, { scale: 1.25 }, { scale: 1, duration: 1.6, ease: EASE });
        },
      });
    });

    // Estágios em grupo
    $$("[data-reveal-group]").forEach((group) => {
      const children = $$(":scope > *", group);
      if (!children.length) return;
      gsap.from(children, {
        opacity: 0,
        y: 34,
        duration: 0.9,
        ease: EASE,
        stagger: 0.09,
        scrollTrigger: { trigger: group, start: "top 84%", once: true },
      });
      children.forEach((child) => child.removeAttribute("data-reveal"));
    });
  }

  /* --- Títulos com quebra em linhas --------------------------------------
     A quebra por linhas depende da métrica real da fonte e da largura do
     container. Medir antes do `document.fonts.ready` (ou sem refazer a
     medida quando a tela muda de largura) deixa cada `.line` com o texto
     re-quebrado dentro de uma caixa `overflow: hidden` — e o título aparece
     cortado. Por isso: espera as fontes, requebra ao redimensionar e, em
     telas estreitas, usa quebra por palavra (sem máscara, não há como cortar). */

  const SPLIT_NARROW = "(max-width: 47.99rem)";
  const originalMarkup = new WeakMap();
  const splitTweens = new WeakMap();

  const rememberMarkup = (element) => {
    if (!originalMarkup.has(element)) originalMarkup.set(element, element.innerHTML);
    return originalMarkup.get(element);
  };

  const resetSplit = (element) => {
    const tween = splitTweens.get(element);
    if (tween) {
      if (tween.scrollTrigger) tween.scrollTrigger.kill();
      tween.kill();
      splitTweens.delete(element);
    }
    element.innerHTML = originalMarkup.get(element) || element.innerHTML;
    delete element.dataset.splitDone;
  };

  const animateParts = (element, parts, offset, stagger, start) => {
    if (!parts.length) return;
    gsap.set(parts, { yPercent: offset });
    splitTweens.set(
      element,
      gsap.to(parts, {
        yPercent: 0,
        duration: 1.1,
        ease: EASE,
        stagger,
        scrollTrigger: { trigger: element, start, once: true },
      })
    );
  };

  function splitHeading(heading) {
    rememberMarkup(heading);
    resetSplit(heading);

    if (window.matchMedia(SPLIT_NARROW).matches) {
      // Sem caixa de máscara: cada palavra sobe no lugar e nada é cortado.
      animateParts(heading, splitWords(heading), 70, 0.035, "top 88%");
      return;
    }

    animateParts(heading, splitLines(heading), 105, 0.09, "top 86%");
  }

  function initSplitHeadings() {
    const headings = $$("[data-split], [data-split-words]");

    headings.forEach((heading) => rememberMarkup(heading));

    const build = () => {
      $$("[data-split]").forEach(splitHeading);

      // Títulos com marcação inline (<em>, <br>) — quebra por palavras para
      // preservar o estilo do conteúdo.
      $$("[data-split-words]").forEach((heading) => {
        resetSplit(heading);
        animateParts(heading, splitWords(heading), 115, 0.05, "top 88%");
      });

      ScrollTrigger.refresh();
    };

    const waitForFonts = () => {
      if (!document.fonts || !document.fonts.ready) return Promise.resolve();
      const ready = document.fonts.ready;
      return Promise.race([ready, new Promise((resolve) => setTimeout(resolve, 1500))]);
    };

    let lastWidth = window.innerWidth;
    let timer = null;

    const scheduleBuild = () => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        const width = window.innerWidth;
        // Requebra só quando a largura muda o bastante para alterar as linhas
        // (evita refazer a cada resize do address bar no mobile).
        if (Math.abs(width - lastWidth) < 80) return;
        lastWidth = width;
        waitForFonts().then(build);
      }, 220);
    };

    waitForFonts().then(build);

    window.addEventListener("resize", scheduleBuild);
    window.addEventListener("orientationchange", scheduleBuild);
  }

  /* --- Contadores -------------------------------------------------------- */
  function initCounters() {
    $$("[data-counter]").forEach((element) => {
      const target = parseFloat(element.dataset.counter);
      const decimals = parseInt(element.dataset.decimals || "0", 10);
      const suffix = element.dataset.suffix || "";
      const prefix = element.dataset.prefix || "";
      const state = { value: 0 };

      gsap.to(state, {
        value: target,
        duration: 2,
        ease: "power2.out",
        scrollTrigger: { trigger: element, start: "top 88%", once: true },
        onUpdate: () => {
          element.textContent =
            prefix +
            state.value.toLocaleString("pt-BR", {
              minimumFractionDigits: decimals,
              maximumFractionDigits: decimals,
            }) +
            suffix;
        },
      });
    });
  }

  /* --- Parallax ---------------------------------------------------------- */
  function initParallax() {
    $$("[data-parallax]").forEach((element) => {
      const speed = parseFloat(element.dataset.speed || "0.1");
      gsap.fromTo(
        element,
        { yPercent: -speed * 100 },
        {
          yPercent: speed * 100,
          ease: "none",
          scrollTrigger: {
            trigger: element.closest("section") || element,
            start: "top bottom",
            end: "bottom top",
            scrub: 0.8,
          },
        }
      );
    });
  }

  /* --- Brilhos de fundo -------------------------------------------------- */
  function initGlows() {
    $$(".glow").forEach((glow, index) => {
      const speed = index % 2 ? 12 : -12;
      gsap.to(glow, {
        yPercent: speed,
        xPercent: index % 3 === 0 ? 6 : -4,
        ease: "none",
        scrollTrigger: {
          trigger: glow.closest("section") || glow,
          start: "top bottom",
          end: "bottom top",
          scrub: 1,
        },
      });
    });
  }

  /* --- Serviços em rolagem horizontal ------------------------------------ */
  function initHorizontal() {
    const wrap = $("[data-horizontal-wrap]");
    const track = $("[data-horizontal-track]");
    if (!wrap || !track) return;

    const desktop = window.matchMedia("(min-width: 62rem)");

    const build = () => {
      if (desktop.matches) {
        const distance = () => Math.max(0, track.scrollWidth - window.innerWidth + 96);
        gsap.to(track, {
          x: () => -distance(),
          ease: "none",
          scrollTrigger: {
            trigger: wrap,
            start: "top top",
            end: () => `+=${distance() + window.innerHeight * 0.6}`,
            pin: true,
            scrub: 0.8,
            invalidateOnRefresh: true,
            anticipatePin: 1,
          },
        });
        gsap.set(track, { x: 0 });
      } else {
        gsap.set(track, { x: 0 });
      }
    };

    build();
    desktop.addEventListener("change", () => {
      ScrollTrigger.getAll().forEach((instance) => {
        if (instance.pin === wrap) instance.kill(true);
      });
      build();
    });
  }

  /* --- Indicador da rolagem de serviços (mobile) ------------------------- */
  function initScrollHint() {
    $$("[data-scroll-hint]").forEach((hint) => {
      const scroller = $(`[data-hint-scroller="${hint.dataset.scrollHint}"]`);
      const rail = $(".services-hint__rail span", hint);
      if (!scroller || !rail || window.matchMedia("(min-width: 62rem)").matches) return;

      const update = () => {
        const max = scroller.scrollWidth - scroller.clientWidth;
        const ratio = max > 0 ? scroller.scrollLeft / max : 0;
        rail.style.setProperty("--progress", `${ratio * 100}%`);
      };
      scroller.addEventListener("scroll", update, { passive: true });
      update();
    });
  }

  /* --- Jornada: linha e nós ---------------------------------------------- */
  function initJourney() {
    const journey = $(".journey");
    if (!journey) return;

    const line = $(".journey__line span", journey);
    const steps = $$(".journey__step", journey);

    if (line) {
      gsap.to(line, {
        scaleX: 1,
        ease: "none",
        scrollTrigger: {
          trigger: journey,
          start: "top 62%",
          end: "bottom 78%",
          scrub: 0.5,
        },
      });
    }

    steps.forEach((step) => {
      ScrollTrigger.create({
        trigger: step,
        start: "top 78%",
        end: "bottom 40%",
        onToggle: (self) => step.classList.toggle("is-active", self.isActive),
      });
    });
  }

  /* --- Marquee: duplicação e velocidade --------------------------------- */
  function initMarquees() {
    $$(".marquee").forEach((marquee) => {
      const track = $(".marquee__track", marquee);
      if (!track) return;

      const original = track.innerHTML;
      for (let i = 0; i < 2; i += 1) track.innerHTML += original;

      const speed = parseFloat(marquee.dataset.speed || "38");
      marquee.style.setProperty("--marquee-duration", `${speed}s`);
    });
  }

  /* --- Inclinação sutil nos cards --------------------------------------- */
  function initTilt() {
    if (!window.matchMedia("(hover: hover) and (pointer: fine)").matches) return;

    $$("[data-tilt]").forEach((card) => {
      const strength = parseFloat(card.dataset.tilt) || 4;
      card.addEventListener("pointermove", (event) => {
        const rect = card.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width - 0.5;
        const y = (event.clientY - rect.top) / rect.height - 0.5;
        gsap.to(card, {
          rotateY: x * strength,
          rotateX: -y * strength,
          transformPerspective: 900,
          duration: 0.5,
          ease: "power2.out",
        });
      });
      card.addEventListener("pointerleave", () => {
        gsap.to(card, { rotateY: 0, rotateX: 0, duration: 0.8, ease: "power3.out" });
      });
    });
  }

  /* --- Seção de destaque com parallax interno ---------------------------- */
  function initStickyPanels() {
    $$("[data-sticky]").forEach((section) => {
      const panels = $$("[data-sticky-panel]", section);
      if (!panels.length) return;

      panels.forEach((panel) => {
        gsap.fromTo(
          panel,
          { opacity: 0, y: 60 },
          {
            opacity: 1,
            y: 0,
            duration: 1,
            ease: EASE,
            scrollTrigger: { trigger: panel, start: "top 84%", once: true },
          }
        );
      });
    });
  }

  /* --- Bootstrap --------------------------------------------------------- */
  function init() {
    initSplitHeadings();
    initReveals();
    initCounters();
    initParallax();
    initGlows();
    initJourney();
    initMarquees();
    initHorizontal();
    initScrollHint();
    initTilt();
    initStickyPanels();

    document.addEventListener("lumina:ready", heroIntro, { once: true });
    if (window.LUMINA.ready) heroIntro();

    window.addEventListener("load", () => ScrollTrigger.refresh());
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();