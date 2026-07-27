/* Il cambio di lingua.

   COME FUNZIONA, e perché così. L'inglese resta scritto nell'HTML: è quello
   che legge chi arriva senza JavaScript, ed è anche la CHIAVE del dizionario.
   Questo file gira una volta sola sui nodi di testo della pagina, si segna
   l'originale, e da lì in poi non fa che riscriverli.

   Nessun `data-i18n` sparso nel markup: una pagina di prosa dove ogni riga
   porta un attributo tecnico diventa illeggibile per chi la scrive, e chi la
   scrive qui è la persona che ci tiene di più. Il prezzo è che se l'inglese
   nell'HTML cambia senza rigenerare `lingue.js`, quella frase resta inglese —
   e la console lo dice, invece di lasciare in pagina una traduzione vecchia
   attaccata a una frase nuova.

   Va caricato DOPO `app.js`, che scrive dentro gli SVG: quello che disegna lui
   dev'essere già in pagina quando qui si prende nota degli originali. */

(() => {
  const NOMI = {
    en: 'English', it: 'Italiano', es: 'Español', fr: 'Français',
    de: 'Deutsch', 'pt-BR': 'Português', ja: '日本語',
  };
  const RICORDO = 'bottlegram-lingua';

  /* I nodi di testo veri: niente script, niente style, niente stringhe vuote.
     Si raccolgono UNA VOLTA, con il loro inglese di partenza. */
  const nodi = [];
  const cammino = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
    acceptNode(n) {
      const padre = n.parentNode?.nodeName;
      if (padre === 'SCRIPT' || padre === 'STYLE') return NodeFilter.FILTER_REJECT;
      return n.nodeValue.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
    },
  });
  for (let n = cammino.nextNode(); n; n = cammino.nextNode()) {
    // Lo spazio intorno si conserva: in «pages: <em>the lighthouse keeper</em>»
    // è l'unica cosa che tiene staccate due parole.
    const grezzo = n.nodeValue;
    nodi.push({ nodo: n, chiave: grezzo.replace(/\s+/g, ' ').trim(), prima: grezzo });
  }

  /* Gli attributi che si vedono lo stesso: il titolo della scheda, quello che
     legge un lettore di schermo, quello che finisce incollato su WhatsApp. */
  const attrNodi = [];
  document.querySelectorAll('title, meta[name="description"], meta[property="og:title"], meta[property="og:description"]')
    .forEach((el) => {
      const dove = el.tagName === 'TITLE' ? 'textContent' : 'content';
      const prima = dove === 'textContent' ? el.textContent : el.getAttribute('content');
      attrNodi.push({ el, dove, prima, chiave: prima.replace(/\s+/g, ' ').trim() });
    });
  document.querySelectorAll('img[alt], [aria-label]').forEach((el) => {
    for (const dove of ['alt', 'aria-label']) {
      const prima = el.getAttribute(dove);
      if (prima && prima.trim()) {
        attrNodi.push({ el, dove, prima, chiave: prima.replace(/\s+/g, ' ').trim() });
      }
    }
  });

  const invariata = (t) => typeof INVARIATE !== 'undefined' && INVARIATE.includes(t);

  function vesti(lingua) {
    const voci = lingua === 'en' ? null : (typeof LINGUE !== 'undefined' ? LINGUE[lingua] : null);
    const orfane = [];

    for (const { nodo, chiave, prima } of nodi) {
      if (!voci) { nodo.nodeValue = prima; continue; }
      const t = voci[chiave];
      if (t) {
        // Lo spazio davanti e dietro si rimette com'era.
        const testa = prima.match(/^\s*/)[0];
        const coda = prima.match(/\s*$/)[0];
        nodo.nodeValue = testa + t + coda;
      } else {
        nodo.nodeValue = prima;
        if (!invariata(chiave)) orfane.push(chiave);
      }
    }

    for (const { el, dove, prima, chiave } of attrNodi) {
      const t = voci ? voci[chiave] : null;
      const valore = t || prima;
      if (dove === 'textContent') el.textContent = valore;
      else el.setAttribute(dove, valore);
      if (voci && !t && !invariata(chiave)) orfane.push(chiave);
    }

    document.documentElement.lang = lingua;
    try { localStorage.setItem(RICORDO, lingua); } catch { /* navigazione privata */ }

    if (orfane.length) {
      console.warn(
        `[lingua] ${orfane.length} frasi senza traduzione in «${lingua}» — restano in inglese.\n` +
        'Se l\'inglese in index.html è cambiato, va rigenerato lingue.js.',
        orfane,
      );
    }
  }

  /* La scelta di partenza: quella di prima, se c'è; altrimenti la lingua del
     browser, se la parliamo; altrimenti l'inglese, che è già scritto. */
  function primaScelta() {
    try {
      const salvata = localStorage.getItem(RICORDO);
      if (salvata && (salvata === 'en' || LINGUE[salvata])) return salvata;
    } catch { /* niente */ }
    for (const chiesta of navigator.languages || [navigator.language || 'en']) {
      if (LINGUE[chiesta]) return chiesta;                       // pt-BR esatto
      const corta = chiesta.split('-')[0];
      if (corta === 'en') return 'en';
      if (LINGUE[corta]) return corta;
      if (corta === 'pt' && LINGUE['pt-BR']) return 'pt-BR';     // pt-PT ci si accontenta
    }
    return 'en';
  }

  /* Il selettore, in barra. Un <select> vero e non una fila di bandiere: le
     bandiere sono paesi, non lingue, e qui si sbaglia sempre qualcuno. */
  function costruisciSelettore(scelta) {
    const barra = document.getElementById('barra');
    if (!barra) return null;
    const guscio = document.createElement('div');
    guscio.className = 'lingue';
    const etichetta = document.createElement('label');
    etichetta.className = 'salta';                 // visibile solo a chi legge con le orecchie
    etichetta.htmlFor = 'scegli-lingua';
    etichetta.textContent = 'Language';
    const sel = document.createElement('select');
    sel.id = 'scegli-lingua';
    for (const [codice, nome] of Object.entries(NOMI)) {
      const o = document.createElement('option');
      o.value = codice;
      o.textContent = nome;
      if (codice === scelta) o.selected = true;
      sel.appendChild(o);
    }
    sel.addEventListener('change', () => vesti(sel.value));
    guscio.append(etichetta, sel);
    barra.appendChild(guscio);
    return sel;
  }

  const scelta = primaScelta();
  costruisciSelettore(scelta);
  if (scelta !== 'en') vesti(scelta);
})();
