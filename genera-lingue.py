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

# ── «Come funziona»: la traversata (28/07) ────────────────────────────────
# Le quattro tappe dicono le stesse cose della pagina «Come funziona»
# dell'app (chiavi howto.* in Localizable.xcstrings), ma NON sono le stesse
# stringhe: là si parla a chi è già dentro, qui a chi sta ancora decidendo.
# Vanno tenute d'accordo nel contenuto, non nella lettera — se un giorno
# cambiano le tre bottiglie o le ore, si cambiano tutte e due.

"In a hurry? The sea takes the long way.": {
 "it": "Sei di fretta? Il mare prende la strada lunga.",
 "es": "¿Tienes prisa? El mar toma el camino largo.",
 "fr": "Tu es pressé ? La mer prend le chemin des écoliers.",
 "de": "In Eile? Das Meer nimmt den langen Weg.",
 "pt-BR": "Com pressa? O mar vai pelo caminho mais longo.",
 "ja": "急いでいますか。海は遠回りをします。"},

"How it works": {
 "it": "Come funziona", "es": "Cómo funciona", "fr": "Comment ça marche",
 "de": "Wie es funktioniert", "pt-BR": "Como funciona", "ja": "遊びかた"},

"Three bottles a day,": {
 "it": "Tre bottiglie al giorno,", "es": "Tres botellas al día,",
 "fr": "Trois bouteilles par jour,", "de": "Drei Flaschen am Tag,",
 "pt-BR": "Três garrafas por dia,", "ja": "一日に三本、"},

"and a whole sea in between.": {
 "it": "e un mare intero in mezzo.", "es": "y un mar entero en medio.",
 "fr": "et une mer entière entre les deux.", "de": "und dazwischen ein ganzes Meer.",
 "pt-BR": "e um mar inteiro no meio.", "ja": "あいだには、ひとつの海。"},

"Bottlegram is a slow messaging app. You write to the sea, and the current decides who you end up talking to.": {
 "it": "Bottlegram è una applicazione di messaggistica lenta. Scrivi al mare, ed è la corrente a decidere con chi finirai per parlare.",
 "es": "Bottlegram es una aplicación de mensajería lenta. Escribes al mar, y la corriente decide con quién acabas hablando.",
 "fr": "Bottlegram est une application de messagerie lente. Tu écris à la mer, et c'est le courant qui décide de ton interlocuteur.",
 "de": "Bottlegram ist eine App für langsame Nachrichten. Du schreibst dem Meer, und die Strömung entscheidet, mit wem du am Ende sprichst.",
 "pt-BR": "Bottlegram é um aplicativo de mensageria lenta. Você escreve para o mar, e a correnteza decide com quem você vai conversar.",
 "ja": "Bottlegram は、ゆっくりとしたメッセージのやりとりをするアプリです。あなたは海に宛てて書き、だれと話すことになるかは潮が決めます。"},

"A stretch of sea seen from above: two coasts, and a bottle drifting from one to the other.": {
 "it": "Un tratto di mare visto dall'alto: due coste, e una bottiglia che va dall'una all'altra.",
 "es": "Un trecho de mar visto desde arriba: dos costas, y una botella que va de una a otra.",
 "fr": "Une étendue de mer vue d'en haut : deux côtes, et une bouteille qui va de l'une à l'autre.",
 "de": "Ein Stück Meer von oben: zwei Küsten und eine Flasche, die von der einen zur anderen treibt.",
 "pt-BR": "Um trecho de mar visto de cima: duas costas, e uma garrafa que vai de uma à outra.",
 "ja": "上から見た海の一角。ふたつの岸と、その一方からもう一方へ流れていく瓶。"},

"Your shore": {
 "it": "La tua riva", "es": "Tu orilla", "fr": "Ta rive",
 "de": "Dein Ufer", "pt-BR": "Sua praia", "ja": "あなたの岸"},

"Someone's shore": {
 "it": "La riva di qualcuno", "es": "La orilla de alguien", "fr": "La rive de quelqu'un",
 "de": "Jemandes Ufer", "pt-BR": "A praia de alguém", "ja": "だれかの岸"},

"six to thirty-six hours": {
 "it": "da sei a trentasei ore", "es": "de seis a treinta y seis horas",
 "fr": "de six à trente-six heures", "de": "sechs bis sechsunddreißig Stunden",
 "pt-BR": "de seis a trinta e seis horas", "ja": "六時間から三十六時間"},

"You throw a bottle": {
 "it": "Lanci una bottiglia", "es": "Lanzas una botella", "fr": "Tu lances une bouteille",
 "de": "Du wirfst eine Flasche", "pt-BR": "Você lança uma garrafa", "ja": "瓶をひとつ放つ"},

"Every day the sea leaves you three bottles. You put a message inside and hand it to the current, and the current chooses who gets it.": {
 "it": "Ogni giorno il mare ti lascia tre bottiglie. Ci metti dentro un messaggio e lo affidi alla corrente, e la corrente sceglie chi lo riceve.",
 "es": "Cada día el mar te deja tres botellas. Metes dentro un mensaje y lo confías a la corriente, y la corriente elige quién lo recibe.",
 "fr": "Chaque jour la mer te laisse trois bouteilles. Tu y glisses un message et tu le confies au courant, et c'est le courant qui choisit qui le reçoit.",
 "de": "Jeden Tag lässt dir das Meer drei Flaschen da. Du legst eine Nachricht hinein und übergibst sie der Strömung, und die Strömung wählt, wer sie bekommt.",
 "pt-BR": "Todo dia o mar te deixa três garrafas. Você põe uma mensagem dentro e a entrega à correnteza, e a correnteza escolhe quem a recebe.",
 "ja": "海は毎日、三本の瓶を置いていきます。ことづてを入れて潮へゆだねれば、だれに届くかは潮が選びます。"},

"Someone finds it": {
 "it": "Qualcuno la trova", "es": "Alguien la encuentra", "fr": "Quelqu'un la trouve",
 "de": "Jemand findet sie", "pt-BR": "Alguém a encontra", "ja": "だれかが拾う"},

"Six to thirty-six hours later it washes up on another castaway's beach. In the same way, other people's bottles wash up on your sand.": {
 "it": "Da sei a trentasei ore dopo approda sulla spiaggia di un altro naufrago. Allo stesso modo, sulla tua sabbia arrivano le bottiglie degli altri.",
 "es": "Entre seis y treinta y seis horas después llega a la playa de otro náufrago. Del mismo modo, a tu arena llegan las botellas de los demás.",
 "fr": "Six à trente-six heures plus tard, elle échoue sur la plage d'un autre naufragé. De la même façon, les bouteilles des autres échouent sur ton sable.",
 "de": "Sechs bis sechsunddreißig Stunden später strandet sie am Strand eines anderen Schiffbrüchigen. Genauso stranden die Flaschen anderer an deinem Sand.",
 "pt-BR": "De seis a trinta e seis horas depois, ela encalha na praia de outro náufrago. Do mesmo modo, na sua areia chegam as garrafas dos outros.",
 "ja": "六時間から三十六時間ののち、べつの漂流者の浜へ流れ着きます。同じように、あなたの砂浜にも、ほかの人の瓶が届きます。"},

"And answers, if they want to": {
 "it": "E se vuole, risponde", "es": "Y si quiere, responde", "fr": "Et s'il veut, il répond",
 "de": "Und antwortet, wenn er mag", "pt-BR": "E responde, se quiser", "ja": "気が向けば、返事が来る"},

"Whoever finds your letter can write back, and a correspondence begins. Whether they answer is up to them, as it always is at sea.": {
 "it": "Chi trova la tua lettera può risponderti, e da lì nasce una corrispondenza. Se rispondere lo decide chi la trova, come in mare è sempre stato.",
 "es": "Quien encuentre tu carta puede contestarte, y de ahí nace una correspondencia. Contestar es cosa suya, como siempre ha sido en el mar.",
 "fr": "Celui qui trouve ta lettre peut te répondre, et une correspondance commence. Répondre, c'est son choix, comme toujours en mer.",
 "de": "Wer deinen Brief findet, kann antworten, und daraus wird ein Briefwechsel. Ob jemand antwortet, entscheidet er selbst, wie es auf See immer war.",
 "pt-BR": "Quem encontra sua carta pode responder, e daí nasce uma correspondência. Responder é escolha de quem a encontra, como sempre foi no mar.",
 "ja": "手紙を拾った人は、返事を書くことができます。そこから文通がはじまります。返すかどうかは拾った人が決めます。海ではずっと、そういうものでした。"},

"The chart follows them": {
 "it": "La carta le segue", "es": "La carta las sigue", "fr": "La carte les suit",
 "de": "Die Karte folgt ihnen", "pt-BR": "A carta as acompanha", "ja": "海図が追いかける"},

"On the map you can watch the bottles you have thrown, and the ones travelling back to you from the shores you already know.": {
 "it": "Sulla mappa guardi le bottiglie che hai lanciato, e quelle che tornano verso di te dalle rive che conosci già.",
 "es": "En el mapa miras las botellas que has lanzado, y las que vuelven hacia ti desde las orillas que ya conoces.",
 "fr": "Sur la carte, tu regardes les bouteilles que tu as lancées, et celles qui reviennent vers toi des rives que tu connais déjà.",
 "de": "Auf der Karte siehst du deine geworfenen Flaschen und die, die von den Ufern, die du schon kennst, zu dir zurückkommen.",
 "pt-BR": "No mapa você acompanha as garrafas que lançou, e as que voltam para você das praias que já conhece.",
 "ja": "地図では、あなたが放った瓶と、すでに知っている岸から戻ってくる瓶を見守れます。"},

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

"Somewhere out there, someone you will never meet is writing to you. The current will carry their bottle to your sand, and yours to a beach you have never seen, in six to thirty-six hours.": {
 "it": "Da qualche parte, qualcuno che non incontrerai mai ti sta scrivendo. La corrente porterà la sua bottiglia sulla tua sabbia, e la tua su una spiaggia che non hai mai visto, fra sei e trentasei ore.",
 "es": "En algún lugar, alguien a quien nunca conocerás te está escribiendo. La corriente llevará su botella a tu arena, y la tuya a una playa que nunca has visto, en un plazo de seis a treinta y seis horas.",
 "fr": "Quelque part, quelqu'un que tu ne rencontreras jamais t'écrit. Le courant portera sa bouteille jusqu'à ton sable, et la tienne vers une plage que tu n'as jamais vue, en six à trente-six heures.",
 "de": "Irgendwo da draußen schreibt dir jemand, dem du nie begegnen wirst. Die Strömung trägt seine Flasche an deinen Sand und deine an einen Strand, den du nie gesehen hast, in sechs bis sechsunddreißig Stunden.",
 "pt-BR": "Em algum lugar, alguém que você nunca vai conhecer está escrevendo para você. A correnteza vai levar a garrafa dessa pessoa até a sua areia, e a sua até uma praia que você nunca viu, em seis a trinta e seis horas.",
 "ja": "どこかで、一生会うことのない誰かがあなたに手紙を書いている。潮はその瓶をあなたの砂へ、あなたの瓶をまだ見ぬ浜へ、六時間から三十六時間かけて運んでいく。"},

"Coming to iPhone and Android": {
 "it": "Presto su iPhone e Android",
 "es": "Pronto en iPhone y Android",
 "fr": "Bientôt sur iPhone et Android",
 "de": "Bald für iPhone und Android",
 "pt-BR": "Em breve para iPhone e Android",
 "ja": "iPhone と Android にまもなく登場"},

"Free to write, free to receive": {
 "it": "Gratis scrivere, gratis ricevere",
 "es": "Gratis escribir, gratis recibir",
 "fr": "Gratuit pour écrire, gratuit pour recevoir",
 "de": "Kostenlos schreiben, kostenlos empfangen",
 "pt-BR": "Grátis para escrever, grátis para receber",
 "ja": "書くのも、受け取るのも無料"},

"The app at Unstad, in the Lofoten, at night: the aurora and a full moon over a dark arctic sea, with a peak on the horizon.": {
 "it": "L'app a Unstad, alle Lofoten, di notte: l'aurora e la luna piena su un mare artico scuro, con una vetta all'orizzonte.",
 "es": "La app en Unstad, en las Lofoten, de noche: la aurora y la luna llena sobre un mar ártico oscuro, con un pico en el horizonte.",
 "fr": "L'application à Unstad, aux Lofoten, la nuit : l'aurore et la pleine lune sur une mer arctique sombre, avec un pic à l'horizon.",
 "de": "Die App in Unstad auf den Lofoten, nachts: das Polarlicht und der Vollmond über einem dunklen arktischen Meer, ein Gipfel am Horizont.",
 "pt-BR": "O app em Unstad, nas Lofoten, à noite: a aurora e a lua cheia sobre um mar ártico escuro, com um pico no horizonte.",
 "ja": "夜のウンスタッド（ロフォーテン）を映すアプリ。暗い北極の海の上にオーロラと満月、水平線には山の頂。"},

"The sea opens soon.": {
 "it": "Il mare apre presto.",
 "es": "El mar abre pronto.",
 "fr": "La mer ouvre bientôt.",
 "de": "Das Meer öffnet bald.",
 "pt-BR": "O mar abre em breve.",
 "ja": "海はもうすぐ開きます。"},

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

"and all of it on purpose.": {
 "it": "ed è tutto voluto.",
 "es": "y todo a propósito.",
 "fr": "et tout est voulu.",
 "de": "und alles mit Absicht.",
 "pt-BR": "e tudo de propósito.",
 "ja": "そのどれもが、わざとだ。"},

"You write, and then you wait.": {
 "it": "Scrivi, e poi aspetti.", "es": "Escribes, y luego esperas.",
 "fr": "Tu écris, puis tu attends.", "de": "Du schreibst, und dann wartest du.",
 "pt-BR": "Você escreve, e então espera.", "ja": "書いて、それから待つ。"},

"A letter takes as long as the water between you takes. A shore across the same sea might answer by morning; the far side of the world will keep you waiting for days. The answer comes when the water brings it — and after the first one, you learn to like the wait.": {
 "it": "Una lettera ci mette quanto ci mette l'acqua che vi separa. Una riva sullo stesso mare può risponderti entro domattina; dall'altra parte del mondo ti farà aspettare giorni. La risposta arriva quando l'acqua la porta — e dopo la prima volta impari ad amare l'attesa.",
 "es": "Una carta tarda lo que tarde el agua que os separa. Una orilla del mismo mar puede responder por la mañana; el otro extremo del mundo te hará esperar días. La respuesta llega cuando el agua la trae, y después de la primera aprendes a querer la espera.",
 "fr": "Une lettre met le temps que met l'eau qui vous sépare. Un rivage sur la même mer répondra peut-être au matin ; l'autre bout du monde te fera attendre des jours. La réponse arrive quand l'eau l'apporte — et après la première, tu apprends à aimer l'attente.",
 "de": "Ein Brief braucht so lange, wie das Wasser zwischen euch braucht. Eine Küste am selben Meer antwortet vielleicht bis zum Morgen; die andere Seite der Welt lässt dich Tage warten. Die Antwort kommt, wenn das Wasser sie bringt — und nach dem ersten Mal lernst du, das Warten zu mögen.",
 "pt-BR": "Uma carta demora o que demorar a água entre vocês. Uma praia no mesmo mar pode responder pela manhã; o outro lado do mundo vai fazer você esperar dias. A resposta chega quando a água a traz — e depois da primeira, você aprende a gostar da espera.",
 "ja": "手紙は、あいだにある水の分だけ時間がかかる。同じ海の向こう岸なら朝には返事が来るかもしれないし、地球の裏側なら何日も待たされる。返事は、水が運んできたときに届く。そして最初の一通のあとは、待つことが好きになっている。"},

"The beach is quiet, and it is yours.": {
 "it": "La spiaggia è quieta, ed è tua.",
 "es": "La playa está en calma, y es tuya.",
 "fr": "La plage est calme, et elle est à toi.",
 "de": "Der Strand ist still, und er gehört dir.",
 "pt-BR": "A praia está quieta, e é sua.",
 "ja": "浜辺は静かで、そしてあなたのものだ。"},

"You have the sound of the water and the light of your own hour. On the sand lie the bottles the tide has brought you, and past them a horizon that asks nothing of you at all.": {
 "it": "Hai il rumore dell'acqua e la luce della tua ora. Sulla sabbia ci sono le bottiglie che la marea ti ha portato, e più in là un orizzonte che non ti chiede niente.",
 "es": "Tienes el sonido del agua y la luz de tu propia hora. En la arena están las botellas que te ha traído la marea, y más allá un horizonte que no te pide nada.",
 "fr": "Tu as le bruit de l'eau et la lumière de ta propre heure. Sur le sable, les bouteilles que la marée t'a apportées, et plus loin un horizon qui ne te demande rien.",
 "de": "Du hast das Geräusch des Wassers und das Licht deiner eigenen Stunde. Im Sand liegen die Flaschen, die dir die Flut gebracht hat, und dahinter ein Horizont, der nichts von dir will.",
 "pt-BR": "Você tem o som da água e a luz da sua própria hora. Na areia estão as garrafas que a maré te trouxe, e mais adiante um horizonte que não pede nada de você.",
 "ja": "あるのは水の音と、あなたのいまの時刻の光。砂の上には潮が運んできた瓶があり、その先には何ひとつ求めてこない水平線がある。"},

"You have all the time in the world to choose the words.": {
 "it": "Hai tutto il tempo del mondo per scegliere le parole.",
 "es": "Tienes todo el tiempo del mundo para elegir las palabras.",
 "fr": "Tu as tout le temps du monde pour choisir les mots.",
 "de": "Du hast alle Zeit der Welt, die Worte zu wählen.",
 "pt-BR": "Você tem todo o tempo do mundo para escolher as palavras.",
 "ja": "言葉を選ぶ時間なら、いくらでもある。"},

"A letter that costs something is written better. Each one is a single letter, and once the cork is in, it sails exactly as you wrote it. So you sit with it a while, and you say the true thing instead of the quick one.": {
 "it": "Una lettera che costa qualcosa si scrive meglio. Ognuna è una lettera sola, e quando il tappo è dentro parte esattamente come l'hai scritta. Così ci stai sopra un po', e dici la cosa vera invece di quella veloce.",
 "es": "Una carta que cuesta algo se escribe mejor. Cada una es una sola carta, y en cuanto el corcho está puesto, zarpa tal como la escribiste. Así que te quedas un rato con ella, y dices lo verdadero en lugar de lo rápido.",
 "fr": "Une lettre qui coûte quelque chose s'écrit mieux. Chacune est une seule lettre, et une fois le bouchon enfoncé, elle part exactement comme tu l'as écrite. Alors tu restes un moment avec elle, et tu dis la chose vraie plutôt que la chose rapide.",
 "de": "Ein Brief, der etwas kostet, wird besser geschrieben. Jeder ist ein einzelner Brief, und sobald der Korken sitzt, segelt er genau so, wie du ihn geschrieben hast. Also bleibst du eine Weile dabei und sagst das Wahre statt des Schnellen.",
 "pt-BR": "Uma carta que custa alguma coisa é mais bem escrita. Cada uma é uma carta só, e quando a rolha entra, ela parte exatamente como você a escreveu. Então você fica um tempo com ela, e diz o que é verdadeiro em vez do que é rápido.",
 "ja": "手間のかかる手紙のほうが、うまく書ける。一通は一通きりで、栓をしたら、書いたとおりのまま海へ出ていく。だからしばらく手元に置いて、早い言葉ではなく本当の言葉を書く。"},

"And the waiting turns out to be the good part.": {
 "it": "E l'attesa si scopre essere la parte bella.",
 "es": "Y resulta que la espera es lo mejor.",
 "fr": "Et l'attente se révèle être le meilleur.",
 "de": "Und das Warten stellt sich als das Schönste heraus.",
 "pt-BR": "E a espera acaba sendo a melhor parte.",
 "ja": "そして待つ時間こそが、いちばんいいところだと分かる。"},

"Days pass. You do other things. Then the tide leaves something on your sand that came in its own time, by its own route — a castaway's handwriting, from a coast you have never seen.": {
 "it": "Passano i giorni. Fai altro. Poi la marea ti lascia sulla sabbia una cosa arrivata coi suoi tempi, per la sua strada — la calligrafia di un naufrago, da una costa che non hai mai visto.",
 "es": "Pasan los días. Haces otras cosas. Entonces la marea deja en tu arena algo que llegó a su tiempo y por su propio camino: la letra de un náufrago, desde una costa que nunca has visto.",
 "fr": "Les jours passent. Tu fais autre chose. Puis la marée laisse sur ton sable quelque chose venu à son heure, par sa propre route — l'écriture d'un naufragé, venue d'une côte que tu n'as jamais vue.",
 "de": "Tage vergehen. Du tust anderes. Dann lässt die Flut etwas in deinem Sand zurück, das zu seiner Zeit und auf seinem eigenen Weg gekommen ist — die Handschrift eines Schiffbrüchigen, von einer Küste, die du nie gesehen hast.",
 "pt-BR": "Os dias passam. Você faz outras coisas. Então a maré deixa na sua areia algo que chegou no seu tempo, pelo seu próprio caminho — a letra de um náufrago, de uma costa que você nunca viu.",
 "ja": "日が過ぎる。ほかのことをして暮らす。するとある日、潮が砂に何かを置いていく。自分の時間をかけ、自分の道をたどって来たもの——見たこともない海岸から届いた、ある漂着者の手書きの文字だ。"},

"Here it is morning and the wind comes off the land. I will not tell you my name, but I will tell you that I planted three fig trees behind the house and one of them took. If this bottle lands anywhere at all, write and tell me the weather where you are.": {
 "it": "Qui è mattina e il vento viene da terra. Non ti dirò il mio nome, ma ti dirò che ho piantato tre fichi dietro casa e uno ha attecchito. Se questa bottiglia approda da qualche parte, scrivimi e dimmi che tempo fa da te.",
 "es": "Aquí es de mañana y el viento viene de tierra. No te diré mi nombre, pero sí que planté tres higueras detrás de la casa y una prendió. Si esta botella llega a alguna parte, escríbeme y dime qué tiempo hace donde estás.",
 "fr": "Ici c'est le matin et le vent vient de la terre. Je ne te dirai pas mon nom, mais je te dirai que j'ai planté trois figuiers derrière la maison et que l'un d'eux a pris. Si cette bouteille aborde quelque part, écris-moi le temps qu'il fait chez toi.",
 "de": "Hier ist Morgen und der Wind kommt vom Land. Ich verrate dir meinen Namen nicht, aber ich sage dir, dass ich hinter dem Haus drei Feigenbäume gepflanzt habe und einer angewachsen ist. Wenn diese Flasche irgendwo anlandet, schreib mir, wie das Wetter bei dir ist.",
 "pt-BR": "Aqui é manhã e o vento vem da terra. Não vou dizer meu nome, mas vou dizer que plantei três figueiras atrás de casa e uma pegou. Se esta garrafa chegar a algum lugar, escreva e me conte que tempo faz aí.",
 "ja": "こちらは朝で、風は陸から吹いてくる。名前は明かさないけれど、家の裏にいちじくを三本植えて、そのうち一本が根づいたことは伝えておく。この瓶がどこかに着いたら、そちらの天気を書いて送ってほしい。"},


"Write a letter, seal it in a bottle, and the current carries it to a castaway's beach, six to thirty-six hours away. A slow messaging app coming to iPhone and Android.": {
 "it": "Scrivi una lettera, chiudila in una bottiglia, e la corrente la porta sulla spiaggia di un naufrago, fra sei e trentasei ore. Un'app di messaggi lenti, in arrivo su iPhone e Android.",
 "es": "Escribe una carta, ciérrala en una botella, y la corriente la lleva a la playa de un náufrago, entre seis y treinta y seis horas después. Una app de mensajes lentos que llega pronto a iPhone y Android.",
 "fr": "Écris une lettre, glisse-la dans une bouteille, et le courant la porte sur la plage d'un naufragé, entre six et trente-six heures plus tard. Une messagerie lente, bientôt sur iPhone et Android.",
 "de": "Schreib einen Brief, verschließ ihn in einer Flasche, und die Strömung trägt ihn an den Strand eines Schiffbrüchigen, sechs bis sechsunddreißig Stunden entfernt. Eine App für langsame Nachrichten, bald auf iPhone und Android.",
 "pt-BR": "Escreva uma carta, feche-a numa garrafa, e a correnteza a leva até a praia de um náufrago, entre seis e trinta e seis horas depois. Um app de mensagens lentas, em breve no iPhone e no Android.",
 "ja": "手紙を書いて瓶に封をすれば、潮がそれを漂着者の浜へ運ぶ。届くまで六時間から三十六時間。もうすぐ iPhone と Android に登場する、ゆっくり届くメッセージアプリ。"},

"The sea has no use for hurry. Write to a castaway on a real beach and let the tide take its time.": {
 "it": "Il mare non sa che farsene della fretta. Scrivi a un naufrago su una spiaggia vera e lascia che la marea si prenda il suo tempo.",
 "es": "Al mar no le sirve de nada la prisa. Escribe a un náufrago en una playa de verdad y deja que la marea se tome su tiempo.",
 "fr": "La mer n'a que faire de la hâte. Écris à un naufragé sur une vraie plage et laisse la marée prendre son temps.",
 "de": "Das Meer weiß mit Eile nichts anzufangen. Schreib einem Schiffbrüchigen an einem wirklichen Strand und lass der Flut ihre Zeit.",
 "pt-BR": "O mar não tem uso para a pressa. Escreva para um náufrago numa praia de verdade e deixe a maré levar o tempo dela.",
 "ja": "海に急ぎは要らない。実在する浜辺にいる漂着者へ手紙を書き、あとは潮の歩みにまかせる。"},

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

"A bottle washed ashore, in the app: sealed with wax, from Glory, a Spirit of the Sea, washed in from Luskentyre.": {
 "it": "Una bottiglia approdata, nell'app: sigillata con la ceralacca, da Glory, uno Spirito del Mare, arrivata da Luskentyre.",
 "es": "Una botella llegada a la orilla, en la app: sellada con lacre, de Glory, un Espíritu del Mar, llegada desde Luskentyre.",
 "fr": "Une bouteille échouée, dans l'application : scellée à la cire, de Glory, un Esprit de la Mer, venue de Luskentyre.",
 "de": "Eine angespülte Flasche in der App: mit Wachs versiegelt, von Glory, einem Geist des Meeres, angetrieben von Luskentyre.",
 "pt-BR": "Uma garrafa que chegou à praia, no app: selada com lacre, de Glory, um Espírito do Mar, vinda de Luskentyre.",
 "ja": "アプリの中の、流れ着いた瓶。封蝋で閉じられ、海の精グローリーからラスケンタイアを経て届いたもの。"},

"A correspondence in the journal: a letter from Glory, a Spirit of the Sea, the reply underneath, and a note that the reply is already sailing.": {
 "it": "Un carteggio nel diario: una lettera di Glory, uno Spirito del Mare, sotto la risposta, e una riga che dice che la risposta è già in viaggio.",
 "es": "Una correspondencia en el diario: una carta de Glory, un Espíritu del Mar, debajo la respuesta, y una nota que dice que la respuesta ya navega.",
 "fr": "Une correspondance dans le journal : une lettre de Glory, un Esprit de la Mer, la réponse en dessous, et une note disant que la réponse est déjà en mer.",
 "de": "Ein Briefwechsel im Tagebuch: ein Brief von Glory, einem Geist des Meeres, darunter die Antwort und ein Hinweis, dass die Antwort schon unterwegs ist.",
 "pt-BR": "Uma correspondência no diário: uma carta de Glory, um Espírito do Mar, a resposta embaixo, e uma nota dizendo que a resposta já está navegando.",
 "ja": "日誌の中の文通。海の精グローリーからの手紙、その下に返事、そして返事がもう海を渡っているという一文。"},

"The nautical chart: a route from Vai, on Crete, west across the Mediterranean and north up the Atlantic to Luskentyre, in Scotland, with the bottle just setting out.": {
 "it": "La carta nautica: una rotta da Vai, a Creta, verso ovest per il Mediterraneo e poi a nord su per l'Atlantico fino a Luskentyre, in Scozia, con la bottiglia appena partita.",
 "es": "La carta náutica: una ruta desde Vai, en Creta, hacia el oeste por el Mediterráneo y luego al norte por el Atlántico hasta Luskentyre, en Escocia, con la botella recién salida.",
 "fr": "La carte marine : une route depuis Vai, en Crète, vers l'ouest à travers la Méditerranée puis vers le nord le long de l'Atlantique jusqu'à Luskentyre, en Écosse, avec la bouteille tout juste partie.",
 "de": "Die Seekarte: eine Route von Vai auf Kreta nach Westen durchs Mittelmeer und dann nach Norden den Atlantik hinauf bis Luskentyre in Schottland, die Flasche gerade erst aufgebrochen.",
 "pt-BR": "A carta náutica: uma rota de Vai, em Creta, para oeste pelo Mediterrâneo e depois para o norte pelo Atlântico até Luskentyre, na Escócia, com a garrafa acabando de partir.",
 "ja": "海図。クレタ島のヴァイから西へ地中海を抜け、大西洋を北上してスコットランドのラスケンタイアへ向かう航路。瓶は出発したばかり。"},

"Dawn at Diamond Beach, as the app draws it: a lilac sky, a pale sun and an iceberg on the water.": {
 "it": "L'alba a Diamond Beach come la disegna l'app: un cielo lilla, un sole pallido e un iceberg sull'acqua.",
 "es": "El alba en Diamond Beach tal como la dibuja la app: un cielo lila, un sol pálido y un iceberg en el agua.",
 "fr": "L'aube à Diamond Beach telle que l'application la dessine : un ciel lilas, un soleil pâle et un iceberg sur l'eau.",
 "de": "Morgengrauen am Diamond Beach, wie die App es zeichnet: ein fliederfarbener Himmel, eine blasse Sonne und ein Eisberg auf dem Wasser.",
 "pt-BR": "O amanhecer em Diamond Beach como o app o desenha: um céu lilás, um sol pálido e um iceberg na água.",
 "ja": "アプリが描くダイヤモンド・ビーチの夜明け。薄紫の空、淡い太陽、水に浮かぶ氷山。"},

"Midday at Matira Beach, as the app draws it: blue sky, turquoise water and a palm on the white sand.": {
 "it": "Mezzogiorno a Matira Beach come lo disegna l'app: cielo azzurro, acqua turchese e una palma sulla sabbia bianca.",
 "es": "El mediodía en Matira Beach tal como lo dibuja la app: cielo azul, agua turquesa y una palmera en la arena blanca.",
 "fr": "Midi à Matira Beach tel que l'application le dessine : un ciel bleu, une eau turquoise et un palmier sur le sable blanc.",
 "de": "Mittag am Matira Beach, wie die App ihn zeichnet: blauer Himmel, türkises Wasser und eine Palme auf dem weißen Sand.",
 "pt-BR": "O meio-dia em Matira Beach como o app o desenha: céu azul, água turquesa e uma palmeira na areia branca.",
 "ja": "アプリが描くマティラ・ビーチの正午。青い空、ターコイズの海、白い砂の上のヤシ。"},

"Dusk at Reynisfjara, as the app draws it: a red sky, the sea stacks and black volcanic sand.": {
 "it": "Il tramonto a Reynisfjara come lo disegna l'app: un cielo rosso, i faraglioni e la sabbia nera vulcanica.",
 "es": "El atardecer en Reynisfjara tal como lo dibuja la app: un cielo rojo, los farallones y la arena negra volcánica.",
 "fr": "Le crépuscule à Reynisfjara tel que l'application le dessine : un ciel rouge, les aiguilles de roche et le sable noir volcanique.",
 "de": "Dämmerung in Reynisfjara, wie die App sie zeichnet: ein roter Himmel, die Felsnadeln und schwarzer Vulkansand.",
 "pt-BR": "O entardecer em Reynisfjara como o app o desenha: um céu vermelho, os rochedos no mar e a areia preta vulcânica.",
 "ja": "アプリが描くレイニスフィヤラの夕暮れ。赤い空、海に立つ岩柱、黒い火山の砂。"},

"Night at Unstad, as the app draws it: the aurora over a dark arctic sea.": {
 "it": "La notte a Unstad come la disegna l'app: l'aurora sopra un mare artico scuro.",
 "es": "La noche en Unstad tal como la dibuja la app: la aurora sobre un mar ártico oscuro.",
 "fr": "La nuit à Unstad telle que l'application la dessine : l'aurore au-dessus d'une mer arctique sombre.",
 "de": "Nacht in Unstad, wie die App sie zeichnet: das Polarlicht über einem dunklen arktischen Meer.",
 "pt-BR": "A noite em Unstad como o app a desenha: a aurora sobre um mar ártico escuro.",
 "ja": "アプリが描くウンスタッドの夜。暗い北極の海の上を渡るオーロラ。"},

"Four of the 250: dawn at Diamond Beach in Iceland, midday on Bora Bora, dusk on the black sand of Reynisfjara, and an arctic night in the Lofoten with the aurora overhead.": {
 "it": "Quattro delle 250: l'alba a Diamond Beach in Islanda, mezzogiorno a Bora Bora, il tramonto sulla sabbia nera di Reynisfjara, e una notte artica alle Lofoten con l'aurora sopra la testa.",
 "es": "Cuatro de las 250: el alba en Diamond Beach, en Islandia, el mediodía en Bora Bora, el atardecer en la arena negra de Reynisfjara y una noche ártica en las Lofoten con la aurora por encima.",
 "fr": "Quatre des 250 : l'aube à Diamond Beach en Islande, midi à Bora Bora, le crépuscule sur le sable noir de Reynisfjara, et une nuit arctique aux Lofoten avec l'aurore au-dessus.",
 "de": "Vier von 250: Morgengrauen am Diamond Beach in Island, Mittag auf Bora Bora, Dämmerung auf dem schwarzen Sand von Reynisfjara und eine arktische Nacht auf den Lofoten mit dem Polarlicht darüber.",
 "pt-BR": "Quatro das 250: o amanhecer em Diamond Beach, na Islândia, o meio-dia em Bora Bora, o entardecer na areia preta de Reynisfjara e uma noite ártica nas Lofoten com a aurora lá em cima.",
 "ja": "250 のうちの四つ。アイスランドのダイヤモンド・ビーチの夜明け、ボラボラ島の正午、レイニスフィヤラの黒い砂の夕暮れ、そして頭上をオーロラが渡るロフォーテンの夜。"},

"One of the 250 shores the storm knows. Yours could be any of them.": {
 "it": "Una delle 250 rive che la tempesta conosce. La tua potrebbe essere una qualsiasi.",
 "es": "Una de las 250 orillas que la tormenta conoce. La tuya podría ser cualquiera.",
 "fr": "Un des 250 rivages que la tempête connaît. Le tien pourrait être n'importe lequel.",
 "de": "Eines von 250 Ufern, die der Sturm kennt. Deines könnte jedes davon sein.",
 "pt-BR": "Uma das 250 praias que a tempestade conhece. A sua pode ser qualquer uma.",
 "ja": "嵐が知っている250の浜辺のひとつ。あなたの浜は、そのどれかもしれない。"},

"Vík, Iceland": {
 "it": "Vík, Islanda", "es": "Vík, Islandia", "fr": "Vík, Islande",
 "de": "Vík, Island", "pt-BR": "Vík, Islândia", "ja": "ヴィーク、アイスランド"},

"La Digue, Seychelles": {
 "it": "La Digue, Seychelles", "es": "La Digue, Seychelles", "fr": "La Digue, Seychelles",
 "de": "La Digue, Seychellen", "pt-BR": "La Digue, Seicheles", "ja": "ラ・ディーグ、セーシェル"},

"Lofoten, Norway": {
 "it": "Lofoten, Norvegia", "es": "Lofoten, Noruega", "fr": "Lofoten, Norvège",
 "de": "Lofoten, Norwegen", "pt-BR": "Lofoten, Noruega", "ja": "ロフォーテン、ノルウェー"},

"Sintra, Portugal": {
 "it": "Sintra, Portogallo", "es": "Sintra, Portugal", "fr": "Sintra, Portugal",
 "de": "Sintra, Portugal", "pt-BR": "Sintra, Portugal", "ja": "シントラ、ポルトガル"},

"One last thing": {
 "it": "Un'ultima cosa", "es": "Una última cosa", "fr": "Une dernière chose",
 "de": "Eine letzte Sache", "pt-BR": "Uma última coisa", "ja": "最後にひとつ"},

"The tide is already on its way.": {
 "it": "La marea è già in viaggio.", "es": "La marea ya está en camino.",
 "fr": "La marée est déjà en route.", "de": "Die Flut ist schon unterwegs.",
 "pt-BR": "A maré já está a caminho.", "ja": "潮はもう動きはじめている。"},

"On a shore you have never seen, a castaway is pushing the cork into a bottle right now. The sea will decide whose sand it touches next. Maybe yours.": {
 "it": "Su una riva che non hai mai visto, un naufrago sta spingendo il tappo in una bottiglia proprio adesso. Il mare deciderà su quale sabbia farla approdare. Magari proprio sulla tua.",
 "es": "En una orilla que nunca has visto, un náufrago está apretando el corcho de una botella ahora mismo. El mar decidirá qué arena toca después. Quizá justo la tuya.",
 "fr": "Sur un rivage que tu n'as jamais vu, un naufragé enfonce le bouchon d'une bouteille en ce moment même. La mer décidera quel sable elle touchera ensuite. Peut-être le tien.",
 "de": "An einem Ufer, das du nie gesehen hast, drückt gerade ein Schiffbrüchiger den Korken in eine Flasche. Das Meer entscheidet, wessen Sand sie als Nächstes berührt. Vielleicht deinen.",
 "pt-BR": "Numa praia que você nunca viu, um náufrago está apertando a rolha de uma garrafa agora mesmo. O mar vai decidir em qual areia ela chega. Quem sabe na sua.",
 "ja": "見たこともない岸辺で、いままさにひとりの漂着者が瓶にコルクを押し込んでいる。次にどの砂に届くかは海が決める。もしかしたら、あなたの砂に。"},

"Who you are here": {
 "it": "Chi sei, qui", "es": "Quién eres aquí", "fr": "Qui tu es ici",
 "de": "Wer du hier bist", "pt-BR": "Quem você é aqui", "ja": "ここでのあなた"},

"On this sea, you are": {
 "it": "Su questo mare sei",
 "es": "En este mar eres",
 "fr": "Sur cette mer, tu es",
 "de": "Auf diesem Meer bist du",
 "pt-BR": "Neste mar, você é",
 "ja": "この海で、あなたは"},

"a seal in wax.": {
 "it": "un sigillo di ceralacca.",
 "es": "un sello de lacre.",
 "fr": "un sceau de cire.",
 "de": "ein Siegel in Wachs.",
 "pt-BR": "um selo de lacre.",
 "ja": "蝋に押された封印だ。"},

"Every castaway presses an emblem into the wax. On this sea, a seal, a shore and their handwriting are how you know a person, and how they know you.": {
 "it": "Ogni naufrago imprime un emblema nella cera. Su questo mare un sigillo, una riva e una calligrafia sono il modo in cui conosci una persona, e lei conosce te.",
 "es": "Cada náufrago imprime un emblema en el lacre. En este mar, un sello, una orilla y una letra son lo que te deja conocer a una persona, y a ella conocerte a ti.",
 "fr": "Chaque naufragé imprime un emblème dans la cire. Sur cette mer, un sceau, un rivage et une écriture sont ce par quoi tu connais quelqu'un, et ce par quoi on te connaît.",
 "de": "Jeder Schiffbrüchige drückt ein Emblem ins Wachs. Auf diesem Meer kennst du einen Menschen an einem Siegel, einem Ufer und seiner Handschrift, und so kennt er dich.",
 "pt-BR": "Cada náufrago imprime um emblema no lacre. Neste mar, um selo, uma praia e uma letra são o jeito de conhecer uma pessoa, e o jeito de ela conhecer você.",
 "ja": "漂着者はみな、蝋に紋章を押す。この海では、封印と、ひとつの岸と、手書きの文字で人を知り、相手もそうしてあなたを知る。"},

"They may be writing to you in a language you have never read. One tap turns it into yours; another puts their own words back, exactly as they wrote them.": {
 "it": "Può darsi che ti scrivano in una lingua che non hai mai letto. Un tocco la porta nella tua; un altro rimette le loro parole com'erano, esattamente come le hanno scritte.",
 "es": "Puede que te escriban en una lengua que nunca has leído. Un toque la convierte en la tuya; otro devuelve sus palabras tal como las escribieron.",
 "fr": "Ils t'écrivent peut-être dans une langue que tu n'as jamais lue. Une touche la met dans la tienne ; une autre remet leurs mots exactement comme ils les ont écrits.",
 "de": "Vielleicht schreibt dir jemand in einer Sprache, die du nie gelesen hast. Ein Tippen macht sie zu deiner; ein weiteres stellt die fremden Worte wieder her, genau so, wie sie geschrieben wurden.",
 "pt-BR": "Pode ser que escrevam para você numa língua que você nunca leu. Um toque a transforma na sua; outro devolve as palavras deles exatamente como foram escritas.",
 "ja": "読んだことのない言語で書かれてくるかもしれない。ひと押しで自分の言葉になり、もうひと押しで、書かれたとおりの言葉に戻る。"},

"What you keep": {
 "it": "Quello che conservi", "es": "Lo que conservas", "fr": "Ce que tu gardes",
 "de": "Was bleibt", "pt-BR": "O que você guarda", "ja": "手元に残るもの"},

"A correspondence, kept on paper.": {
 "it": "Un carteggio, tenuto sulla carta.",
 "es": "Una correspondencia, guardada en papel.",
 "fr": "Une correspondance, gardée sur papier.",
 "de": "Ein Briefwechsel, auf Papier bewahrt.",
 "pt-BR": "Uma correspondência, guardada no papel.",
 "ja": "紙に残る、文通。"},

"Letters stay here, in a journal made of paper, in the order the sea delivered them — yours on one side, theirs on the other, each with the day it came ashore written underneath.": {
 "it": "Qui le lettere restano, in un diario di carta, nell'ordine in cui il mare le ha consegnate — le tue da una parte, le loro dall'altra, ognuna con sotto il giorno in cui è approdata.",
 "es": "Aquí las cartas se quedan, en un diario de papel, en el orden en que el mar las entregó: las tuyas de un lado, las suyas del otro, cada una con el día en que llegó a la orilla escrito debajo.",
 "fr": "Ici, les lettres restent, dans un journal de papier, dans l'ordre où la mer les a remises — les tiennes d'un côté, les leurs de l'autre, chacune avec, en dessous, le jour où elle a abordé.",
 "de": "Hier bleiben Briefe, in einem Tagebuch aus Papier, in der Reihenfolge, in der das Meer sie brachte — deine auf der einen Seite, ihre auf der anderen, jeder mit dem Tag darunter, an dem er anlandete.",
 "pt-BR": "Aqui as cartas ficam, num diário de papel, na ordem em que o mar as entregou — as suas de um lado, as dele do outro, cada uma com o dia em que chegou escrito embaixo.",
 "ja": "ここでは手紙が残る。紙の日誌に、海が届けた順のまま。自分のものは片側に、相手のものは反対側に、それぞれの下に岸へ着いた日が書かれている。"},

"You may give a correspondent a private name, only for your own pages:": {
 "it": "A chi ti scrive puoi dare un nome privato, solo per le tue pagine:",
 "es": "A quien te escribe puedes darle un nombre privado, solo para tus páginas:",
 "fr": "Tu peux donner à un correspondant un nom privé, rien que pour tes pages :",
 "de": "Einem Briefpartner darfst du einen eigenen Namen geben, nur für deine Seiten:",
 "pt-BR": "Você pode dar a quem escreve para você um nome particular, só para as suas páginas:",
 "ja": "文通の相手には、自分の日誌のなかだけで通じる名前をつけられる。"},

"the lighthouse keeper": {
 "it": "il guardiano del faro", "es": "el farero", "fr": "le gardien du phare",
 "de": "der Leuchtturmwärter", "pt-BR": "o faroleiro", "ja": "灯台守"},

"the girl with the boat": {
 "it": "la ragazza con la barca", "es": "la chica de la barca",
 "fr": "la fille au bateau", "de": "das Mädchen mit dem Boot",
 "pt-BR": "a moça do barco", "ja": "舟をもつ娘"},

". Only you will ever see it. And when a bottle of theirs is still out on the water, the journal simply says so, and asks you to wait.": {
 "it": ". Lo vedrai solo tu. E quando una loro bottiglia è ancora in mare, il diario lo dice e basta, e ti chiede di aspettare.",
 "es": ". Solo tú lo verás. Y cuando una botella suya sigue en el agua, el diario lo dice sin más, y te pide que esperes.",
 "fr": ". Toi seul le verras. Et lorsqu'une de leurs bouteilles est encore sur l'eau, le journal le dit simplement, et te demande d'attendre.",
 "de": ". Nur du wirst ihn je sehen. Und wenn eine Flasche von ihnen noch auf dem Wasser ist, sagt das Tagebuch es einfach und bittet dich zu warten.",
 "pt-BR": ". Só você vai ver esse nome. E quando uma garrafa deles ainda está na água, o diário simplesmente diz isso, e pede que você espere.",
 "ja": "。その名前を見るのは、あなただけだ。相手の瓶がまだ海の上にあるときは、日誌がそう告げて、待つように言うだけだ。"},

"The tide keeps its own time — and while you are here, so do you.": {
 "it": "La marea ha un suo tempo — e finché sei qui, ce l'hai anche tu.",
 "es": "La marea lleva su propio tiempo, y mientras estés aquí, tú también.",
 "fr": "La marée a son propre temps — et tant que tu es ici, toi aussi.",
 "de": "Die Gezeiten haben ihre eigene Zeit — und solange du hier bist, hast du sie auch.",
 "pt-BR": "A maré tem o tempo dela — e enquanto você estiver aqui, você também tem.",
 "ja": "潮には潮の時間がある。そしてここにいるあいだは、あなたにも。"},

"Where you wake up": {
 "it": "Dove ti svegli", "es": "Dónde te despiertas", "fr": "Où tu te réveilles",
 "de": "Wo du aufwachst", "pt-BR": "Onde você acorda", "ja": "目を覚ます場所"},

"The storm leaves you": {
 "it": "La tempesta ti lascia",
 "es": "La tormenta te deja",
 "fr": "La tempête te laisse",
 "de": "Der Sturm setzt dich",
 "pt-BR": "A tempestade deixa você",
 "ja": "嵐があなたを置いていくのは、"},

"on a real beach.": {
 "it": "su una spiaggia vera.",
 "es": "en una playa de verdad.",
 "fr": "sur une vraie plage.",
 "de": "an einem wirklichen Strand ab.",
 "pt-BR": "numa praia de verdade.",
 "ja": "本物の浜辺。"},
"Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Real stretches of coast at their real coordinates, and yours is drawn by lot. From that first morning on, it is home. The light on it is the light of your own hour: open it at midnight and your beach is dark, with the stars out over the water. Every wave is drawn by the app, line by line.": {
 "it": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Tratti di costa veri alle loro coordinate vere, e la tua te la dà la sorte. Da quella prima mattina è casa. La luce che ci sta sopra è quella della tua ora: aprila a mezzanotte e la tua spiaggia è buia, con le stelle sull'acqua. Ogni onda la disegna l'app, linea per linea.",
 "es": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Tramos de costa reales en sus coordenadas reales, y la tuya te toca en suerte. Desde esa primera mañana es tu casa. La luz que la baña es la de tu propia hora: ábrela a medianoche y tu playa está a oscuras, con las estrellas sobre el agua. Cada ola la dibuja la app, línea a línea.",
 "fr": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. De vraies portions de côte à leurs vraies coordonnées, et la tienne t'échoit au hasard. Dès ce premier matin, c'est chez toi. La lumière qui la baigne est celle de ta propre heure : ouvre à minuit et ta plage est sombre, les étoiles au-dessus de l'eau. Chaque vague est dessinée par l'application, trait par trait.",
 "de": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Echte Küstenstücke an ihren echten Koordinaten, und deines fällt dir durch Los zu. Von jenem ersten Morgen an ist es dein Zuhause. Das Licht darauf ist das deiner eigenen Stunde: öffne sie um Mitternacht, und dein Strand ist dunkel, die Sterne über dem Wasser. Jede Welle zeichnet die App, Strich für Strich.",
 "pt-BR": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Trechos de costa reais nas coordenadas reais, e a sua vem por sorteio. Desde aquela primeira manhã, é casa. A luz sobre ela é a da sua própria hora: abra à meia-noite e a sua praia está escura, com as estrelas sobre a água. Cada onda é desenhada pelo app, linha por linha.",
 "ja": "カーラ・ゴロリッツェ。レイニスフィヤラ。アンス・スルス・ダルジャン。実在する海岸を、実在する座標のままに。そして自分の浜は、くじで決まる。最初の朝から、そこが家になる。射す光はあなたのいまの時刻の光だ。真夜中に開けば浜は暗く、水の上に星が出ている。波の一本一本を、アプリが線で描いている。"},


"The crossing": {
 "it": "La traversata", "es": "La travesía", "fr": "La traversée",
 "de": "Die Überfahrt", "pt-BR": "A travessia", "ja": "航路"},

"You can watch it go.": {
 "it": "Puoi guardarla andare.", "es": "Puedes verla marchar.",
 "fr": "Tu peux la regarder s'en aller.", "de": "Du kannst ihr nachsehen.",
 "pt-BR": "Você pode vê-la partir.", "ja": "旅立っていくのを、見ていられる。"},

"your shore": {
 "it": "la tua riva", "es": "tu orilla", "fr": "ton rivage",
 "de": "dein Ufer", "pt-BR": "sua praia", "ja": "あなたの岸"},

"still at sea": {
 "it": "ancora in mare", "es": "aún en el mar", "fr": "encore en mer",
 "de": "noch auf See", "pt-BR": "ainda no mar", "ja": "まだ海の上"},

"A bottle you have thrown leaves a line on the chart, and the line grows while you sleep. The solid part is the distance already sailed; the dashes ahead appear only once you know who is waiting at the far end.": {
 "it": "Una bottiglia che hai lanciato lascia una linea sulla carta, e la linea cresce mentre dormi. Il tratto pieno è la distanza già navigata; il tratteggio davanti compare solo quando sai chi aspetta dall'altra parte.",
 "es": "Una botella que has lanzado deja una línea en la carta, y la línea crece mientras duermes. El trazo continuo es la distancia ya navegada; los guiones de delante solo aparecen cuando sabes quién espera al otro extremo.",
 "fr": "Une bouteille que tu as lancée laisse une ligne sur la carte, et la ligne grandit pendant ton sommeil. Le trait plein est la distance déjà parcourue ; les pointillés devant n'apparaissent qu'une fois que tu sais qui attend à l'autre bout.",
 "de": "Eine geworfene Flasche hinterlässt eine Linie auf der Karte, und die Linie wächst, während du schläfst. Der durchgezogene Teil ist die bereits gesegelte Strecke; die Striche voraus erscheinen erst, wenn du weißt, wer am anderen Ende wartet.",
 "pt-BR": "Uma garrafa que você lançou deixa uma linha na carta, e a linha cresce enquanto você dorme. O traço cheio é a distância já navegada; os tracejados à frente só aparecem quando você sabe quem espera do outro lado.",
 "ja": "投げた瓶は海図に一本の線を残し、その線は眠っているあいだも伸びていく。実線はすでに渡った距離。その先の破線は、向こう岸で誰が待っているかを知ってからでないと現れない。"},

"The islands of castaways whose letters you have read stay marked there for good — a private map of everyone the sea has introduced you to.": {
 "it": "Le isole dei naufraghi di cui hai letto le lettere restano segnate per sempre — una mappa privata di tutti quelli che il mare ti ha presentato.",
 "es": "Las islas de los náufragos cuyas cartas has leído quedan marcadas para siempre: un mapa privado de todos los que el mar te ha presentado.",
 "fr": "Les îles des naufragés dont tu as lu les lettres restent marquées pour de bon — une carte privée de tous ceux que la mer t'a présentés.",
 "de": "Die Inseln der Schiffbrüchigen, deren Briefe du gelesen hast, bleiben für immer eingezeichnet — eine private Karte all jener, die das Meer dir vorgestellt hat.",
 "pt-BR": "As ilhas dos náufragos cujas cartas você leu ficam marcadas para sempre — um mapa particular de todos que o mar apresentou a você.",
 "ja": "手紙を読んだ相手の島は、そのまま海図に残りつづける。海が引き合わせてくれた人たちだけの、自分だけの地図になる。"},

"The chart is the app's own: coastlines from Natural Earth, public domain, carried inside the app and drawn on your phone.": {
 "it": "La carta è tutta dell'app: coste da Natural Earth, di pubblico dominio, portate dentro l'app e disegnate sul tuo telefono.",
 "es": "La carta es de la propia app: costas de Natural Earth, de dominio público, llevadas dentro de la app y dibujadas en tu teléfono.",
 "fr": "La carte appartient à l'application : côtes issues de Natural Earth, domaine public, embarquées avec elle et dessinées sur ton téléphone.",
 "de": "Die Karte gehört der App selbst: Küstenlinien von Natural Earth, gemeinfrei, in der App mitgeführt und auf deinem Telefon gezeichnet.",
 "pt-BR": "A carta é do próprio app: costas do Natural Earth, de domínio público, carregadas dentro do app e desenhadas no seu celular.",
 "ja": "海図はアプリ自身のものだ。海岸線はパブリックドメインの Natural Earth をアプリの中に持ち、あなたの電話の上で描かれる。"},

"·": {
 "it": "·", "es": "·", "fr": "·", "de": "·", "pt-BR": "·", "ja": "·"},

"Privacy": {
 "it": "Privacy",
 "es": "Privacidad",
 "fr": "Confidentialité",
 "de": "Datenschutz",
 "pt-BR": "Privacidade",
 "ja": "プライバシー"},

"Press — Bottlegram": {
 "it": "Stampa — Bottlegram",
 "es": "Prensa — Bottlegram",
 "fr": "Presse — Bottlegram",
 "de": "Presse — Bottlegram",
 "pt-BR": "Imprensa — Bottlegram",
 "ja": "プレス — Bottlegram"},

"Bottlegram — press kit": {
 "it": "Bottlegram — press kit",
 "es": "Bottlegram — press kit",
 "fr": "Bottlegram — dossier de presse",
 "de": "Bottlegram — Pressemappe",
 "pt-BR": "Bottlegram — kit de imprensa",
 "ja": "Bottlegram — プレスキット"},

"Pages": {
 "it": "Pagine",
 "es": "Páginas",
 "fr": "Pages",
 "de": "Seiten",
 "pt-BR": "Páginas",
 "ja": "ページ"},

"Press kit": {
 "it": "Press kit",
 "es": "Press kit",
 "fr": "Dossier de presse",
 "de": "Pressemappe",
 "pt-BR": "Kit de imprensa",
 "ja": "プレスキット"},

"Two iPhone screens against a blurred sunset. On the left, the beach of Luskentyre with a bottle washed up on the sand, at 20:41 on a Thursday. On the right, the answer that came back, at 13:41 on the Friday. Between them, empty space and the words «seventeen hours».": {
 "it": "Due schermi di iPhone su un tramonto sfocato. A sinistra la spiaggia di Luskentyre con una bottiglia approdata sulla sabbia, alle 20:41 di giovedì. A destra la risposta che è tornata, alle 13:41 di venerdì. In mezzo, spazio vuoto e le parole «seventeen hours».",
 "es": "Dos pantallas de iPhone sobre un atardecer desenfocado. A la izquierda, la playa de Luskentyre con una botella varada en la arena, a las 20:41 de un jueves. A la derecha, la respuesta que volvió, a las 13:41 del viernes. Entre ambas, espacio vacío y las palabras «seventeen hours».",
 "fr": "Deux écrans d'iPhone sur un coucher de soleil flou. À gauche, la plage de Luskentyre avec une bouteille échouée sur le sable, à 20h41 un jeudi. À droite, la réponse qui est revenue, à 13h41 le vendredi. Entre les deux, du vide et les mots « seventeen hours ».",
 "de": "Zwei iPhone-Bildschirme vor einem unscharfen Sonnenuntergang. Links der Strand von Luskentyre mit einer angespülten Flasche im Sand, donnerstags um 20:41 Uhr. Rechts die Antwort, die zurückkam, freitags um 13:41 Uhr. Dazwischen leerer Raum und die Worte «seventeen hours».",
 "pt-BR": "Duas telas de iPhone sobre um pôr do sol desfocado. À esquerda, a praia de Luskentyre com uma garrafa encalhada na areia, às 20h41 de uma quinta-feira. À direita, a resposta que voltou, às 13h41 da sexta. Entre elas, espaço vazio e as palavras «seventeen hours».",
 "ja": "ぼかした夕焼けを背にした二つの iPhone の画面。左は木曜日の20時41分、砂に打ち上げられた瓶のあるラスケンタイアの浜。右は金曜日の13時41分、返ってきた返事。その間には余白と「seventeen hours」の文字。"},

"Luskentyre at dusk, and the answer that came back the next day. The times are the ones the phone recorded.": {
 "it": "Luskentyre al tramonto, e la risposta tornata il giorno dopo. Gli orari sono quelli che ha segnato il telefono.",
 "es": "Luskentyre al atardecer, y la respuesta que volvió al día siguiente. Las horas son las que registró el teléfono.",
 "fr": "Luskentyre au crépuscule, et la réponse revenue le lendemain. Les heures sont celles qu'a enregistrées le téléphone.",
 "de": "Luskentyre in der Dämmerung und die Antwort, die am nächsten Tag zurückkam. Die Uhrzeiten sind die, die das Telefon festgehalten hat.",
 "pt-BR": "Luskentyre ao entardecer, e a resposta que voltou no dia seguinte. Os horários são os que o telefone registrou.",
 "ja": "夕暮れのラスケンタイアと、翌日に返ってきた返事。時刻は端末が記録したそのままです。"},

"In one paragraph": {
 "it": "In un paragrafo",
 "es": "En un párrafo",
 "fr": "En un paragraphe",
 "de": "In einem Absatz",
 "pt-BR": "Em um parágrafo",
 "ja": "一段落で"},

"Bottlegram is a slow messaging app for people who will never meet. You write a letter, seal it in a bottle and give it to the current. Six to thirty-six hours later it washes up on one of 250 illustrated beaches, each at its real coordinates, and another castaway finds it. If they write back, you take turns, one letter each. Bottlegram is free and coming soon to iPhone and Android.": {
 "it": "Bottlegram è un'app di messaggi lenti fra persone che non si incontreranno mai. Scrivi una lettera, la chiudi in una bottiglia e la affidi alla corrente. Da sei a trentasei ore dopo approda su una di 250 spiagge illustrate, ognuna alle sue coordinate vere, e un altro naufrago la trova. Se risponde, vi date il turno, una lettera a testa. Bottlegram è gratis e arriva presto su iPhone e Android.",
 "es": "Bottlegram es una app de mensajes lentos entre personas que nunca se conocerán. Escribes una carta, la cierras en una botella y la entregas a la corriente. Entre seis y treinta y seis horas después llega a una de 250 playas ilustradas, cada una en sus coordenadas reales, y otro náufrago la encuentra. Si contesta, os turnáis, una carta cada uno. Bottlegram es gratis y llega pronto a iPhone y Android.",
 "fr": "Bottlegram est une messagerie lente entre des personnes qui ne se rencontreront jamais. Vous écrivez une lettre, vous la scellez dans une bouteille et vous la confiez au courant. Six à trente-six heures plus tard, elle échoue sur l'une de 250 plages illustrées, chacune à ses vraies coordonnées, et un autre naufragé la trouve. S'il répond, vous écrivez chacun à votre tour, une lettre chacun. Bottlegram est gratuit et arrive bientôt sur iPhone et Android.",
 "de": "Bottlegram ist eine App für langsame Nachrichten zwischen Menschen, die sich nie begegnen werden. Sie schreiben einen Brief, verschließen ihn in einer Flasche und übergeben ihn der Strömung. Sechs bis sechsunddreißig Stunden später wird er an einen von 250 illustrierten Stränden gespült, jeder an seinen echten Koordinaten, und ein anderer Schiffbrüchiger findet ihn. Antwortet er, schreiben Sie abwechselnd, ein Brief nach dem anderen. Bottlegram ist kostenlos und kommt bald auf iPhone und Android.",
 "pt-BR": "Bottlegram é um app de mensagens lentas entre pessoas que nunca vão se conhecer. Você escreve uma carta, fecha numa garrafa e entrega à correnteza. De seis a trinta e seis horas depois ela chega a uma de 250 praias ilustradas, cada uma nas suas coordenadas reais, e outro náufrago a encontra. Se ele responder, vocês se revezam, uma carta de cada vez. Bottlegram é grátis e chega em breve ao iPhone e ao Android.",
 "ja": "Bottlegram は、一生会うことのない人どうしの、ゆっくり届くメッセージアプリです。手紙を書き、瓶に封じ、潮に託します。六時間から三十六時間後、それは実在の座標にある 250 の描かれた浜のどれかに流れ着き、別の漂着者が見つけます。返事が来れば、一通ずつ交互に書いていきます。Bottlegram は無料で、まもなく iPhone と Android に登場します。"},

"The story": {
 "it": "La storia",
 "es": "La historia",
 "fr": "L'histoire",
 "de": "Die Geschichte",
 "pt-BR": "A história",
 "ja": "はじまり"},

"I photograph the sea. Seascapes mostly, and long exposures above all. A long exposure is a photograph you make by waiting: you hold the shutter open and stand still, and the water draws itself onto the frame while, to anyone watching, nothing at all is happening.": {
 "it": "Fotografo il mare. Paesaggi soprattutto, e lunghe esposizioni più di ogni altra cosa. Una lunga esposizione è una fotografia che si fa aspettando: tieni l'otturatore aperto e stai fermo, e l'acqua si disegna da sola sul fotogramma mentre, per chi guarda, non sta succedendo niente.",
 "es": "Fotografío el mar. Paisajes marinos sobre todo, y largas exposiciones más que nada. Una larga exposición es una fotografía que se hace esperando: mantienes el obturador abierto y te quedas quieto, y el agua se dibuja sola sobre el fotograma mientras, para quien mira, no está pasando nada.",
 "fr": "Je photographie la mer. Des paysages marins surtout, et des poses longues plus que tout. Une pose longue est une photographie que l'on fait en attendant : on garde l'obturateur ouvert et on ne bouge plus, et l'eau se dessine toute seule sur l'image alors que, pour qui regarde, il ne se passe rien du tout.",
 "de": "Ich fotografiere das Meer. Vor allem Seelandschaften, und Langzeitbelichtungen mehr als alles andere. Eine Langzeitbelichtung ist eine Fotografie, die man durch Warten macht: Man hält den Verschluss offen und steht still, und das Wasser zeichnet sich von selbst auf das Bild, während für jeden Zuschauer überhaupt nichts geschieht.",
 "pt-BR": "Eu fotografo o mar. Paisagens marinhas sobretudo, e longas exposições mais do que tudo. Uma longa exposição é uma fotografia que se faz esperando: você mantém o obturador aberto e fica parado, e a água se desenha sozinha no quadro enquanto, para quem olha, não está acontecendo nada.",
 "ja": "私は海を撮る写真家です。海景が中心で、なかでも長時間露光を好みます。長時間露光とは、待つことで撮る写真です。シャッターを開いたまま動かずにいると、傍から見れば何も起きていないあいだに、水がひとりでに像を描いていきます。"},

"I love walking on beaches, and I have done since I was a boy, always looking for the same thing in the sand: a bottle with a letter inside, written years earlier by someone I would never meet, telling me something true about their life.": {
 "it": "Amo camminare sulle spiagge, e lo faccio da quando ero bambino, cercando nella sabbia sempre la stessa cosa: una bottiglia con dentro una lettera, scritta anni prima da qualcuno che non incontrerò mai, che mi racconta qualcosa di vero della sua vita.",
 "es": "Me encanta caminar por las playas, y lo hago desde niño, buscando en la arena siempre lo mismo: una botella con una carta dentro, escrita años antes por alguien a quien nunca conoceré, que me cuenta algo verdadero de su vida.",
 "fr": "J'aime marcher sur les plages, et je le fais depuis l'enfance, en cherchant dans le sable toujours la même chose : une bouteille avec une lettre dedans, écrite des années plus tôt par quelqu'un que je ne rencontrerai jamais, et qui me raconte quelque chose de vrai sur sa vie.",
 "de": "Ich liebe es, an Stränden zu gehen, und tue es, seit ich ein Junge war, immer auf der Suche nach demselben im Sand: einer Flasche mit einem Brief darin, Jahre zuvor geschrieben von jemandem, dem ich nie begegnen werde, und der mir etwas Wahres aus seinem Leben erzählt.",
 "pt-BR": "Amo caminhar pelas praias, e faço isso desde menino, procurando na areia sempre a mesma coisa: uma garrafa com uma carta dentro, escrita anos antes por alguém que nunca vou encontrar, contando algo verdadeiro da sua vida.",
 "ja": "浜を歩くのが好きで、子どもの頃からずっと、砂の中に同じものを探しながら歩いています。中に手紙の入った瓶。何年も前に、二度と会うことのない誰かが書いた、その人の人生の本当のことが記された手紙です。"},

"I have never found one.": {
 "it": "Non l'ho mai trovata.",
 "es": "Nunca la he encontrado.",
 "fr": "Je n'en ai jamais trouvé.",
 "de": "Gefunden habe ich nie eine.",
 "pt-BR": "Nunca encontrei nenhuma.",
 "ja": "一度も見つかりませんでした。"},

"So I built it. Two hundred and fifty beaches, each at its real coordinates, and a tide that carries a bottle along the real sea route between two coasts, taking the time that much water would take.": {
 "it": "Così me la sono costruita. Duecentocinquanta spiagge, ognuna alle sue coordinate vere, e una marea che porta una bottiglia lungo la rotta di mare vera fra due coste, prendendosi il tempo che ci vorrebbe per tutta quell'acqua.",
 "es": "Así que me la construí. Doscientas cincuenta playas, cada una en sus coordenadas reales, y una marea que lleva una botella por la ruta marina real entre dos costas, tomándose el tiempo que haría falta para toda esa agua.",
 "fr": "Alors je l'ai construite. Deux cent cinquante plages, chacune à ses vraies coordonnées, et une marée qui porte une bouteille le long de la vraie route maritime entre deux côtes, en prenant le temps qu'il faudrait pour toute cette eau.",
 "de": "Also habe ich sie gebaut. Zweihundertfünfzig Strände, jeder an seinen echten Koordinaten, und eine Tide, die eine Flasche entlang der echten Seeroute zwischen zwei Küsten trägt und sich dafür die Zeit nimmt, die all dieses Wasser brauchen würde.",
 "pt-BR": "Então eu a construí. Duzentas e cinquenta praias, cada uma nas suas coordenadas reais, e uma maré que leva uma garrafa pela rota marítima real entre duas costas, levando o tempo que toda aquela água levaria.",
 "ja": "だから自分で作りました。それぞれが実在の座標にある二百五十の浜と、二つの海岸のあいだの実際の航路に沿って瓶を運ぶ潮。それだけの海を渡るのにかかるはずの時間を、そのままかけて。"},

"Tomorrow, a bottle from someone you do not know will wash up on your sand. That is the whole app.": {
 "it": "Domani sulla tua sabbia arriverà la bottiglia di qualcuno che non conosci. L'app è tutta qui.",
 "es": "Mañana llegará a tu arena la botella de alguien a quien no conoces. La app es toda esto.",
 "fr": "Demain, sur votre sable, arrivera la bouteille de quelqu'un que vous ne connaissez pas. L'application, c'est tout entière cela.",
 "de": "Morgen wird an Ihrem Sand die Flasche von jemandem anspülen, den Sie nicht kennen. Das ist die ganze App.",
 "pt-BR": "Amanhã chegará à sua areia a garrafa de alguém que você não conhece. O app é só isso.",
 "ja": "明日、あなたの砂浜に、知らない誰かの瓶が流れ着きます。このアプリはそれだけです。"},

"Francesco Gola, seascape photographer": {
 "it": "Francesco Gola, fotografo di paesaggio marino",
 "es": "Francesco Gola, fotógrafo de paisaje marino",
 "fr": "Francesco Gola, photographe de paysages marins",
 "de": "Francesco Gola, Seelandschaftsfotograf",
 "pt-BR": "Francesco Gola, fotógrafo de paisagem marinha",
 "ja": "フランチェスコ・ゴーラ（海景写真家）"},

"The sea chooses who reads it": {
 "it": "Chi la legge, lo sceglie il mare",
 "es": "Quién la lee lo elige el mar",
 "fr": "La mer choisit qui la lit",
 "de": "Wer ihn liest, entscheidet das Meer",
 "pt-BR": "Quem lê é o mar que escolhe",
 "ja": "誰が読むかは、海が決める"},

"Every day the sea leaves you three bottles. You put a letter in one and hand it to the current, and the current carries it to a beach of its own choosing.": {
 "it": "Ogni giorno il mare ti lascia tre bottiglie. Ci metti dentro una lettera e la affidi alla corrente, e la corrente la porta su una spiaggia che sceglie lei.",
 "es": "Cada día el mar te deja tres botellas. Metes dentro una carta y la entregas a la corriente, y la corriente la lleva a una playa que elige ella.",
 "fr": "Chaque jour la mer vous laisse trois bouteilles. Vous glissez une lettre dans l'une d'elles et vous la confiez au courant, et le courant la porte vers une plage de son choix.",
 "de": "Jeden Tag lässt Ihnen das Meer drei Flaschen. Sie legen einen Brief hinein und geben ihn der Strömung, und die Strömung trägt ihn an einen Strand ihrer Wahl.",
 "pt-BR": "Todo dia o mar deixa três garrafas para você. Você põe uma carta dentro e a entrega à correnteza, e a correnteza a leva para uma praia que ela mesma escolhe.",
 "ja": "海は毎日、三本の瓶をあなたに残します。その一本に手紙を入れて潮に託すと、潮はそれを自分の選んだ浜へ運んでいきます。"},

"The sea takes its time": {
 "it": "Il mare si prende il suo tempo",
 "es": "El mar se toma su tiempo",
 "fr": "La mer prend son temps",
 "de": "Das Meer lässt sich Zeit",
 "pt-BR": "O mar leva o tempo dele",
 "ja": "海は急がない"},

"Every beach is a real place, at its real latitude and longitude, and the routes between them run around the coastlines instead of through them: a bottle bound for the far side of Africa goes around Africa. The further your letter has to travel, the longer the sea keeps it. Six hours sometimes, a day and a half other times. While it is out there you can follow it on a nautical chart, a little further along every time you look.": {
 "it": "Ogni spiaggia è un posto vero, alla sua latitudine e longitudine, e le rotte fra loro girano attorno alle coste invece di attraversarle: una bottiglia diretta dall'altra parte dell'Africa fa il giro dell'Africa. Più lontano deve andare la tua lettera, più a lungo il mare se la tiene. A volte sei ore, a volte un giorno e mezzo. Mentre è là fuori la segui su una carta nautica, un po' più avanti ogni volta che guardi.",
 "es": "Cada playa es un lugar real, en su latitud y su longitud, y las rutas entre ellas rodean las costas en vez de atravesarlas: una botella que va al otro lado de África da la vuelta a África. Cuanto más lejos tenga que ir tu carta, más tiempo se la queda el mar. A veces seis horas, a veces día y medio. Mientras está ahí fuera la sigues en una carta náutica, un poco más allá cada vez que miras.",
 "fr": "Chaque plage est un lieu réel, à sa latitude et à sa longitude, et les routes entre elles contournent les côtes au lieu de les traverser : une bouteille qui va de l'autre côté de l'Afrique fait le tour de l'Afrique. Plus votre lettre doit voyager loin, plus la mer la garde longtemps. Parfois six heures, parfois un jour et demi. Pendant qu'elle est au large, vous la suivez sur une carte marine, un peu plus loin à chaque fois que vous regardez.",
 "de": "Jeder Strand ist ein realer Ort, auf seinem echten Breiten- und Längengrad, und die Routen zwischen ihnen führen um die Küsten herum statt hindurch: eine Flasche, die ans andere Ende Afrikas soll, fährt um Afrika herum. Je weiter Ihr Brief reisen muss, desto länger behält ihn das Meer. Mal sechs Stunden, mal anderthalb Tage. Solange er draußen ist, verfolgen Sie ihn auf einer Seekarte, bei jedem Blick ein Stück weiter.",
 "pt-BR": "Cada praia é um lugar real, na sua latitude e na sua longitude, e as rotas entre elas contornam as costas em vez de atravessá-las: uma garrafa que vai para o outro lado da África dá a volta na África. Quanto mais longe sua carta tiver que ir, mais tempo o mar a segura. Às vezes seis horas, às vezes um dia e meio. Enquanto ela está lá fora você a segue numa carta náutica, um pouco mais adiante a cada vez que olha.",
 "ja": "どの浜も実在の場所で、実際の緯度と経度を持っています。浜と浜を結ぶ航路は陸を突っ切らず、海岸線を回り込みます。アフリカの向こう側へ向かう瓶は、アフリカをぐるりと回るのです。遠くへ運ぶ手紙ほど、海は長く手元に置きます。六時間のこともあれば、一日半のこともあります。航海中は海図の上で追うことができ、見るたびに少しずつ進んでいます。"},

"They can answer, and then it is your turn": {
 "it": "Può rispondere, e poi tocca a te",
 "es": "Puede responder, y luego te toca a ti",
 "fr": "Il peut répondre, et c'est ensuite votre tour",
 "de": "Sie können antworten, und dann sind Sie dran",
 "pt-BR": "Pode responder, e depois é a sua vez",
 "ja": "返事が来たら、次はあなたの番"},

"Whoever finds your letter can write back, and the sea takes its own time to deliver the answer. A correspondence alternates: you write, they answer, you write again. Once the cork is in, the letter belongs to the sea. Everything you choose to keep goes into a journal that stays on your beach.": {
 "it": "Chi trova la tua lettera può risponderti, e il mare si prende il suo tempo per consegnarti la risposta. Una corrispondenza si alterna: scrivi tu, risponde lui, scrivi di nuovo. Quando il tappo è dentro, la lettera appartiene al mare. Tutto quello che decidi di tenere finisce in un diario che resta sulla tua spiaggia.",
 "es": "Quien encuentre tu carta puede responderte, y el mar se toma su tiempo para entregarte la respuesta. Una correspondencia se alterna: escribes tú, responde él, vuelves a escribir. Una vez puesto el corcho, la carta pertenece al mar. Todo lo que decides guardar va a un diario que se queda en tu playa.",
 "fr": "Celui qui trouve votre lettre peut vous répondre, et la mer prend son temps pour vous livrer la réponse. Une correspondance alterne : vous écrivez, il répond, vous écrivez de nouveau. Une fois le bouchon enfoncé, la lettre appartient à la mer. Tout ce que vous choisissez de garder va dans un journal qui reste sur votre plage.",
 "de": "Wer Ihren Brief findet, kann zurückschreiben, und das Meer lässt sich Zeit, Ihnen die Antwort zu bringen. Ein Briefwechsel wechselt sich ab: Sie schreiben, die andere Person antwortet, Sie schreiben wieder. Sobald der Korken sitzt, gehört der Brief dem Meer. Alles, was Sie behalten wollen, kommt in ein Tagebuch, das an Ihrem Strand bleibt.",
 "pt-BR": "Quem encontrar sua carta pode responder, e o mar leva o tempo dele para entregar a resposta. Uma correspondência se alterna: você escreve, a pessoa responde, você escreve de novo. Depois que a rolha entra, a carta pertence ao mar. Tudo o que você decidir guardar vai para um diário que fica na sua praia.",
 "ja": "手紙を見つけた人は返事を書くことができ、それを届けるのに海はまた時間をかけます。文通は交互に進みます。あなたが書き、相手が答え、またあなたが書く。栓をした手紙は、もう海のものです。残したいと思ったものはすべて、あなたの浜にとどまる日誌に収められます。"},

"And then there are the spirits": {
 "it": "E poi ci sono gli spiriti",
 "es": "Y luego están los espíritus",
 "fr": "Et puis il y a les esprits",
 "de": "Und dann sind da die Geister",
 "pt-BR": "E então há os espíritos",
 "ja": "そして、海の魂たち"},

"privacy page": {
 "it": "pagina della privacy",
 "es": "página de privacidad",
 "fr": "page de confidentialité",
 "de": "Datenschutzseite",
 "pt-BR": "página de privacidade",
 "ja": "プライバシーのページ"},

"says exactly what happens to whatever you write back.": {
 "it": "dice esattamente cosa succede a quello che scrivi tu.",
 "es": "dice exactamente qué pasa con lo que escribes tú.",
 "fr": "dit exactement ce qu'il advient de ce que vous écrivez en retour.",
 "de": "sagt genau, was mit dem geschieht, was Sie zurückschreiben.",
 "pt-BR": "diz exatamente o que acontece com o que você escreve de volta.",
 "ja": "に詳しく書いてあります。"},

"Fact sheet": {
 "it": "Scheda",
 "es": "Ficha",
 "fr": "Fiche",
 "de": "Steckbrief",
 "pt-BR": "Ficha",
 "ja": "ファクトシート"},

"Name": {
 "it": "Nome",
 "es": "Nombre",
 "fr": "Nom",
 "de": "Name",
 "pt-BR": "Nome",
 "ja": "名称"},

"Developer": {
 "it": "Autore",
 "es": "Autor",
 "fr": "Auteur",
 "de": "Entwickler",
 "pt-BR": "Autor",
 "ja": "開発者"},

"Platform": {
 "it": "Piattaforma",
 "es": "Plataforma",
 "fr": "Plateforme",
 "de": "Plattform",
 "pt-BR": "Plataforma",
 "ja": "対応"},

"Category": {
 "it": "Categoria",
 "es": "Categoría",
 "fr": "Catégorie",
 "de": "Kategorie",
 "pt-BR": "Categoria",
 "ja": "カテゴリ"},

"Release": {
 "it": "Uscita",
 "es": "Lanzamiento",
 "fr": "Sortie",
 "de": "Erscheint",
 "pt-BR": "Lançamento",
 "ja": "公開"},

"Price": {
 "it": "Prezzo",
 "es": "Precio",
 "fr": "Prix",
 "de": "Preis",
 "pt-BR": "Preço",
 "ja": "価格"},

"Languages": {
 "it": "Lingue",
 "es": "Idiomas",
 "fr": "Langues",
 "de": "Sprachen",
 "pt-BR": "Idiomas",
 "ja": "対応言語"},

"Website": {
 "it": "Sito",
 "es": "Sitio",
 "fr": "Site",
 "de": "Website",
 "pt-BR": "Site",
 "ja": "サイト"},

"Contact": {
 "it": "Contatto",
 "es": "Contacto",
 "fr": "Contact",
 "de": "Kontakt",
 "pt-BR": "Contato",
 "ja": "連絡先"},

"Social Networking": {
 "it": "Social Networking",
 "es": "Redes sociales",
 "fr": "Réseaux sociaux",
 "de": "Soziale Netze",
 "pt-BR": "Redes sociais",
 "ja": "ソーシャルネットワーキング"},

"iOS and Android": {
 "it": "iOS e Android", "es": "iOS y Android", "fr": "iOS et Android",
 "de": "iOS und Android", "pt-BR": "iOS e Android", "ja": "iOS・Android"},

"Coming soon": {
 "it": "Prossimamente",
 "es": "Próximamente",
 "fr": "Bientôt",
 "de": "Demnächst",
 "pt-BR": "Em breve",
 "ja": "近日公開"},

"Free, with optional purchases": {
 "it": "Gratis, con acquisti facoltativi",
 "es": "Gratis, con compras opcionales",
 "fr": "Gratuit, avec des achats facultatifs",
 "de": "Kostenlos, mit optionalen Käufen",
 "pt-BR": "Grátis, com compras opcionais",
 "ja": "無料（購入は任意）"},

"English, Italian, German, Spanish, French, Japanese, Brazilian Portuguese": {
 "it": "Inglese, italiano, tedesco, spagnolo, francese, giapponese, portoghese brasiliano",
 "es": "Inglés, italiano, alemán, español, francés, japonés, portugués de Brasil",
 "fr": "Anglais, italien, allemand, espagnol, français, japonais, portugais brésilien",
 "de": "Englisch, Italienisch, Deutsch, Spanisch, Französisch, Japanisch, brasilianisches Portugiesisch",
 "pt-BR": "Inglês, italiano, alemão, espanhol, francês, japonês, português do Brasil",
 "ja": "英語、イタリア語、ドイツ語、スペイン語、フランス語、日本語、ブラジルポルトガル語"},

"illustrated beaches, each one different at dawn, at midday, at dusk and at night": {
 "it": "spiagge illustrate, ognuna diversa all'alba, a mezzogiorno, al tramonto e di notte",
 "es": "playas ilustradas, cada una distinta al alba, al mediodía, al atardecer y de noche",
 "fr": "plages illustrées, chacune différente à l'aube, à midi, au crépuscule et la nuit",
 "de": "illustrierte Strände, jeder anders im Morgengrauen, mittags, in der Dämmerung und nachts",
 "pt-BR": "praias ilustradas, cada uma diferente ao amanhecer, ao meio-dia, ao entardecer e à noite",
 "ja": "描かれた浜。夜明け、正午、夕暮れ、夜でそれぞれ違う表情になる"},

"sea routes between them, every one measured around the real coastline": {
 "it": "rotte di mare fra loro, ognuna misurata attorno alla costa vera",
 "es": "rutas marinas entre ellas, cada una medida rodeando la costa real",
 "fr": "routes maritimes entre elles, chacune mesurée en contournant la côte réelle",
 "de": "Seerouten dazwischen, jede entlang der echten Küstenlinie vermessen",
 "pt-BR": "rotas marítimas entre elas, cada uma medida contornando a costa real",
 "ja": "浜と浜を結ぶ航路。すべて実際の海岸線を回り込んで計測"},

"bottles a day": {
 "it": "bottiglie al giorno",
 "es": "botellas al día",
 "fr": "bouteilles par jour",
 "de": "Flaschen pro Tag",
 "pt-BR": "garrafas por dia",
 "ja": "本の瓶が毎日"},

"hours for a letter to cross the sea": {
 "it": "ore perché una lettera attraversi il mare",
 "es": "horas para que una carta cruce el mar",
 "fr": "heures pour qu'une lettre traverse la mer",
 "de": "Stunden, bis ein Brief das Meer überquert",
 "pt-BR": "horas para uma carta atravessar o mar",
 "ja": "時間で手紙は海を渡る"},

"Images": {
 "it": "Immagini",
 "es": "Imágenes",
 "fr": "Images",
 "de": "Bilder",
 "pt-BR": "Imagens",
 "ja": "画像"},

"Everything here may be reproduced freely in coverage of Bottlegram, in print or online, with or without credit. Each screenshot opens at full size; the zip holds all ten as PNG, with and without captions, along with the app icon and a feature graphic.": {
 "it": "Tutto quello che c'è qui si può riprodurre liberamente per parlare di Bottlegram, su carta o in rete, con o senza credito. Ogni schermata si apre a piena grandezza; lo zip le ha tutte e dieci in PNG, con e senza didascalia, insieme all'icona dell'app e a una grafica in evidenza.",
 "es": "Todo lo que hay aquí puede reproducirse libremente para hablar de Bottlegram, en papel o en línea, con o sin crédito. Cada captura se abre a tamaño completo; el zip tiene las diez en PNG, con y sin pie, junto con el icono de la app y una imagen destacada.",
 "fr": "Tout ce qui se trouve ici peut être reproduit librement pour parler de Bottlegram, sur papier ou en ligne, avec ou sans crédit. Chaque capture s'ouvre en taille réelle ; le zip contient les dix en PNG, avec et sans légende, avec l'icône de l'application et un visuel de présentation.",
 "de": "Alles hier darf in Berichten über Bottlegram frei verwendet werden, gedruckt oder online, mit oder ohne Nennung. Jeder Screenshot öffnet sich in voller Größe; das Zip enthält alle zehn als PNG, mit und ohne Bildunterschrift, dazu das App-Icon und eine Vorstellungsgrafik.",
 "pt-BR": "Tudo o que está aqui pode ser reproduzido livremente para falar do Bottlegram, impresso ou on-line, com ou sem crédito. Cada captura abre em tamanho real; o zip traz as dez em PNG, com e sem legenda, junto com o ícone do app e uma imagem de destaque.",
 "ja": "ここにあるものはすべて、Bottlegram を紹介する記事に、紙でもウェブでも、クレジットの有無を問わず自由に使えます。スクリーンショットはそれぞれ原寸で開きます。zip には十枚すべてが PNG で、キャプションありとなしの両方、さらにアプリのアイコンとフィーチャーグラフィックが入っています。"},

"Luskentyre at sunset, with bottles on the sand.": {
 "it": "Luskentyre al tramonto, con bottiglie sulla sabbia.",
 "es": "Luskentyre al atardecer, con botellas en la arena.",
 "fr": "Luskentyre au coucher du soleil, avec des bouteilles sur le sable.",
 "de": "Luskentyre bei Sonnenuntergang, mit Flaschen im Sand.",
 "pt-BR": "Luskentyre ao pôr do sol, com garrafas na areia.",
 "ja": "夕暮れのラスケンタイア、砂の上の瓶。"},

"An open correspondence: a letter, and the reply that came back.": {
 "it": "Una corrispondenza aperta: una lettera, e la risposta che è tornata.",
 "es": "Una correspondencia abierta: una carta, y la respuesta que volvió.",
 "fr": "Une correspondance ouverte : une lettre, et la réponse qui est revenue.",
 "de": "Ein offener Briefwechsel: ein Brief und die Antwort, die zurückkam.",
 "pt-BR": "Uma correspondência aberta: uma carta, e a resposta que voltou.",
 "ja": "開かれた文通。一通の手紙と、返ってきた返事。"},

"Everything, as a zip": {
 "it": "Tutto quanto, in uno zip",
 "es": "Todo, en un zip",
 "fr": "Tout, en un zip",
 "de": "Alles, als ZIP",
 "pt-BR": "Tudo, em um zip",
 "ja": "すべてを ZIP で"},

"App preview": {
 "it": "Anteprima dell'app",
 "es": "Vista previa de la app",
 "fr": "Aperçu de l'application",
 "de": "App-Vorschau",
 "pt-BR": "Prévia do app",
 "ja": "アプリのプレビュー"},

"25 seconds": {
 "it": "25 secondi",
 "es": "25 segundos",
 "fr": "25 secondes",
 "de": "25 Sekunden",
 "pt-BR": "25 segundos",
 "ja": "25秒"},

"Trying it before it opens": {
 "it": "Provarla prima che apra",
 "es": "Probarla antes de que abra",
 "fr": "L'essayer avant l'ouverture",
 "de": "Ausprobieren, bevor es losgeht",
 "pt-BR": "Experimentar antes de abrir",
 "ja": "公開前に試す"},

"Bottlegram opens soon on iPhone and Android. Until then, write to this address and you get a build to try, along with a beach of your own and enough bottles to see what comes back:": {
 "it": "Bottlegram apre presto su iPhone e Android. Fino ad allora, scrivi a questo indirizzo e ricevi una build da provare, con una spiaggia tua e bottiglie a sufficienza per vedere cosa torna indietro:",
 "es": "Bottlegram abre pronto en iPhone y Android. Hasta entonces, escribe a esta dirección y recibirás una build para probar, con una playa propia y botellas suficientes para ver qué vuelve:",
 "fr": "Bottlegram ouvre bientôt sur iPhone et Android. D'ici là, écrivez à cette adresse et vous recevrez une version à essayer, avec une plage à vous et assez de bouteilles pour voir ce qui revient :",
 "de": "Bottlegram öffnet bald auf iPhone und Android. Bis dahin schreiben Sie an diese Adresse und Sie erhalten einen Build zum Ausprobieren, dazu einen eigenen Strand und genug Flaschen, um zu sehen, was zurückkommt:",
 "pt-BR": "O Bottlegram abre em breve no iPhone e no Android. Até lá, escreva para este endereço e você recebe uma build para testar, com uma praia sua e garrafas suficientes para ver o que volta:",
 "ja": "Bottlegram はまもなく iPhone と Android で公開されます。それまでのあいだ、このアドレスに連絡いただければ試用ビルドをお送りします。あなた専用の浜と、何が返ってくるかを確かめるのに十分な数の瓶つきで。"},

"The same address reaches Francesco directly for an interview, a question, or any detail beyond this page.": {
 "it": "Lo stesso indirizzo arriva direttamente a Francesco per un'intervista, una domanda, o qualunque dettaglio oltre questa pagina.",
 "es": "La misma dirección llega directamente a Francesco para una entrevista, una pregunta o cualquier detalle más allá de esta página.",
 "fr": "La même adresse joint directement Francesco pour une interview, une question, ou tout détail au-delà de cette page.",
 "de": "Dieselbe Adresse erreicht Francesco direkt, für ein Interview, eine Frage oder jedes Detail über diese Seite hinaus.",
 "pt-BR": "O mesmo endereço chega diretamente ao Francesco para uma entrevista, uma pergunta ou qualquer detalhe além desta página.",
 "ja": "同じアドレスはフランチェスコ本人に直接届きます。取材のご依頼、ご質問、このページの先の詳細などはこちらへ。"},

"The beach": {
 "it": "La spiaggia",
 "es": "La playa",
 "fr": "La plage",
 "de": "Der Strand",
 "pt-BR": "A praia",
 "ja": "浜辺"},

"No map service, no tracking, no cookies: this page does not know who you are, exactly like the sea.": {
 "it": "Nessun servizio di mappe, nessun tracciamento, nessun cookie: questa pagina non sa chi sei, esattamente come il mare.",
 "es": "Ningún servicio de mapas, ningún rastreo, ninguna cookie: esta página no sabe quién eres, exactamente como el mar.",
 "fr": "Aucun service de cartes, aucun traçage, aucun cookie : cette page ne sait pas qui vous êtes, exactement comme la mer.",
 "de": "Kein Kartendienst, kein Tracking, keine Cookies: Diese Seite weiß nicht, wer Sie sind, genau wie das Meer.",
 "pt-BR": "Nenhum serviço de mapas, nenhum rastreamento, nenhum cookie: esta página não sabe quem você é, exatamente como o mar.",
 "ja": "地図サービスなし、追跡なし、Cookie なし。このページは海と同じく、あなたが誰かを知りません。"},

"Why slow": {
 "it": "Perché lenta",
 "es": "Por qué lenta",
 "fr": "Pourquoi lente",
 "de": "Warum langsam",
 "pt-BR": "Por que lenta",
 "ja": "なぜ、ゆっくりなのか"},

"The sea has its spirits. They were here long before any castaway, each with a life of their own to tell, and every so often one of them picks up a bottle and writes to you. If a spirit writes to you, you were lucky. Their letters always carry their mark.": {
 "it": "Il mare ha i suoi spiriti. Erano qui molto prima di qualunque naufrago, ognuno con una vita sua da raccontare, e ogni tanto uno di loro prende una bottiglia e scrive a te. Se ti scrive uno spirito, sei stato fortunato. Le loro lettere portano sempre il loro segno.",
 "es": "El mar tiene sus espíritus. Estaban aquí mucho antes que cualquier náufrago, cada uno con una vida propia que contar, y de vez en cuando uno de ellos coge una botella y te escribe. Si te escribe un espíritu, has tenido suerte. Sus cartas llevan siempre su marca.",
 "fr": "La mer a ses esprits. Ils étaient là bien avant le premier naufragé, chacun avec sa propre vie à raconter, et de temps en temps l'un d'eux prend une bouteille et vous écrit. Si un esprit vous écrit, vous avez eu de la chance. Leurs lettres portent toujours leur marque.",
 "de": "Das Meer hat seine Geister. Sie waren lange vor jedem Schiffbrüchigen hier, jeder mit einem eigenen Leben zu erzählen, und hin und wieder nimmt einer von ihnen eine Flasche und schreibt Ihnen. Wenn ein Geist Ihnen schreibt, hatten Sie Glück. Ihre Briefe tragen immer ihr Zeichen.",
 "pt-BR": "O mar tem seus espíritos. Estavam aqui muito antes de qualquer náufrago, cada um com uma vida própria para contar, e de vez em quando um deles pega uma garrafa e escreve para você. Se um espírito escrever para você, você teve sorte. As cartas deles trazem sempre a sua marca.",
 "ja": "この海には魂たちがいます。どの漂着者よりもずっと前からここにいて、それぞれに語るべき生涯を持ち、ときおりそのうちの一人が瓶を手に取り、あなたに手紙を書きます。魂から手紙が届いたなら、あなたは幸運でした。その手紙には必ず彼らの印があります。"},

"Somewhere a phone is buzzing and someone is waiting for an answer. Here, the sea is carrying yours.": {
 "it": "Da qualche parte un telefono sta vibrando e qualcuno aspetta una risposta. Qui, la tua la sta portando il mare.",
 "es": "En algún sitio un teléfono está vibrando y alguien espera una respuesta. Aquí, la tuya la lleva el mar.",
 "fr": "Quelque part un téléphone vibre et quelqu'un attend une réponse. Ici, c'est la mer qui porte la vôtre.",
 "de": "Irgendwo vibriert ein Telefon und jemand wartet auf eine Antwort. Hier trägt das Meer Ihre.",
 "pt-BR": "Em algum lugar um telefone está vibrando e alguém espera uma resposta. Aqui, a sua está sendo levada pelo mar.",
 "ja": "どこかで電話が震え、誰かが返事を待っています。ここでは、あなたの返事を海が運んでいます。"},

"Here your letter is at sea, and the sea can take more than a day to deliver it. While it travels you can watch it cross the chart, or forget about it until the tide comes back. It ends up on a beach you have never seen, and someone you will never meet decides whether to write back.": {
 "it": "Qui la tua lettera è in mare, e il mare ci può mettere più di un giorno per consegnarla. Mentre viaggia puoi guardarla attraversare la carta, o dimenticartene finché la marea non torna. Finisce su una spiaggia che non hai mai visto, e qualcuno che non incontrerai mai decide se risponderti.",
 "es": "Aquí tu carta está en el mar, y el mar puede tardar más de un día en entregarla. Mientras viaja puedes verla cruzar la carta náutica, u olvidarte de ella hasta que vuelva la marea. Acaba en una playa que nunca has visto, y alguien a quien nunca conocerás decide si te responde.",
 "fr": "Ici votre lettre est en mer, et la mer peut mettre plus d'une journée à la livrer. Pendant qu'elle voyage, vous pouvez la regarder traverser la carte, ou l'oublier jusqu'au retour de la marée. Elle finit sur une plage que vous n'avez jamais vue, et quelqu'un que vous ne rencontrerez jamais décide s'il vous répond.",
 "de": "Hier ist Ihr Brief auf See, und das Meer kann länger als einen Tag brauchen, um ihn zuzustellen. Während er reist, können Sie ihm auf der Karte zusehen oder ihn vergessen, bis die Flut zurückkommt. Er landet an einem Strand, den Sie nie gesehen haben, und jemand, dem Sie nie begegnen werden, entscheidet, ob er zurückschreibt.",
 "pt-BR": "Aqui sua carta está no mar, e o mar pode levar mais de um dia para entregá-la. Enquanto ela viaja, você pode vê-la atravessar a carta náutica, ou esquecê-la até a maré voltar. Ela vai parar numa praia que você nunca viu, e alguém que você nunca vai conhecer decide se responde.",
 "ja": "ここでは、あなたの手紙は海の上にあり、海はそれを届けるのに一日以上かけることもあります。旅のあいだは海図の上を進むのを眺めてもいいし、潮が戻るまで忘れていてもいい。手紙は見たこともない浜に流れ着き、一生会うことのない誰かが返事を書くかどうかを決めます。"},

"A friend of mine said it better: in a world that runs at two thousand miles an hour and expects us to answer at the same speed, this feels like the best possible reply.": {
 "it": "Un mio amico l'ha detta meglio: in un mondo che va a duemila all'ora e pretende che rispondiamo alla stessa velocità, questa mi sembra la migliore delle risposte.",
 "es": "Un amigo mío lo dijo mejor: en un mundo que va a dos mil por hora y pretende que respondamos a la misma velocidad, esta me parece la mejor de las respuestas.",
 "fr": "Un ami me l'a dit mieux : dans un monde qui file à deux mille à l'heure et qui exige qu'on réponde à la même vitesse, cela me semble la meilleure des réponses.",
 "de": "Ein Freund hat es besser gesagt: In einer Welt, die zweitausend Sachen fährt und erwartet, dass wir genauso schnell antworten, scheint mir das die beste aller Antworten.",
 "pt-BR": "Um amigo meu disse melhor: num mundo que corre a dois mil por hora e exige que a gente responda na mesma velocidade, essa me parece a melhor das respostas.",
 "ja": "友人が、もっとうまく言ってくれました。時速二千キロで走り、同じ速さで返事をすることを求めてくる世界にあって、これは考えうる最良の返事に思える、と。"},

"A slow messaging app where letters travel by sea, and the current decides who reads them and when.": {
 "it": "Un'app di messaggi lenti dove le lettere viaggiano via mare, ed è la corrente a decidere chi le legge e dopo quanto.",
 "es": "Una app de mensajes lentos donde las cartas viajan por mar y la corriente decide quién las lee y cuándo.",
 "fr": "Une application de messages lents où les lettres voyagent par la mer, et où le courant décide qui les lira et quand.",
 "de": "Eine App für langsame Nachrichten, in der Briefe über das Meer reisen und die Strömung entscheidet, wer sie liest und wann.",
 "pt-BR": "Um app de mensagens lentas onde as cartas viajam pelo mar e a correnteza decide quem as lê e quando.",
 "ja": "手紙が海を渡り、誰がいつ読むかは潮が決める、ゆっくりとしたメッセージアプリ。"},

"Press kit for Bottlegram: a slow messaging app where letters travel by sea, and the current decides who reads them and when. Screenshots, fact sheet.": {
 "it": "Press kit di Bottlegram: un'app di messaggi lenti dove le lettere viaggiano via mare, ed è la corrente a decidere chi le legge e dopo quanto. Schermate, scheda.",
 "es": "Press kit de Bottlegram: una app de mensajes lentos donde las cartas viajan por mar y la corriente decide quién las lee y cuándo. Capturas, ficha.",
 "fr": "Dossier de presse de Bottlegram : une application de messages lents où les lettres voyagent par la mer, et où le courant décide qui les lira et quand. Captures, fiche.",
 "de": "Pressemappe zu Bottlegram: eine App für langsame Nachrichten, in der Briefe über das Meer reisen und die Strömung entscheidet, wer sie liest und wann. Screenshots, Steckbrief.",
 "pt-BR": "Kit de imprensa do Bottlegram: um app de mensagens lentas onde as cartas viajam pelo mar e a correnteza decide quem as lê e quando. Capturas, ficha.",
 "ja": "Bottlegram のプレスキット。手紙が海を渡り、誰がいつ読むかは潮が決める、ゆっくりとしたメッセージアプリ。スクリーンショット、ファクトシート。"},

"Press": {
 "it": "Stampa",
 "es": "Prensa",
 "fr": "Presse",
 "de": "Presse",
 "pt-BR": "Imprensa",
 "ja": "プレス"},

"Support": {
 "it": "Supporto",
 "es": "Soporte",
 "fr": "Assistance",
 "de": "Support",
 "pt-BR": "Suporte",
 "ja": "サポート"},

"A bottle, thrown well, can reach anyone.": {
 "it": "Una bottiglia, lanciata bene, può raggiungere chiunque.",
 "es": "Una botella, bien lanzada, puede llegar a cualquiera.",
 "fr": "Une bouteille, bien lancée, peut atteindre n'importe qui.",
 "de": "Eine gut geworfene Flasche kann jeden erreichen.",
 "pt-BR": "Uma garrafa, bem lançada, pode alcançar qualquer um.",
 "ja": "うまく投げた瓶は、誰のもとにも届きうる。"},

# ── Le cinque domande (11/09) ─────────────────────────────────────────────
# Sono del solo sito: nell'app le stesse cose si dicono a chi e' gia' dentro.
# «The Wreck Emporium» invece porta i nomi dell'app (shop.title), perche' e' un
# posto che chi legge poi trova aperto sul telefono con quel nome.

"Before you ask": {
 "it": "Prima di chiedere", "es": "Antes de preguntar", "fr": "Avant de demander",
 "de": "Bevor du fragst", "pt-BR": "Antes de perguntar", "ja": "その前に"},

"Five questions, answered plainly.": {
 "it": "Cinque domande, con risposte chiare.",
 "es": "Cinco preguntas, con respuestas claras.",
 "fr": "Cinq questions, des réponses claires.",
 "de": "Fünf Fragen, klar beantwortet.",
 "pt-BR": "Cinco perguntas, com respostas claras.",
 "ja": "五つの質問に、はっきり答えます。"},

"How long does a letter take?": {
 "it": "Quanto ci mette una lettera?", "es": "¿Cuánto tarda una carta?",
 "fr": "Combien de temps met une lettre ?", "de": "Wie lange braucht ein Brief?",
 "pt-BR": "Quanto tempo leva uma carta?", "ja": "手紙はどれくらいかかりますか。"},

"Between six and thirty-six hours, and it is the water that decides which: a shore across the same sea may answer by morning, the far side of the world will keep you waiting. Once the cork is in, it is out of your hands.": {
 "it": "Fra le sei e le trentasei ore, e quale delle due lo decide l'acqua: una costa sullo stesso mare può risponderti entro domattina, l'altra parte del mondo ti farà aspettare. Una volta messo il tappo, non è più cosa tua.",
 "es": "Entre seis y treinta y seis horas, y cuál de las dos lo decide el agua: una costa del mismo mar puede responderte por la mañana, el otro lado del mundo te hará esperar. Una vez puesto el corcho, ya no está en tus manos.",
 "fr": "Entre six et trente-six heures, et c'est l'eau qui décide : une côte sur la même mer peut répondre au matin, l'autre bout du monde te fera attendre. Une fois le bouchon mis, cela ne t'appartient plus.",
 "de": "Zwischen sechs und sechsunddreißig Stunden, und welche davon, entscheidet das Wasser: eine Küste am selben Meer antwortet vielleicht bis zum Morgen, die andere Seite der Welt lässt dich warten. Ist der Korken drin, liegt es nicht mehr bei dir.",
 "pt-BR": "Entre seis e trinta e seis horas, e qual delas quem decide é a água: uma costa do mesmo mar pode responder pela manhã, o outro lado do mundo vai te fazer esperar. Depois que a rolha entra, já não está nas suas mãos.",
 "ja": "六時間から三十六時間。どちらになるかを決めるのは水です。同じ海の向こう岸なら朝には返事が来るかもしれませんし、地球の裏側ならずっと待つことになります。栓をしたら、もうあなたの手を離れます。"},

"Can I choose who I write to?": {
 "it": "Posso scegliere a chi scrivo?", "es": "¿Puedo elegir a quién escribo?",
 "fr": "Puis-je choisir à qui j'écris ?", "de": "Kann ich wählen, wem ich schreibe?",
 "pt-BR": "Posso escolher para quem escrevo?", "ja": "誰に書くかを選べますか。"},

"The first time, the current chooses: you hand it the bottle and it picks the beach. Once someone has written back, that correspondence is yours: you go on writing to them for as long as you both keep answering.": {
 "it": "La prima volta sceglie la corrente: le affidi la bottiglia e la spiaggia la sceglie lei. Quando qualcuno ti ha risposto, quel carteggio è tuo: continui a scrivere a quella persona finché tutti e due rispondete.",
 "es": "La primera vez elige la corriente: le entregas la botella y ella escoge la playa. Cuando alguien te ha contestado, esa correspondencia es tuya: le sigues escribiendo mientras ambos sigan respondiendo.",
 "fr": "La première fois, c'est le courant qui choisit : tu lui confies la bouteille et il choisit la plage. Dès que quelqu'un t'a répondu, cette correspondance est à toi : tu continues à lui écrire tant que vous vous répondez tous les deux.",
 "de": "Beim ersten Mal wählt die Strömung: Du gibst ihr die Flasche, und sie sucht den Strand aus. Sobald jemand geantwortet hat, gehört dieser Briefwechsel dir: Du schreibst dieser Person weiter, solange ihr beide antwortet.",
 "pt-BR": "Na primeira vez, quem escolhe é a correnteza: você entrega a garrafa e ela escolhe a praia. Quando alguém responde, aquela correspondência é sua: você continua escrevendo para essa pessoa enquanto os dois continuarem respondendo.",
 "ja": "最初の一通は、海流が選びます。瓶を託せば、どの浜に着くかは海流が決めます。誰かが返事をくれたら、その文通はあなたのものです。二人が返しつづけるかぎり、その相手に書きつづけられます。"},

"And if nobody answers?": {
 "it": "E se non risponde nessuno?", "es": "¿Y si no responde nadie?",
 "fr": "Et si personne ne répond ?", "de": "Und wenn niemand antwortet?",
 "pt-BR": "E se ninguém responder?", "ja": "誰も返事をくれなかったら。"},

"Then you throw another. The sea gives you three bottles every day, and by then somebody else's may already be on your sand. A letter that comes back means more here, because someone chose to write it.": {
 "it": "Allora ne lanci un'altra. Il mare ti dà tre bottiglie ogni giorno, e intanto sulla tua sabbia può esserci già quella di qualcun altro. Qui una lettera che torna vale di più, perché qualcuno ha scelto di scriverla.",
 "es": "Entonces lanzas otra. El mar te da tres botellas cada día, y para entonces en tu arena puede haber ya la de otra persona. Aquí una carta que vuelve vale más, porque alguien eligió escribirla.",
 "fr": "Alors tu en lances une autre. La mer te donne trois bouteilles chaque jour, et d'ici là celle de quelqu'un d'autre est peut-être déjà sur ton sable. Ici, une lettre qui revient compte davantage, parce que quelqu'un a choisi de l'écrire.",
 "de": "Dann wirfst du eine neue. Das Meer gibt dir jeden Tag drei Flaschen, und bis dahin liegt vielleicht schon die von jemand anderem in deinem Sand. Ein Brief, der zurückkommt, bedeutet hier mehr, weil jemand ihn schreiben wollte.",
 "pt-BR": "Então você joga outra. O mar te dá três garrafas todo dia, e até lá a de outra pessoa já pode estar na sua areia. Aqui uma carta que volta vale mais, porque alguém escolheu escrevê-la.",
 "ja": "そのときは、もう一本投げればいい。海は毎日三本の瓶をくれますし、そのころには誰かの瓶があなたの砂に届いているかもしれません。ここで返ってくる手紙に重みがあるのは、誰かが書くことを選んだからです。"},

"Who reads what I write?": {
 "it": "Chi legge quello che scrivo?", "es": "¿Quién lee lo que escribo?",
 "fr": "Qui lit ce que j'écris ?", "de": "Wer liest, was ich schreibe?",
 "pt-BR": "Quem lê o que eu escrevo?", "ja": "書いたものは誰が読みますか。"},

"The castaway whose beach it washes up on. If someone reports a letter, a person reads that letter and the correspondence it belongs to, and decides whether the sea keeps its writer.": {
 "it": "Il naufrago sulla cui spiaggia approda. Se qualcuno segnala una lettera, una persona legge quella lettera e il carteggio di cui fa parte, e decide se il mare tiene chi l'ha scritta.",
 "es": "El náufrago a cuya playa llega. Si alguien denuncia una carta, una persona lee esa carta y la correspondencia a la que pertenece, y decide si el mar se queda con quien la escribió.",
 "fr": "Le naufragé sur la plage duquel elle échoue. Si quelqu'un signale une lettre, une personne lit cette lettre et la correspondance dont elle fait partie, et décide si la mer garde celui qui l'a écrite.",
 "de": "Der Schiffbrüchige, an dessen Strand er anlandet. Meldet jemand einen Brief, liest ein Mensch diesen Brief und den Briefwechsel, zu dem er gehört, und entscheidet, ob das Meer seinen Verfasser behält.",
 "pt-BR": "O náufrago em cuja praia ela chega. Se alguém denuncia uma carta, uma pessoa lê aquela carta e a correspondência a que ela pertence, e decide se o mar fica com quem a escreveu.",
 "ja": "その瓶が流れ着いた浜の漂着者です。誰かが手紙を通報すると、人がその手紙と、それを含む文通を読み、書いた人を海が置いておくかどうかを決めます。"},

"It is written out in full on the privacy page.": {
 "it": "È scritto per esteso nella pagina della privacy.",
 "es": "Está escrito por completo en la página de privacidad.",
 "fr": "C'est écrit en toutes lettres sur la page de confidentialité.",
 "de": "Es steht vollständig auf der Datenschutzseite.",
 "pt-BR": "Está escrito por inteiro na página de privacidade.",
 "ja": "詳しくはプライバシーのページに書いてあります。"},

"Is it free?": {
 "it": "È gratis?", "es": "¿Es gratis?", "fr": "C'est gratuit ?",
 "de": "Ist es kostenlos?", "pt-BR": "É grátis?", "ja": "無料ですか。"},

"Yes. Writing a letter and receiving one are free. On your beach there is also a Wreck Emporium with a few things in it, and they mostly help with what this costs: the work on the app, the servers that keep the sea running.": {
 "it": "Sì. Scrivere una lettera e riceverne una è gratis. Sulla tua spiaggia c'è anche l'Emporio del Relitto con dentro qualche cosa, e serve soprattutto ad aiutare con quello che tutto questo costa: il lavoro sull'app, i server che tengono in piedi il mare.",
 "es": "Sí. Escribir una carta y recibirla es gratis. En tu playa está también el Emporio del Naufragio con unas cuantas cosas dentro, y sirven sobre todo para ayudar con lo que todo esto cuesta: el trabajo en la app, los servidores que mantienen el mar en pie.",
 "fr": "Oui. Écrire une lettre et en recevoir une, c'est gratuit. Sur ta plage il y a aussi l'Emporium de l'Épave, avec quelques objets dedans, et ils servent surtout à aider avec ce que tout cela coûte : le travail sur l'app, les serveurs qui tiennent la mer debout.",
 "de": "Ja. Einen Brief zu schreiben und einen zu bekommen ist kostenlos. An deinem Strand steht außerdem das Kontor des Wracks mit ein paar Dingen darin, und die helfen vor allem bei dem, was das hier kostet: die Arbeit an der App, die Server, die das Meer am Laufen halten.",
 "pt-BR": "Sim. Escrever uma carta e receber uma é grátis. Na sua praia fica também o Empório do Naufrágio com algumas coisas dentro, e elas servem sobretudo para ajudar com o que tudo isso custa: o trabalho no app, os servidores que mantêm o mar de pé.",
 "ja": "はい。手紙を書くのも、受け取るのも無料です。あなたの浜には難破商館もあり、いくつか品物が置いてあります。それらは主に、これにかかるもの、つまりアプリの制作と、海を動かしつづけるサーバーを支えるためのものです。"},

"Coastlines from Natural Earth (public domain). Sounds from freesound.org (CC0). This page knows you only as a visitor, the way the sea knows you only as a castaway.": {
 "it": "Coste da Natural Earth (pubblico dominio). Suoni da freesound.org (CC0). Questa pagina ti conosce solo come visitatore, come il mare ti conosce solo come naufrago.",
 "es": "Costas de Natural Earth (dominio público). Sonidos de freesound.org (CC0). Esta página te conoce solo como visitante, igual que el mar te conoce solo como náufrago.",
 "fr": "Côtes issues de Natural Earth (domaine public). Sons de freesound.org (CC0). Cette page te connaît seulement comme visiteur, comme la mer te connaît seulement comme naufragé.",
 "de": "Küstenlinien von Natural Earth (gemeinfrei). Klänge von freesound.org (CC0). Diese Seite kennt dich nur als Besucher, so wie das Meer dich nur als Schiffbrüchigen kennt.",
 "pt-BR": "Costas do Natural Earth (domínio público). Sons do freesound.org (CC0). Esta página conhece você só como visitante, do jeito que o mar conhece você só como náufrago.",
 "ja": "海岸線は Natural Earth（パブリックドメイン）。音は freesound.org（CC0）。このページにとってあなたはただの訪問者で、海にとってあなたがただの漂着者であるのと同じです。"},

# ── La privacy (05/11/2026) ───────────────────────────────────────────────
# La pagina entra nelle sette lingue. I nomi dei servizi sono in INVARIATE.

"Privacy — Bottlegram": {
 "it": "Privacy — Bottlegram",
 "es": "Privacidad — Bottlegram",
 "fr": "Confidentialité — Bottlegram",
 "de": "Datenschutz — Bottlegram",
 "pt-BR": "Privacidade — Bottlegram",
 "ja": "プライバシー — Bottlegram"},

"Bottlegram never asks who you are. What little the sea keeps, who else touches a letter, and how to take it all back.": {
 "it": "Bottlegram non ti chiede mai chi sei. Quel poco che il mare tiene, chi altro tocca una lettera, e come riprenderti tutto.",
 "es": "Bottlegram nunca te pregunta quién eres. Lo poco que guarda el mar, quién más toca una carta y cómo recuperarlo todo.",
 "fr": "Bottlegram ne te demande jamais qui tu es. Le peu que la mer garde, qui d'autre touche une lettre, et comment tout reprendre.",
 "de": "Bottlegram fragt nie, wer du bist. Das Wenige, das das Meer behält, wer sonst einen Brief berührt, und wie du alles zurücknimmst.",
 "pt-BR": "O Bottlegram nunca pergunta quem você é. O pouco que o mar guarda, quem mais toca uma carta e como pegar tudo de volta.",
 "ja": "Bottlegram はあなたが誰なのかを決して尋ねません。海が覚えておくわずかなこと、手紙に触れるほかの誰か、そしてすべてを取り戻す方法。"},

"In effect since 5 November 2026 · Bottlegram is published by Bulb Mode SRL Semplificata, Via Ancona 15, 60035 Jesi (AN), Italy · VAT IT02730980428": {
 "it": "In vigore dal 5 novembre 2026 · Bottlegram è pubblicata da Bulb Mode SRL Semplificata, Via Ancona 15, 60035 Jesi (AN), Italia · P. IVA IT02730980428",
 "es": "En vigor desde el 5 de noviembre de 2026 · Bottlegram está publicada por Bulb Mode SRL Semplificata, Via Ancona 15, 60035 Jesi (AN), Italia · IVA IT02730980428",
 "fr": "En vigueur depuis le 5 novembre 2026 · Bottlegram est publiée par Bulb Mode SRL Semplificata, Via Ancona 15, 60035 Jesi (AN), Italie · TVA IT02730980428",
 "de": "Gültig seit dem 5. November 2026 · Bottlegram wird herausgegeben von Bulb Mode SRL Semplificata, Via Ancona 15, 60035 Jesi (AN), Italien · USt-IdNr. IT02730980428",
 "pt-BR": "Em vigor desde 5 de novembro de 2026 · O Bottlegram é publicado por Bulb Mode SRL Semplificata, Via Ancona 15, 60035 Jesi (AN), Itália · IVA IT02730980428",
 "ja": "2026年11月5日施行 · Bottlegram の提供者：Bulb Mode SRL Semplificata、Via Ancona 15, 60035 Jesi (AN), イタリア · VAT IT02730980428"},

"This page does not know who you are. Neither does the sea. What follows is the whole of it, written to be read.": {
 "it": "Questa pagina non sa chi sei. E nemmeno il mare. Quello che segue è tutto, scritto per essere letto.",
 "es": "Esta página no sabe quién eres. Tampoco el mar. Lo que sigue es todo, escrito para ser leído.",
 "fr": "Cette page ne sait pas qui tu es. La mer non plus. Ce qui suit, c'est tout, écrit pour être lu.",
 "de": "Diese Seite weiß nicht, wer du bist. Das Meer auch nicht. Was folgt, ist alles, und es ist zum Lesen geschrieben.",
 "pt-BR": "Esta página não sabe quem você é. O mar também não. O que vem a seguir é tudo, escrito para ser lido.",
 "ja": "このページは、あなたが誰なのかを知りません。海も知りません。ここに書いたことがすべてで、読まれるために書いてあります。"},

"The short version": {
 "it": "In breve",
 "es": "En pocas palabras",
 "fr": "En bref",
 "de": "Kurz gesagt",
 "pt-BR": "Em poucas palavras",
 "ja": "かんたんに言えば"},

"Bottlegram never asks your name, your email address, your phone number, your contacts or your location in order to use it. There is no signup form. When you first open the app, an anonymous account is created for you: a random identifier, and nothing attached to it. There is no advertising, no analytics, no tracking of any kind, in the app or on this site.": {
 "it": "Per usare Bottlegram non ti chiediamo mai il nome, l'indirizzo email, il numero di telefono, i contatti o la posizione. Non c'è un modulo di registrazione. La prima volta che apri l'app ti viene creato un account anonimo: un identificativo casuale, e niente attaccato. Non c'è pubblicità, non ci sono statistiche, non c'è tracciamento di alcun tipo, né nell'app né su questo sito.",
 "es": "Bottlegram nunca te pide tu nombre, tu correo, tu número de teléfono, tus contactos ni tu ubicación para usarla. No hay formulario de registro. La primera vez que abres la app se crea para ti una cuenta anónima: un identificador aleatorio, sin nada más. No hay publicidad, ni estadísticas, ni seguimiento de ningún tipo, ni en la app ni en este sitio.",
 "fr": "Pour utiliser Bottlegram, on ne te demande jamais ton nom, ton adresse e-mail, ton numéro de téléphone, tes contacts ni ta position. Il n'y a pas de formulaire d'inscription. La première fois que tu ouvres l'app, un compte anonyme est créé pour toi : un identifiant aléatoire, et rien d'autre. Il n'y a ni publicité, ni statistiques, ni pistage d'aucune sorte, ni dans l'app ni sur ce site.",
 "de": "Bottlegram fragt nie nach deinem Namen, deiner E-Mail-Adresse, deiner Telefonnummer, deinen Kontakten oder deinem Standort, um es zu benutzen. Es gibt kein Anmeldeformular. Wenn du die App zum ersten Mal öffnest, wird ein anonymes Konto für dich angelegt: eine zufällige Kennung, und nichts daran. Es gibt keine Werbung, keine Statistik und kein Tracking jeglicher Art, weder in der App noch auf dieser Seite.",
 "pt-BR": "O Bottlegram nunca pede seu nome, seu e-mail, seu telefone, seus contatos ou sua localização para ser usado. Não há formulário de cadastro. Na primeira vez que você abre o app, uma conta anônima é criada para você: um identificador aleatório, e nada mais. Não há publicidade, nem estatísticas, nem rastreamento de nenhum tipo, nem no app nem neste site.",
 "ja": "Bottlegram を使うために、名前、メールアドレス、電話番号、連絡先、位置情報を求めることはありません。登録フォームもありません。はじめてアプリを開くと、匿名のアカウントがひとつ作られます。ランダムな識別子だけで、ほかには何も結びついていません。広告も、アクセス解析も、どんな種類の追跡も、アプリにもこのサイトにもありません。"},

"There is exactly one place where you may choose to give a name and an email address: the “Write to us” form in the Wreck Emporium, and only so that we can write back. Both fields are optional, and the message is sent whether you fill them or not. It is stored with your anonymous account, so that a problem can be looked into on the right beach, and it never travels with your letters.": {
 "it": "C'è un solo posto dove puoi scegliere di lasciare un nome e un indirizzo email: il modulo «Scrivici» nell'Emporio del Relitto, e solo perché possiamo risponderti. Tutti e due i campi sono facoltativi, e il messaggio parte comunque, che tu li riempia o no. Viene conservato insieme al tuo account anonimo, perché un problema si possa cercare sulla spiaggia giusta, e non viaggia mai con le tue lettere.",
 "es": "Hay un solo lugar donde puedes elegir dejar un nombre y un correo: el formulario «Escríbenos» del Emporio del Naufragio, y solo para que podamos responderte. Los dos campos son opcionales, y el mensaje se envía los rellenes o no. Se guarda junto a tu cuenta anónima, para que un problema pueda buscarse en la playa correcta, y nunca viaja con tus cartas.",
 "fr": "Il existe un seul endroit où tu peux choisir de laisser un nom et une adresse e-mail : le formulaire « Écris-nous » de l'Emporium de l'Épave, et seulement pour qu'on puisse te répondre. Les deux champs sont facultatifs, et le message part que tu les remplisses ou non. Il est conservé avec ton compte anonyme, pour qu'un problème puisse être cherché sur la bonne plage, et il ne voyage jamais avec tes lettres.",
 "de": "Es gibt genau einen Ort, an dem du einen Namen und eine E-Mail-Adresse hinterlassen kannst: das Formular „Schreib uns“ im Kontor des Wracks, und nur, damit wir dir antworten können. Beide Felder sind freiwillig, und die Nachricht geht ab, ob du sie ausfüllst oder nicht. Sie wird zusammen mit deinem anonymen Konto gespeichert, damit ein Problem am richtigen Strand gesucht werden kann, und sie reist nie mit deinen Briefen.",
 "pt-BR": "Existe um único lugar onde você pode escolher deixar um nome e um e-mail: o formulário «Fale conosco» no Empório do Naufrágio, e só para que a gente possa responder. Os dois campos são opcionais, e a mensagem é enviada mesmo que você não os preencha. Ela fica guardada junto da sua conta anônima, para que um problema possa ser procurado na praia certa, e nunca viaja com as suas cartas.",
 "ja": "名前とメールアドレスを残せる場所は、ひとつだけです。難破商館の「たよりを送る」フォームで、返事を書くためだけのものです。どちらの欄も任意で、書いても書かなくてもメッセージは送られます。メッセージはあなたの匿名アカウントと一緒に保存されます。問題を正しい浜で調べるためで、あなたの手紙と一緒に旅することはありません。"},

"What the sea keeps": {
 "it": "Cosa tiene il mare",
 "es": "Lo que guarda el mar",
 "fr": "Ce que la mer garde",
 "de": "Was das Meer behält",
 "pt-BR": "O que o mar guarda",
 "ja": "海が覚えておくこと"},

"To carry letters between castaways, the sea has to remember a few things:": {
 "it": "Per portare lettere fra naufraghi, il mare deve ricordare poche cose:",
 "es": "Para llevar cartas entre náufragos, el mar tiene que recordar unas pocas cosas:",
 "fr": "Pour porter des lettres entre naufragés, la mer doit se souvenir de quelques choses :",
 "de": "Um Briefe zwischen Schiffbrüchigen zu tragen, muss sich das Meer ein paar Dinge merken:",
 "pt-BR": "Para levar cartas entre náufragos, o mar precisa lembrar algumas coisas:",
 "ja": "漂流者のあいだで手紙を運ぶために、海はいくつかのことを覚えておく必要があります。"},

"An anonymous account": {
 "it": "Un account anonimo",
 "es": "Una cuenta anónima",
 "fr": "Un compte anonyme",
 "de": "Ein anonymes Konto",
 "pt-BR": "Uma conta anônima",
 "ja": "匿名のアカウント"},

": a random identifier created on your first launch. It is not linked to your name, email, or any identity, because none was ever asked.": {
 "it": ": un identificativo casuale creato al primo avvio. Non è legato al tuo nome, alla tua email o a qualunque identità, perché nessuna è mai stata chiesta.",
 "es": ": un identificador aleatorio creado la primera vez que abres la app. No está ligado a tu nombre, a tu correo ni a ninguna identidad, porque nunca se pidió ninguna.",
 "fr": " : un identifiant aléatoire créé au premier lancement. Il n'est lié ni à ton nom, ni à ton e-mail, ni à aucune identité, puisqu'aucune n'a jamais été demandée.",
 "de": ": eine zufällige Kennung, beim ersten Start erzeugt. Sie ist nicht mit deinem Namen, deiner E-Mail oder irgendeiner Identität verbunden, denn danach wurde nie gefragt.",
 "pt-BR": ": um identificador aleatório criado na primeira vez que você abre o app. Ele não está ligado ao seu nome, ao seu e-mail nem a nenhuma identidade, porque nenhuma foi pedida.",
 "ja": "：最初の起動時に作られるランダムな識別子です。名前やメールアドレス、どんな身元とも結びついていません。そもそも尋ねていないからです。"},

"Your beach and your language": {
 "it": "La tua spiaggia e la tua lingua",
 "es": "Tu playa y tu idioma",
 "fr": "Ta plage et ta langue",
 "de": "Dein Strand und deine Sprache",
 "pt-BR": "Sua praia e seu idioma",
 "ja": "あなたの浜と言語"},

": the stretch of coast you were cast on, and the language you write in, so the tide can favour letters you will understand.": {
 "it": ": il tratto di costa su cui sei naufragato, e la lingua in cui scrivi, perché la marea possa preferire lettere che capirai.",
 "es": ": el trozo de costa donde naufragaste y el idioma en que escribes, para que la marea pueda preferir cartas que entiendas.",
 "fr": " : le bout de côte où tu as échoué, et la langue dans laquelle tu écris, pour que la marée puisse préférer des lettres que tu comprendras.",
 "de": ": das Stück Küste, an dem du gestrandet bist, und die Sprache, in der du schreibst, damit die Flut Briefe bevorzugen kann, die du verstehst.",
 "pt-BR": ": o trecho de costa onde você naufragou e o idioma em que escreve, para que a maré possa preferir cartas que você vai entender.",
 "ja": "：あなたが流れ着いた海岸と、あなたが書く言語です。潮が、あなたに読める手紙を選べるようにするためです。"},

"Your letters": {
 "it": "Le tue lettere",
 "es": "Tus cartas",
 "fr": "Tes lettres",
 "de": "Deine Briefe",
 "pt-BR": "Suas cartas",
 "ja": "あなたの手紙"},

": what you write and what you receive, with the times of throwing, landfall and reading, and the translations you asked for. Letters are the app; without them there is nothing to deliver.": {
 "it": ": quello che scrivi e quello che ricevi, con gli orari del lancio, dell'approdo e della lettura, e le traduzioni che hai chiesto. Le lettere sono l'app; senza di loro non c'è niente da consegnare.",
 "es": ": lo que escribes y lo que recibes, con las horas del lanzamiento, de la llegada y de la lectura, y las traducciones que pediste. Las cartas son la app; sin ellas no hay nada que entregar.",
 "fr": " : ce que tu écris et ce que tu reçois, avec les heures du lancer, de l'arrivée et de la lecture, et les traductions que tu as demandées. Les lettres sont l'app ; sans elles, il n'y a rien à livrer.",
 "de": ": was du schreibst und was du bekommst, mit den Zeiten von Wurf, Landung und Lesen, und den Übersetzungen, um die du gebeten hast. Die Briefe sind die App; ohne sie gibt es nichts zuzustellen.",
 "pt-BR": ": o que você escreve e o que recebe, com os horários do lançamento, da chegada e da leitura, e as traduções que você pediu. As cartas são o app; sem elas não há nada para entregar.",
 "ja": "：あなたが書いたものと受け取ったもの、投げた時刻、流れ着いた時刻、読んだ時刻、そして頼んだ翻訳です。手紙こそがアプリで、手紙がなければ届けるものがありません。"},

"The rules you accepted": {
 "it": "Le regole che hai accettato",
 "es": "Las reglas que aceptaste",
 "fr": "Les règles que tu as acceptées",
 "de": "Die Regeln, denen du zugestimmt hast",
 "pt-BR": "As regras que você aceitou",
 "ja": "同意した掟"},

": which version of the rules of the sea you agreed to, and when.": {
 "it": ": quale versione delle regole del mare hai accettato, e quando.",
 "es": ": qué versión de las reglas del mar aceptaste, y cuándo.",
 "fr": " : quelle version des règles de la mer tu as acceptée, et quand.",
 "de": ": welcher Fassung der Regeln des Meeres du zugestimmt hast, und wann.",
 "pt-BR": ": qual versão das regras do mar você aceitou, e quando.",
 "ja": "：どの版の「海の掟」に、いつ同意したか。"},

"Reports and blocks": {
 "it": "Segnalazioni e blocchi",
 "es": "Denuncias y bloqueos",
 "fr": "Signalements et blocages",
 "de": "Meldungen und Blockierungen",
 "pt-BR": "Denúncias e bloqueios",
 "ja": "報告とブロック"},

": if you report a letter to the Sea or block a correspondent, that is remembered, so the tide never brings you together again.": {
 "it": ": se segnali una lettera al Mare o blocchi chi ti scrive, il mare se lo ricorda, perché la marea non vi faccia mai più incontrare.",
 "es": ": si denuncias una carta al Mar o bloqueas a quien te escribe, el mar lo recuerda, para que la marea no vuelva a juntaros nunca.",
 "fr": " : si tu signales une lettre à la Mer ou bloques quelqu'un qui t'écrit, la mer s'en souvient, pour que la marée ne vous réunisse plus jamais.",
 "de": ": Wenn du einen Brief dem Meer meldest oder jemanden blockierst, merkt sich das Meer das, damit die Flut euch nie wieder zusammenführt.",
 "pt-BR": ": se você denuncia uma carta ao Mar ou bloqueia quem escreve, o mar se lembra, para que a maré nunca mais junte vocês.",
 "ja": "：手紙を海に報告したり、相手をブロックしたりすると、海はそれを覚えておきます。潮が二度とふたりを引き合わせないようにするためです。"},

"What you own": {
 "it": "Quello che possiedi",
 "es": "Lo que tienes",
 "fr": "Ce que tu possèdes",
 "de": "Was dir gehört",
 "pt-BR": "O que você tem",
 "ja": "あなたの持ち物"},

": whether you have bought the sextant, the bonfire, the seal you press on your letters, or the other things in the Wreck Emporium. We never see your payment details, only that the purchase happened.": {
 "it": ": se hai comprato il sestante, il falò, il sigillo che imprimi sulle lettere, o le altre cose dell'Emporio del Relitto. Non vediamo mai i tuoi dati di pagamento, solo che l'acquisto è avvenuto.",
 "es": ": si has comprado el sextante, la hoguera, el sello que imprimes en tus cartas u otras cosas del Emporio del Naufragio. Nunca vemos tus datos de pago, solo que la compra se hizo.",
 "fr": " : si tu as acheté le sextant, le feu de camp, le sceau que tu presses sur tes lettres, ou les autres choses de l'Emporium de l'Épave. Nous ne voyons jamais tes données de paiement, seulement que l'achat a eu lieu.",
 "de": ": ob du den Sextanten, das Lagerfeuer, das Siegel für deine Briefe oder die anderen Dinge aus dem Kontor des Wracks gekauft hast. Deine Zahlungsdaten sehen wir nie, nur, dass der Kauf stattgefunden hat.",
 "pt-BR": ": se você comprou o sextante, a fogueira, o selo que imprime nas cartas ou as outras coisas do Empório do Naufrágio. Nunca vemos seus dados de pagamento, só que a compra aconteceu.",
 "ja": "：六分儀、焚き火、手紙に押す封蝋、そのほか難破商館の品を買ったかどうか。支払いの情報を見ることはなく、購入があったことだけを知ります。"},

"What you write to us": {
 "it": "Quello che ci scrivi",
 "es": "Lo que nos escribes",
 "fr": "Ce que tu nous écris",
 "de": "Was du uns schreibst",
 "pt-BR": "O que você nos escreve",
 "ja": "あなたからのたより"},

": if you use the “Write to us” form, we keep your message, the app version and the language it was written in, plus the name and email address you chose to leave, if you left any. It is kept so a bug can be chased and a question answered, and it is the only place in Bottlegram where an email address exists at all.": {
 "it": ": se usi il modulo «Scrivici», teniamo il tuo messaggio, la versione dell'app e la lingua in cui è scritto, più il nome e l'indirizzo email che hai scelto di lasciare, se ne hai lasciati. Lo teniamo per inseguire un errore e rispondere a una domanda, ed è l'unico posto di Bottlegram dove esista un indirizzo email.",
 "es": ": si usas el formulario «Escríbenos», guardamos tu mensaje, la versión de la app y el idioma en que está escrito, además del nombre y el correo que hayas elegido dejar, si dejaste alguno. Lo guardamos para perseguir un error y responder una pregunta, y es el único lugar de Bottlegram donde existe un correo.",
 "fr": " : si tu utilises le formulaire « Écris-nous », nous gardons ton message, la version de l'app et la langue dans laquelle il est écrit, plus le nom et l'adresse e-mail que tu as choisi de laisser, si tu en as laissé. Nous le gardons pour traquer un bug et répondre à une question, et c'est le seul endroit de Bottlegram où une adresse e-mail existe.",
 "de": ": Wenn du das Formular „Schreib uns“ benutzt, behalten wir deine Nachricht, die App-Version und die Sprache, in der sie geschrieben ist, dazu den Namen und die E-Mail-Adresse, die du hinterlassen hast, falls überhaupt. Wir behalten sie, um einem Fehler nachzugehen und eine Frage zu beantworten, und es ist der einzige Ort in Bottlegram, an dem es eine E-Mail-Adresse gibt.",
 "pt-BR": ": se você usa o formulário «Fale conosco», guardamos sua mensagem, a versão do app e o idioma em que ela foi escrita, mais o nome e o e-mail que você escolheu deixar, se deixou. Guardamos para correr atrás de um erro e responder a uma pergunta, e é o único lugar do Bottlegram onde existe um e-mail.",
 "ja": "：「たよりを送る」フォームを使うと、メッセージ、アプリのバージョン、書かれた言語、そして残してくれた場合は名前とメールアドレスを保存します。不具合を追い、質問に答えるためで、Bottlegram のなかでメールアドレスが存在する場所はここだけです。"},

"The nicknames you give a correspondent stay on your device. They are your private marginalia; the sea never sees them.": {
 "it": "I soprannomi che dai a chi ti scrive restano sul tuo telefono. Sono le tue note a margine; il mare non le vede mai.",
 "es": "Los apodos que das a quien te escribe se quedan en tu teléfono. Son tus notas al margen; el mar nunca las ve.",
 "fr": "Les surnoms que tu donnes à qui t'écrit restent sur ton téléphone. Ce sont tes notes dans la marge ; la mer ne les voit jamais.",
 "de": "Die Spitznamen, die du deinen Briefpartnern gibst, bleiben auf deinem Telefon. Sie sind deine Randnotizen; das Meer sieht sie nie.",
 "pt-BR": "Os apelidos que você dá a quem escreve ficam no seu telefone. São suas anotações na margem; o mar nunca as vê.",
 "ja": "文通相手につけたあだ名は、あなたの電話の中に残ります。あなただけの余白の書き込みで、海が目にすることはありません。"},

"Your own wax seal and your ship are different, and it is worth being plain about them: the emblem, the colour and the ship you choose in the Emporium are kept by the sea and travel on the letters you send, because their whole purpose is that other castaways can recognise you across messages. Everyone who reads a letter of yours sees them. They say nothing about who you are, since they are drawings, but they are not private.": {
 "it": "Il tuo sigillo di ceralacca e la tua nave sono un'altra cosa, ed è giusto dirlo chiaro: l'emblema, il colore e la nave che scegli nell'Emporio li tiene il mare e viaggiano sulle lettere che mandi, perché servono proprio a farti riconoscere dagli altri naufraghi da una lettera all'altra. Chiunque legga una tua lettera li vede. Non dicono niente di chi sei, sono disegni, ma non sono privati.",
 "es": "Tu sello de lacre y tu barco son otra cosa, y conviene decirlo claro: el emblema, el color y el barco que eliges en el Emporio los guarda el mar y viajan en las cartas que envías, porque sirven justamente para que otros náufragos te reconozcan de una carta a otra. Quien lea una carta tuya los ve. No dicen nada de quién eres, son dibujos, pero no son privados.",
 "fr": "Ton sceau de cire et ton navire, c'est autre chose, et autant le dire clairement : l'emblème, la couleur et le navire que tu choisis dans l'Emporium sont gardés par la mer et voyagent sur les lettres que tu envoies, car ils servent justement à ce que les autres naufragés te reconnaissent d'une lettre à l'autre. Quiconque lit une de tes lettres les voit. Ils ne disent rien de qui tu es, ce sont des dessins, mais ils ne sont pas privés.",
 "de": "Dein Wachssiegel und dein Schiff sind etwas anderes, und das soll klar gesagt sein: Das Emblem, die Farbe und das Schiff, die du im Kontor wählst, behält das Meer, und sie reisen auf den Briefen, die du schickst, denn genau dafür sind sie da: damit andere Schiffbrüchige dich von Brief zu Brief wiedererkennen. Wer einen Brief von dir liest, sieht sie. Sie sagen nichts darüber, wer du bist, es sind Zeichnungen, aber privat sind sie nicht.",
 "pt-BR": "Seu selo de lacre e seu navio são outra coisa, e vale dizer com clareza: o emblema, a cor e o navio que você escolhe no Empório ficam com o mar e viajam nas cartas que você envia, porque servem justamente para que outros náufragos reconheçam você de uma carta para outra. Quem lê uma carta sua os vê. Eles não dizem nada sobre quem você é, são desenhos, mas não são privados.",
 "ja": "あなたの封蝋と船は別です。はっきり書いておきます。商館で選んだ紋章、色、船は海が保存し、あなたが送る手紙と一緒に旅します。ほかの漂流者が、手紙から手紙へとあなたを見分けられるようにするためのものだからです。あなたの手紙を読む人は、それを目にします。絵なので、あなたが誰かは何も語りませんが、非公開ではありません。"},

"What the sea never asks": {
 "it": "Cosa il mare non chiede mai",
 "es": "Lo que el mar nunca pregunta",
 "fr": "Ce que la mer ne demande jamais",
 "de": "Was das Meer nie fragt",
 "pt-BR": "O que o mar nunca pergunta",
 "ja": "海が決して尋ねないこと"},

"Your location is never read. The app asks your date of birth once, before it lets you in, keeps only the answer on your phone and forgets the date. Notifications are scheduled locally on your device by the app itself; there is no push server watching you.": {
 "it": "La tua posizione non viene mai letta. L'app ti chiede la data di nascita una volta sola, prima di farti entrare, tiene sul telefono solo la risposta e dimentica la data. Le notifiche le programma l'app stessa sul tuo telefono; non c'è un server di notifiche che ti osserva.",
 "es": "Tu ubicación nunca se lee. La app te pide la fecha de nacimiento una sola vez, antes de dejarte entrar, guarda en el teléfono solo la respuesta y olvida la fecha. Las notificaciones las programa la propia app en tu teléfono; no hay un servidor de notificaciones vigilándote.",
 "fr": "Ta position n'est jamais lue. L'app te demande ta date de naissance une seule fois, avant de te laisser entrer, garde sur ton téléphone la réponse seulement et oublie la date. Les notifications sont programmées par l'app elle-même sur ton téléphone ; aucun serveur de notifications ne te surveille.",
 "de": "Dein Standort wird nie gelesen. Die App fragt einmal nach deinem Geburtsdatum, bevor sie dich hineinlässt, behält auf deinem Telefon nur die Antwort und vergisst das Datum. Mitteilungen plant die App selbst auf deinem Gerät; es gibt keinen Push-Server, der dich beobachtet.",
 "pt-BR": "Sua localização nunca é lida. O app pede sua data de nascimento uma única vez, antes de deixar você entrar, guarda no telefone só a resposta e esquece a data. As notificações são programadas pelo próprio app no seu telefone; não há um servidor de notificações observando você.",
 "ja": "位置情報を読むことはありません。アプリは中に入る前に一度だけ生年月日を尋ね、答えだけを電話に残して、日付は忘れます。通知はアプリ自身があなたの端末の中で予定するもので、あなたを見張るプッシュサーバーはありません。"},

"Who else touches a letter": {
 "it": "Chi altro tocca una lettera",
 "es": "Quién más toca una carta",
 "fr": "Qui d'autre touche une lettre",
 "de": "Wer sonst einen Brief berührt",
 "pt-BR": "Quem mais toca uma carta",
 "ja": "手紙に触れる、ほかの誰か"},

"A few services do narrow work under our instruction, and each sees only what its work requires:": {
 "it": "Alcuni servizi fanno un lavoro preciso su nostra istruzione, e ognuno vede solo quello che il suo lavoro richiede:",
 "es": "Algunos servicios hacen un trabajo concreto siguiendo nuestras instrucciones, y cada uno ve solo lo que su trabajo requiere:",
 "fr": "Quelques services font un travail précis sur nos instructions, et chacun ne voit que ce que son travail exige :",
 "de": "Ein paar Dienste erledigen in unserem Auftrag eine eng umrissene Arbeit, und jeder sieht nur, was diese Arbeit braucht:",
 "pt-BR": "Alguns serviços fazem um trabalho específico sob nossa instrução, e cada um vê só o que esse trabalho exige:",
 "ja": "いくつかのサービスが、私たちの指示のもとで限られた仕事をしています。どれも、その仕事に必要なものだけを目にします。"},

"hosts the sea: the database where accounts and letters live, in Frankfurt, in the European Union.": {
 "it": "ospita il mare: il database dove vivono gli account e le lettere, a Francoforte, nell'Unione europea.",
 "es": "aloja el mar: la base de datos donde viven las cuentas y las cartas, en Fráncfort, en la Unión Europea.",
 "fr": "héberge la mer : la base de données où vivent les comptes et les lettres, à Francfort, dans l'Union européenne.",
 "de": "beherbergt das Meer: die Datenbank, in der Konten und Briefe liegen, in Frankfurt, in der Europäischen Union.",
 "pt-BR": "hospeda o mar: o banco de dados onde ficam as contas e as cartas, em Frankfurt, na União Europeia.",
 "ja": "は海そのものを預かっています。アカウントと手紙が置かれたデータベースで、場所は欧州連合のフランクフルトです。"},

"checks the text of each letter before it sails, so the sea keeps to its rules. It sees only the text.": {
 "it": "controlla il testo di ogni lettera prima che salpi, perché il mare rispetti le sue regole. Vede solo il testo.",
 "es": "revisa el texto de cada carta antes de que zarpe, para que el mar cumpla sus reglas. Solo ve el texto.",
 "fr": "vérifie le texte de chaque lettre avant qu'elle prenne la mer, pour que la mer respecte ses règles. Il ne voit que le texte.",
 "de": "prüft den Text jedes Briefes, bevor er in See sticht, damit sich das Meer an seine Regeln hält. Es sieht nur den Text.",
 "pt-BR": "confere o texto de cada carta antes de ela zarpar, para que o mar cumpra suas regras. Vê só o texto.",
 "ja": "は、手紙が海へ出る前に一通ずつ本文を確かめ、海が掟を守れるようにしています。目にするのは本文だけです。"},

"translates a letter when you ask it to, and sees that letter's text to do so.": {
 "it": "traduce una lettera quando glielo chiedi, e per farlo ne vede il testo.",
 "es": "traduce una carta cuando se lo pides, y para hacerlo ve su texto.",
 "fr": "traduit une lettre quand tu le demandes, et en voit le texte pour le faire.",
 "de": "übersetzt einen Brief, wenn du darum bittest, und sieht dafür seinen Text.",
 "pt-BR": "traduz uma carta quando você pede, e para isso vê o texto dela.",
 "ja": "は、あなたが頼んだときに手紙を翻訳し、そのために本文を目にします。"},

"processes the text of your letters when you correspond with a spirit of the sea. It sees the letters of that correspondence and the language you write in.": {
 "it": "elabora il testo delle tue lettere quando sei in corrispondenza con uno spirito del mare. Vede le lettere di quel carteggio e la lingua in cui scrivi.",
 "es": "procesa el texto de tus cartas cuando te escribes con un espíritu del mar. Ve las cartas de esa correspondencia y el idioma en que escribes.",
 "fr": "traite le texte de tes lettres quand tu corresponds avec un esprit de la mer. Il voit les lettres de cette correspondance et la langue dans laquelle tu écris.",
 "de": "verarbeitet den Text deiner Briefe, wenn du mit einem Geist des Meeres schreibst. Es sieht die Briefe dieses Briefwechsels und die Sprache, in der du schreibst.",
 "pt-BR": "processa o texto das suas cartas quando você se corresponde com um espírito do mar. Vê as cartas dessa correspondência e o idioma em que você escreve.",
 "ja": "は、あなたが海の精と文通しているとき、あなたの手紙の本文を処理します。目にするのはその文通の手紙と、あなたが書く言語です。"},

"handles every purchase on iPhone, and": {
 "it": "gestisce ogni acquisto su iPhone, e",
 "es": "gestiona cada compra en iPhone, y",
 "fr": "gère chaque achat sur iPhone, et",
 "de": "wickelt jeden Kauf auf dem iPhone ab, und",
 "pt-BR": "cuida de cada compra no iPhone, e",
 "ja": "が iPhone での購入をすべて扱い、"},

"every purchase on Android. Payment happens entirely on their side.": {
 "it": "ogni acquisto su Android. Il pagamento avviene tutto dalla loro parte.",
 "es": "cada compra en Android. El pago ocurre por completo de su lado.",
 "fr": "chaque achat sur Android. Le paiement se fait entièrement de leur côté.",
 "de": "jeden Kauf auf Android. Die Zahlung geschieht vollständig auf ihrer Seite.",
 "pt-BR": "cada compra no Android. O pagamento acontece inteiramente do lado deles.",
 "ja": "が Android での購入をすべて扱います。支払いはすべて、それぞれの側で行われます。"},

"delivers the messages sent from the “Write to us” form to our mailbox, and sees what that message contains, including the name and address you chose to leave. It also tells our moderator that a report is waiting: a count and a link, never the letter. It never touches your letters.": {
 "it": "consegna alla nostra casella i messaggi mandati con il modulo «Scrivici», e vede quello che contengono, compresi il nome e l'indirizzo che hai scelto di lasciare. Avvisa anche il nostro moderatore che c'è una segnalazione in attesa: un numero e un link, mai la lettera. Non tocca mai le tue lettere.",
 "es": "entrega en nuestro buzón los mensajes enviados con el formulario «Escríbenos», y ve lo que contienen, incluidos el nombre y la dirección que elegiste dejar. También avisa a nuestro moderador de que hay una denuncia pendiente: un número y un enlace, nunca la carta. Nunca toca tus cartas.",
 "fr": "livre dans notre boîte les messages envoyés avec le formulaire « Écris-nous », et voit ce qu'ils contiennent, y compris le nom et l'adresse que tu as choisi de laisser. Il prévient aussi notre modérateur qu'un signalement attend : un nombre et un lien, jamais la lettre. Il ne touche jamais tes lettres.",
 "de": "stellt die Nachrichten aus dem Formular „Schreib uns“ in unser Postfach zu und sieht, was darin steht, auch den Namen und die Adresse, die du hinterlassen hast. Es sagt außerdem unserem Moderator, dass eine Meldung wartet: eine Zahl und ein Link, nie der Brief. Deine Briefe berührt es nie.",
 "pt-BR": "entrega na nossa caixa de correio as mensagens enviadas pelo formulário «Fale conosco», e vê o que elas contêm, inclusive o nome e o endereço que você escolheu deixar. Também avisa nosso moderador que há uma denúncia esperando: um número e um link, nunca a carta. Nunca toca nas suas cartas.",
 "ja": "は、「たよりを送る」フォームのメッセージを私たちのメールボックスに届け、その中身を目にします。あなたが残した名前とアドレスも含みます。報告が待っていることを管理人に知らせもしますが、伝えるのは件数とリンクだけで、手紙は送りません。あなたの手紙に触れることはありません。"},

"One more pair of eyes, and it is human: when a letter is reported, a person reads it, that letter and that correspondence, nothing else, to decide whether the sea keeps its writer. This happens within a day of the report.": {
 "it": "C'è un altro paio d'occhi, ed è umano: quando una lettera viene segnalata, una persona la legge, quella lettera e quel carteggio e nient'altro, per decidere se il mare tiene chi l'ha scritta. Succede entro un giorno dalla segnalazione.",
 "es": "Hay un par de ojos más, y es humano: cuando una carta se denuncia, una persona la lee, esa carta y esa correspondencia y nada más, para decidir si el mar se queda con quien la escribió. Ocurre en el plazo de un día desde la denuncia.",
 "fr": "Il y a une autre paire d'yeux, et elle est humaine : quand une lettre est signalée, une personne la lit, cette lettre et cette correspondance, rien d'autre, pour décider si la mer garde celui qui l'a écrite. Cela se fait dans la journée qui suit le signalement.",
 "de": "Es gibt noch ein Paar Augen, und es ist menschlich: Wird ein Brief gemeldet, liest ein Mensch ihn, diesen Brief und diesen Briefwechsel, sonst nichts, um zu entscheiden, ob das Meer seinen Verfasser behält. Das geschieht innerhalb eines Tages nach der Meldung.",
 "pt-BR": "Há mais um par de olhos, e ele é humano: quando uma carta é denunciada, uma pessoa a lê, aquela carta e aquela correspondência, nada mais, para decidir se o mar fica com quem a escreveu. Isso acontece em até um dia depois da denúncia.",
 "ja": "もうひとつ、人の目があります。手紙が報告されると、ひとりの人がそれを読みます。その手紙とその文通だけを読み、書いた人を海に残すかどうかを決めます。報告から一日以内に行われます。"},

"Where it travels": {
 "it": "Dove viaggia",
 "es": "Adónde viaja",
 "fr": "Où elle voyage",
 "de": "Wohin es reist",
 "pt-BR": "Para onde viaja",
 "ja": "どこへ渡るのか"},

"The sea itself lives in the European Union. OpenAI, Google, Anthropic and Resend are based in the United States, so the text they handle crosses the ocean. Each of those transfers rests on the European Commission's Standard Contractual Clauses, or on the EU–US Data Privacy Framework where the company is certified under it. Apple and Google Play handle purchases under their own privacy policies.": {
 "it": "Il mare vive nell'Unione europea. OpenAI, Google, Anthropic e Resend hanno sede negli Stati Uniti, quindi il testo che trattano attraversa l'oceano. Ognuno di questi trasferimenti si fonda sulle Clausole contrattuali tipo della Commissione europea, o sul Data Privacy Framework UE–USA quando l'azienda vi è certificata. Apple e Google Play gestiscono gli acquisti secondo le loro informative.",
 "es": "El mar vive en la Unión Europea. OpenAI, Google, Anthropic y Resend tienen su sede en Estados Unidos, así que el texto que tratan cruza el océano. Cada una de esas transferencias se basa en las Cláusulas Contractuales Tipo de la Comisión Europea, o en el Marco de Privacidad de Datos UE–EE. UU. cuando la empresa está certificada en él. Apple y Google Play gestionan las compras según sus propias políticas de privacidad.",
 "fr": "La mer vit dans l'Union européenne. OpenAI, Google, Anthropic et Resend sont établis aux États-Unis, donc le texte qu'ils traitent traverse l'océan. Chacun de ces transferts repose sur les clauses contractuelles types de la Commission européenne, ou sur le cadre de protection des données UE–États-Unis lorsque l'entreprise y est certifiée. Apple et Google Play gèrent les achats selon leurs propres politiques de confidentialité.",
 "de": "Das Meer selbst liegt in der Europäischen Union. OpenAI, Google, Anthropic und Resend sitzen in den Vereinigten Staaten, also überquert der Text, den sie bearbeiten, den Ozean. Jede dieser Übermittlungen stützt sich auf die Standardvertragsklauseln der Europäischen Kommission oder auf den EU-US-Datenschutzrahmen, wenn das Unternehmen danach zertifiziert ist. Apple und Google Play wickeln Käufe nach ihren eigenen Datenschutzerklärungen ab.",
 "pt-BR": "O mar vive na União Europeia. OpenAI, Google, Anthropic e Resend têm sede nos Estados Unidos, então o texto que eles tratam atravessa o oceano. Cada uma dessas transferências se apoia nas Cláusulas Contratuais Padrão da Comissão Europeia, ou no Quadro de Privacidade de Dados UE–EUA quando a empresa é certificada nele. Apple e Google Play cuidam das compras segundo suas próprias políticas de privacidade.",
 "ja": "海そのものは欧州連合にあります。OpenAI、Google、Anthropic、Resend は米国の企業なので、これらが扱う本文は海を渡ります。こうした移転はいずれも、欧州委員会の標準契約条項、または企業が認証を受けている場合は EU・米国データ・プライバシー・フレームワークに基づいています。Apple と Google Play は、それぞれのプライバシーポリシーに従って購入を扱います。"},

"Why we may": {
 "it": "Perché possiamo",
 "es": "Por qué podemos",
 "fr": "Pourquoi nous le pouvons",
 "de": "Warum wir das dürfen",
 "pt-BR": "Por que podemos",
 "ja": "なぜ扱えるのか"},

"Carrying your letters, keeping your beach and translating a letter when you ask are what you agreed to when you began; that agreement is the legal basis (Article 6(1)(b) of the GDPR). Screening letters, handling reports and keeping a banished account from coming back rest on our legitimate interest, and yours, in a sea that is safe to write on (Article 6(1)(f)). So does answering what you write to us. Where the law requires us to keep something or hand it over, we do (Article 6(1)(c)).": {
 "it": "Portare le tue lettere, tenere la tua spiaggia e tradurre una lettera quando lo chiedi sono ciò che hai accettato cominciando; quell'accordo è la base giuridica (articolo 6, paragrafo 1, lettera b del GDPR). Vagliare le lettere, gestire le segnalazioni e impedire a un account bandito di tornare si fondano sul nostro legittimo interesse, e sul tuo, a un mare dove si possa scrivere tranquilli (articolo 6, paragrafo 1, lettera f). Così anche rispondere a quello che ci scrivi. Quando la legge ci obbliga a conservare qualcosa o a consegnarlo, lo facciamo (articolo 6, paragrafo 1, lettera c).",
 "es": "Llevar tus cartas, mantener tu playa y traducir una carta cuando lo pides es lo que aceptaste al empezar; ese acuerdo es la base jurídica (artículo 6.1.b del RGPD). Revisar las cartas, gestionar las denuncias e impedir que una cuenta desterrada vuelva se basan en nuestro interés legítimo, y en el tuyo, en un mar donde se pueda escribir con tranquilidad (artículo 6.1.f). También responder a lo que nos escribes. Cuando la ley nos obliga a conservar algo o a entregarlo, lo hacemos (artículo 6.1.c).",
 "fr": "Porter tes lettres, garder ta plage et traduire une lettre quand tu le demandes, c'est ce que tu as accepté en commençant ; cet accord est la base légale (article 6, paragraphe 1, point b du RGPD). Vérifier les lettres, traiter les signalements et empêcher un compte banni de revenir reposent sur notre intérêt légitime, et le tien, à une mer où l'on peut écrire en paix (article 6, paragraphe 1, point f). Répondre à ce que tu nous écris aussi. Quand la loi nous oblige à conserver ou à transmettre quelque chose, nous le faisons (article 6, paragraphe 1, point c).",
 "de": "Deine Briefe zu tragen, deinen Strand zu halten und einen Brief zu übersetzen, wenn du darum bittest, ist das, dem du zu Beginn zugestimmt hast; diese Vereinbarung ist die Rechtsgrundlage (Art. 6 Abs. 1 lit. b DSGVO). Briefe zu prüfen, Meldungen zu bearbeiten und ein verbanntes Konto an der Rückkehr zu hindern, beruht auf unserem berechtigten Interesse, und deinem, an einem Meer, auf dem man in Ruhe schreiben kann (Art. 6 Abs. 1 lit. f). Ebenso, auf das zu antworten, was du uns schreibst. Wenn das Gesetz uns verpflichtet, etwas aufzubewahren oder herauszugeben, tun wir es (Art. 6 Abs. 1 lit. c).",
 "pt-BR": "Levar suas cartas, manter sua praia e traduzir uma carta quando você pede é o que você aceitou ao começar; esse acordo é a base legal (artigo 6.º, n.º 1, alínea b do RGPD). Conferir as cartas, cuidar das denúncias e impedir que uma conta banida volte se baseiam no nosso interesse legítimo, e no seu, por um mar onde se possa escrever em paz (artigo 6.º, n.º 1, alínea f). Responder ao que você nos escreve também. Quando a lei nos obriga a guardar algo ou entregá-lo, nós o fazemos (artigo 6.º, n.º 1, alínea c).",
 "ja": "手紙を運ぶこと、あなたの浜を保つこと、頼まれたときに手紙を翻訳することは、あなたが始めるときに同意したことで、その合意が法的根拠です（GDPR 第6条第1項(b)）。手紙の確認、報告の処理、追放されたアカウントを戻らせないことは、安心して書ける海であってほしいという、私たちとあなたの正当な利益に基づきます（同(f)）。あなたからのたよりに答えることも同じです。法律が何かの保管や提出を求めるときは、それに従います（同(c)）。"},

"How long": {
 "it": "Per quanto tempo",
 "es": "Cuánto tiempo",
 "fr": "Combien de temps",
 "de": "Wie lange",
 "pt-BR": "Por quanto tempo",
 "ja": "どれくらいのあいだ"},

"Your account, your beach, your letters and their translations": {
 "it": "Il tuo account, la tua spiaggia, le tue lettere e le loro traduzioni",
 "es": "Tu cuenta, tu playa, tus cartas y sus traducciones",
 "fr": "Ton compte, ta plage, tes lettres et leurs traductions",
 "de": "Dein Konto, dein Strand, deine Briefe und ihre Übersetzungen",
 "pt-BR": "Sua conta, sua praia, suas cartas e as traduções delas",
 "ja": "アカウント、浜、手紙とその翻訳"},

": until you leave the sea.": {
 "it": ": finché non abbandoni il mare.",
 "es": ": hasta que abandones el mar.",
 "fr": " : jusqu'à ce que tu quittes la mer.",
 "de": ": bis du das Meer verlässt.",
 "pt-BR": ": até você abandonar o mar.",
 "ja": "：あなたが海を去るまで。"},

"A report and the copy of the reported letter": {
 "it": "Una segnalazione e la copia della lettera segnalata",
 "es": "Una denuncia y la copia de la carta denunciada",
 "fr": "Un signalement et la copie de la lettre signalée",
 "de": "Eine Meldung und die Kopie des gemeldeten Briefes",
 "pt-BR": "Uma denúncia e a cópia da carta denunciada",
 "ja": "報告と、報告された手紙の写し"},

": until the writer of that letter leaves the sea.": {
 "it": ": finché chi ha scritto quella lettera non abbandona il mare.",
 "es": ": hasta que quien escribió esa carta abandone el mar.",
 "fr": " : jusqu'à ce que l'auteur de cette lettre quitte la mer.",
 "de": ": bis der Verfasser dieses Briefes das Meer verlässt.",
 "pt-BR": ": até quem escreveu essa carta abandonar o mar.",
 "ja": "：その手紙を書いた人が海を去るまで。"},

"A banished account that leaves": {
 "it": "Un account bandito che se ne va",
 "es": "Una cuenta desterrada que se va",
 "fr": "Un compte banni qui s'en va",
 "de": "Ein verbanntes Konto, das geht",
 "pt-BR": "Uma conta banida que vai embora",
 "ja": "追放されたアカウントが去るとき"},

": one random identifier, for as long as the ban stands, so that leaving does not undo it.": {
 "it": ": un identificativo casuale, finché il bando resta, perché andarsene non lo annulli.",
 "es": ": un identificador aleatorio, mientras dure el destierro, para que irse no lo anule.",
 "fr": " : un identifiant aléatoire, tant que le bannissement tient, pour que partir ne l'annule pas.",
 "de": ": eine zufällige Kennung, solange die Verbannung gilt, damit Gehen sie nicht aufhebt.",
 "pt-BR": ": um identificador aleatório, enquanto o banimento durar, para que ir embora não o anule.",
 "ja": "：ランダムな識別子ひとつを、追放が続くあいだ。去ることで追放が消えないようにするためです。"},

": until you ask us to delete it, together with the copy in our mailbox.": {
 "it": ": finché non ci chiedi di cancellarlo, insieme alla copia nella nostra casella.",
 "es": ": hasta que nos pidas borrarlo, junto con la copia de nuestro buzón.",
 "fr": " : jusqu'à ce que tu nous demandes de l'effacer, avec la copie dans notre boîte.",
 "de": ": bis du uns bittest, es zu löschen, zusammen mit der Kopie in unserem Postfach.",
 "pt-BR": ": até você pedir que a gente apague, junto com a cópia na nossa caixa de correio.",
 "ja": "：削除を頼まれるまで。私たちのメールボックスにある写しも一緒です。"},

"Backups of the database": {
 "it": "Le copie di sicurezza del database",
 "es": "Las copias de seguridad de la base de datos",
 "fr": "Les sauvegardes de la base de données",
 "de": "Sicherungskopien der Datenbank",
 "pt-BR": "Os backups do banco de dados",
 "ja": "データベースのバックアップ"},

": up to seven days, then they are overwritten.": {
 "it": ": fino a sette giorni, poi vengono sovrascritte.",
 "es": ": hasta siete días, después se sobrescriben.",
 "fr": " : jusqu'à sept jours, puis elles sont écrasées.",
 "de": ": bis zu sieben Tage, dann werden sie überschrieben.",
 "pt-BR": ": até sete dias, depois são sobrescritos.",
 "ja": "：最長7日間。その後は上書きされます。"},

"Leaving the sea": {
 "it": "Abbandonare il mare",
 "es": "Abandonar el mar",
 "fr": "Quitter la mer",
 "de": "Das Meer verlassen",
 "pt-BR": "Abandonar o mar",
 "ja": "海を去る"},

"You can delete your account from inside the app, in the Wreck Emporium. It is immediate: your account, your letters, your correspondences, your blocks and what you wrote to us leave the sea, including your letters on the sands of those who received them. Reports you made about someone else's letter stay, with nothing that links them to you. A new launch of the app is a new castaway.": {
 "it": "Puoi cancellare il tuo account dall'app, nell'Emporio del Relitto. È immediato: il tuo account, le tue lettere, i tuoi carteggi, i tuoi blocchi e quello che ci hai scritto lasciano il mare, comprese le tue lettere sulle spiagge di chi le ha ricevute. Le segnalazioni che hai fatto sulla lettera di qualcun altro restano, senza niente che le leghi a te. Un nuovo avvio dell'app è un nuovo naufrago.",
 "es": "Puedes borrar tu cuenta desde la app, en el Emporio del Naufragio. Es inmediato: tu cuenta, tus cartas, tus correspondencias, tus bloqueos y lo que nos escribiste dejan el mar, incluidas tus cartas en las playas de quienes las recibieron. Las denuncias que hiciste sobre la carta de otra persona se quedan, sin nada que las ligue a ti. Abrir de nuevo la app es un náufrago nuevo.",
 "fr": "Tu peux supprimer ton compte depuis l'app, dans l'Emporium de l'Épave. C'est immédiat : ton compte, tes lettres, tes correspondances, tes blocages et ce que tu nous as écrit quittent la mer, y compris tes lettres sur les plages de ceux qui les ont reçues. Les signalements que tu as faits sur la lettre de quelqu'un d'autre restent, sans rien qui les relie à toi. Un nouveau lancement de l'app, c'est un nouveau naufragé.",
 "de": "Du kannst dein Konto in der App löschen, im Kontor des Wracks. Es geht sofort: dein Konto, deine Briefe, deine Briefwechsel, deine Blockierungen und was du uns geschrieben hast, verlassen das Meer, auch deine Briefe an den Stränden derer, die sie bekommen haben. Meldungen, die du über den Brief eines anderen gemacht hast, bleiben, ohne etwas, das sie mit dir verbindet. Ein neuer Start der App ist ein neuer Schiffbrüchiger.",
 "pt-BR": "Você pode apagar sua conta pelo app, no Empório do Naufrágio. É imediato: sua conta, suas cartas, suas correspondências, seus bloqueios e o que você nos escreveu deixam o mar, inclusive suas cartas nas praias de quem as recebeu. As denúncias que você fez sobre a carta de outra pessoa ficam, sem nada que as ligue a você. Abrir o app de novo é um náufrago novo.",
 "ja": "アカウントはアプリの中、難破商館から削除できます。すぐに行われます。アカウント、手紙、文通、ブロック、そして私たちへのたよりが海から消え、相手の浜に届いたあなたの手紙も消えます。ほかの人の手紙についてあなたがした報告は残りますが、あなたと結びつくものは何も残りません。もう一度アプリを開けば、新しい漂流者です。"},

"Deleting the app without leaving the sea removes the app from your phone, but your beach waits for you in the sea until you return or leave it properly. On an iPhone, the key to it stays in your iCloud Keychain, so installing Bottlegram again brings you back to the same beach.": {
 "it": "Cancellare l'app senza abbandonare il mare la toglie dal telefono, ma la tua spiaggia ti aspetta nel mare finché non torni o non te ne vai come si deve. Su iPhone la chiave resta nel tuo Portachiavi iCloud, quindi se reinstalli Bottlegram ti risvegli sulla stessa spiaggia.",
 "es": "Borrar la app sin abandonar el mar la quita del teléfono, pero tu playa te espera en el mar hasta que vuelvas o te vayas como es debido. En iPhone la llave se queda en tu Llavero de iCloud, así que si vuelves a instalar Bottlegram despiertas en la misma playa.",
 "fr": "Supprimer l'app sans quitter la mer l'enlève de ton téléphone, mais ta plage t'attend dans la mer jusqu'à ce que tu reviennes ou que tu partes pour de bon. Sur iPhone, la clé reste dans ton trousseau iCloud, donc si tu réinstalles Bottlegram tu te réveilles sur la même plage.",
 "de": "Wenn du die App löschst, ohne das Meer zu verlassen, verschwindet sie von deinem Telefon, aber dein Strand wartet im Meer auf dich, bis du zurückkommst oder richtig gehst. Auf dem iPhone bleibt der Schlüssel in deinem iCloud-Schlüsselbund, und wenn du Bottlegram neu installierst, wachst du am selben Strand auf.",
 "pt-BR": "Apagar o app sem abandonar o mar tira o app do telefone, mas sua praia espera por você no mar até você voltar ou ir embora direito. No iPhone, a chave fica nas suas Chaves do iCloud, então, se você instalar o Bottlegram de novo, acorda na mesma praia.",
 "ja": "海を去らずにアプリを削除すると、アプリは電話から消えますが、あなたの浜は、戻ってくるか正式に去るまで海で待っています。iPhone では鍵が iCloud キーチェーンに残るので、Bottlegram を入れ直すと同じ浜で目を覚まします。"},

"Your rights": {
 "it": "I tuoi diritti",
 "es": "Tus derechos",
 "fr": "Tes droits",
 "de": "Deine Rechte",
 "pt-BR": "Seus direitos",
 "ja": "あなたの権利"},

"Whatever the law of your shore grants you, such as access, correction, erasure, objection or a copy of your data, you can exercise by writing to the lighthouse. Erasure you can also do yourself, in the app, without asking anyone. Because accounts are anonymous, we can only act on the account you write from or describe to us; we cannot look anyone up by name, because we do not have names.": {
 "it": "Qualunque cosa ti riconosca la legge della tua riva, come l'accesso, la rettifica, la cancellazione, l'opposizione o una copia dei tuoi dati, puoi esercitarla scrivendo al faro. La cancellazione puoi farla anche da solo, nell'app, senza chiedere a nessuno. Poiché gli account sono anonimi, possiamo agire solo sull'account da cui scrivi o che ci descrivi; non possiamo cercare nessuno per nome, perché i nomi non li abbiamo.",
 "es": "Lo que te reconozca la ley de tu orilla, como el acceso, la rectificación, la supresión, la oposición o una copia de tus datos, puedes ejercerlo escribiendo al faro. La supresión puedes hacerla tú mismo, en la app, sin pedírselo a nadie. Como las cuentas son anónimas, solo podemos actuar sobre la cuenta desde la que escribes o que nos describes; no podemos buscar a nadie por su nombre, porque no tenemos nombres.",
 "fr": "Tout ce que la loi de ton rivage t'accorde, comme l'accès, la rectification, l'effacement, l'opposition ou une copie de tes données, tu peux l'exercer en écrivant au phare. L'effacement, tu peux aussi le faire toi-même, dans l'app, sans rien demander à personne. Comme les comptes sont anonymes, nous ne pouvons agir que sur le compte depuis lequel tu écris ou que tu nous décris ; nous ne pouvons chercher personne par son nom, puisque nous n'avons pas de noms.",
 "de": "Was dir das Gesetz deiner Küste zusteht, etwa Auskunft, Berichtigung, Löschung, Widerspruch oder eine Kopie deiner Daten, kannst du ausüben, indem du dem Leuchtturm schreibst. Die Löschung kannst du auch selbst erledigen, in der App, ohne jemanden zu fragen. Weil die Konten anonym sind, können wir nur auf das Konto reagieren, von dem du schreibst oder das du uns beschreibst; nach Namen können wir niemanden suchen, denn Namen haben wir nicht.",
 "pt-BR": "O que a lei da sua praia garante a você, como acesso, correção, exclusão, oposição ou uma cópia dos seus dados, você pode exercer escrevendo para o farol. A exclusão você também pode fazer sozinho, no app, sem pedir a ninguém. Como as contas são anônimas, só podemos agir sobre a conta da qual você escreve ou que você nos descreve; não podemos procurar ninguém pelo nome, porque não temos nomes.",
 "ja": "アクセス、訂正、削除、異議、データの写しの取得など、あなたの岸の法律が認める権利は、灯台に手紙を書けば行使できます。削除は、誰にも頼まずにアプリの中で自分で行うこともできます。アカウントは匿名なので、私たちが対応できるのは、あなたが書いてきたアカウントか、説明してくれたアカウントだけです。名前を持っていないので、名前で人を探すことはできません。"},

"If you think we have got something wrong, you can complain to the Italian data protection authority, the Garante per la protezione dei dati personali (": {
 "it": "Se pensi che abbiamo sbagliato qualcosa, puoi presentare reclamo al Garante per la protezione dei dati personali (",
 "es": "Si crees que nos hemos equivocado en algo, puedes reclamar ante la autoridad italiana de protección de datos, el Garante per la protezione dei dati personali (",
 "fr": "Si tu penses que nous avons mal fait quelque chose, tu peux te plaindre auprès de l'autorité italienne de protection des données, le Garante per la protezione dei dati personali (",
 "de": "Wenn du meinst, dass wir etwas falsch gemacht haben, kannst du dich bei der italienischen Datenschutzbehörde beschweren, dem Garante per la protezione dei dati personali (",
 "pt-BR": "Se você acha que erramos em algo, pode reclamar à autoridade italiana de proteção de dados, o Garante per la protezione dei dati personali (",
 "ja": "私たちの扱いに誤りがあると思うときは、イタリアのデータ保護機関である Garante per la protezione dei dati personali（"},

"), or to the authority where you live.": {
 "it": "), o all'autorità del paese in cui vivi.",
 "es": "), o a la autoridad del lugar donde vives.",
 "fr": "), ou à l'autorité du pays où tu vis.",
 "de": ") oder bei der Behörde dort, wo du lebst.",
 "pt-BR": "), ou à autoridade do lugar onde você vive.",
 "ja": "）、またはお住まいの国の機関に苦情を申し立てることができます。"},

"Children": {
 "it": "Bambini e ragazzi",
 "es": "Menores",
 "fr": "Les enfants",
 "de": "Kinder",
 "pt-BR": "Crianças",
 "ja": "子どもについて"},

"Bottlegram is a place where castaways write to castaways, and it is not directed at children. It is not for anyone under 18, and the app asks your date of birth before it lets you in.": {
 "it": "Bottlegram è un posto dove i naufraghi scrivono ai naufraghi, e non è pensata per i bambini. Non è per chi ha meno di 18 anni, e l'app chiede la data di nascita prima di farti entrare.",
 "es": "Bottlegram es un lugar donde los náufragos escriben a náufragos, y no está pensada para menores. No es para menores de 18 años, y la app pide la fecha de nacimiento antes de dejarte entrar.",
 "fr": "Bottlegram est un endroit où des naufragés écrivent à des naufragés, et elle ne s'adresse pas aux enfants. Elle n'est pas pour les moins de 18 ans, et l'app demande la date de naissance avant de te laisser entrer.",
 "de": "Bottlegram ist ein Ort, an dem Schiffbrüchige Schiffbrüchigen schreiben, und es richtet sich nicht an Kinder. Es ist nicht für Menschen unter 18, und die App fragt nach dem Geburtsdatum, bevor sie dich hineinlässt.",
 "pt-BR": "O Bottlegram é um lugar onde náufragos escrevem para náufragos, e não é feito para crianças. Não é para menores de 18 anos, e o app pede a data de nascimento antes de deixar você entrar.",
 "ja": "Bottlegram は漂流者が漂流者に手紙を書く場所で、子ども向けではありません。18歳未満の方は利用できず、アプリは中に入る前に生年月日を尋ねます。"},

"Changes": {
 "it": "Cambiamenti",
 "es": "Cambios",
 "fr": "Changements",
 "de": "Änderungen",
 "pt-BR": "Mudanças",
 "ja": "変更について"},

"If this page changes, the date at the top changes with it. Nothing will ever be collected quietly that this page does not say out loud.": {
 "it": "Se questa pagina cambia, cambia anche la data in cima. Niente verrà mai raccolto in silenzio che questa pagina non dica ad alta voce.",
 "es": "Si esta página cambia, cambia también la fecha de arriba. Nunca se recogerá en silencio nada que esta página no diga en voz alta.",
 "fr": "Si cette page change, la date en haut change avec elle. Rien ne sera jamais collecté en silence que cette page ne dise à voix haute.",
 "de": "Wenn sich diese Seite ändert, ändert sich das Datum oben mit ihr. Nichts wird je still gesammelt, was diese Seite nicht laut sagt.",
 "pt-BR": "Se esta página mudar, a data no topo muda junto. Nada será coletado em silêncio que esta página não diga em voz alta.",
 "ja": "このページが変わるときは、上の日付も変わります。このページがはっきり言っていないことを、黙って集めることは決してありません。"},

"Writing to whoever keeps the lighthouse": {
 "it": "Scrivere a chi tiene il faro",
 "es": "Escribir a quien cuida el faro",
 "fr": "Écrire à qui garde le phare",
 "de": "An den, der den Leuchtturm hütet",
 "pt-BR": "Escrever para quem cuida do farol",
 "ja": "灯台守へのたより"},

"For any question about your data, or anything else at all, this address reaches a real person:": {
 "it": "Per qualunque domanda sui tuoi dati, o su qualunque altra cosa, questo indirizzo raggiunge una persona vera:",
 "es": "Para cualquier pregunta sobre tus datos, o sobre cualquier otra cosa, esta dirección llega a una persona de verdad:",
 "fr": "Pour toute question sur tes données, ou sur n'importe quoi d'autre, cette adresse arrive à une vraie personne :",
 "de": "Für jede Frage zu deinen Daten, oder zu irgendetwas anderem, erreicht diese Adresse einen echten Menschen:",
 "pt-BR": "Para qualquer pergunta sobre seus dados, ou sobre qualquer outra coisa, este endereço chega a uma pessoa de verdade:",
 "ja": "あなたのデータについての質問も、そのほかのことも、このアドレスに送れば本物の人に届きます。"},


# ── La press, fase 2 della revisione (05/11/2026) ─────────────────────────

"At a glance": {
 "it": "A colpo d'occhio",
 "es": "De un vistazo",
 "fr": "En un coup d'œil",
 "de": "Auf einen Blick",
 "pt-BR": "De relance",
 "ja": "ひと目で"},

"Status": {
 "it": "Stato",
 "es": "Estado",
 "fr": "Statut",
 "de": "Status",
 "pt-BR": "Situação",
 "ja": "状況"},

"Coming soon on iPhone and Android": {
 "it": "In arrivo su iPhone e Android",
 "es": "Muy pronto en iPhone y Android",
 "fr": "Bientôt sur iPhone et Android",
 "de": "Bald auf iPhone und Android",
 "pt-BR": "Em breve no iPhone e no Android",
 "ja": "まもなく iPhone と Android で"},

"Free, with optional purchases in the Wreck Emporium": {
 "it": "Gratis, con acquisti facoltativi nell'Emporio del Relitto",
 "es": "Gratis, con compras opcionales en el Emporio del Naufragio",
 "fr": "Gratuit, avec des achats facultatifs dans l'Emporium de l'Épave",
 "de": "Kostenlos, mit optionalen Käufen im Kontor des Wracks",
 "pt-BR": "Grátis, com compras opcionais no Empório do Naufrágio",
 "ja": "無料。難破商館での購入は任意です"},

"Press contact": {
 "it": "Contatto stampa",
 "es": "Contacto de prensa",
 "fr": "Contact presse",
 "de": "Pressekontakt",
 "pt-BR": "Contato de imprensa",
 "ja": "報道関係のお問い合わせ"},

"250 illustrated beaches · 31,125 sea routes · three bottles a day · six to thirty-six hours a crossing": {
 "it": "250 spiagge illustrate · 31.125 rotte di mare · tre bottiglie al giorno · da sei a trentasei ore per una traversata",
 "es": "250 playas ilustradas · 31.125 rutas marinas · tres botellas al día · de seis a treinta y seis horas por travesía",
 "fr": "250 plages illustrées · 31 125 routes maritimes · trois bouteilles par jour · six à trente-six heures par traversée",
 "de": "250 illustrierte Strände · 31.125 Seerouten · drei Flaschen am Tag · sechs bis sechsunddreißig Stunden pro Überfahrt",
 "pt-BR": "250 praias ilustradas · 31.125 rotas marítimas · três garrafas por dia · de seis a trinta e seis horas por travessia",
 "ja": "描かれた浜 250・海の航路 31,125・一日に瓶 3 本・一度の航海に 6〜36 時間"},

"Download the press kit": {
 "it": "Scarica il press kit",
 "es": "Descargar el kit de prensa",
 "fr": "Télécharger le dossier de presse",
 "de": "Pressemappe herunterladen",
 "pt-BR": "Baixar o kit de imprensa",
 "ja": "プレスキットをダウンロード"},

"Read the story": {
 "it": "Leggi la storia",
 "es": "Leer la historia",
 "fr": "Lire l'histoire",
 "de": "Die Geschichte lesen",
 "pt-BR": "Ler a história",
 "ja": "物語を読む"},

"Francesco Gola ·": {
 "it": "Francesco Gola ·",
 "es": "Francesco Gola ·",
 "fr": "Francesco Gola ·",
 "de": "Francesco Gola ·",
 "pt-BR": "Francesco Gola ·",
 "ja": "Francesco Gola ·"},

"About Bottlegram": {
 "it": "Bottlegram, in breve",
 "es": "Sobre Bottlegram",
 "fr": "À propos de Bottlegram",
 "de": "Über Bottlegram",
 "pt-BR": "Sobre o Bottlegram",
 "ja": "Bottlegram について"},

"Bottlegram is a slow messaging app made by Francesco Gola, an Italian seascape photographer. Each castaway writes a letter, seals it in a bottle, and the current carries it to another castaway's beach somewhere in the world, six to thirty-six hours later. The sea has 250 illustrated beaches at real coordinates, joined by 31,125 routes measured around real coastlines. Bottlegram is free, with optional purchases in the Wreck Emporium, and is coming soon to iPhone and Android.": {
 "it": "Bottlegram è un'app di messaggi lenti creata da Francesco Gola, fotografo italiano di paesaggio marino. Ogni naufrago scrive una lettera, la chiude in una bottiglia, e la corrente la porta sulla spiaggia di un altro naufrago da qualche parte nel mondo, da sei a trentasei ore dopo. Il mare ha 250 spiagge illustrate alle loro coordinate vere, unite da 31.125 rotte misurate attorno alle coste vere. Bottlegram è gratis, con acquisti facoltativi nell'Emporio del Relitto, e arriva presto su iPhone e Android.",
 "es": "Bottlegram es una app de mensajes lentos creada por Francesco Gola, fotógrafo italiano de paisaje marino. Cada náufrago escribe una carta, la cierra en una botella, y la corriente la lleva a la playa de otro náufrago en algún lugar del mundo, entre seis y treinta y seis horas después. El mar tiene 250 playas ilustradas en sus coordenadas reales, unidas por 31.125 rutas medidas alrededor de las costas reales. Bottlegram es gratis, con compras opcionales en el Emporio del Naufragio, y llega pronto a iPhone y Android.",
 "fr": "Bottlegram est une messagerie lente créée par Francesco Gola, photographe italien de paysages marins. Chaque naufragé écrit une lettre, la scelle dans une bouteille, et le courant la porte sur la plage d'un autre naufragé, quelque part dans le monde, six à trente-six heures plus tard. La mer compte 250 plages illustrées à leurs vraies coordonnées, reliées par 31 125 routes mesurées autour des vraies côtes. Bottlegram est gratuit, avec des achats facultatifs dans l'Emporium de l'Épave, et arrive bientôt sur iPhone et Android.",
 "de": "Bottlegram ist eine App für langsame Nachrichten von Francesco Gola, einem italienischen Seelandschaftsfotografen. Jeder Schiffbrüchige schreibt einen Brief, verschließt ihn in einer Flasche, und die Strömung trägt ihn sechs bis sechsunddreißig Stunden später an den Strand eines anderen Schiffbrüchigen, irgendwo auf der Welt. Das Meer hat 250 illustrierte Strände an ihren echten Koordinaten, verbunden durch 31.125 Routen, die entlang der echten Küsten gemessen sind. Bottlegram ist kostenlos, mit optionalen Käufen im Kontor des Wracks, und kommt bald auf iPhone und Android.",
 "pt-BR": "Bottlegram é um app de mensagens lentas criado por Francesco Gola, fotógrafo italiano de paisagem marinha. Cada náufrago escreve uma carta, fecha numa garrafa, e a correnteza a leva até a praia de outro náufrago em algum lugar do mundo, de seis a trinta e seis horas depois. O mar tem 250 praias ilustradas nas suas coordenadas reais, ligadas por 31.125 rotas medidas ao redor das costas reais. Bottlegram é grátis, com compras opcionais no Empório do Naufrágio, e chega em breve ao iPhone e ao Android.",
 "ja": "Bottlegram は、イタリアの海景写真家フランチェスコ・ゴーラが作った、ゆっくり届くメッセージアプリです。漂着者はそれぞれ手紙を書いて瓶に封じ、潮がそれを六時間から三十六時間かけて、世界のどこかにいる別の漂着者の浜へ運びます。海には実在の座標にある 250 の描かれた浜があり、実際の海岸線に沿って測った 31,125 の航路で結ばれています。Bottlegram は無料で、難破商館での購入は任意です。まもなく iPhone と Android に登場します。"},

"About Francesco Gola": {
 "it": "Francesco Gola, in breve",
 "es": "Sobre Francesco Gola",
 "fr": "À propos de Francesco Gola",
 "de": "Über Francesco Gola",
 "pt-BR": "Sobre Francesco Gola",
 "ja": "フランチェスコ・ゴーラについて"},

"Francesco Gola photographs the sea, most of it in long exposures. As a boy he searched beaches for a bottle with a letter inside. He never found one, so he built Bottlegram.": {
 "it": "Francesco Gola fotografa il mare, quasi sempre in lunga esposizione. Da bambino cercava sulle spiagge una bottiglia con dentro una lettera. Non l'ha mai trovata, così ha costruito Bottlegram.",
 "es": "Francesco Gola fotografía el mar, casi siempre en larga exposición. De niño buscaba en las playas una botella con una carta dentro. Nunca la encontró, así que construyó Bottlegram.",
 "fr": "Francesco Gola photographie la mer, presque toujours en pose longue. Enfant, il cherchait sur les plages une bouteille avec une lettre dedans. Il n'en a jamais trouvé, alors il a construit Bottlegram.",
 "de": "Francesco Gola fotografiert das Meer, meist mit Langzeitbelichtung. Als Junge suchte er an Stränden nach einer Flasche mit einem Brief darin. Er fand nie eine, also baute er Bottlegram.",
 "pt-BR": "Francesco Gola fotografa o mar, quase sempre em longa exposição. Quando menino, procurava nas praias uma garrafa com uma carta dentro. Nunca encontrou, então construiu o Bottlegram.",
 "ja": "フランチェスコ・ゴーラは海を撮る写真家で、その多くは長時間露光です。子どもの頃、手紙の入った瓶を探して浜を歩きました。一度も見つからなかったので、Bottlegram を作りました。"},

"In Francesco's words": {
 "it": "Con le parole di Francesco",
 "es": "En palabras de Francesco",
 "fr": "Dans les mots de Francesco",
 "de": "In Francescos Worten",
 "pt-BR": "Nas palavras de Francesco",
 "ja": "フランチェスコの言葉"},

"“A long exposure is a photograph you make by waiting.”": {
 "it": "«Una lunga esposizione è una fotografia che si fa aspettando.»",
 "es": "«Una larga exposición es una fotografía que se hace esperando.»",
 "fr": "« Une pose longue est une photographie que l'on fait en attendant. »",
 "de": "„Eine Langzeitbelichtung ist eine Fotografie, die man durch Warten macht.“",
 "pt-BR": "“Uma longa exposição é uma fotografia que se faz esperando.”",
 "ja": "「長時間露光とは、待つことで撮る写真です。」"},

"“I have never found one. So I built it.”": {
 "it": "«Non l'ho mai trovata. Così me la sono costruita.»",
 "es": "«Nunca la he encontrado. Así que me la construí.»",
 "fr": "« Je n'en ai jamais trouvé. Alors je l'ai construite. »",
 "de": "„Gefunden habe ich nie eine. Also habe ich sie gebaut.“",
 "pt-BR": "“Nunca encontrei nenhuma. Então eu a construí.”",
 "ja": "「一度も見つかりませんでした。だから自分で作りました。」"},

"“Tomorrow, a bottle from someone you do not know will wash up on your sand. That is the whole app.”": {
 "it": "«Domani sulla tua sabbia arriverà la bottiglia di qualcuno che non conosci. L'app è tutta qui.»",
 "es": "«Mañana llegará a tu arena la botella de alguien a quien no conoces. La app es toda esto.»",
 "fr": "« Demain, sur votre sable, arrivera la bouteille de quelqu'un que vous ne connaissez pas. L'application, c'est tout entière cela. »",
 "de": "„Morgen wird an Ihrem Sand die Flasche von jemandem anspülen, den Sie nicht kennen. Das ist die ganze App.“",
 "pt-BR": "“Amanhã chegará à sua areia a garrafa de alguém que você não conhece. O app é só isso.”",
 "ja": "「明日、あなたの砂浜に、知らない誰かの瓶が流れ着きます。このアプリはそれだけです。」"},

"All three may be quoted as Francesco Gola, the maker of Bottlegram.": {
 "it": "Tutte e tre si possono citare come Francesco Gola, l'autore di Bottlegram.",
 "es": "Las tres pueden citarse como Francesco Gola, el creador de Bottlegram.",
 "fr": "Les trois peuvent être citées au nom de Francesco Gola, le créateur de Bottlegram.",
 "de": "Alle drei dürfen als Zitat von Francesco Gola, dem Macher von Bottlegram, verwendet werden.",
 "pt-BR": "As três podem ser citadas como de Francesco Gola, o criador do Bottlegram.",
 "ja": "三つとも、Bottlegram の作者フランチェスコ・ゴーラの言葉として引用できます。"},

"This page knows you only as a visitor, the way the sea knows you only as a castaway.": {
 "it": "Questa pagina ti conosce solo come visitatore, come il mare ti conosce solo come naufrago.",
 "es": "Esta página te conoce solo como visitante, igual que el mar te conoce solo como náufrago.",
 "fr": "Cette page vous connaît seulement comme visiteur, comme la mer vous connaît seulement comme naufragé.",
 "de": "Diese Seite kennt Sie nur als Besucher, so wie das Meer Sie nur als Schiffbrüchigen kennt.",
 "pt-BR": "Esta página conhece você só como visitante, do jeito que o mar conhece você só como náufrago.",
 "ja": "このページにとってあなたはただの訪問者で、海にとってあなたがただの漂着者であるのと同じです。"},


# ── Le didascalie della scheda store, alt della galleria press (05/11/2026) ──

"A beach at the end of the world": {
 "it": "Una spiaggia in capo al mondo",
 "es": "Una playa en el fin del mundo",
 "fr": "Une plage au bout du monde",
 "de": "Ein Strand am Ende der Welt",
 "pt-BR": "Uma praia no fim do mundo",
 "ja": "世界の果ての浜"},

"The tide brings you a bottle": {
 "it": "La marea ti porta una bottiglia",
 "es": "La marea te trae una botella",
 "fr": "La marée t’apporte une bouteille",
 "de": "Die Flut bringt dir eine Flasche",
 "pt-BR": "A maré te traz uma garrafa",
 "ja": "潮が瓶を運んでくる"},

"Write to whoever the sea chooses": {
 "it": "Scrivi a chi sceglie il mare",
 "es": "Escribe a quien elija el mar",
 "fr": "Écris à qui la mer choisira",
 "de": "Das Meer wählt, wer dich liest",
 "pt-BR": "Escreva para quem o mar escolher",
 "ja": "海が選ぶ誰かに手紙を書く"},

"Uncork a letter from far away": {
 "it": "Stappa una lettera da lontano",
 "es": "Descorcha una carta de lejos",
 "fr": "Débouche une lettre lointaine",
 "de": "Entkorke Post von weit her",
 "pt-BR": "Abra uma carta vinda de longe",
 "ja": "遠い岸からの手紙をひらく"},

"Follow it around the coastlines": {
 "it": "Seguila attorno alle coste",
 "es": "Síguela rodeando las costas",
 "fr": "Suis-la le long des côtes",
 "de": "Folge ihr die Küsten entlang",
 "pt-BR": "Siga sua garrafa costa afora",
 "ja": "海岸線をめぐる瓶を追いかける"},

"Answer, then wait for the tide": {
 "it": "Rispondi, poi aspetta la marea",
 "es": "Responde y espera a la marea",
 "fr": "Réponds, puis attends la marée",
 "de": "Antworte und warte auf die Flut",
 "pt-BR": "Responda e espere a maré",
 "ja": "返事を書いて、潮を待つ"},

"250 real beaches, drawn by hand": {
 "it": "250 spiagge vere, disegnate a mano",
 "es": "250 playas dibujadas a mano",
 "fr": "250 vraies plages, faites main",
 "de": "250 echte Orte, handgezeichnet",
 "pt-BR": "250 praias reais, feitas à mão",
 "ja": "実在の浜、250か所を手描きで"},

"From Lofoten to Bora Bora": {
 "it": "Dalle Lofoten a Bora Bora",
 "es": "De las Lofoten a Bora Bora",
 "fr": "Des Lofoten à Bora Bora",
 "de": "Von den Lofoten bis Bora Bora",
 "pt-BR": "Das Lofoten a Bora Bora",
 "ja": "ロフォーテンからボラボラまで"},

"Each one changes with the hour": {
 "it": "Ognuna cambia con l’ora",
 "es": "Cada una cambia con la hora",
 "fr": "Chacune change avec l’heure",
 "de": "Zu jeder Tageszeit ein anderer",
 "pt-BR": "Cada uma muda com as horas",
 "ja": "どの浜も、刻々と姿を変える"},

"Sign it with your wax seal": {
 "it": "Firmala con il tuo sigillo",
 "es": "Fírmala con tu sello de lacre",
 "fr": "Signe-la de ton sceau de cire",
 "de": "Unterschreib mit deinem Siegel",
 "pt-BR": "Assine com seu selo de lacre",
 "ja": "あなたの印で封をする"},

}

# Le frasi che non si traducono: nomi propri, indirizzi, la rosa dei venti.
INVARIATE = [",",  # la virgola fra i due soprannomi: punteggiatura, non testo
             "Bottlegram", "N", "bottlegram@bulbmode.com",
             # Numeri, sigle e indirizzi del press kit: si scrivono uguale in
             # tutte e sette, e senza questa riga la console li denuncia
             # ogni volta come frasi senza traduzione.
             # 1, 2, 4: i numeri delle tappe della traversata. C'era solo il
             # "3" delle bottiglie, e gli altri tre finivano nell'elenco delle
             # frasi senza traduzione a ogni giro, dove coprivano le vere.
             "iOS", "www.bottlegram.app", "250", "31,125", "1", "2", "3", "4",
             "6–36", "32 MB",
             # I nomi delle spiagge dell'approdo che ruota: endonimi, come
             # nell'app. I LUOGHI invece si traducono (voci qui sopra).
             "Cala Goloritzé", "Reynisfjara", "Anse Source d'Argent",
             "Haukland Beach", "Praia da Ursa",
             # I servizi nominati dalla privacy: nomi propri, uguali in tutte e sette.
             "Bulb Mode SRL Semplificata", "Supabase", "OpenAI", "Google Cloud Translation", "Anthropic", "Apple", "Google Play", "Resend", "www.garanteprivacy.it"]

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
 # LE REGOLE DEL MARE NON STANNO PIÙ SULLA PAGINA (vivono nell'app, e un
 # giorno in una pagina loro): qui restano solo i versi del naufragio e le
 # parole dell'approdo, che sono dell'app e dall'app si rileggono.
 "The storm took the ship, the cargo, and every map you owned.",
 "The sea, in return, left you one thing: a beach at the end of the world.",
 "They say the tide brings words from other castaways. And that a bottle, thrown well, can reach anyone.",
 "Your new home",
 "Every day the tide will bring bottles from other shores. You can throw three of your own each day. Speak kindly — words travel far.",
 # La firma della lettera: dal 09/09 nell'app gli sconosciuti sono naufraghi,
 # e dal 05/11 il sito usa la stessa parola, letta dall'app.
 "A castaway",
 # LA FIRMA DELLA LETTERA NON SI RILEGGE PIU DALL'APP: dentro l'app gli
 # sconosciuti sono diventati naufraghi, e quella stringa li non c'e' piu.
 # Sul sito resta, ed e' vera — quindi la voce e' passata a mano in SITO,
 # invece di sparire in silenzio a ogni rigenerazione.
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
