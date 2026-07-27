# Il sito di Bottlegram

Una pagina sola, statica, senza dipendenze: `index.html`, `styles.css`, `app.js`
e due immagini. Niente build, niente npm, niente framework — come l'app, che non
ha una libreria esterna.

```
index.html     la pagina — tutte le parole stanno qui dentro
styles.css     i colori dell'app: carta, inchiostro, mare notturno, pergamena
app.js         i sigilli di ceralacca, le venti spiagge disegnate, i versi che affiorano
assets/        icona (favicon) e anteprima 1200×630 per i link social
.nojekyll      dice a GitHub Pages di servire i file così come sono
```

## Da dove viene la grafica

Niente è inventato: i valori arrivano dal repo dell'app e vanno tenuti allineati.

| Sul sito | Nell'app |
|---|---|
| `--carta`, `--inchiostro`, `--ceralacca` | `Bottlegram/Support/Theme.swift` |
| le 20 tavolozze in `TAVOLOZZE` (5 biomi × 4 fasi) | `Theme.palette(biome:phase:)` |
| i 24 emblemi in `GLIFI` | `Bottlegram/Support/SealGlyph.swift` |
| pergamena, inchiostro bruno e blu della carta | `Views/Map/VoyageMapView.swift` |
| il prologo, le regole del mare, le voci della schermata | `Resources/Localizable.xcstrings` |
| le spiagge citate (Cala Goloritzé, Reynisfjara…) | `Content/BeachCatalog.swift` |
| il carattere: Iowan Old Style, Georgia corsivo per la voce del mare | `Font.paper` / `Font.mare` |

Se cambi il tema dell'app, i due valori vanno cambiati insieme.

## La lingua

Solo inglese, e sta tutta nell'HTML: chi arriva senza JavaScript legge comunque
ogni parola. Le uniche stringhe in `app.js` sono le voci dentro la schermata
disegnata (Map, Journal, Throw, Emporium) — la traduzione vera dell'app.

## Il tono

Questa pagina non spiega come funziona l'app: la fa desiderare. Niente ore,
niente conteggi, niente «cinque sulla sabbia» — la meccanica sta nell'App Store,
qui c'è solo il motivo per volerla. Il filo è uno: **in un mondo di messaggi
istantanei, questo è un posto dove si rallenta**; una lettera ci mette ore o
giorni a seconda di quanto mare c'è fra due naufraghi, e l'attesa non è il
prezzo — è la cosa bella.

Tre pezzi lavorano insieme e non vanno smontati singolarmente:

- **Il naufragio** (`.prologo`) — non sono tre paragrafi, sono **tre atti**. La
  tempesta resta ferma e i versi le passano davanti uno alla volta; il verso in
  scena comanda il fondale (`app.js` → `inScena`, classi `.atto-1/2/3`): nel
  primo la nave sbanda ancora, nel secondo il mare se l'è presa e il cielo si
  apre, nel terzo la pioggia smette e galleggia una bottiglia. È `position:
  sticky` con margine negativo — per questo il `body` non ha `overflow-x:
  hidden` (lo ammazzerebbe) e la sezione non ha `overflow`.
- **L'attesa** (`#attesa`) — quattro frasi che si possono ricordare, molta aria
  in mezzo. Se aggiungi una riga, tolga qualcosa: la pagina vive di vuoto.
- **La chiusa** — «Somewhere to go when everything else is shouting.» L'altra
  metà della frase («The tide keeps its own time…») è diventata il divisorio
  fra il diario e le spiagge: due frasi buone non stanno nella stessa riga.

Nessuna sezione è di solo testo: accanto alle parole c'è sempre qualcosa da
guardare, e **niente è una fotografia** — la pagina scrive «not one of these is
a photograph», e deve restare vero. Le quattro schermate del telefono sono
disegnate: la spiaggia di mezzogiorno con tre bottiglie (`#attesa`), il
carteggio del diario (`#diario`), la spiaggia interattiva (`#spiagge`, l'unica
che cambia con bioma e ora) e la carta nautica (`#carta`). Le regole (`#regole`)
hanno per fondale la **spiaggia larga** — `disegnaSpiaggiaLarga()`, stesse
tavolozze — con una velatura che si dirada verso destra: a sinistra si legge, a
destra si guarda. Se un giorno arrivano gli screenshot veri, prendono il posto
dell'SVG dentro `.schermo` e il resto non si tocca.

## Guardarla in locale

Basta aprire `index.html` con un doppio clic — non serve un server.

## Metterla online con GitHub Pages

**Sì, ha senso**: è una pagina statica, GitHub Pages è gratis, dà HTTPS, non
richiede build e regge senza problemi il traffico di un lancio. L'unica cosa che
non fa è codice lato server — che qui non serve.

**Tienila in un repo suo**, non in quello dell'app: così il sito si pubblica
senza toccare il repo di Bottlegram.

### 1. Repo e primo push

Con la CLI di GitHub (`brew install gh`, poi `gh auth login`):

```bash
cd ~/Documents/Development/bottlegram-sito && git init -b main && git add . && git commit -m "Il sito di Bottlegram" && gh repo create bottlegram-sito --public --source=. --push
```

Senza `gh`: crea a mano un repo vuoto chiamato `bottlegram-sito` su
github.com/new (pubblico, senza README), poi:

```bash
cd ~/Documents/Development/bottlegram-sito && git init -b main && git add . && git commit -m "Il sito di Bottlegram" && git remote add origin https://github.com/TUO-UTENTE/bottlegram-sito.git && git push -u origin main
```

### 2. Accendere Pages

Sul repo: **Settings → Pages → Source: Deploy from a branch**, ramo `main`,
cartella `/ (root)`, **Save**. Dopo un paio di minuti la pagina è su:

```
https://TUO-UTENTE.github.io/bottlegram-sito/
```

### 3. Le volte dopo

```bash
cd ~/Documents/Development/bottlegram-sito && git add . && git commit -m "quello che hai cambiato" && git push
```

Pages ripubblica da solo a ogni push.

### Un dominio tuo (facoltativo)

Se prendi `bottlegram.app` o simile:

1. crea un file `CNAME` in questa cartella con dentro solo il dominio, e fai push;
2. dal pannello del dominio punta un `CNAME` di `www` a `TUO-UTENTE.github.io`,
   e per il dominio nudo quattro record `A` verso `185.199.108.153`,
   `185.199.109.153`, `185.199.110.153`, `185.199.111.153`;
3. su **Settings → Pages** scrivi il dominio e spunta **Enforce HTTPS**.

## Rimasto da decidere

- **«Coming to the App Store»**: quando l'app esce, in `index.html` trasforma
  lo `<span class="bollo">` in un `<a href="…">` verso la scheda, e togli la
  riga sotto («Not out yet»).
- **Le schermate vere**: al posto dei tre telefoni disegnati si possono mettere
  screenshot dell'app (sostituendo l'SVG dentro `.schermo`); i disegni restano
  un buon secondo posto, perché sono fatti con gli stessi colori.
- **L'anteprima social** (`assets/anteprima.png`, 1200×630) è generata a mano:
  se cambia la frase dell'apertura, va rifatta anche lì.
- **Chi firma**: in fondo c'è solo il recapito `bottlegram@bulbmode.com`
  (lo stesso di `RegoleDelMareView.contatto` e della scheda App Store). Se vuoi
  una riga d'autore o una nota di privacy più lunga, va nel `<footer>`.
