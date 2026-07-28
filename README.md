# Il sito di Bottlegram

Una pagina sola, statica, senza dipendenze: `index.html`, `styles.css`, `app.js`
e due immagini. Niente build, niente npm, niente framework — come l'app, che non
ha una libreria esterna.

```
index.html       la pagina — tutte le parole inglesi stanno qui dentro
styles.css       i colori dell'app: carta, inchiostro, mare notturno, pergamena
app.js           i sigilli di ceralacca, le venti spiagge disegnate, i versi che affiorano
lingue.js        le altre sei lingue (GENERATO — vedi sotto)
lingua.js        il cambio di lingua
genera-lingue.py il sorgente di lingue.js
assets/          icona, anteprima social, e le tre schermate vere dell'app
.nojekyll        dice a GitHub Pages di servire i file così come sono
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

## Le sette lingue

it, en, es, fr, de, pt-BR, ja — tutte dentro la stessa pagina, perché GitHub
Pages non ha niente lato server.

**L'inglese sta nell'HTML e non si tocca**: è quello che legge chi arriva senza
JavaScript, ed è anche la CHIAVE del dizionario. Niente `data-i18n` sparsi nel
markup: una pagina di prosa dove ogni riga porta un attributo tecnico diventa
illeggibile per chi la scrive.

```
lingue.js        GENERATO, non si corregge a mano
lingua.js        scambia i nodi di testo, ricorda la scelta, indovina la lingua del browser
genera-lingue.py il sorgente di lingue.js
```

`genera-lingue.py` rimette insieme due cose diverse, e la differenza conta:

- le frasi che **esistono nell'app** — le regole del mare, i versi del
  naufragio, le voci della schermata disegnata — vengono rilette da
  `Bottlegram/Resources/Localizable.xcstrings` **a ogni rigenerazione**. Sono
  quelle che si dichiarano ad Apple: se divergessero dall'app di una virgola
  sarebbe un difetto, non una sfumatura. Nessuno le riscrive qui;
- le frasi del **solo sito** stanno scritte a mano dentro lo script.

Per rifarlo, dopo aver cambiato una parola inglese in `index.html` o una
traduzione nell'app:

```bash
cd ~/Documents/Development/bottlegram-sito && python3 genera-lingue.py > lingue.js
```

(lo script cerca l'app in `~/Documents/Development/Bottlegram`: se il repo si
sposta, la riga `XCSTRINGS` in cima va cambiata.)

**Come ci si accorge che è ora di rigenerare:** se l'inglese in `index.html`
cambia e `lingue.js` no, quella frase resta inglese e la console del browser
elenca esattamente quali — invece di lasciare in pagina una traduzione vecchia
attaccata a una frase nuova, che è il modo in cui questi file mentono.

**Rimasto indietro:** la spiaggia interattiva di `#spiagge` disegna il nome del
posto (`Haukland Beach, Lofoten, Norway`). Il nome proprio è giusto che resti in
endonimo — è la regola dell'app — ma **il paese no**: nell'app `Lofoten,
Norvegia` è tradotto (chiavi `country.*`), qui è fisso in inglese perché lo
scrive `app.js` da una tabella sua.

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
- **La chiusa** — «Somewhere to savour the quiet, while everything else is
  racing.» L'altra metà della frase («The tide keeps its own time…») è
  diventata il divisorio fra il diario e le spiagge: due frasi buone non
  stanno nella stessa riga.

Nessuna sezione è di solo testo: accanto alle parole c'è sempre qualcosa da
guardare, e **niente è una fotografia** — la pagina scrive «not one of these is
a photograph», e deve restare vero anche adesso che tre schermate su quattro
sono catture dell'app: quello che si vede lì dentro lo disegna l'app, non una
macchina fotografica. Spiaggia (`#attesa`), diario (`#diario`) e carta
(`#carta`) sono `assets/schermata-*.png`, fatte su un naufrago che vive in un
`banco_di_prova` (vedi `vetrina.mjs` nella cartella di lavoro). La spiaggia di
`#spiagge` **resta disegnata**: è l'unica con cui si gioca, e una fotografia non
cambia con i pulsanti. Le regole (`#regole`)
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
- **L'anteprima social** (`assets/anteprima.png`, 1200×630) è generata a mano:
  se cambia la frase dell'apertura, va rifatta anche lì.
- **Chi firma**: in fondo c'è solo il recapito `bottlegram@bulbmode.com`
  (lo stesso di `RegoleDelMareView.contatto` e della scheda App Store). Se vuoi
  una riga d'autore o una nota di privacy più lunga, va nel `<footer>`.
