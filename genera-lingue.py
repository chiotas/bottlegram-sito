# -*- coding: utf-8 -*-
"""
Genera `lingue.js` del sito.

Due sorgenti, e la differenza conta:
  · le frasi che ESISTONO NELL'APP (le regole del mare, i versi del prologo,
    il benvenuto) vengono lette da Localizable.xcstrings a ogni rigenerazione.
    Sono quelle che si dichiarano ad Apple: non possono divergere di una
    virgola dall'app, e infatti nessuno le riscrive a mano qui.
  · le frasi del solo sito (il richiamo, le quattro dell'attesa, i titoli)
    stanno qui sotto, scritte a mano.

    python3 genera-lingue.py > ~/Documents/Development/bottlegram-sito/lingue.js
"""
import json, sys

XCSTRINGS = "/Users/francescogola/Documents/Development/Bottlegram/Bottlegram/Resources/Localizable.xcstrings"
LINGUE = ["it", "es", "fr", "de", "pt-BR", "ja"]

# ── Le frasi del solo sito ─────────────────────────────────────────────────
# chiave = l'inglese esatto della pagina. Non è un codice: è il testo, così
# leggendo questo file si vede l'originale accanto alla traduzione.
SITO = {

"Bottlegram — a slow messaging app": {
 "it": "Bottlegram — un'app di messaggi lenti",
 "es": "Bottlegram — una app de mensajes lentos",
 "fr": "Bottlegram — une messagerie lente",
 "de": "Bottlegram — langsame Nachrichten",
 "pt-BR": "Bottlegram — um app de mensagens lentas",
 "ja": "Bottlegram — ゆっくり届くメッセージ"},

"Skip to content": {
 "it": "Vai al contenuto", "es": "Ir al contenido", "fr": "Aller au contenu",
 "de": "Zum Inhalt springen", "pt-BR": "Ir para o conteúdo", "ja": "本文へ"},

"The waiting": {
 "it": "L'attesa", "es": "La espera", "fr": "L'attente",
 "de": "Das Warten", "pt-BR": "A espera", "ja": "待つこと"},

"The journal": {
 "it": "Il diario", "es": "El diario", "fr": "Le journal",
 "de": "Das Tagebuch", "pt-BR": "O diário", "ja": "日誌"},

"The beaches": {
 "it": "Le spiagge", "es": "Las playas", "fr": "Les plages",
 "de": "Die Strände", "pt-BR": "As praias", "ja": "浜辺"},

"The chart": {
 "it": "La carta", "es": "La carta náutica", "fr": "La carte",
 "de": "Die Seekarte", "pt-BR": "A carta náutica", "ja": "海図"},

"A slow messaging app": {
 "it": "Un'app di messaggi lenti", "es": "Una app de mensajes lentos",
 "fr": "Une messagerie lente", "de": "Langsame Nachrichten",
 "pt-BR": "Um app de mensagens lentas", "ja": "ゆっくり届くメッセージ"},

"The sea has no use for hurry.": {
 "it": "Il mare non sa che farsene della fretta.",
 "es": "Al mar no le sirve de nada la prisa.",
 "fr": "La mer n'a que faire de la hâte.",
 "de": "Das Meer weiß mit Eile nichts anzufangen.",
 "pt-BR": "O mar não tem uso para a pressa.",
 "ja": "海に急ぎは要らない。"},

"Somewhere out there, a stranger is writing to you. No names. No noise. Only the tide, and whatever it decides to leave on your sand.": {
 "it": "Da qualche parte, uno sconosciuto ti sta scrivendo. Nessun nome. Nessun rumore. Solo la marea, e quello che decide di lasciarti sulla sabbia.",
 "es": "En algún lugar, un desconocido te está escribiendo. Sin nombres. Sin ruido. Solo la marea, y lo que decida dejarte en la arena.",
 "fr": "Quelque part, un inconnu vous écrit. Aucun nom. Aucun bruit. Rien que la marée, et ce qu'elle décide de laisser sur votre sable.",
 "de": "Irgendwo da draußen schreibt Ihnen ein Fremder. Keine Namen. Kein Lärm. Nur die Gezeiten und das, was sie in Ihrem Sand zurücklassen.",
 "pt-BR": "Em algum lugar, um desconhecido está escrevendo para você. Sem nomes. Sem barulho. Só a maré, e o que ela decidir deixar na sua areia.",
 "ja": "どこかで、見知らぬ誰かがあなたに手紙を書いている。名前もなく、騒がしさもなく。あるのは潮と、それが砂に残していくものだけ。"},

"Coming to the App Store": {
 "it": "Presto sull'App Store", "es": "Pronto en la App Store",
 "fr": "Bientôt sur l'App Store", "de": "Bald im App Store",
 "pt-BR": "Em breve na App Store", "ja": "App Store にまもなく登場"},

"Not out yet. The sea is still being tested.": {
 "it": "Non è ancora uscita. Il mare è ancora in collaudo.",
 "es": "Todavía no ha salido. El mar aún se está probando.",
 "fr": "Pas encore sortie. La mer est encore à l'essai.",
 "de": "Noch nicht erschienen. Das Meer wird noch erprobt.",
 "pt-BR": "Ainda não saiu. O mar ainda está em testes.",
 "ja": "まだ公開前です。海はいま試験中。"},

"The shipwreck": {
 "it": "Il naufragio", "es": "El naufragio", "fr": "Le naufrage",
 "de": "Der Schiffbruch", "pt-BR": "O naufrágio", "ja": "難破"},

"Sardegna, Italy": {
 "it": "Sardegna, Italia", "es": "Cerdeña, Italia", "fr": "Sardaigne, Italie",
 "de": "Sardinien, Italien", "pt-BR": "Sardenha, Itália", "ja": "サルデーニャ、イタリア"},

"The point": {
 "it": "Il punto", "es": "El porqué", "fr": "L'essentiel",
 "de": "Worum es geht", "pt-BR": "O ponto", "ja": "要するに"},

"Everything here is slow,": {
 "it": "Qui è tutto lento,", "es": "Aquí todo es lento,",
 "fr": "Ici tout est lent,", "de": "Hier ist alles langsam,",
 "pt-BR": "Aqui tudo é lento,", "ja": "ここでは何もかもが遅い。"},

"and none of it is by accident.": {
 "it": "e non è successo per caso.", "es": "y nada de ello es casualidad.",
 "fr": "et rien de tout cela n'est un hasard.", "de": "und nichts davon ist ein Versehen.",
 "pt-BR": "e nada disso é por acaso.", "ja": "そのどれもが、偶然ではない。"},

"You write, and then you wait.": {
 "it": "Scrivi, e poi aspetti.", "es": "Escribes, y luego esperas.",
 "fr": "Vous écrivez, puis vous attendez.", "de": "Sie schreiben, und dann warten Sie.",
 "pt-BR": "Você escreve, e então espera.", "ja": "書いて、それから待つ。"},

"A letter takes as long as the water between you takes. A shore across the same sea might answer by morning; the far side of the world will keep you waiting for days. Nothing you can tap will make it come sooner — and after the first one, you stop wanting it to.": {
 "it": "Una lettera ci mette quanto ci mette l'acqua che vi separa. Una riva sullo stesso mare può risponderti entro domattina; dall'altra parte del mondo ti farà aspettare giorni. Non c'è niente da toccare che la faccia arrivare prima — e dopo la prima volta smetti di volerlo.",
 "es": "Una carta tarda lo que tarde el agua que os separa. Una orilla del mismo mar puede responder por la mañana; el otro extremo del mundo te hará esperar días. No hay nada que puedas tocar para que llegue antes, y después de la primera dejas de quererlo.",
 "fr": "Une lettre met le temps que met l'eau qui vous sépare. Un rivage sur la même mer répondra peut-être au matin ; l'autre bout du monde vous fera attendre des jours. Rien de ce que vous toucherez ne la fera venir plus tôt — et après la première, vous cessez de le souhaiter.",
 "de": "Ein Brief braucht so lange, wie das Wasser zwischen Ihnen braucht. Eine Küste am selben Meer antwortet vielleicht bis zum Morgen; die andere Seite der Welt lässt Sie Tage warten. Kein Tippen bringt ihn früher — und nach dem ersten Mal wollen Sie es gar nicht mehr.",
 "pt-BR": "Uma carta demora o que demorar a água entre vocês. Uma praia no mesmo mar pode responder pela manhã; o outro lado do mundo vai fazer você esperar dias. Não há nada em que tocar para que chegue antes — e depois da primeira, você para de querer isso.",
 "ja": "手紙は、あいだにある水の分だけ時間がかかる。同じ海の向こう岸なら朝には返事が来るかもしれないし、地球の裏側なら何日も待たされる。早く着かせるために押せるものは何もない。そして最初の一通のあとは、押したいとも思わなくなる。"},

"The beach is empty, and it is yours.": {
 "it": "La spiaggia è vuota, ed è tua.", "es": "La playa está vacía, y es tuya.",
 "fr": "La plage est vide, et elle est à vous.", "de": "Der Strand ist leer, und er gehört Ihnen.",
 "pt-BR": "A praia está vazia, e é sua.", "ja": "浜辺には誰もいない。そしてそれはあなたのものだ。"},

"Nobody is online. Nobody is away. Nobody is typing, and nothing is marked delivered, seen or read. There is a shore, the sound of the water, and a horizon that asks nothing of you at all.": {
 "it": "Nessuno è online. Nessuno è assente. Nessuno sta scrivendo, e niente è segnato come consegnato, visualizzato o letto. C'è una riva, il rumore dell'acqua, e un orizzonte che non ti chiede niente.",
 "es": "Nadie está en línea. Nadie está ausente. Nadie está escribiendo, y nada aparece como entregado, visto o leído. Hay una orilla, el sonido del agua y un horizonte que no te pide nada.",
 "fr": "Personne n'est en ligne. Personne n'est absent. Personne n'est en train d'écrire, et rien n'est marqué distribué, vu ou lu. Il y a un rivage, le bruit de l'eau, et un horizon qui ne vous demande rien.",
 "de": "Niemand ist online. Niemand ist abwesend. Niemand tippt, und nichts ist als zugestellt, gesehen oder gelesen markiert. Es gibt ein Ufer, das Geräusch des Wassers und einen Horizont, der nichts von Ihnen will.",
 "pt-BR": "Ninguém está on-line. Ninguém está ausente. Ninguém está digitando, e nada é marcado como entregue, visto ou lido. Há uma praia, o som da água e um horizonte que não pede nada de você.",
 "ja": "誰もオンラインではない。誰も離席していない。誰も入力中ではなく、送信済みも既読もない。あるのは岸と、水の音と、何ひとつ求めてこない水平線だけ。"},

"You have all the time in the world to choose the words.": {
 "it": "Hai tutto il tempo del mondo per scegliere le parole.",
 "es": "Tienes todo el tiempo del mundo para elegir las palabras.",
 "fr": "Vous avez tout le temps du monde pour choisir les mots.",
 "de": "Sie haben alle Zeit der Welt, die Worte zu wählen.",
 "pt-BR": "Você tem todo o tempo do mundo para escolher as palavras.",
 "ja": "言葉を選ぶ時間なら、いくらでもある。"},

"A letter that costs something is written better. You will not fire off seven in a row here, you will not correct yourself an hour later, and you cannot call one back. So you sit with it a while, and you say the true thing instead of the quick one.": {
 "it": "Una lettera che costa qualcosa si scrive meglio. Qui non ne spari sette di fila, non ti correggi un'ora dopo, e non puoi richiamarne indietro nessuna. Così ci stai sopra un po', e dici la cosa vera invece di quella veloce.",
 "es": "Una carta que cuesta algo se escribe mejor. Aquí no soltarás siete seguidas, no te corregirás una hora después y no puedes retirar ninguna. Así que te quedas un rato con ella, y dices lo verdadero en lugar de lo rápido.",
 "fr": "Une lettre qui coûte quelque chose s'écrit mieux. Ici vous n'en enverrez pas sept d'affilée, vous ne vous corrigerez pas une heure plus tard, et vous ne pouvez en rappeler aucune. Alors vous restez un moment avec elle, et vous dites la chose vraie plutôt que la chose rapide.",
 "de": "Ein Brief, der etwas kostet, wird besser geschrieben. Hier feuern Sie nicht sieben hintereinander ab, korrigieren sich nicht eine Stunde später und können keinen zurückholen. Also bleiben Sie eine Weile dabei und sagen das Wahre statt des Schnellen.",
 "pt-BR": "Uma carta que custa alguma coisa é mais bem escrita. Aqui você não dispara sete seguidas, não se corrige uma hora depois e não pode chamar nenhuma de volta. Então você fica um tempo com ela, e diz o que é verdadeiro em vez do que é rápido.",
 "ja": "手間のかかる手紙のほうが、うまく書ける。ここでは七通を続けざまに送ることもなく、一時間後に言い直すこともなく、送ったものを取り消すこともできない。だからしばらく手元に置いて、早い言葉ではなく本当の言葉を書く。"},

"And the waiting turns out to be the good part.": {
 "it": "E l'attesa si scopre essere la parte bella.",
 "es": "Y resulta que la espera es lo mejor.",
 "fr": "Et l'attente se révèle être le meilleur.",
 "de": "Und das Warten stellt sich als das Schönste heraus.",
 "pt-BR": "E a espera acaba sendo a melhor parte.",
 "ja": "そして待つ時間こそが、いちばんいいところだと分かる。"},

"Days pass. You do other things. Then the tide leaves something on your sand that nobody scheduled, nobody promoted and nobody could have sold you — a stranger's handwriting, from a coast you have never seen.": {
 "it": "Passano i giorni. Fai altro. Poi la marea ti lascia sulla sabbia una cosa che nessuno aveva programmato, nessuno aveva sponsorizzato e nessuno avrebbe potuto venderti — la calligrafia di uno sconosciuto, da una costa che non hai mai visto.",
 "es": "Pasan los días. Haces otras cosas. Entonces la marea deja en tu arena algo que nadie programó, nadie promocionó y nadie podría haberte vendido: la letra de un desconocido, desde una costa que nunca has visto.",
 "fr": "Les jours passent. Vous faites autre chose. Puis la marée laisse sur votre sable quelque chose que personne n'avait programmé, que personne n'avait promu et que personne n'aurait pu vous vendre — l'écriture d'un inconnu, venue d'une côte que vous n'avez jamais vue.",
 "de": "Tage vergehen. Sie tun anderes. Dann lässt die Flut etwas in Ihrem Sand zurück, das niemand geplant, niemand beworben und niemand Ihnen hätte verkaufen können — die Handschrift eines Fremden, von einer Küste, die Sie nie gesehen haben.",
 "pt-BR": "Os dias passam. Você faz outras coisas. Então a maré deixa na sua areia algo que ninguém programou, ninguém promoveu e ninguém poderia ter vendido para você — a letra de um desconhecido, de uma costa que você nunca viu.",
 "ja": "日が過ぎる。ほかのことをして暮らす。するとある日、潮が砂に何かを置いていく。誰も予定せず、誰も宣伝せず、誰にも売ることのできなかったもの——見たこともない海岸から届いた、知らない誰かの手書きの文字だ。"},

"Somewhere to go when everything else is shouting.": {
 "it": "Un posto dove andare quando tutto il resto urla.",
 "es": "Un sitio al que ir cuando todo lo demás grita.",
 "fr": "Un endroit où aller quand tout le reste crie.",
 "de": "Ein Ort für die Zeiten, in denen alles andere schreit.",
 "pt-BR": "Um lugar para ir quando todo o resto está gritando.",
 "ja": "ほかのすべてが叫んでいるとき、行ける場所。"},

"Here it is morning and the wind comes off the land. I will not tell you my name, but I will tell you that I planted three fig trees behind the house and one of them took. If this bottle lands anywhere at all, write and tell me the weather where you are.": {
 "it": "Qui è mattina e il vento viene da terra. Non ti dirò il mio nome, ma ti dirò che ho piantato tre fichi dietro casa e uno ha attecchito. Se questa bottiglia approda da qualche parte, scrivimi e dimmi che tempo fa da te.",
 "es": "Aquí es de mañana y el viento viene de tierra. No te diré mi nombre, pero sí que planté tres higueras detrás de la casa y una prendió. Si esta botella llega a alguna parte, escríbeme y dime qué tiempo hace donde estás.",
 "fr": "Ici c'est le matin et le vent vient de la terre. Je ne vous dirai pas mon nom, mais je vous dirai que j'ai planté trois figuiers derrière la maison et que l'un d'eux a pris. Si cette bouteille aborde quelque part, écrivez-moi le temps qu'il fait chez vous.",
 "de": "Hier ist Morgen und der Wind kommt vom Land. Ich nenne Ihnen meinen Namen nicht, aber ich sage Ihnen, dass ich hinter dem Haus drei Feigenbäume gepflanzt habe und einer angewachsen ist. Wenn diese Flasche irgendwo anlandet, schreiben Sie mir, wie das Wetter bei Ihnen ist.",
 "pt-BR": "Aqui é manhã e o vento vem da terra. Não vou dizer meu nome, mas vou dizer que plantei três figueiras atrás de casa e uma pegou. Se esta garrafa chegar a algum lugar, escreva e me conte que tempo faz aí.",
 "ja": "こちらは朝で、風は陸から吹いてくる。名前は明かさないけれど、家の裏にいちじくを三本植えて、そのうち一本が根づいたことは伝えておく。この瓶がどこかに着いたら、そちらの天気を書いて送ってほしい。"},

"Every day the tide will bring bottles from strangers across the sea. Speak kindly — words travel far.": {
 "it": "Ogni giorno la marea porterà bottiglie di sconosciuti da tutto il mare. Parla con gentilezza — le parole vanno lontano.",
 "es": "Cada día la marea traerá botellas de desconocidos de todo el mar. Habla con amabilidad: las palabras llegan lejos.",
 "fr": "Chaque jour, la marée apportera des bouteilles d'inconnus de toute la mer. Parlez avec douceur — les mots vont loin.",
 "de": "Jeden Tag bringt die Flut Flaschen von Fremden aus dem ganzen Meer. Sprechen Sie freundlich — Worte reisen weit.",
 "pt-BR": "Todo dia a maré vai trazer garrafas de desconhecidos de todo o mar. Fale com gentileza — as palavras vão longe.",
 "ja": "毎日、潮が海じゅうの見知らぬ人たちの瓶を運んでくる。やさしい言葉を。言葉は遠くまで行く。"},


"The sea has no use for hurry. Write to a stranger on a real beach and let the tide take days to carry it — no names, no feeds, an iPhone app for people who want the waiting back.": {
 "it": "Il mare non sa che farsene della fretta. Scrivi a uno sconosciuto su una spiaggia vera e lascia che la marea ci metta giorni a portarla — niente nomi, niente feed, un'app per iPhone per chi si rivuole indietro l'attesa.",
 "es": "Al mar no le sirve de nada la prisa. Escribe a un desconocido en una playa de verdad y deja que la marea tarde días en llevarla: sin nombres, sin feeds, una app de iPhone para quien quiere recuperar la espera.",
 "fr": "La mer n'a que faire de la hâte. Écrivez à un inconnu sur une vraie plage et laissez la marée mettre des jours à l'emporter — aucun nom, aucun fil, une application iPhone pour qui veut retrouver l'attente.",
 "de": "Das Meer weiß mit Eile nichts anzufangen. Schreiben Sie einem Fremden an einem wirklichen Strand und lassen Sie die Flut Tage dafür brauchen — keine Namen, keine Feeds, eine iPhone-App für alle, die das Warten zurückwollen.",
 "pt-BR": "O mar não tem uso para a pressa. Escreva para um desconhecido numa praia de verdade e deixe a maré levar dias para entregar — sem nomes, sem feeds, um app de iPhone para quem quer a espera de volta.",
 "ja": "海に急ぎは要らない。実在する浜辺にいる見知らぬ誰かへ手紙を書き、潮が何日もかけて運ぶのにまかせる。名前もフィードもない、待つ時間を取り戻したい人のための iPhone アプリ。"},

"The sea has no use for hurry. Write to a stranger on a real beach and let the tide take days to carry it.": {
 "it": "Il mare non sa che farsene della fretta. Scrivi a uno sconosciuto su una spiaggia vera e lascia che la marea ci metta giorni a portarla.",
 "es": "Al mar no le sirve de nada la prisa. Escribe a un desconocido en una playa de verdad y deja que la marea tarde días en llevarla.",
 "fr": "La mer n'a que faire de la hâte. Écrivez à un inconnu sur une vraie plage et laissez la marée mettre des jours à l'emporter.",
 "de": "Das Meer weiß mit Eile nichts anzufangen. Schreiben Sie einem Fremden an einem wirklichen Strand und lassen Sie die Flut Tage dafür brauchen.",
 "pt-BR": "O mar não tem uso para a pressa. Escreva para um desconhecido numa praia de verdade e deixe a maré levar dias para entregar.",
 "ja": "海に急ぎは要らない。実在する浜辺にいる見知らぬ誰かへ手紙を書き、潮が何日もかけて運ぶのにまかせる。"},

"Sections": {
 "it": "Sezioni", "es": "Secciones", "fr": "Sections",
 "de": "Abschnitte", "pt-BR": "Seções", "ja": "セクション"},

"A nautical chart with the route of a bottle across the open sea": {
 "it": "Una carta nautica con la rotta di una bottiglia attraverso il mare aperto",
 "es": "Una carta náutica con la ruta de una botella a través del mar abierto",
 "fr": "Une carte marine avec la route d'une bouteille en pleine mer",
 "de": "Eine Seekarte mit der Route einer Flasche über das offene Meer",
 "pt-BR": "Uma carta náutica com a rota de uma garrafa pelo mar aberto",
 "ja": "外洋を渡る瓶の航路を記した海図"},

"The app at Cala Goloritzé at midday: turquoise sea, pale sand, and four bottles washed up on the shore.": {
 "it": "L'app a Cala Goloritzé a mezzogiorno: mare turchese, sabbia chiara e quattro bottiglie approdate sulla riva.",
 "es": "La app en Cala Goloritzé a mediodía: mar turquesa, arena clara y cuatro botellas llegadas a la orilla.",
 "fr": "L'application à Cala Goloritzé à midi : mer turquoise, sable clair et quatre bouteilles échouées sur le rivage.",
 "de": "Die App an der Cala Goloritzé zur Mittagszeit: türkisfarbenes Meer, heller Sand und vier angespülte Flaschen.",
 "pt-BR": "O app em Cala Goloritzé ao meio-dia: mar turquesa, areia clara e quatro garrafas na praia.",
 "ja": "正午のカーラ・ゴロリッツェのアプリ画面。ターコイズの海、明るい砂、岸に打ち上げられた四本の瓶。"},

"A correspondence in the journal: a letter from a stranger the reader has privately named Black sand, the reply underneath, and a note saying a bottle of theirs is still at sea.": {
 "it": "Un carteggio nel diario: la lettera di uno sconosciuto a cui chi legge ha dato in privato il nome «Black sand», sotto la risposta, e un avviso che dice che una loro bottiglia è ancora in mare.",
 "es": "Una correspondencia en el diario: la carta de un desconocido a quien quien lee ha llamado en privado «Black sand», debajo la respuesta, y un aviso de que una botella suya sigue en el mar.",
 "fr": "Une correspondance dans le journal : la lettre d'un inconnu que le lecteur a nommé en privé « Black sand », la réponse en dessous, et une note indiquant qu'une de leurs bouteilles est encore en mer.",
 "de": "Ein Briefwechsel im Tagebuch: der Brief eines Fremden, den die lesende Person im Stillen „Black sand“ genannt hat, darunter die Antwort und ein Hinweis, dass eine Flasche von ihnen noch auf See ist.",
 "pt-BR": "Uma correspondência no diário: a carta de um desconhecido a quem quem lê deu em particular o nome «Black sand», a resposta abaixo, e um aviso de que uma garrafa dele ainda está no mar.",
 "ja": "日誌のなかの文通。読み手が心のなかで「Black sand」と名づけた相手からの手紙、その下に返信、そして相手の瓶がまだ海の上にあることを告げる一行。"},

"The nautical chart: a route drawn from Cala Goloritzé out of the Mediterranean and north across the Atlantic towards Iceland, with the bottle partway along it.": {
 "it": "La carta nautica: una rotta disegnata da Cala Goloritzé fuori dal Mediterraneo e su per l'Atlantico verso l'Islanda, con la bottiglia a metà strada.",
 "es": "La carta náutica: una ruta trazada desde Cala Goloritzé fuera del Mediterráneo y hacia el norte por el Atlántico rumbo a Islandia, con la botella a medio camino.",
 "fr": "La carte marine : une route tracée depuis Cala Goloritzé, hors de la Méditerranée et vers le nord à travers l'Atlantique en direction de l'Islande, la bouteille à mi-parcours.",
 "de": "Die Seekarte: eine Route von der Cala Goloritzé aus dem Mittelmeer hinaus und nordwärts über den Atlantik Richtung Island, die Flasche auf halbem Weg.",
 "pt-BR": "A carta náutica: uma rota traçada de Cala Goloritzé para fora do Mediterrâneo e ao norte pelo Atlântico rumo à Islândia, com a garrafa no meio do caminho.",
 "ja": "海図。カーラ・ゴロリッツェから地中海を出て、大西洋を北上しアイスランドへ向かう航路。瓶はその途中にいる。"},

"The beach, as the app draws it: the shore and the hour chosen with the buttons beside it.": {
 "it": "La spiaggia come la disegna l'app: la costa e l'ora scelte con i pulsanti qui accanto.",
 "es": "La playa tal como la dibuja la app: la costa y la hora elegidas con los botones de al lado.",
 "fr": "La plage telle que l'application la dessine : le rivage et l'heure choisis avec les boutons à côté.",
 "de": "Der Strand, wie die App ihn zeichnet: Küste und Stunde, gewählt mit den Schaltflächen daneben.",
 "pt-BR": "A praia como o app a desenha: a costa e a hora escolhidas com os botões ao lado.",
 "ja": "アプリが描く浜辺。海岸と時刻は、となりのボタンで選ぶ。"},

"Who you are here": {
 "it": "Chi sei, qui", "es": "Quién eres aquí", "fr": "Qui vous êtes ici",
 "de": "Wer Sie hier sind", "pt-BR": "Quem você é aqui", "ja": "ここでのあなた"},

"No name. No face.": {
 "it": "Nessun nome. Nessun volto.", "es": "Sin nombre. Sin rostro.",
 "fr": "Pas de nom. Pas de visage.", "de": "Kein Name. Kein Gesicht.",
 "pt-BR": "Sem nome. Sem rosto.", "ja": "名前もなく、顔もない。"},

"A seal in wax.": {
 "it": "Un sigillo di ceralacca.", "es": "Un sello de lacre.",
 "fr": "Un sceau de cire.", "de": "Ein Siegel in Wachs.",
 "pt-BR": "Um selo de lacre.", "ja": "あるのは蝋の封印だけ。"},

"Every castaway presses the same emblem into the wax, always — and on this sea that is the whole of a person: no profile, no photograph, no history, nothing to look up afterwards. A stranger, a shore, and their handwriting.": {
 "it": "Ogni naufrago imprime sempre lo stesso emblema nella cera — e su questo mare quello è tutto di una persona: nessun profilo, nessuna fotografia, nessuno storico, niente da andare a cercare dopo. Uno sconosciuto, una riva, e la sua calligrafia.",
 "es": "Cada náufrago imprime siempre el mismo emblema en el lacre, y en este mar eso es toda una persona: sin perfil, sin fotografía, sin historial, sin nada que buscar después. Un desconocido, una orilla y su letra.",
 "fr": "Chaque naufragé imprime toujours le même emblème dans la cire — et sur cette mer, c'est là tout un être : pas de profil, pas de photographie, pas d'historique, rien à aller chercher ensuite. Un inconnu, un rivage, et son écriture.",
 "de": "Jeder Schiffbrüchige drückt stets dasselbe Emblem ins Wachs — und auf diesem Meer ist das ein ganzer Mensch: kein Profil, kein Foto, keine Chronik, nichts zum Nachschlagen. Ein Fremder, ein Ufer und seine Handschrift.",
 "pt-BR": "Cada náufrago imprime sempre o mesmo emblema no lacre — e neste mar isso é uma pessoa inteira: sem perfil, sem fotografia, sem histórico, nada para procurar depois. Um desconhecido, uma praia e a letra dele.",
 "ja": "どの漂流者も、いつも同じ紋章を蝋に押す。この海では、それが人のすべてだ。プロフィールも、写真も、履歴もなく、あとから調べられるものは何もない。見知らぬ誰かと、ひとつの岸と、その手書きの文字だけ。"},

"They may be writing to you in a language you have never read. One tap turns it into yours; another puts their own words back, exactly as they wrote them.": {
 "it": "Può darsi che ti scrivano in una lingua che non hai mai letto. Un tocco la porta nella tua; un altro rimette le loro parole com'erano, esattamente come le hanno scritte.",
 "es": "Puede que te escriban en una lengua que nunca has leído. Un toque la convierte en la tuya; otro devuelve sus palabras tal como las escribieron.",
 "fr": "Ils vous écrivent peut-être dans une langue que vous n'avez jamais lue. Une touche la met dans la vôtre ; une autre remet leurs mots exactement comme ils les ont écrits.",
 "de": "Vielleicht schreibt man Ihnen in einer Sprache, die Sie nie gelesen haben. Ein Tippen macht sie zu Ihrer; ein weiteres stellt die eigenen Worte wieder her, genau so, wie sie geschrieben wurden.",
 "pt-BR": "Pode ser que escrevam para você numa língua que você nunca leu. Um toque a transforma na sua; outro devolve as palavras deles exatamente como foram escritas.",
 "ja": "読んだことのない言語で書かれてくるかもしれない。ひと押しで自分の言葉になり、もうひと押しで、書かれたとおりの言葉に戻る。"},

"What you keep": {
 "it": "Quello che conservi", "es": "Lo que conservas", "fr": "Ce que vous gardez",
 "de": "Was bleibt", "pt-BR": "O que você guarda", "ja": "手元に残るもの"},

"A correspondence, not a chat.": {
 "it": "Un carteggio, non una chat.", "es": "Una correspondencia, no un chat.",
 "fr": "Une correspondance, pas une conversation.", "de": "Ein Briefwechsel, kein Chat.",
 "pt-BR": "Uma correspondência, não um chat.", "ja": "チャットではなく、文通。"},

"Letters do not scroll away here. They stay in a journal made of paper, in the order the sea delivered them — yours on one side, theirs on the other, each with the day it came ashore written underneath.": {
 "it": "Qui le lettere non scorrono via. Restano in un diario di carta, nell'ordine in cui il mare le ha consegnate — le tue da una parte, le loro dall'altra, ognuna con sotto il giorno in cui è approdata.",
 "es": "Aquí las cartas no se van con el desplazamiento. Se quedan en un diario de papel, en el orden en que el mar las entregó: las tuyas de un lado, las suyas del otro, cada una con el día en que llegó a la orilla escrito debajo.",
 "fr": "Ici, les lettres ne défilent pas au loin. Elles restent dans un journal de papier, dans l'ordre où la mer les a remises — les vôtres d'un côté, les leurs de l'autre, chacune avec, en dessous, le jour où elle a abordé.",
 "de": "Hier scrollen Briefe nicht davon. Sie bleiben in einem Tagebuch aus Papier, in der Reihenfolge, in der das Meer sie brachte — Ihre auf der einen Seite, ihre auf der anderen, jeder mit dem Tag darunter, an dem er anlandete.",
 "pt-BR": "Aqui as cartas não somem com a rolagem. Elas ficam num diário de papel, na ordem em que o mar as entregou — as suas de um lado, as dele do outro, cada uma com o dia em que chegou escrito embaixo.",
 "ja": "ここでは手紙が流れて消えたりしない。紙の日誌に、海が届けた順のまま残る。自分のものは片側に、相手のものは反対側に、それぞれの下に岸へ着いた日が書かれている。"},

"You may give a stranger a private name, only for your own pages:": {
 "it": "A uno sconosciuto puoi dare un nome privato, solo per le tue pagine:",
 "es": "A un desconocido puedes darle un nombre privado, solo para tus páginas:",
 "fr": "Vous pouvez donner à un inconnu un nom privé, rien que pour vos pages :",
 "de": "Einem Fremden dürfen Sie einen eigenen Namen geben, nur für Ihre Seiten:",
 "pt-BR": "Você pode dar a um desconhecido um nome particular, só para as suas páginas:",
 "ja": "見知らぬ相手には、自分の日誌のなかだけで通じる名前をつけられる。"},

"the lighthouse keeper": {
 "it": "il guardiano del faro", "es": "el farero", "fr": "le gardien du phare",
 "de": "der Leuchtturmwärter", "pt-BR": "o faroleiro", "ja": "灯台守"},

"the girl with the boat": {
 "it": "la ragazza con la barca", "es": "la chica de la barca",
 "fr": "la fille au bateau", "de": "das Mädchen mit dem Boot",
 "pt-BR": "a moça do barco", "ja": "舟をもつ娘"},

". They will never know it. And when a bottle of theirs is still out on the water, the journal simply says so, and asks you to wait.": {
 "it": ". Loro non lo sapranno mai. E quando una loro bottiglia è ancora in mare, il diario lo dice e basta, e ti chiede di aspettare.",
 "es": ". Ellos nunca lo sabrán. Y cuando una botella suya sigue en el agua, el diario lo dice sin más, y te pide que esperes.",
 "fr": ". Ils ne le sauront jamais. Et lorsqu'une de leurs bouteilles est encore sur l'eau, le journal le dit simplement, et vous demande d'attendre.",
 "de": ". Sie werden es nie erfahren. Und wenn eine Flasche von ihnen noch auf dem Wasser ist, sagt das Tagebuch es einfach und bittet Sie zu warten.",
 "pt-BR": ". Eles nunca vão saber. E quando uma garrafa deles ainda está na água, o diário simplesmente diz isso, e pede que você espere.",
 "ja": "。相手がそれを知ることはない。相手の瓶がまだ海の上にあるときは、日誌がそう告げて、待つように言うだけだ。"},

"The tide keeps its own time — and while you are here, so do you.": {
 "it": "La marea ha un suo tempo — e finché sei qui, ce l'hai anche tu.",
 "es": "La marea lleva su propio tiempo, y mientras estés aquí, tú también.",
 "fr": "La marée a son propre temps — et tant que vous êtes ici, vous aussi.",
 "de": "Die Gezeiten haben ihre eigene Zeit — und solange Sie hier sind, haben Sie sie auch.",
 "pt-BR": "A maré tem o tempo dela — e enquanto você estiver aqui, você também tem.",
 "ja": "潮には潮の時間がある。そしてここにいるあいだは、あなたにも。"},

"Where you wake up": {
 "it": "Dove ti svegli", "es": "Dónde te despiertas", "fr": "Où vous vous réveillez",
 "de": "Wo Sie aufwachen", "pt-BR": "Onde você acorda", "ja": "目を覚ます場所"},

"A real beach, and not one you picked.": {
 "it": "Una spiaggia vera, e non l'hai scelta tu.",
 "es": "Una playa de verdad, y no la has elegido tú.",
 "fr": "Une vraie plage, et ce n'est pas vous qui l'avez choisie.",
 "de": "Ein wirklicher Strand — und keiner, den Sie ausgesucht haben.",
 "pt-BR": "Uma praia de verdade, e não foi você que escolheu.",
 "ja": "本物の浜辺。しかも、自分で選んだのではない。"},
"Cala Goloritzé. Reynisfjara. Anse Source d'Argent. True stretches of coast at their true coordinates — and yours is drawn by lot. The storm decides where it leaves you, and from that morning on it is home. The light on it is the light of your own hour: open it at midnight and your beach is dark, with the stars out over the water. Not one of these is a photograph. Every wave is drawn by the app, line by line.": {
 "it": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Tratti di costa veri alle loro coordinate vere — e la tua te la dà la sorte. Decide la tempesta dove lasciarti, e da quella mattina è casa. La luce che ci sta sopra è quella della tua ora: aprila a mezzanotte e la tua spiaggia è buia, con le stelle sull'acqua. Nessuna di queste è una fotografia. Ogni onda la disegna l'app, linea per linea.",
 "es": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Tramos de costa reales en sus coordenadas reales, y la tuya te toca en suerte. La tormenta decide dónde dejarte, y desde esa mañana es tu casa. La luz que la baña es la de tu propia hora: ábrela a medianoche y tu playa está a oscuras, con las estrellas sobre el agua. Ninguna de estas es una fotografía. Cada ola la dibuja la app, línea a línea.",
 "fr": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. De vraies portions de côte à leurs vraies coordonnées — et la vôtre vous échoit au hasard. C'est la tempête qui décide où elle vous laisse, et dès ce matin-là c'est chez vous. La lumière qui la baigne est celle de votre propre heure : ouvrez à minuit et votre plage est sombre, les étoiles au-dessus de l'eau. Aucune n'est une photographie. Chaque vague est dessinée par l'application, trait par trait.",
 "de": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Echte Küstenstücke an ihren echten Koordinaten — und Ihres fällt Ihnen durch Los zu. Der Sturm entscheidet, wo er Sie zurücklässt, und von jenem Morgen an ist es Ihr Zuhause. Das Licht darauf ist das Ihrer eigenen Stunde: öffnen Sie um Mitternacht, und Ihr Strand ist dunkel, die Sterne über dem Wasser. Keines davon ist eine Fotografie. Jede Welle zeichnet die App, Strich für Strich.",
 "pt-BR": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Trechos de costa reais nas coordenadas reais — e a sua vem por sorteio. A tempestade decide onde deixar você, e daquela manhã em diante é casa. A luz sobre ela é a da sua própria hora: abra à meia-noite e a sua praia está escura, com as estrelas sobre a água. Nenhuma delas é uma fotografia. Cada onda é desenhada pelo app, linha por linha.",
 "ja": "カーラ・ゴロリッツェ。レイニスフィヤラ。アンス・スルス・ダルジャン。実在する海岸を、実在する座標のままに。そして自分の浜は、くじで決まる。どこに打ち上げるかを決めるのは嵐で、その朝からそこが家になる。射す光はあなたのいまの時刻の光だ。真夜中に開けば浜は暗く、水の上に星が出ている。どれも写真ではない。波の一本一本を、アプリが線で描いている。"},


"The shore": {
 "it": "La riva", "es": "La orilla", "fr": "Le rivage",
 "de": "Das Ufer", "pt-BR": "A praia", "ja": "岸"},

"The hour": {
 "it": "L'ora", "es": "La hora", "fr": "L'heure",
 "de": "Die Stunde", "pt-BR": "A hora", "ja": "時刻"},
"Here you can try them all. In the app you get one, and you do not choose it — which is the best thing about it. On arctic beaches, at night, the aurora passes overhead.": {
 "it": "Qui puoi provarle tutte. Nell'app te ne tocca una, e non la scegli tu — che è la cosa più bella. Sulle spiagge artiche, di notte, l'aurora passa sopra la testa.",
 "es": "Aquí puedes probarlas todas. En la app te toca una, y no la eliges tú, que es lo mejor de todo. En las playas árticas, de noche, la aurora pasa por encima.",
 "fr": "Ici vous pouvez toutes les essayer. Dans l'application vous en recevez une, et vous ne la choisissez pas — c'est ce qu'il y a de plus beau. Sur les plages arctiques, la nuit, l'aurore passe au-dessus.",
 "de": "Hier können Sie alle ausprobieren. In der App bekommen Sie einen, und Sie suchen ihn nicht aus — das ist das Schönste daran. An arktischen Stränden zieht nachts das Polarlicht über Sie hinweg.",
 "pt-BR": "Aqui você pode experimentar todas. No app você ganha uma, e não é você que escolhe — que é o melhor disso. Nas praias árticas, à noite, a aurora passa lá em cima.",
 "ja": "ここでは全部を試せる。アプリでは一つだけが与えられ、それを自分で選ぶことはできない——そこがいちばんいいところだ。北極圏の浜では、夜になるとオーロラが頭上を渡っていく。"},


"The crossing": {
 "it": "La traversata", "es": "La travesía", "fr": "La traversée",
 "de": "Die Überfahrt", "pt-BR": "A travessia", "ja": "航路"},

"You can watch it go.": {
 "it": "Puoi guardarla andare.", "es": "Puedes verla marchar.",
 "fr": "Vous pouvez la regarder s'en aller.", "de": "Sie können ihr nachsehen.",
 "pt-BR": "Você pode vê-la partir.", "ja": "旅立っていくのを、見ていられる。"},

"your shore": {
 "it": "la tua riva", "es": "tu orilla", "fr": "votre rivage",
 "de": "Ihr Ufer", "pt-BR": "sua praia", "ja": "あなたの岸"},

"still at sea": {
 "it": "ancora in mare", "es": "aún en el mar", "fr": "encore en mer",
 "de": "noch auf See", "pt-BR": "ainda no mar", "ja": "まだ海の上"},

"A bottle you have thrown leaves a line on the chart, and the line grows while you sleep. The solid part is the distance already sailed; the dashes ahead appear only once you know who is waiting at the far end.": {
 "it": "Una bottiglia che hai lanciato lascia una linea sulla carta, e la linea cresce mentre dormi. Il tratto pieno è la distanza già navigata; il tratteggio davanti compare solo quando sai chi aspetta dall'altra parte.",
 "es": "Una botella que has lanzado deja una línea en la carta, y la línea crece mientras duermes. El trazo continuo es la distancia ya navegada; los guiones de delante solo aparecen cuando sabes quién espera al otro extremo.",
 "fr": "Une bouteille que vous avez lancée laisse une ligne sur la carte, et la ligne grandit pendant votre sommeil. Le trait plein est la distance déjà parcourue ; les pointillés devant n'apparaissent qu'une fois que vous savez qui attend à l'autre bout.",
 "de": "Eine geworfene Flasche hinterlässt eine Linie auf der Karte, und die Linie wächst, während Sie schlafen. Der durchgezogene Teil ist die bereits gesegelte Strecke; die Striche voraus erscheinen erst, wenn Sie wissen, wer am anderen Ende wartet.",
 "pt-BR": "Uma garrafa que você lançou deixa uma linha na carta, e a linha cresce enquanto você dorme. O traço cheio é a distância já navegada; os tracejados à frente só aparecem quando você sabe quem espera do outro lado.",
 "ja": "投げた瓶は海図に一本の線を残し、その線は眠っているあいだも伸びていく。実線はすでに渡った距離。その先の破線は、向こう岸で誰が待っているかを知ってからでないと現れない。"},

"The islands of strangers whose letters you have read stay marked there for good — a private map of everyone the sea has introduced you to.": {
 "it": "Le isole degli sconosciuti di cui hai letto le lettere restano segnate per sempre — una mappa privata di tutti quelli che il mare ti ha presentato.",
 "es": "Las islas de los desconocidos cuyas cartas has leído quedan marcadas para siempre: un mapa privado de todos los que el mar te ha presentado.",
 "fr": "Les îles des inconnus dont vous avez lu les lettres restent marquées pour de bon — une carte privée de tous ceux que la mer vous a présentés.",
 "de": "Die Inseln der Fremden, deren Briefe Sie gelesen haben, bleiben für immer eingezeichnet — eine private Karte all jener, die das Meer Ihnen vorgestellt hat.",
 "pt-BR": "As ilhas dos desconhecidos cujas cartas você leu ficam marcadas para sempre — um mapa particular de todos que o mar apresentou a você.",
 "ja": "手紙を読んだ相手の島は、そのまま海図に残りつづける。海が引き合わせてくれた人たちだけの、自分だけの地図になる。"},

"The chart is the app's own: coastlines from Natural Earth, public domain, carried inside it. No map service is ever called, and nothing about where you are leaves your hands.": {
 "it": "La carta è tutta dell'app: coste da Natural Earth, di pubblico dominio, portate dentro. Nessun servizio di mappe viene mai chiamato, e niente di dove sei esce dalle tue mani.",
 "es": "La carta es de la propia app: costas de Natural Earth, de dominio público, llevadas dentro. Nunca se llama a ningún servicio de mapas, y nada sobre dónde estás sale de tus manos.",
 "fr": "La carte appartient à l'application : côtes issues de Natural Earth, domaine public, embarquées avec elle. Aucun service cartographique n'est jamais appelé, et rien de votre position ne quitte vos mains.",
 "de": "Die Karte gehört der App selbst: Küstenlinien von Natural Earth, gemeinfrei, im Programm mitgeführt. Kein Kartendienst wird je aufgerufen, und nichts über Ihren Standort verlässt Ihre Hände.",
 "pt-BR": "A carta é do próprio app: costas do Natural Earth, de domínio público, carregadas dentro dele. Nenhum serviço de mapas é chamado, e nada sobre onde você está sai das suas mãos.",
 "ja": "海図はアプリ自身のものだ。海岸線はパブリックドメインの Natural Earth を内部に持っている。地図サービスを呼ぶことは一度もなく、あなたの居場所に関する情報が手元から出ていくこともない。"},

"Before you go": {
 "it": "Prima di andare", "es": "Antes de irte", "fr": "Avant de partir",
 "de": "Bevor Sie gehen", "pt-BR": "Antes de ir", "ja": "行く前に"},

"At the foot of every open letter there is “Report to the Sea”. The correspondence closes, and the letter does not come back to your sand. You can block its author in the same gesture: the tide will never bring you together again, in either direction.": {
 "it": "In fondo a ogni lettera aperta c'è «Riferisci al Mare». Il carteggio si chiude, e la lettera non torna sulla tua sabbia. Con lo stesso gesto puoi bloccare chi l'ha scritta: la marea non vi rimetterà più insieme, né in un verso né nell'altro.",
 "es": "Al pie de cada carta abierta está «Informar al Mar». La correspondencia se cierra y la carta no vuelve a tu arena. Con el mismo gesto puedes bloquear a quien la escribió: la marea no volverá a reuniros, en ninguna dirección.",
 "fr": "Au bas de chaque lettre ouverte se trouve « Signaler à la Mer ». La correspondance se ferme, et la lettre ne revient pas sur votre sable. Du même geste, vous pouvez bloquer son auteur : la marée ne vous réunira plus jamais, dans aucun sens.",
 "de": "Am Fuß jedes geöffneten Briefes steht „Dem Meer melden“. Der Briefwechsel schließt sich, und der Brief kehrt nicht in Ihren Sand zurück. Mit derselben Geste können Sie den Verfasser sperren: Die Flut wird Sie nie wieder zusammenbringen, in keine Richtung.",
 "pt-BR": "No pé de cada carta aberta há «Relatar ao Mar». A correspondência se encerra, e a carta não volta para a sua areia. No mesmo gesto você pode bloquear quem a escreveu: a maré nunca mais vai juntar vocês, em nenhuma direção.",
 "ja": "開いた手紙の末尾には「海に知らせる」がある。文通はそこで閉じ、その手紙が砂に戻ってくることはない。同じ動作で相手をブロックすることもできる。そうすれば潮が二人を引き合わせることは、どちらの向きにも二度とない。"},

"For an urgent report, a problem, or any question at all, this address reaches a real person:": {
 "it": "Per una segnalazione urgente, un problema o una domanda qualsiasi, questo indirizzo arriva a una persona vera:",
 "es": "Para un aviso urgente, un problema o cualquier duda, esta dirección llega a una persona de verdad:",
 "fr": "Pour un signalement urgent, un problème ou n'importe quelle question, cette adresse atteint une personne réelle :",
 "de": "Für eine dringende Meldung, ein Problem oder irgendeine Frage erreicht diese Adresse einen echten Menschen:",
 "pt-BR": "Para um aviso urgente, um problema ou qualquer dúvida, este endereço chega a uma pessoa de verdade:",
 "ja": "緊急の報告、不具合、そのほかどんな質問でも、この宛先は実在の人間に届く。"},

"A bottle, thrown well, can reach anyone.": {
 "it": "Una bottiglia, lanciata bene, può raggiungere chiunque.",
 "es": "Una botella, bien lanzada, puede llegar a cualquiera.",
 "fr": "Une bouteille, bien lancée, peut atteindre n'importe qui.",
 "de": "Eine gut geworfene Flasche kann jeden erreichen.",
 "pt-BR": "Uma garrafa, bem lançada, pode alcançar qualquer um.",
 "ja": "うまく投げた瓶は、誰のもとにも届きうる。"},

"Coastlines from Natural Earth (public domain). Sounds from freesound.org (CC0). No map service, no tracking, no cookies: this page does not know who you are, exactly like the sea.": {
 "it": "Coste da Natural Earth (pubblico dominio). Suoni da freesound.org (CC0). Nessun servizio di mappe, nessun tracciamento, nessun cookie: questa pagina non sa chi sei, esattamente come il mare.",
 "es": "Costas de Natural Earth (dominio público). Sonidos de freesound.org (CC0). Sin servicio de mapas, sin rastreo, sin cookies: esta página no sabe quién eres, igual que el mar.",
 "fr": "Côtes issues de Natural Earth (domaine public). Sons de freesound.org (CC0). Aucun service cartographique, aucun traçage, aucun cookie : cette page ne sait pas qui vous êtes, exactement comme la mer.",
 "de": "Küstenlinien von Natural Earth (gemeinfrei). Klänge von freesound.org (CC0). Kein Kartendienst, kein Tracking, keine Cookies: Diese Seite weiß nicht, wer Sie sind — genau wie das Meer.",
 "pt-BR": "Costas do Natural Earth (domínio público). Sons do freesound.org (CC0). Sem serviço de mapas, sem rastreamento, sem cookies: esta página não sabe quem você é, exatamente como o mar.",
 "ja": "海岸線は Natural Earth（パブリックドメイン）。音は freesound.org（CC0）。地図サービスも、追跡も、Cookie もない。このページはあなたが誰かを知らない——海とまったく同じように。"},
}

# Le frasi che non si traducono: nomi propri, indirizzi, la rosa dei venti.
INVARIATE = [",",  # la virgola fra i due soprannomi: punteggiatura, non testo
             "Bottlegram", "Cala Goloritzé", "N", "bottlegram@bulbmode.com",
             # La spiaggia disegnata cambia da sola con i pulsanti: i suoi nomi
             # li scrive app.js e sono nomi propri, tranne il paese — che è un
             # difetto noto, segnato nel README.
             "Haukland Beach", "Lofoten, Norway", "Bottles washed ashore: 2", "2",
             "The beach, as the app draws it — Haukland Beach, Night"]

# ── Le frasi che vengono dall'app ──────────────────────────────────────────
app = json.load(open(XCSTRINGS))
da_app = {}
for chiave, v in app["strings"].items():
    loc = v.get("localizations", {})
    en = loc.get("en", {}).get("stringUnit", {}).get("value") or chiave
    en = " ".join(en.split())
    valori = {lg: u.get("stringUnit", {}).get("value") for lg, u in loc.items() if u.get("stringUnit")}
    da_app[en] = valori

DAL_SITO = [
 # Le voci che l'app scrive DENTRO la schermata disegnata: la barra in basso,
 # i biomi e le ore. Sono parole dell'app, quindi vengono dall'app.
 "Map", "Journal", "Throw", "Emporium",
 "Mediterranean", "Tropical", "Arctic", "Volcanic", "Wild Atlantic",
 "Dawn", "Day", "Dusk", "Night",
 "The storm took the ship, the cargo, and every map you owned.",
 "The sea, in return, left you one thing: a beach at the end of the world.",
 "They say the tide brings words from other castaways. And that a bottle, thrown well, can reach anyone.",
 "Your new home", "A stranger", "The rules of the sea",
 "Here you write to strangers, and a stranger deserves the same courtesy as a neighbour. These are the few rules that keep this sea liveable.",
 "The sea tolerates none of this",
 "Harassment, insults, threats, hate or discrimination, sexual content, spam and scams. Zero tolerance: a letter like that is taken out of the sea, and whoever wrote it can be banished from their beach — even the first time.",
 "Any letter can be reported to the Sea",
 "Someone looks, within a day",
 "Every report is read by a person within 24 hours. The letter may be taken out of the sea and its author banished.",
 "Stay a stranger",
 "Nobody here knows who you are, and that is for the best: do not write your surname, your address, your number or your profiles. A letter sails and cannot be called back.",
 "Writing to whoever keeps the lighthouse",
 ]

# ── Il montaggio ───────────────────────────────────────────────────────────
fuori = {lg: {} for lg in LINGUE}
mancano = []

for en, per_lingua in SITO.items():
    if not any(per_lingua.values()):
        continue  # voce di servizio, non nella pagina
    for lg in LINGUE:
        t = per_lingua.get(lg)
        if t:
            fuori[lg][en] = t
        else:
            mancano.append((lg, en))

for en in DAL_SITO:
    valori = da_app.get(en)
    if not valori:
        mancano.append(("*", "NON TROVATA NELL'APP: " + en))
        continue
    for lg in LINGUE:
        t = valori.get(lg)
        if t:
            fuori[lg][en] = t
        else:
            mancano.append((lg, en))

if mancano:
    for lg, en in mancano:
        print(f"// MANCA [{lg}] {en[:70]}", file=sys.stderr)

print("""/* Le sette lingue del sito.

   GENERATO — non si corregge qui. La sorgente è `genera-lingue.py` (fuori dal
   repo, nella cartella di lavoro), che rimette insieme due cose diverse:

     · le frasi che esistono NELL'APP — le regole del mare, i versi del
       naufragio, il benvenuto — rilette da Localizable.xcstrings a ogni
       rigenerazione. Sono quelle che si dichiarano ad Apple: se divergessero
       dall'app di una virgola sarebbe un difetto, non una sfumatura;
     · le frasi del solo sito, scritte a mano dentro quello script.

   LA CHIAVE È L'INGLESE DELLA PAGINA, non un codice. Così qui si legge
   l'originale accanto alla traduzione, e se un giorno l'inglese in
   `index.html` cambia, la voce smette semplicemente di combaciare e la
   console lo dice — invece di lasciare una traduzione vecchia attaccata a una
   frase nuova, che è il modo in cui questi file mentono.

   L'inglese non sta qui dentro: sta nell'HTML, ed è quello che legge chi
   arriva senza JavaScript. */""")
print("const LINGUE = " + json.dumps(fuori, ensure_ascii=False, indent=1) + ";")
print("const INVARIATE = " + json.dumps(INVARIATE, ensure_ascii=False) + ";")
