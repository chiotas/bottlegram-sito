/* ─────────────────────────────────────────────────────────────────────────
   Bottlegram — la pagina.

   Tre cose sole: i sigilli (portati da SealGlyph.swift), la spiaggia disegnata
   (portata da Theme.swift + BeachScene) e l'inglese. Niente librerie: l'app non
   ne ha nemmeno una, e una pagina che la presenta non può pesare di più.
   ───────────────────────────────────────────────────────────────────────── */

'use strict';

/* ── I sigilli ───────────────────────────────────────────────────────────
   Gli stessi emblemi di Bottlegram/Support/SealGlyph.swift, tracciati in un
   riquadro 100×100 invece che nel rect unitario. Riempimento even-odd: i buchi
   (la gobba della luna, l'occhio del pesce) vengono da lì.                  */

const GLIFI = {
  moon: "M8 50A40 40 0 1 0 88 50A40 40 0 1 0 8 50ZM34 44A26 26 0 1 0 86 44A26 26 0 1 0 34 44Z",
  anchor: "M38 13A12 11 0 1 0 62 13A12 11 0 1 0 38 13ZM44 13A6 5.5 0 1 0 56 13A6 5.5 0 1 0 44 13ZM46 24L54 24L54 75L46 75ZM28 32L46 32L46 40L28 40ZM54 32L72 32L72 40L54 40ZM20 54A30 30 0 0 0 80 54L71 54A21 21 0 0 1 29 54ZM20 54L13.5 42L29 54ZM80 54L86.5 42L71 54Z",
  star: "M50 2L62 38L98 50L62 62L50 98L38 62L2 50L38 38Z",
  leaf: "M50 4Q102 40 50 82Q-2 40 50 4ZM49 80L51 80A2 2 0 0 1 53 82L53 94A2 2 0 0 1 51 96L49 96A2 2 0 0 1 47 94L47 82A2 2 0 0 1 49 80Z",
  shell: "M50 82L10.681 54.468Q10.439 36.89 27.836 39.423Q35.739 23.719 50 34Q64.261 23.719 72.164 39.423Q89.561 36.89 89.319 54.468ZM40 84L60 84L56 94L44 94ZM45.383 73.13L30.182 47.255L32.906 45.837ZM50 72L48.464 42.029L51.536 42.029ZM54.617 73.13L67.094 45.837L69.818 47.255Z",
  candle: "M43 42L57 42A5 5 0 0 1 62 47L62 87A5 5 0 0 1 57 92L43 92A5 5 0 0 1 38 87L38 47A5 5 0 0 1 43 42ZM50 6Q70 24 50 38Q30 24 50 6Z",
  flame: "M50 4Q95 52 50 94Q5 52 50 4ZM50 50Q66 70 50 86Q34 70 50 50Z",
  compass: "M2 50A48 48 0 1 0 98 50A48 48 0 1 0 2 50ZM10 50A40 40 0 1 0 90 50A40 40 0 1 0 10 50ZM50 16L58 42L84 50L58 58L50 84L42 58L16 50L42 42Z",
  bottle: "M44 4L56 4A4 4 0 0 1 60 8L60 10A4 4 0 0 1 56 14L44 14A4 4 0 0 1 40 10L40 8A4 4 0 0 1 44 4ZM42 14L58 14L58 30L42 30ZM42 30L58 30A12 12 0 0 1 70 42L70 82A12 12 0 0 1 58 94L42 94A12 12 0 0 1 30 82L30 42A12 12 0 0 1 42 30ZM42 50L58 50L58 76L42 76Z",
  fish: "M10 50Q40 6 70 50Q40 94 10 50ZM70 50L94 28L94 72ZM24 44.5A4.5 4.5 0 1 0 33 44.5A4.5 4.5 0 1 0 24 44.5Z",
  gull: "M5 62Q26 20 50 46Q74 20 95 62Q72 42 50 60Q28 42 5 62Z",
  wave: "M6 24Q28 2 50 24Q72 46 94 24L94 37Q72 59 50 37Q28 15 6 37ZM6 56Q28 34 50 56Q72 78 94 56L94 69Q72 91 50 69Q28 47 6 69Z",
  sun: "M28 50A22 22 0 1 0 72 50A22 22 0 1 0 28 50ZM98 50L72.934 55.128L72.934 44.872ZM83.941 83.941L62.59 69.843L69.843 62.59ZM50 98L44.872 72.934L55.128 72.934ZM16.059 83.941L30.157 62.59L37.41 69.843ZM2 50L27.066 44.872L27.066 55.128ZM16.059 16.059L37.41 30.157L30.157 37.41ZM50 2L55.128 27.066L44.872 27.066ZM83.941 16.059L69.843 37.41L62.59 30.157Z",
  mountains: "M4 82L36 28L52 52L68 18L96 82Z",
  sailboat: "M8 70L92 70L78 86L22 86ZM54 8L86 64L54 64ZM46 16L46 64L14 64Z",
  lighthouse: "M38 88L43 32L57 32L62 88ZM41 20L59 20L59 32L41 32ZM39 20L50 6L61 20ZM28 88L72 88L72 96L28 96Z",
  key: "M30 19A20 15 0 1 0 70 19A20 15 0 1 0 30 19ZM39 19A11 8 0 1 0 61 19A11 8 0 1 0 39 19ZM46 34L54 34L54 92L46 92ZM54 70L70 70L70 77L54 77ZM54 82L66 82L66 89L54 89Z",
  quill: "M82 6Q30 14 28 70Q74 56 82 6ZM28 70L14 94L33 76Z",
  starfish: "M50 3Q57.641 39.483 94.7 35.476Q62.364 54.017 77.626 88.024Q50 63 22.374 88.024Q37.636 54.017 5.3 35.476Q42.359 39.483 50 3Z",
  hourglass: "M22 2L78 2L78 9L22 9ZM26 9L74 9L56 50L74 91L26 91L44 50ZM22 91L78 91L78 98L22 98Z",
  paperBoat: "M4 58L96 58L72 84L28 84ZM50 10L74 54L26 54Z",
  heart: "M50 88C26 68 6 52 6 34Q14 0 50 28Q86 0 94 34C94 52 74 68 50 88Z",
  pine: "M50 2L68 28L59 28L76 54L65 54L84 80L55 80L55 94L45 94L45 80L16 80L35 54L24 54L41 28L32 28Z",
  palm: "M44 94Q40 60 55 34L63 36Q50 62 56 94ZM58 33Q30 14 12 28Q32 32 58 33ZM58 33Q38 8 30 6Q50 20 58 33ZM58 33Q70 6 86 8Q72 24 58 33ZM58 33Q84 24 96 40Q78 40 58 33Z"
};

document.querySelectorAll('path[data-glifo]').forEach(p => {
  p.setAttribute('d', GLIFI[p.dataset.glifo] || '');
});

/* SwiftUI ragiona in HSB, il CSS in HSL: senza questa conversione la cera
   verrebbe più chiara di quella dell'app. */
function hsb(h, s, b) {
  const l = b * (1 - s / 2);
  const sl = (l === 0 || l === 1) ? 0 : (b - l) / Math.min(l, 1 - l);
  return `hsl(${(h * 360).toFixed(1)} ${(sl * 100).toFixed(1)}% ${(l * 100).toFixed(1)}%)`;
}

/* Il sigillo di ceralacca, come SealBadge: cera con la luce da sinistra in
   alto, bordo scuro, filo di carta all'interno, emblema impresso. */
function sigillo(glifo, tinta) {
  const id = 'cera-' + glifo + '-' + String(tinta).replace('.', '');
  return `<svg class="sigillo-cera" viewBox="0 0 100 100" aria-hidden="true">
    <defs><radialGradient id="${id}" cx="38%" cy="32%" r="72%">
      <stop offset="0%" stop-color="${hsb(tinta, 0.50, 0.70)}"/>
      <stop offset="100%" stop-color="${hsb(tinta, 0.62, 0.48)}"/>
    </radialGradient></defs>
    <circle cx="50" cy="50" r="49" fill="url(#${id})"/>
    <circle cx="50" cy="50" r="48" fill="none" stroke="${hsb(tinta, 0.65, 0.38)}" stroke-width="4"/>
    <circle cx="50" cy="50" r="39" fill="none" stroke="#F5EBD1" stroke-opacity="0.4" stroke-width="2"/>
    <g transform="translate(26.25 26.25) scale(0.475)">
      <path d="${GLIFI[glifo]}" fill="#F5EBD1" fill-rule="evenodd"/>
    </g>
  </svg>`;
}

document.querySelectorAll('[data-sigillo]').forEach(el => {
  el.innerHTML = sigillo(el.dataset.sigillo, parseFloat(el.dataset.tinta) || 0.02);
});

const FILA = [['anchor', 0.02], ['moon', 0.63], ['starfish', 0.09], ['compass', 0.11],
              ['quill', 0.95], ['palm', 0.35], ['gull', 0.55], ['hourglass', 0.75],
              ['shell', 0.06], ['sailboat', 0.48]];
const fila = document.getElementById('fila-sigilli');
if (fila) {
  fila.innerHTML = FILA.map(([g, t]) => `<div>${sigillo(g, t)}</div>`).join('');
}

/* ── Le spiagge ──────────────────────────────────────────────────────────
   Le venti tavolozze sono copiate una per una da Theme.palette(biome:phase:).
   Non arrotondate, non "vicine": sono quei colori.                          */

const TAVOLOZZE = {
 "mediterranean": {
  "day":   {"skyTop":"#478FDE", "skyMid":"#8CC2F0", "skyHorizon":"#D9EDF5", "seaFar":"#0D528C", "seaMid":"#1A78AD", "seaNear":"#4CADC2", "sandDry":"#EDD9A8", "sandWet":"#CCB285", "silhouette":"#2E4738", "sunOrMoon":"#FFF2BF", "isNight":false},
  "dawn":  {"skyTop":"#7373B2", "skyMid":"#E6AD8C", "skyHorizon":"#FCD9A6", "seaFar":"#33477A", "seaMid":"#596B94", "seaNear":"#9E949E", "sandDry":"#DEC29E", "sandWet":"#B89980", "silhouette":"#383347", "sunOrMoon":"#FFCC8C", "isNight":false},
  "dusk":  {"skyTop":"#403873", "skyMid":"#CC6B6B", "skyHorizon":"#FAAD6B", "seaFar":"#262E61", "seaMid":"#4C477A", "seaNear":"#B27A73", "sandDry":"#CCA88C", "sandWet":"#9E8070", "silhouette":"#262138", "sunOrMoon":"#FF9E66", "isNight":false},
  "night": {"skyTop":"#0A0F2E", "skyMid":"#141F47", "skyHorizon":"#24335C", "seaFar":"#08122E", "seaMid":"#0F1F42", "seaNear":"#1F3357", "sandDry":"#595766", "sandWet":"#404052", "silhouette":"#0D0F1F", "sunOrMoon":"#F2F2E0", "isNight":true}
 },
 "tropical": {
  "day":   {"skyTop":"#40A6E6", "skyMid":"#8CD1F0", "skyHorizon":"#E0F5F5", "seaFar":"#007399", "seaMid":"#0DA6B2", "seaNear":"#73DBD1", "sandDry":"#FAF0D6", "sandWet":"#E0CFAD", "silhouette":"#1F4C33", "sunOrMoon":"#FFF7CC", "isNight":false},
  "dawn":  {"skyTop":"#8C80BF", "skyMid":"#F2B899", "skyHorizon":"#FFE0B2", "seaFar":"#2E5980", "seaMid":"#4C8C9E", "seaNear":"#A6B2A8", "sandDry":"#F2DEC2", "sandWet":"#D1B899", "silhouette":"#33334C", "sunOrMoon":"#FFD194", "isNight":false},
  "dusk":  {"skyTop":"#4C3373", "skyMid":"#E67380", "skyHorizon":"#FFB273", "seaFar":"#1F3361", "seaMid":"#40527A", "seaNear":"#BF857A", "sandDry":"#E0BDA3", "sandWet":"#B28F80", "silhouette":"#241A38", "sunOrMoon":"#FF9961", "isNight":false},
  "night": {"skyTop":"#081233", "skyMid":"#0F244C", "skyHorizon":"#1A3861", "seaFar":"#051A33", "seaMid":"#0A2E47", "seaNear":"#1A475C", "sandDry":"#616170", "sandWet":"#474759", "silhouette":"#0A121F", "sunOrMoon":"#F5F5E6", "isNight":true}
 },
 "arctic": {
  "day":   {"skyTop":"#8CB8D9", "skyMid":"#BFD9EB", "skyHorizon":"#EBF2F5", "seaFar":"#265273", "seaMid":"#407A94", "seaNear":"#80B2BD", "sandDry":"#E8EBF0", "sandWet":"#C2C9D4", "silhouette":"#596B85", "sunOrMoon":"#FFFAE6", "isNight":false},
  "dawn":  {"skyTop":"#807AAD", "skyMid":"#D9B2B2", "skyHorizon":"#F5D9C7", "seaFar":"#33426B", "seaMid":"#526685", "seaNear":"#94949E", "sandDry":"#E0D9DE", "sandWet":"#BAB8C7", "silhouette":"#4C5270", "sunOrMoon":"#FFD9AD", "isNight":false},
  "dusk":  {"skyTop":"#38407A", "skyMid":"#8C6B99", "skyHorizon":"#E69E8C", "seaFar":"#1F2E59", "seaMid":"#384773", "seaNear":"#856B85", "sandDry":"#CCC4D4", "sandWet":"#A3A1B8", "silhouette":"#2E3357", "sunOrMoon":"#FFAD7A", "isNight":false},
  "night": {"skyTop":"#050D26", "skyMid":"#0D2E40", "skyHorizon":"#1A524C", "seaFar":"#051429", "seaMid":"#0D243D", "seaNear":"#1A3D4C", "sandDry":"#70788F", "sandWet":"#545C73", "silhouette":"#212942", "sunOrMoon":"#F0F5EB", "isNight":true}
 },
 "volcanic": {
  "day":   {"skyTop":"#668CAD", "skyMid":"#A6BDCC", "skyHorizon":"#DBE0E0", "seaFar":"#1F3D52", "seaMid":"#335C70", "seaNear":"#61858F", "sandDry":"#38363B", "sandWet":"#212129", "silhouette":"#1A1A21", "sunOrMoon":"#FAF5D9", "isNight":false},
  "dawn":  {"skyTop":"#595280", "skyMid":"#BF8580", "skyHorizon":"#F2B88C", "seaFar":"#262E4C", "seaMid":"#404766", "seaNear":"#806B75", "sandDry":"#3D363D", "sandWet":"#26242E", "silhouette":"#1A1724", "sunOrMoon":"#FFC785", "isNight":false},
  "dusk":  {"skyTop":"#332659", "skyMid":"#9E4C61", "skyHorizon":"#EB8559", "seaFar":"#1A1F40", "seaMid":"#333359", "seaNear":"#8C5961", "sandDry":"#332B36", "sandWet":"#1F1C26", "silhouette":"#14121F", "sunOrMoon":"#FF9459", "isNight":false},
  "night": {"skyTop":"#080A1F", "skyMid":"#121733", "skyHorizon":"#212647", "seaFar":"#080F21", "seaMid":"#0F1A33", "seaNear":"#1C2942", "sandDry":"#24242E", "sandWet":"#171721", "silhouette":"#0D0D17", "sunOrMoon":"#F2F0E0", "isNight":true}
 },
 "atlantic": {
  "day":   {"skyTop":"#6B94BF", "skyMid":"#A8C4D9", "skyHorizon":"#E0EBEB", "seaFar":"#1A4C5C", "seaMid":"#2E707A", "seaNear":"#669E99", "sandDry":"#E3D4B2", "sandWet":"#BDAB8F", "silhouette":"#475742", "sunOrMoon":"#FFF7D9", "isNight":false},
  "dawn":  {"skyTop":"#6B6B9E", "skyMid":"#D19E94", "skyHorizon":"#F5D1A8", "seaFar":"#293D59", "seaMid":"#476173", "seaNear":"#8F8A8C", "sandDry":"#D6C2A8", "sandWet":"#AD9985", "silhouette":"#3D4247", "sunOrMoon":"#FFD194", "isNight":false},
  "dusk":  {"skyTop":"#38336B", "skyMid":"#AD616B", "skyHorizon":"#F09E6B", "seaFar":"#1F2952", "seaMid":"#38426B", "seaNear":"#946B70", "sandDry":"#C2A38F", "sandWet":"#947A70", "silhouette":"#242133", "sunOrMoon":"#FF9961", "isNight":false},
  "night": {"skyTop":"#080D29", "skyMid":"#121C42", "skyHorizon":"#1F2E54", "seaFar":"#081429", "seaMid":"#0D213B", "seaNear":"#1C364C", "sandDry":"#575461", "sandWet":"#3D3D4C", "silhouette":"#0D0F1C", "sunOrMoon":"#F2F2E3", "isNight":true}
 }
};

/* Una riva vera per bioma, presa da Content/BeachCatalog.swift. */
const RIVE = {
  mediterranean: { nome: 'Cala Goloritzé',       luogo: 'Sardegna, Italy' },
  tropical:      { nome: "Anse Source d'Argent", luogo: 'La Digue, Seychelles' },
  arctic:        { nome: 'Haukland Beach',       luogo: 'Lofoten, Norway' },
  volcanic:      { nome: 'Reynisfjara',          luogo: 'Vík, Iceland' },
  atlantic:      { nome: 'Praia da Ursa',        luogo: 'Sintra, Portugal' }
};

/* Le sagome dell'app: pini sul Mediterraneo e sull'Atlantico, palme ai
   tropici, montagne all'orizzonte dove la costa è alta. `lontana` le manda
   dietro al mare, all'altezza della linea d'orizzonte. */
const SAGOME = {
  mediterranean: { glifo: 'pine',      x: 196, y: 352, s: 148 },
  tropical:      { glifo: 'palm',      x: 166, y: 292, s: 196 },
  arctic:        { glifo: 'mountains', x: 4,   y: 132, s: 190, lontana: true },
  volcanic:      { glifo: 'mountains', x: 118, y: 108, s: 218, lontana: true },
  atlantic:      { glifo: 'pine',      x: -20, y: 348, s: 156 }
};

/* Una banda d'acqua o di sabbia: cresta ondulata in cima, giù fino al fondo. */
function banda(y, amp) {
  return `M0 ${y} Q37.5 ${y - amp} 75 ${y} T150 ${y} T225 ${y} T300 ${y} L300 650 L0 650 Z`;
}

function stelline(n) {
  let s = '';
  for (let i = 0; i < n; i++) {
    // Deterministiche: la stessa spiaggia ha sempre lo stesso cielo.
    const x = ((i * 61.803) % 100) * 3;
    const y = ((i * 37.77) % 100) * 3.1;
    const r = 0.5 + ((i * 13) % 5) * 0.22;
    const o = 0.35 + ((i * 7) % 6) * 0.1;
    s += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${r.toFixed(2)}" fill="#fff" opacity="${o.toFixed(2)}"/>`;
  }
  return s;
}

function tondo(x, glifo, etichetta) {
  return `<g transform="translate(${x} 566)">
    <circle r="21" fill="#000" fill-opacity="0.30"/>
    <circle r="21" fill="none" stroke="#fff" stroke-opacity="0.35" stroke-width="1"/>
    <g transform="translate(-7.5 -7.5) scale(0.15)"><path d="${GLIFI[glifo]}" fill="#fff" fill-rule="evenodd"/></g>
    <text y="34" text-anchor="middle" font-size="9.5" fill="#fff" opacity="0.95">${etichetta}</text>
  </g>`;
}

function disegnaSpiaggia(bioma, fase, quante = 2) {
  const p = TAVOLOZZE[bioma][fase];
  const riva = RIVE[bioma];
  const sag = SAGOME[bioma];
  const notte = p.isNight;
  const T = (k) => testo(k);
  // Gli id dei gradienti sono globali nel documento: se due scene convivessero
  // sulla stessa pagina, la seconda userebbe il cielo della prima.
  const u = bioma + '-' + fase;

  return `
  <defs>
    <linearGradient id="g-cielo-${u}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${p.skyTop}"/>
      <stop offset="72%" stop-color="${p.skyMid}"/>
      <stop offset="100%" stop-color="${p.skyHorizon}"/>
    </linearGradient>
    <radialGradient id="g-astro-${u}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="${p.sunOrMoon}" stop-opacity="0.30"/>
      <stop offset="100%" stop-color="${p.sunOrMoon}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="g-aurora-${u}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#2ED9A0" stop-opacity="0"/>
      <stop offset="45%" stop-color="#2ED9A0" stop-opacity="0.42"/>
      <stop offset="100%" stop-color="#7BE0D6" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="g-lancia-${u}" x1="0.2" y1="0.1" x2="0.8" y2="0.9">
      <stop offset="0%" stop-color="#547EA8"/><stop offset="100%" stop-color="#21476B"/>
    </linearGradient>
    <linearGradient id="g-fondo-${u}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0.28"/>
    </linearGradient>
  </defs>

  <rect width="300" height="300" fill="url(#g-cielo-${u})"/>
  ${notte ? stelline(34) : ''}
  ${(bioma === 'arctic' && notte)
      ? `<path d="M-20 96 C60 44 150 122 330 58 L330 106 C150 170 60 92 -20 144 Z" fill="url(#g-aurora-${u})"/>
         <path d="M-20 138 C70 96 160 158 330 104 L330 138 C160 192 70 130 -20 176 Z" fill="url(#g-aurora-${u})" opacity="0.5"/>` : ''}
  <circle cx="228" cy="86" r="58" fill="url(#g-astro-${u})"/>
  <circle cx="228" cy="86" r="17" fill="${p.sunOrMoon}" opacity="0.95"/>

  ${sag.lontana ? sagoma(sag, p.silhouette) : ''}

  <path d="${banda(292, 6)}"  fill="${p.seaFar}"/>
  <path d="${banda(336, 9)}"  fill="${p.seaMid}"/>
  <path d="${banda(388, 12)}" fill="${p.seaNear}"/>
  <path d="${banda(444, 9)}"  fill="${p.sandWet}"/>
  <path d="${banda(486, 7)}"  fill="${p.sandDry}"/>

  ${sag.lontana ? '' : sagoma(sag, p.silhouette)}

  ${bottiglietta(66, 534, -24)}
  ${bottiglietta(244, 518, 16)}
  ${quante > 2 ? bottiglietta(150, 528, -8) : ''}

  <rect y="470" width="300" height="180" fill="url(#g-fondo-${u})"/>

  <g font-family="Iowan Old Style, Palatino, Georgia, serif" fill="#fff"
     style="filter: drop-shadow(0 1px 3px rgba(0,0,0,.55))">
    <text x="18" y="52" font-size="17" font-weight="600">${riva.nome}</text>
    <text x="18" y="71" font-size="11.5" font-style="italic" opacity="0.85">${riva.luogo}</text>

    <g transform="translate(240 40)">
      <rect x="-32" y="-13" width="64" height="26" rx="13" fill="#000" fill-opacity="0.32"/>
      <g transform="translate(-19 -11) rotate(-18 5.5 11)"><g transform="scale(0.11)"><path d="${GLIFI.bottle}" fill="#fff" fill-rule="evenodd"/></g></g>
      <text x="8" y="5" font-size="14" font-weight="700">${quante}</text>
    </g>

    <g transform="translate(150 496)">
      <rect x="-92" y="-13" width="184" height="26" rx="13" fill="#000" fill-opacity="0.35"/>
      <text y="4.5" text-anchor="middle" font-size="11" font-style="italic">Bottles washed ashore: ${quante}</text>
    </g>

    ${tondo(40, 'compass', T('scena.mappa'))}
    ${tondo(100, 'quill', T('scena.diario'))}
    ${tondo(258, 'key', T('scena.emporio'))}

    <g transform="translate(180 558)">
      <circle r="31" fill="url(#g-lancia-${u})"/>
      <circle r="31" fill="none" stroke="#142E4A" stroke-width="1.4"/>
      <circle r="25" fill="none" stroke="#F5EBD1" stroke-opacity="0.5" stroke-width="1"/>
      <g transform="rotate(-12)"><g transform="translate(-7.5 -16) scale(0.15 0.32)"><path d="${GLIFI.bottle}" fill="#F5EBD1" fill-rule="evenodd"/></g></g>
      <text y="42" text-anchor="middle" font-size="9.5">${T('scena.lancia')}</text>
    </g>
  </g>`;
}

function sagoma(s, colore) {
  return `<g transform="translate(${s.x} ${s.y}) scale(${s.s / 100})" opacity="0.95">
    <path d="${GLIFI[s.glifo]}" fill="${colore}" fill-rule="evenodd"/></g>`;
}

/* Una bottiglia arenata: vetro di mare, tappo di sughero, etichetta di carta. */
function bottiglietta(x, y, gradi) {
  return `<g transform="translate(${x} ${y}) rotate(${gradi}) scale(1.05)">
    <rect x="-4" y="-19" width="8" height="6" rx="1.6" fill="#C08A4E"/>
    <path d="M-5.5 -13 h11 v6 q0 2.6 2.4 4.2 l1.7 1.2 q2 1.4 2 3.8 v15 q0 2.6 -2.6 2.6 h-15.6 q-2.6 0 -2.6 -2.6 v-15 q0 -2.4 2 -3.8 l1.7 -1.2 q2.4 -1.6 2.4 -4.2 z" fill="#C7DED4" fill-opacity="0.92"/>
    <rect x="-6" y="2" width="12" height="9" rx="1" fill="#F5EBD1" fill-opacity="0.9"/>
  </g>`;
}

/* ── Le parole della schermata ───────────────────────────────────────────
   Le stesse voci dell'app, nella sua traduzione inglese vera
   (Resources/Localizable.xcstrings). */

const T = {
  'scena.alt': 'The beach, as the app draws it',
  'scena.mappa': 'Map', 'scena.diario': 'Journal', 'scena.emporio': 'Emporium', 'scena.lancia': 'Throw',
  'scena.arenate': 'Bottles washed ashore: 2',
  'bioma.mediterranean': 'Mediterranean', 'bioma.tropical': 'Tropical', 'bioma.arctic': 'Arctic',
  'bioma.volcanic': 'Volcanic', 'bioma.atlantic': 'Wild Atlantic',
  'fase.dawn': 'Dawn', 'fase.day': 'Day', 'fase.dusk': 'Dusk', 'fase.night': 'Night'
};
const testo = (k) => T[k] || k;

/* ── I comandi della vetrina ─────────────────────────────────────────── */

const BIOMI = ['mediterranean', 'tropical', 'arctic', 'volcanic', 'atlantic'];
const FASI = ['dawn', 'day', 'dusk', 'night'];
let biomaScelto = 'arctic';
let faseScelta = 'night';

function costruisciChip(contenitore, valori, prefisso, scelto, alClick) {
  contenitore.innerHTML = valori.map(v =>
    `<button type="button" class="chip" data-val="${v}" data-chiave="${prefisso}.${v}" aria-pressed="${v === scelto}"></button>`
  ).join('');
  contenitore.querySelectorAll('.chip').forEach(b => {
    b.addEventListener('click', () => {
      contenitore.querySelectorAll('.chip').forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      alClick(b.dataset.val);
      rendi();
    });
  });
}

function etichetteChip() {
  document.querySelectorAll('.chip[data-chiave]').forEach(b => { b.textContent = testo(b.dataset.chiave); });
}

/* LA SPIAGGIA CHE SI PROVA È L'APP VERA, non più il disegno.
   Venti fotografie, cinque coste per quattro ore, fatte con la bandiera
   `--phase` su un naufrago che vive in una campana di vetro. Il disegno resta
   nel file (`disegnaSpiaggia`) e continua a servire al fondale delle regole.

   L'ALT NON È DINAMICO di proposito: lo scambio di lingua fotografa gli
   attributi una volta sola, quindi un alt riscritto da qui resterebbe inglese
   per sempre. Quale costa e quale ora si legge dai pulsanti accanto, che sono
   tradotti. */
const scena = document.getElementById('scena');
function rendi() {
  if (!scena) return;
  scena.src = `assets/spiagge/${biomaScelto}-${faseScelta}.jpg`;
}

const contBiomi = document.getElementById('biomi');
const contFasi = document.getElementById('fasi');
if (contBiomi && contFasi) {
  costruisciChip(contBiomi, BIOMI, 'bioma', biomaScelto, v => { biomaScelto = v; });
  costruisciChip(contFasi, FASI, 'fase', faseScelta, v => { faseScelta = v; });
  etichetteChip();
  rendi();

  /* Le altre diciannove si tirano giù quando la sezione si avvicina, non prima:
     chi non arriva fin qui non paga un megabyte e mezzo per niente. E si
     tirano giù PRIMA che qualcuno prema, perché una vetrina che sbianca a ogni
     pulsante non è una vetrina. Prima le altre ore della costa che si sta
     guardando — è lì che va il primo dito. */
  const sezione = document.getElementById('spiagge');
  if (sezione && 'IntersectionObserver' in window) {
    const scorta = new IntersectionObserver(([v], oss) => {
      if (!v.isIntersecting) return;
      oss.disconnect();
      const code = [
        ...FASI.map(f => `${biomaScelto}-${f}`),
        ...BIOMI.flatMap(b => FASI.map(f => `${b}-${f}`)),
      ];
      const viste = new Set();
      const pigro = window.requestIdleCallback || ((f) => setTimeout(f, 200));
      for (const nome of code) {
        if (viste.has(nome)) continue;
        viste.add(nome);
        pigro(() => { new Image().src = `assets/spiagge/${nome}.jpg`; });
      }
    }, { rootMargin: '600px 0px' });
    scorta.observe(sezione);
  }
}

/* ── Le parole che affiorano ─────────────────────────────────────────
   Gli stessi tre movimenti di Onboarding/Affiora: l'opacità che sale, la
   sfocatura che si scioglie, il piccolo scivolamento verso l'alto. */

const affioranti = document.querySelectorAll('.affiora');

/* FINITA L'APPARIZIONE, IL FILTRO SE NE VA DAVVERO. `filter: blur(0)` non è
   «nessun filtro»: l'elemento resta su uno strato suo e il browser continua a
   farci passare sopra un filtro a ogni disegno, per sempre. Era metà dello
   scatto che si sentiva scorrendo sulla carta dell'approdo. */
function smettiDiFiltrare(el) {
  el.addEventListener('transitionend', (e) => {
    if (e.propertyName === 'filter') el.classList.add('posata-giu');
  }, { once: true });
  // Rete di sicurezza: se la transizione non parte (movimento ridotto, elemento
  // già a posto) l'evento non arriva mai e il filtro resterebbe lì.
  setTimeout(() => el.classList.add('posata-giu'), 1600);
}

if ('IntersectionObserver' in window) {
  const guardia = new IntersectionObserver((voci) => {
    voci.forEach(v => {
      if (!v.isIntersecting) return;
      v.target.classList.add('emersa');
      smettiDiFiltrare(v.target);
      guardia.unobserve(v.target);
    });
  }, { threshold: 0.35, rootMargin: '0px 0px -8% 0px' });
  affioranti.forEach(el => guardia.observe(el));
} else {
  affioranti.forEach(el => { el.classList.add('emersa'); el.classList.add('posata-giu'); });
}

/* I versi del naufragio, invece, tornano sott'acqua quando escono di scena:
   sono tre, e devono arrivare uno alla volta. Chi apre la pagina non deve
   poterli leggere tutti insieme prima che il mare glieli porti. */

const versi = document.querySelectorAll('.verso');
const tempesta = document.getElementById('tempesta');

/* Il verso in scena comanda anche il fondale: primo atto la nave, secondo il
   mare che se l'è presa e il cielo che si apre, terzo la bottiglia. */
function inScena(elemento) {
  elemento.classList.add('emersa');
  const atto = [...versi].indexOf(elemento) + 1;
  if (tempesta && atto > 0) tempesta.className = 'tempesta atto-' + atto;
}

if ('IntersectionObserver' in window) {
  const risacca = new IntersectionObserver((voci) => {
    voci.forEach(v => {
      if (v.intersectionRatio > 0.55) inScena(v.target);
      else v.target.classList.remove('emersa');
    });
  }, { threshold: [0, 0.55, 1] });
  versi.forEach(el => risacca.observe(el));
} else {
  versi.forEach(el => el.classList.add('emersa'));
}

/* ── La barra che si posa sulla carta ────────────────────────────────── */

/* La barra si posa sulla CARTA e resta trasparente sul BUIO.
   Prima guardava solo se l'eroe era ancora in campo: appena usciva, la barra
   diventava carta — e restava carta sopra la tempesta, che è nera. Una striscia
   giallastra sopra un temporale notturno.
   Ora si guarda cosa c'è DAVVERO sotto la barra: una striscia alta un pixel
   subito sotto di lei, e le sezioni scure che la attraversano. Se ce n'è una,
   la barra resta com'era all'inizio. */
const barra = document.getElementById('barra');
if (barra) {
  /* SI GUARDA COSA C'È DAVVERO SOTTO LA BARRA, un punto solo, appena sotto il
     suo bordo. Se quel punto sta dentro una sezione scura la barra resta
     trasparente come all'inizio; se sta sulla carta, si posa.

     PRIMA guardava se l'eroe era ancora in campo, e appena usciva diventava
     carta: restava carta anche sopra la tempesta, che è nera — una striscia
     giallastra sopra un temporale notturno.
     POI ci ho provato con un `IntersectionObserver` su una striscia alta un
     pixel, e sbagliava al primo colpo: la prima risposta dell'osservatore
     arriva prima che il disegno sia assestato, vedeva zero sezioni scure e
     posava la barra sopra il mare del titolo. Un punto letto quando serve non
     ha quel problema. */
  const SOTTO_LA_BARRA = 57;
  const scure = [...document.querySelectorAll('.notte')];
  let inCoda = false;
  const controlla = () => {
    inCoda = false;
    /* Geometria, non `elementsFromPoint`. Chiedere «cosa c'è sotto questo
       punto» sembrava più diretto, e su Safari sbagliava: durante l'assestarsi
       delle barre del browser, per un istante da quel punto tornava solo la
       barra stessa, la riga diceva «carta» e ci restava — perché dopo non
       succede più niente che la faccia ricontrollare. Un rettangolo non ha
       istanti storti. */
    const scuro = scure.some((s) => {
      const r = s.getBoundingClientRect();
      return r.top <= SOTTO_LA_BARRA && r.bottom > SOTTO_LA_BARRA;
    });
    barra.classList.toggle('posata', !scuro);
  };
  const quandoPuoi = () => {
    if (inCoda) return;
    inCoda = true;
    requestAnimationFrame(controlla);
  };
  window.addEventListener('scroll', quandoPuoi, { passive: true });
  window.addEventListener('resize', quandoPuoi);
  controlla();
  /* E ancora, quando il disegno si è assestato. Al primo colpo Safari può
     avere rettangoli non ancora buoni: la barra si posava per mezzo secondo
     sopra il mare del titolo, e con la dissolvenza di mezzo secondo addosso si
     faceva in tempo a vederla. */
  window.addEventListener('load', quandoPuoi);
  requestAnimationFrame(() => requestAnimationFrame(controlla));
  /* E dopo il salto a un'ancora. Arrivando su un indirizzo con `#sezione` il
     browser salta li senza che parta uno scorrimento che si possa ascoltare:
     la barra restava com'era al primo fotogramma, cioe carta sopra la
     tempesta. Succede anche cliccando una voce della navigazione. */
  window.addEventListener('hashchange', quandoPuoi);
  setTimeout(controlla, 120);
  setTimeout(controlla, 600);
}

/* ── La spiaggia larga ───────────────────────────────────────────────────
   La stessa scena del telefono, ma sdraiata: serve come fondale a tutta
   pagina. Nessuna interfaccia sopra — qui la spiaggia è solo un posto.    */

function bandaLarga(y, amp) {
  return `M0 ${y} Q180 ${y - amp} 360 ${y} T720 ${y} T1080 ${y} T1440 ${y} L1440 760 L0 760 Z`;
}

function stellineLarghe(n) {
  let s = '';
  for (let i = 0; i < n; i++) {
    const x = ((i * 61.803) % 100) * 14.4;
    const y = -800 + ((i * 37.77) % 100) * 11.4;
    const r = 0.9 + ((i * 13) % 5) * 0.35;
    const o = 0.35 + ((i * 7) % 6) * 0.1;
    s += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${r.toFixed(2)}" fill="#fff" opacity="${o.toFixed(2)}"/>`;
  }
  return s;
}

function disegnaSpiaggiaLarga(bioma, fase) {
  const p = TAVOLOZZE[bioma][fase];
  const u = 'larga-' + bioma + '-' + fase;
  const notte = p.isNight;
  const sagoma = (glifo, x, y, s, colore) =>
    `<g transform="translate(${x} ${y}) scale(${s / 100})"><path d="${GLIFI[glifo]}" fill="${colore}" fill-rule="evenodd"/></g>`;

  return `
  <defs>
    <linearGradient id="cielo-${u}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${p.skyTop}"/>
      <stop offset="72%" stop-color="${p.skyMid}"/>
      <stop offset="100%" stop-color="${p.skyHorizon}"/>
    </linearGradient>
    <radialGradient id="astro-${u}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="${p.sunOrMoon}" stop-opacity="0.34"/>
      <stop offset="100%" stop-color="${p.sunOrMoon}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="aurora-${u}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#2ED9A0" stop-opacity="0"/>
      <stop offset="45%" stop-color="#2ED9A0" stop-opacity="0.38"/>
      <stop offset="100%" stop-color="#7BE0D6" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <rect x="0" y="-820" width="1440" height="1220" fill="url(#cielo-${u})"/>
  ${notte ? stellineLarghe(54) : ''}
  ${(bioma === 'arctic' && notte)
      ? `<path d="M-40 110 C260 40 640 150 1500 60 L1500 130 C640 220 260 110 -40 180 Z" fill="url(#aurora-${u})"/>` : ''}
  <circle cx="1108" cy="126" r="128" fill="url(#astro-${u})"/>
  <circle cx="1108" cy="126" r="38" fill="${p.sunOrMoon}" opacity="0.95"/>

  <path d="${bandaLarga(372, 10)}" fill="${p.seaFar}"/>
  <path d="${bandaLarga(432, 16)}" fill="${p.seaMid}"/>
  <path d="${bandaLarga(506, 22)}" fill="${p.seaNear}"/>
  <path d="${bandaLarga(580, 16)}" fill="${p.sandWet}"/>
  <path d="${bandaLarga(646, 12)}" fill="${p.sandDry}"/>

  ${sagoma('pine', -30, 300, 280, p.silhouette)}
  ${sagoma('pine', 150, 400, 190, p.silhouette)}
  ${sagoma('palm', 1180, 250, 330, p.silhouette)}

  <g transform="translate(430 660) rotate(-18) scale(1.7)">
    <rect x="-4" y="-19" width="8" height="6" rx="1.6" fill="#C08A4E"/>
    <path d="M-5.5 -13 h11 v6 q0 2.6 2.4 4.2 l1.7 1.2 q2 1.4 2 3.8 v15 q0 2.6 -2.6 2.6 h-15.6 q-2.6 0 -2.6 -2.6 v-15 q0 -2.4 2 -3.8 l1.7 -1.2 q2.4 -1.6 2.4 -4.2 z" fill="#C7DED4" fill-opacity="0.92"/>
    <rect x="-6" y="2" width="12" height="9" rx="1" fill="#F5EBD1" fill-opacity="0.9"/>
  </g>
  <g transform="translate(880 700) rotate(12) scale(1.5)">
    <rect x="-4" y="-19" width="8" height="6" rx="1.6" fill="#C08A4E"/>
    <path d="M-5.5 -13 h11 v6 q0 2.6 2.4 4.2 l1.7 1.2 q2 1.4 2 3.8 v15 q0 2.6 -2.6 2.6 h-15.6 q-2.6 0 -2.6 -2.6 v-15 q0 -2.4 2 -3.8 l1.7 -1.2 q2.4 -1.6 2.4 -4.2 z" fill="#C7DED4" fill-opacity="0.92"/>
    <rect x="-6" y="2" width="12" height="9" rx="1" fill="#F5EBD1" fill-opacity="0.9"/>
  </g>`;
}

/* La spiaggia di mezzogiorno, tre bottiglie sulla sabbia: sta accanto alle
   quattro frasi dell'attesa, e non cambia. */
const scenaAttesa = document.getElementById('scena-attesa');
if (scenaAttesa) {
  scenaAttesa.innerHTML = disegnaSpiaggia('mediterranean', 'day', 3);
}

const scenaRegole = document.getElementById('scena-regole');
if (scenaRegole) {
  scenaRegole.innerHTML = disegnaSpiaggiaLarga('atlantic', 'dusk');
}
