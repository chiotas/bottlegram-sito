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

"In a hurry? The sea is not.": {
 "it": "Sei di fretta? Il mare no.",
 "es": "¿Tienes prisa? El mar no.",
 "fr": "Tu es pressé ? La mer, non.",
 "de": "In Eile? Das Meer nicht.",
 "pt-BR": "Com pressa? O mar não.",
 "ja": "急いでいますか。海は急ぎません。"},

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

"Bottlegram is a slow messaging app. You do not write to anybody in particular — it is the current that decides who you end up talking to.": {
 "it": "Bottlegram è una applicazione di messaggistica lenta. Non scrivi a nessuno in particolare, è la corrente a decidere il tuo interlocutore.",
 "es": "Bottlegram es una aplicación de mensajería lenta. No escribes a nadie en particular: es la corriente la que decide con quién acabas hablando.",
 "fr": "Bottlegram est une application de messagerie lente. Tu n'écris à personne en particulier — c'est le courant qui décide de ton interlocuteur.",
 "de": "Bottlegram ist eine App für langsame Nachrichten. Du schreibst niemandem bestimmten — die Strömung entscheidet, mit wem du am Ende sprichst.",
 "pt-BR": "Bottlegram é um aplicativo de mensageria lenta. Você não escreve para ninguém em particular — é a correnteza que decide com quem você vai conversar.",
 "ja": "Bottlegram は、ゆっくりとしたメッセージのやりとりをするアプリです。宛先はあなたが決めません。だれと話すことになるかは、潮が決めます。"},

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

"Every day the sea leaves you three bottles. You put a message inside and hand it to the current, without choosing who gets it.": {
 "it": "Ogni giorno il mare ti lascia tre bottiglie. Ci metti dentro un messaggio e lo affidi alla corrente, senza scegliere per chi.",
 "es": "Cada día el mar te deja tres botellas. Metes dentro un mensaje y lo confías a la corriente, sin elegir para quién.",
 "fr": "Chaque jour la mer te laisse trois bouteilles. Tu y glisses un message et tu le confies au courant, sans choisir pour qui.",
 "de": "Jeden Tag lässt dir das Meer drei Flaschen da. Du legst eine Nachricht hinein und übergibst sie der Strömung, ohne zu wählen, für wen.",
 "pt-BR": "Todo dia o mar te deixa três garrafas. Você põe uma mensagem dentro e a entrega à correnteza, sem escolher para quem.",
 "ja": "海は毎日、三本の瓶を置いていきます。ことづてを入れて、宛先を選ばずに潮へゆだねます。"},

"Someone finds it": {
 "it": "Qualcuno la trova", "es": "Alguien la encuentra", "fr": "Quelqu'un la trouve",
 "de": "Jemand findet sie", "pt-BR": "Alguém a encontra", "ja": "だれかが拾う"},

"Six to thirty-six hours later it washes up on another castaway's beach. In the same way, other people's bottles wash up on your sand.": {
 "it": "Da sei a trentasei ore dopo approda sulla spiaggia di un altro naufrago. Allo stesso modo, sulla tua sabbia arrivano le bottiglie degli altri.",
 "es": "Entre seis y treinta y seis horas después llega a la playa de otro náufrago. Del mismo modo, a tu arena llegan las botellas de los demás.",
 "fr": "Six à trente-six heures plus tard, elle échoue sur la plage d'un autre naufragé. De la même façon, les bouteilles des autres échouent sur ton sable.",
 "de": "Sechs bis sechsunddreißig Stunden später strandet sie am Strand eines anderen Schiffbrüchigen. Genauso stranden fremde Flaschen an deinem Sand.",
 "pt-BR": "De seis a trinta e seis horas depois, ela encalha na praia de outro náufrago. Do mesmo modo, na sua areia chegam as garrafas dos outros.",
 "ja": "六時間から三十六時間ののち、べつの漂流者の浜へ流れ着きます。同じように、あなたの砂浜にも、ほかの人の瓶が届きます。"},

"And answers, if they want to": {
 "it": "E se vuole, risponde", "es": "Y si quiere, responde", "fr": "Et s'il veut, il répond",
 "de": "Und antwortet, wenn er mag", "pt-BR": "E responde, se quiser", "ja": "気が向けば、返事が来る"},

"Whoever finds your letter can write back, and a correspondence begins. Nobody has to: a bottle that goes unanswered is a thing that happens at sea.": {
 "it": "Chi trova la tua lettera può risponderti, e da lì nasce una corrispondenza. Nessuno è obbligato: una bottiglia senza risposta è una cosa che in mare succede.",
 "es": "Quien encuentre tu carta puede contestarte, y de ahí nace una correspondencia. Nadie está obligado: una botella sin respuesta es algo que en el mar pasa.",
 "fr": "Celui qui trouve ta lettre peut te répondre, et une correspondance commence. Personne n'y est tenu : une bouteille sans réponse, ça arrive en mer.",
 "de": "Wer deinen Brief findet, kann antworten, und daraus wird ein Briefwechsel. Niemand muss: eine Flasche ohne Antwort kommt auf See vor.",
 "pt-BR": "Quem encontra sua carta pode responder, e daí nasce uma correspondência. Ninguém é obrigado: uma garrafa sem resposta é coisa que acontece no mar.",
 "ja": "手紙を拾った人は、返事を書くことができます。そこから文通がはじまります。返事は義務ではありません。答えのない瓶も、海ではよくあることです。"},

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

"Somewhere out there, a stranger is writing to you. No names. No noise. Only the tide, and whatever it decides to leave on your sand.": {
 "it": "Da qualche parte, uno sconosciuto ti sta scrivendo. Nessun nome. Nessun rumore. Solo la marea, e quello che decide di lasciarti sulla sabbia.",
 "es": "En algún lugar, un desconocido te está escribiendo. Sin nombres. Sin ruido. Solo la marea, y lo que decida dejarte en la arena.",
 "fr": "Quelque part, un inconnu t'écrit. Aucun nom. Aucun bruit. Rien que la marée, et ce qu'elle décide de laisser sur ton sable.",
 "de": "Irgendwo da draußen schreibt dir ein Fremder. Keine Namen. Kein Lärm. Nur die Gezeiten und das, was sie in deinem Sand zurücklassen.",
 "pt-BR": "Em algum lugar, um desconhecido está escrevendo para você. Sem nomes. Sem barulho. Só a maré, e o que ela decidir deixar na sua areia.",
 "ja": "どこかで、見知らぬ誰かがあなたに手紙を書いている。名前もなく、騒がしさもなく。あるのは潮と、それが砂に残していくものだけ。"},

"Coming to the App Store": {
 "it": "Presto sull'App Store", "es": "Pronto en la App Store",
 "fr": "Bientôt sur l'App Store", "de": "Bald im App Store",
 "pt-BR": "Em breve na App Store", "ja": "App Store にまもなく登場"},

"A stranger": {
 "it": "Uno sconosciuto", "es": "Un desconocido", "fr": "Un inconnu",
 "de": "Jemand Unbekanntes", "pt-BR": "Um desconhecido", "ja": "見知らぬ誰か"},

"Free · No ads · No accounts": {
 "it": "Gratis · Niente pubblicità · Nessun account",
 "es": "Gratis · Sin anuncios · Sin cuentas",
 "fr": "Gratuit · Sans publicité · Sans compte",
 "de": "Kostenlos · Keine Werbung · Kein Konto",
 "pt-BR": "Grátis · Sem anúncios · Sem contas",
 "ja": "無料・広告なし・アカウントなし"},

"The app at Ficogrande, on Stromboli: the volcano smoking under a full moon, and two bottles washed up on the black sand.": {
 "it": "L'app a Ficogrande, a Stromboli: il vulcano che fuma sotto la luna piena, e due bottiglie arrivate sulla sabbia nera.",
 "es": "La app en Ficogrande, en Stromboli: el volcán humeando bajo la luna llena y dos botellas varadas en la arena negra.",
 "fr": "L'app à Ficogrande, sur Stromboli : le volcan qui fume sous la pleine lune, et deux bouteilles échouées sur le sable noir.",
 "de": "Die App in Ficogrande auf Stromboli: der rauchende Vulkan unter dem Vollmond und zwei Flaschen, die am schwarzen Sand angespült sind.",
 "pt-BR": "O app em Ficogrande, em Stromboli: o vulcão fumegando sob a lua cheia e duas garrafas na areia preta.",
 "ja": "ストロンボリ島フィコグランデのアプリ画面。満月の下で煙を上げる火山と、黒い砂に流れ着いた二本の瓶。"},

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
 "fr": "Tu écris, puis tu attends.", "de": "Du schreibst, und dann wartest du.",
 "pt-BR": "Você escreve, e então espera.", "ja": "書いて、それから待つ。"},

"A letter takes as long as the water between you takes. A shore across the same sea might answer by morning; the far side of the world will keep you waiting for days. Nothing you can tap will make it come sooner — and after the first one, you stop wanting it to.": {
 "it": "Una lettera ci mette quanto ci mette l'acqua che vi separa. Una riva sullo stesso mare può risponderti entro domattina; dall'altra parte del mondo ti farà aspettare giorni. Non c'è niente da toccare che la faccia arrivare prima — e dopo la prima volta smetti di volerlo.",
 "es": "Una carta tarda lo que tarde el agua que os separa. Una orilla del mismo mar puede responder por la mañana; el otro extremo del mundo te hará esperar días. No hay nada que puedas tocar para que llegue antes, y después de la primera dejas de quererlo.",
 "fr": "Une lettre met le temps que met l'eau qui vous sépare. Un rivage sur la même mer répondra peut-être au matin ; l'autre bout du monde te fera attendre des jours. Rien de ce que tu peux toucher ne la fera venir plus tôt — et après la première, tu cesses de le souhaiter.",
 "de": "Ein Brief braucht so lange, wie das Wasser zwischen euch braucht. Eine Küste am selben Meer antwortet vielleicht bis zum Morgen; die andere Seite der Welt lässt dich Tage warten. Kein Tippen bringt ihn früher — und nach dem ersten Mal willst du es gar nicht mehr.",
 "pt-BR": "Uma carta demora o que demorar a água entre vocês. Uma praia no mesmo mar pode responder pela manhã; o outro lado do mundo vai fazer você esperar dias. Não há nada em que tocar para que chegue antes — e depois da primeira, você para de querer isso.",
 "ja": "手紙は、あいだにある水の分だけ時間がかかる。同じ海の向こう岸なら朝には返事が来るかもしれないし、地球の裏側なら何日も待たされる。早く着かせるために押せるものは何もない。そして最初の一通のあとは、押したいとも思わなくなる。"},

"The beach is empty, and it is yours.": {
 "it": "La spiaggia è vuota, ed è tua.", "es": "La playa está vacía, y es tuya.",
 "fr": "La plage est vide, et elle est à toi.", "de": "Der Strand ist leer, und er gehört dir.",
 "pt-BR": "A praia está vazia, e é sua.", "ja": "浜辺には誰もいない。そしてそれはあなたのものだ。"},

"Nobody is online. Nobody is away. Nobody is typing, and nothing is marked delivered, seen or read. There is a shore, the sound of the water, and a horizon that asks nothing of you at all.": {
 "it": "Nessuno è online. Nessuno è assente. Nessuno sta scrivendo, e niente è segnato come consegnato, visualizzato o letto. C'è una riva, il rumore dell'acqua, e un orizzonte che non ti chiede niente.",
 "es": "Nadie está en línea. Nadie está ausente. Nadie está escribiendo, y nada aparece como entregado, visto o leído. Hay una orilla, el sonido del agua y un horizonte que no te pide nada.",
 "fr": "Personne n'est en ligne. Personne n'est absent. Personne n'est en train d'écrire, et rien n'est marqué distribué, vu ou lu. Il y a un rivage, le bruit de l'eau, et un horizon qui ne te demande rien.",
 "de": "Niemand ist online. Niemand ist abwesend. Niemand tippt, und nichts ist als zugestellt, gesehen oder gelesen markiert. Es gibt ein Ufer, das Geräusch des Wassers und einen Horizont, der nichts von dir will.",
 "pt-BR": "Ninguém está on-line. Ninguém está ausente. Ninguém está digitando, e nada é marcado como entregue, visto ou lido. Há uma praia, o som da água e um horizonte que não pede nada de você.",
 "ja": "誰もオンラインではない。誰も離席していない。誰も入力中ではなく、送信済みも既読もない。あるのは岸と、水の音と、何ひとつ求めてこない水平線だけ。"},

"You have all the time in the world to choose the words.": {
 "it": "Hai tutto il tempo del mondo per scegliere le parole.",
 "es": "Tienes todo el tiempo del mundo para elegir las palabras.",
 "fr": "Tu as tout le temps du monde pour choisir les mots.",
 "de": "Du hast alle Zeit der Welt, die Worte zu wählen.",
 "pt-BR": "Você tem todo o tempo do mundo para escolher as palavras.",
 "ja": "言葉を選ぶ時間なら、いくらでもある。"},

"A letter that costs something is written better. You will not fire off seven in a row here, you will not correct yourself an hour later, and you cannot call one back. So you sit with it a while, and you say the true thing instead of the quick one.": {
 "it": "Una lettera che costa qualcosa si scrive meglio. Qui non ne spari sette di fila, non ti correggi un'ora dopo, e non puoi richiamarne indietro nessuna. Così ci stai sopra un po', e dici la cosa vera invece di quella veloce.",
 "es": "Una carta que cuesta algo se escribe mejor. Aquí no soltarás siete seguidas, no te corregirás una hora después y no puedes retirar ninguna. Así que te quedas un rato con ella, y dices lo verdadero en lugar de lo rápido.",
 "fr": "Une lettre qui coûte quelque chose s'écrit mieux. Ici tu n'en enverras pas sept d'affilée, tu ne te corrigeras pas une heure plus tard, et tu ne peux en rappeler aucune. Alors tu restes un moment avec elle, et tu dis la chose vraie plutôt que la chose rapide.",
 "de": "Ein Brief, der etwas kostet, wird besser geschrieben. Hier feuerst du nicht sieben hintereinander ab, korrigierst dich nicht eine Stunde später und kannst keinen zurückholen. Also bleibst du eine Weile dabei und sagst das Wahre statt des Schnellen.",
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
 "fr": "Les jours passent. Tu fais autre chose. Puis la marée laisse sur ton sable quelque chose que personne n'avait programmé, que personne n'avait promu et que personne n'aurait pu te vendre — l'écriture d'un inconnu, venue d'une côte que tu n'as jamais vue.",
 "de": "Tage vergehen. Du tust anderes. Dann lässt die Flut etwas in deinem Sand zurück, das niemand geplant, niemand beworben und niemand dir hätte verkaufen können — die Handschrift eines Fremden, von einer Küste, die du nie gesehen hast.",
 "pt-BR": "Os dias passam. Você faz outras coisas. Então a maré deixa na sua areia algo que ninguém programou, ninguém promoveu e ninguém poderia ter vendido para você — a letra de um desconhecido, de uma costa que você nunca viu.",
 "ja": "日が過ぎる。ほかのことをして暮らす。するとある日、潮が砂に何かを置いていく。誰も予定せず、誰も宣伝せず、誰にも売ることのできなかったもの——見たこともない海岸から届いた、知らない誰かの手書きの文字だ。"},

"Somewhere to savour the quiet, while everything else is racing.": {
 "it": "Un posto dove godersi la quiete, mentre tutto il resto corre.",
 "es": "Un lugar donde disfrutar de la calma, mientras todo lo demás corre.",
 "fr": "Un endroit où savourer le calme, pendant que tout le reste court.",
 "de": "Ein Ort, an dem man die Stille genießt, während alles andere rennt.",
 "pt-BR": "Um lugar para saborear a quietude, enquanto todo o resto corre.",
 "ja": "ほかのすべてが走りつづけるあいだ、静けさを味わえる場所。"},

"Here it is morning and the wind comes off the land. I will not tell you my name, but I will tell you that I planted three fig trees behind the house and one of them took. If this bottle lands anywhere at all, write and tell me the weather where you are.": {
 "it": "Qui è mattina e il vento viene da terra. Non ti dirò il mio nome, ma ti dirò che ho piantato tre fichi dietro casa e uno ha attecchito. Se questa bottiglia approda da qualche parte, scrivimi e dimmi che tempo fa da te.",
 "es": "Aquí es de mañana y el viento viene de tierra. No te diré mi nombre, pero sí que planté tres higueras detrás de la casa y una prendió. Si esta botella llega a alguna parte, escríbeme y dime qué tiempo hace donde estás.",
 "fr": "Ici c'est le matin et le vent vient de la terre. Je ne te dirai pas mon nom, mais je te dirai que j'ai planté trois figuiers derrière la maison et que l'un d'eux a pris. Si cette bouteille aborde quelque part, écris-moi le temps qu'il fait chez toi.",
 "de": "Hier ist Morgen und der Wind kommt vom Land. Ich verrate dir meinen Namen nicht, aber ich sage dir, dass ich hinter dem Haus drei Feigenbäume gepflanzt habe und einer angewachsen ist. Wenn diese Flasche irgendwo anlandet, schreib mir, wie das Wetter bei dir ist.",
 "pt-BR": "Aqui é manhã e o vento vem da terra. Não vou dizer meu nome, mas vou dizer que plantei três figueiras atrás de casa e uma pegou. Se esta garrafa chegar a algum lugar, escreva e me conte que tempo faz aí.",
 "ja": "こちらは朝で、風は陸から吹いてくる。名前は明かさないけれど、家の裏にいちじくを三本植えて、そのうち一本が根づいたことは伝えておく。この瓶がどこかに着いたら、そちらの天気を書いて送ってほしい。"},

"Every day the tide will bring bottles from strangers across the sea. Speak kindly — words travel far.": {
 "it": "Ogni giorno la marea porterà bottiglie di sconosciuti da tutto il mare. Parla con gentilezza — le parole vanno lontano.",
 "es": "Cada día la marea traerá botellas de desconocidos de todo el mar. Habla con amabilidad: las palabras llegan lejos.",
 "fr": "Chaque jour, la marée apportera des bouteilles d'inconnus de toute la mer. Parle avec douceur — les mots vont loin.",
 "de": "Jeden Tag bringt die Flut Flaschen von Fremden aus dem ganzen Meer. Sprich freundlich — Worte reisen weit.",
 "pt-BR": "Todo dia a maré vai trazer garrafas de desconhecidos de todo o mar. Fale com gentileza — as palavras vão longe.",
 "ja": "毎日、潮が海じゅうの見知らぬ人たちの瓶を運んでくる。やさしい言葉を。言葉は遠くまで行く。"},


"The sea has no use for hurry. Write to a stranger on a real beach and let the tide take days to carry it — no names, no feeds, an iPhone app for people who want the waiting back.": {
 "it": "Il mare non sa che farsene della fretta. Scrivi a uno sconosciuto su una spiaggia vera e lascia che la marea ci metta giorni a portarla — niente nomi, niente feed, un'app per iPhone per chi si rivuole indietro l'attesa.",
 "es": "Al mar no le sirve de nada la prisa. Escribe a un desconocido en una playa de verdad y deja que la marea tarde días en llevarla: sin nombres, sin feeds, una app de iPhone para quien quiere recuperar la espera.",
 "fr": "La mer n'a que faire de la hâte. Écris à un inconnu sur une vraie plage et laisse la marée mettre des jours à l'emporter — aucun nom, aucun fil, une application iPhone pour qui veut retrouver l'attente.",
 "de": "Das Meer weiß mit Eile nichts anzufangen. Schreib einem Fremden an einem wirklichen Strand und lass die Flut Tage dafür brauchen — keine Namen, keine Feeds, eine iPhone-App für alle, die das Warten zurückwollen.",
 "pt-BR": "O mar não tem uso para a pressa. Escreva para um desconhecido numa praia de verdade e deixe a maré levar dias para entregar — sem nomes, sem feeds, um app de iPhone para quem quer a espera de volta.",
 "ja": "海に急ぎは要らない。実在する浜辺にいる見知らぬ誰かへ手紙を書き、潮が何日もかけて運ぶのにまかせる。名前もフィードもない、待つ時間を取り戻したい人のための iPhone アプリ。"},

"The sea has no use for hurry. Write to a stranger on a real beach and let the tide take days to carry it.": {
 "it": "Il mare non sa che farsene della fretta. Scrivi a uno sconosciuto su una spiaggia vera e lascia che la marea ci metta giorni a portarla.",
 "es": "Al mar no le sirve de nada la prisa. Escribe a un desconocido en una playa de verdad y deja que la marea tarde días en llevarla.",
 "fr": "La mer n'a que faire de la hâte. Écris à un inconnu sur une vraie plage et laisse la marée mettre des jours à l'emporter.",
 "de": "Das Meer weiß mit Eile nichts anzufangen. Schreib einem Fremden an einem wirklichen Strand und lass die Flut Tage dafür brauchen.",
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

"Dawn at Anse Source d'Argent, as the app draws it: a rose sky, calm water, a palm on the sand.": {
 "it": "L'alba ad Anse Source d'Argent come la disegna l'app: un cielo rosa, l'acqua calma, una palma sulla sabbia.",
 "es": "El alba en Anse Source d'Argent tal como la dibuja la app: un cielo rosado, agua en calma, una palmera en la arena.",
 "fr": "L'aube à Anse Source d'Argent telle que l'application la dessine : un ciel rose, une eau calme, un palmier sur le sable.",
 "de": "Morgengrauen an der Anse Source d'Argent, wie die App es zeichnet: ein rosa Himmel, stilles Wasser, eine Palme im Sand.",
 "pt-BR": "O amanhecer em Anse Source d'Argent como o app o desenha: um céu rosado, água calma, uma palmeira na areia.",
 "ja": "アプリが描くアンス・スルス・ダルジャンの夜明け。薔薇色の空、静かな水、砂の上の一本のやし。"},

"Midday at Cala Goloritzé, as the app draws it: blue sky, turquoise sea, bottles on the pale sand.": {
 "it": "Mezzogiorno a Cala Goloritzé come lo disegna l'app: cielo azzurro, mare turchese, bottiglie sulla sabbia chiara.",
 "es": "El mediodía en Cala Goloritzé tal como lo dibuja la app: cielo azul, mar turquesa, botellas en la arena clara.",
 "fr": "Midi à Cala Goloritzé tel que l'application le dessine : ciel bleu, mer turquoise, des bouteilles sur le sable clair.",
 "de": "Mittag an der Cala Goloritzé, wie die App ihn zeichnet: blauer Himmel, türkisfarbenes Meer, Flaschen im hellen Sand.",
 "pt-BR": "O meio-dia em Cala Goloritzé como o app o desenha: céu azul, mar turquesa, garrafas na areia clara.",
 "ja": "アプリが描くカーラ・ゴロリッツェの正午。青い空、ターコイズの海、明るい砂の上の瓶。"},

"Dusk at Reynisfjara, as the app draws it: an ember sky over black volcanic sand.": {
 "it": "Il tramonto a Reynisfjara come lo disegna l'app: un cielo di brace sopra la sabbia vulcanica nera.",
 "es": "El atardecer en Reynisfjara tal como lo dibuja la app: un cielo de brasas sobre la arena volcánica negra.",
 "fr": "Le crépuscule à Reynisfjara tel que l'application le dessine : un ciel de braise sur le sable volcanique noir.",
 "de": "Dämmerung in Reynisfjara, wie die App sie zeichnet: ein glutroter Himmel über schwarzem Vulkansand.",
 "pt-BR": "O entardecer em Reynisfjara como o app o desenha: um céu de brasas sobre a areia vulcânica preta.",
 "ja": "アプリが描くレイニスフィヤラの夕暮れ。黒い火山砂の上に、燠火のような空。"},

"Night at Haukland Beach, as the app draws it: the aurora over a dark arctic sea.": {
 "it": "La notte a Haukland Beach come la disegna l'app: l'aurora sopra un mare artico scuro.",
 "es": "La noche en Haukland Beach tal como la dibuja la app: la aurora sobre un mar ártico oscuro.",
 "fr": "La nuit à Haukland Beach telle que l'application la dessine : l'aurore au-dessus d'une mer arctique sombre.",
 "de": "Nacht am Haukland Beach, wie die App sie zeichnet: das Polarlicht über einem dunklen arktischen Meer.",
 "pt-BR": "A noite em Haukland Beach como o app a desenha: a aurora sobre um mar ártico escuro.",
 "ja": "アプリが描くハウクラン・ビーチの夜。暗い北極の海の上を渡るオーロラ。"},

"It turns by itself: dawn at La Digue, midday in Sardegna, dusk on the black sand of Reynisfjara, and an arctic night with the aurora overhead. In the app you get one shore, and you do not choose it — which is the best thing about it.": {
 "it": "Gira da sola: l'alba a La Digue, mezzogiorno in Sardegna, il tramonto sulla sabbia nera di Reynisfjara, e una notte artica con l'aurora sopra la testa. Nell'app te ne tocca una, e non la scegli tu — che è la cosa più bella.",
 "es": "Gira sola: el alba en La Digue, el mediodía en Cerdeña, el atardecer en la arena negra de Reynisfjara y una noche ártica con la aurora por encima. En la app te toca una, y no la eliges tú — que es lo mejor de todo.",
 "fr": "Elle tourne toute seule : l'aube à La Digue, midi en Sardaigne, le crépuscule sur le sable noir de Reynisfjara, et une nuit arctique avec l'aurore au-dessus. Dans l'application tu en reçois une, et tu ne la choisis pas — c'est ce qu'il y a de plus beau.",
 "de": "Er wechselt von selbst: Morgengrauen auf La Digue, Mittag auf Sardinien, Dämmerung auf dem schwarzen Sand von Reynisfjara und eine arktische Nacht mit dem Polarlicht darüber. In der App bekommst du einen Strand, und du suchst ihn nicht aus — das ist das Schönste daran.",
 "pt-BR": "Ela gira sozinha: o amanhecer em La Digue, o meio-dia na Sardenha, o entardecer na areia preta de Reynisfjara e uma noite ártica com a aurora lá em cima. No app você ganha uma praia, e não é você que escolhe — que é o melhor disso.",
 "ja": "ひとりでに移り変わる。ラ・ディーグの夜明け、サルデーニャの正午、レイニスフィヤラの黒い砂の夕暮れ、そして頭上をオーロラが渡る北極の夜。アプリでは一つの浜だけが与えられ、それを選ぶことはできない——そこがいちばんいいところだ。"},

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

"On a shore you have never seen, a stranger is pushing the cork into a bottle right now. The sea will decide whose sand it touches next. Maybe yours.": {
 "it": "Su una riva che non hai mai visto, uno sconosciuto sta spingendo il tappo in una bottiglia proprio adesso. Il mare deciderà su quale sabbia farla approdare. Magari proprio sulla tua.",
 "es": "En una orilla que nunca has visto, un desconocido está apretando el corcho de una botella ahora mismo. El mar decidirá qué arena toca después. Quizá justo la tuya.",
 "fr": "Sur un rivage que tu n'as jamais vu, un inconnu enfonce le bouchon d'une bouteille en ce moment même. La mer décidera quel sable elle touchera ensuite. Peut-être le tien.",
 "de": "An einem Ufer, das du nie gesehen hast, drückt gerade ein Fremder den Korken in eine Flasche. Das Meer entscheidet, wessen Sand sie als Nächstes berührt. Vielleicht deinen.",
 "pt-BR": "Numa praia que você nunca viu, um desconhecido está apertando a rolha de uma garrafa agora mesmo. O mar vai decidir em qual areia ela chega. Quem sabe na sua.",
 "ja": "見たこともない岸辺で、いままさに見知らぬ誰かが瓶にコルクを押し込んでいる。次にどの砂に届くかは海が決める。もしかしたら、あなたの砂に。"},

"Who you are here": {
 "it": "Chi sei, qui", "es": "Quién eres aquí", "fr": "Qui tu es ici",
 "de": "Wer du hier bist", "pt-BR": "Quem você é aqui", "ja": "ここでのあなた"},

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
 "fr": "Ils t'écrivent peut-être dans une langue que tu n'as jamais lue. Une touche la met dans la tienne ; une autre remet leurs mots exactement comme ils les ont écrits.",
 "de": "Vielleicht schreibt dir jemand in einer Sprache, die du nie gelesen hast. Ein Tippen macht sie zu deiner; ein weiteres stellt die fremden Worte wieder her, genau so, wie sie geschrieben wurden.",
 "pt-BR": "Pode ser que escrevam para você numa língua que você nunca leu. Um toque a transforma na sua; outro devolve as palavras deles exatamente como foram escritas.",
 "ja": "読んだことのない言語で書かれてくるかもしれない。ひと押しで自分の言葉になり、もうひと押しで、書かれたとおりの言葉に戻る。"},

"What you keep": {
 "it": "Quello che conservi", "es": "Lo que conservas", "fr": "Ce que tu gardes",
 "de": "Was bleibt", "pt-BR": "O que você guarda", "ja": "手元に残るもの"},

"A correspondence, not a chat.": {
 "it": "Un carteggio, non una chat.", "es": "Una correspondencia, no un chat.",
 "fr": "Une correspondance, pas une conversation.", "de": "Ein Briefwechsel, kein Chat.",
 "pt-BR": "Uma correspondência, não um chat.", "ja": "チャットではなく、文通。"},

"Letters do not scroll away here. They stay in a journal made of paper, in the order the sea delivered them — yours on one side, theirs on the other, each with the day it came ashore written underneath.": {
 "it": "Qui le lettere non scorrono via. Restano in un diario di carta, nell'ordine in cui il mare le ha consegnate — le tue da una parte, le loro dall'altra, ognuna con sotto il giorno in cui è approdata.",
 "es": "Aquí las cartas no se van con el desplazamiento. Se quedan en un diario de papel, en el orden en que el mar las entregó: las tuyas de un lado, las suyas del otro, cada una con el día en que llegó a la orilla escrito debajo.",
 "fr": "Ici, les lettres ne défilent pas au loin. Elles restent dans un journal de papier, dans l'ordre où la mer les a remises — les tiennes d'un côté, les leurs de l'autre, chacune avec, en dessous, le jour où elle a abordé.",
 "de": "Hier scrollen Briefe nicht davon. Sie bleiben in einem Tagebuch aus Papier, in der Reihenfolge, in der das Meer sie brachte — deine auf der einen Seite, ihre auf der anderen, jeder mit dem Tag darunter, an dem er anlandete.",
 "pt-BR": "Aqui as cartas não somem com a rolagem. Elas ficam num diário de papel, na ordem em que o mar as entregou — as suas de um lado, as dele do outro, cada uma com o dia em que chegou escrito embaixo.",
 "ja": "ここでは手紙が流れて消えたりしない。紙の日誌に、海が届けた順のまま残る。自分のものは片側に、相手のものは反対側に、それぞれの下に岸へ着いた日が書かれている。"},

"You may give a stranger a private name, only for your own pages:": {
 "it": "A uno sconosciuto puoi dare un nome privato, solo per le tue pagine:",
 "es": "A un desconocido puedes darle un nombre privado, solo para tus páginas:",
 "fr": "Tu peux donner à un inconnu un nom privé, rien que pour tes pages :",
 "de": "Einem Fremden darfst du einen eigenen Namen geben, nur für deine Seiten:",
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
 "fr": ". Ils ne le sauront jamais. Et lorsqu'une de leurs bouteilles est encore sur l'eau, le journal le dit simplement, et te demande d'attendre.",
 "de": ". Sie werden es nie erfahren. Und wenn eine Flasche von ihnen noch auf dem Wasser ist, sagt das Tagebuch es einfach und bittet dich zu warten.",
 "pt-BR": ". Eles nunca vão saber. E quando uma garrafa deles ainda está na água, o diário simplesmente diz isso, e pede que você espere.",
 "ja": "。相手がそれを知ることはない。相手の瓶がまだ海の上にあるときは、日誌がそう告げて、待つように言うだけだ。"},

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

"A real beach, and not one you picked.": {
 "it": "Una spiaggia vera, e non l'hai scelta tu.",
 "es": "Una playa de verdad, y no la has elegido tú.",
 "fr": "Une vraie plage, et ce n'est pas toi qui l'as choisie.",
 "de": "Ein wirklicher Strand — und keiner, den du ausgesucht hast.",
 "pt-BR": "Uma praia de verdade, e não foi você que escolheu.",
 "ja": "本物の浜辺。しかも、自分で選んだのではない。"},
"Cala Goloritzé. Reynisfjara. Anse Source d'Argent. True stretches of coast at their true coordinates — and yours is drawn by lot. The storm decides where it leaves you, and from that morning on it is home. The light on it is the light of your own hour: open it at midnight and your beach is dark, with the stars out over the water. Not one of these is a photograph. Every wave is drawn by the app, line by line.": {
 "it": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Tratti di costa veri alle loro coordinate vere — e la tua te la dà la sorte. Decide la tempesta dove lasciarti, e da quella mattina è casa. La luce che ci sta sopra è quella della tua ora: aprila a mezzanotte e la tua spiaggia è buia, con le stelle sull'acqua. Nessuna di queste è una fotografia. Ogni onda la disegna l'app, linea per linea.",
 "es": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Tramos de costa reales en sus coordenadas reales, y la tuya te toca en suerte. La tormenta decide dónde dejarte, y desde esa mañana es tu casa. La luz que la baña es la de tu propia hora: ábrela a medianoche y tu playa está a oscuras, con las estrellas sobre el agua. Ninguna de estas es una fotografía. Cada ola la dibuja la app, línea a línea.",
 "fr": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. De vraies portions de côte à leurs vraies coordonnées — et la tienne t'échoit au hasard. C'est la tempête qui décide où elle te laisse, et dès ce matin-là c'est chez toi. La lumière qui la baigne est celle de ta propre heure : ouvre à minuit et ta plage est sombre, les étoiles au-dessus de l'eau. Aucune n'est une photographie. Chaque vague est dessinée par l'application, trait par trait.",
 "de": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Echte Küstenstücke an ihren echten Koordinaten — und deines fällt dir durch Los zu. Der Sturm entscheidet, wo er dich zurücklässt, und von jenem Morgen an ist es dein Zuhause. Das Licht darauf ist das deiner eigenen Stunde: öffne sie um Mitternacht, und dein Strand ist dunkel, die Sterne über dem Wasser. Keines davon ist eine Fotografie. Jede Welle zeichnet die App, Strich für Strich.",
 "pt-BR": "Cala Goloritzé. Reynisfjara. Anse Source d'Argent. Trechos de costa reais nas coordenadas reais — e a sua vem por sorteio. A tempestade decide onde deixar você, e daquela manhã em diante é casa. A luz sobre ela é a da sua própria hora: abra à meia-noite e a sua praia está escura, com as estrelas sobre a água. Nenhuma delas é uma fotografia. Cada onda é desenhada pelo app, linha por linha.",
 "ja": "カーラ・ゴロリッツェ。レイニスフィヤラ。アンス・スルス・ダルジャン。実在する海岸を、実在する座標のままに。そして自分の浜は、くじで決まる。どこに打ち上げるかを決めるのは嵐で、その朝からそこが家になる。射す光はあなたのいまの時刻の光だ。真夜中に開けば浜は暗く、水の上に星が出ている。どれも写真ではない。波の一本一本を、アプリが線で描いている。"},


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

"The islands of strangers whose letters you have read stay marked there for good — a private map of everyone the sea has introduced you to.": {
 "it": "Le isole degli sconosciuti di cui hai letto le lettere restano segnate per sempre — una mappa privata di tutti quelli che il mare ti ha presentato.",
 "es": "Las islas de los desconocidos cuyas cartas has leído quedan marcadas para siempre: un mapa privado de todos los que el mar te ha presentado.",
 "fr": "Les îles des inconnus dont tu as lu les lettres restent marquées pour de bon — une carte privée de tous ceux que la mer t'a présentés.",
 "de": "Die Inseln der Fremden, deren Briefe du gelesen hast, bleiben für immer eingezeichnet — eine private Karte all jener, die das Meer dir vorgestellt hat.",
 "pt-BR": "As ilhas dos desconhecidos cujas cartas você leu ficam marcadas para sempre — um mapa particular de todos que o mar apresentou a você.",
 "ja": "手紙を読んだ相手の島は、そのまま海図に残りつづける。海が引き合わせてくれた人たちだけの、自分だけの地図になる。"},

"The chart is the app's own: coastlines from Natural Earth, public domain, carried inside it. No map service is ever called, and nothing about where you are leaves your hands.": {
 "it": "La carta è tutta dell'app: coste da Natural Earth, di pubblico dominio, portate dentro. Nessun servizio di mappe viene mai chiamato, e niente di dove sei esce dalle tue mani.",
 "es": "La carta es de la propia app: costas de Natural Earth, de dominio público, llevadas dentro. Nunca se llama a ningún servicio de mapas, y nada sobre dónde estás sale de tus manos.",
 "fr": "La carte appartient à l'application : côtes issues de Natural Earth, domaine public, embarquées avec elle. Aucun service cartographique n'est jamais appelé, et rien de ta position ne quitte tes mains.",
 "de": "Die Karte gehört der App selbst: Küstenlinien von Natural Earth, gemeinfrei, im Programm mitgeführt. Kein Kartendienst wird je aufgerufen, und nichts über deinen Standort verlässt deine Hände.",
 "pt-BR": "A carta é do próprio app: costas do Natural Earth, de domínio público, carregadas dentro dele. Nenhum serviço de mapas é chamado, e nada sobre onde você está sai das suas mãos.",
 "ja": "海図はアプリ自身のものだ。海岸線はパブリックドメインの Natural Earth を内部に持っている。地図サービスを呼ぶことは一度もなく、あなたの居場所に関する情報が手元から出ていくこともない。"},

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

"Two iPhone screens against a blurred sunset. On the left, the beach of Luskentyre with a bottle washed up on the sand, at 20:41 on a Thursday. On the right, an open letter from a stranger, at 13:41 on the Friday. Between them, empty space and the words «seventeen hours».": {
 "it": "Due schermi di iPhone su un tramonto sfocato. A sinistra la spiaggia di Luskentyre con una bottiglia approdata sulla sabbia, alle 20:41 di giovedì. A destra la lettera aperta di uno sconosciuto, alle 13:41 di venerdì. In mezzo, spazio vuoto e le parole «seventeen hours».",
 "es": "Dos pantallas de iPhone sobre un atardecer desenfocado. A la izquierda, la playa de Luskentyre con una botella varada en la arena, a las 20:41 de un jueves. A la derecha, la carta abierta de un desconocido, a las 13:41 del viernes. Entre ambas, espacio vacío y las palabras «seventeen hours».",
 "fr": "Deux écrans d'iPhone sur un coucher de soleil flou. À gauche, la plage de Luskentyre avec une bouteille échouée sur le sable, à 20h41 un jeudi. À droite, la lettre ouverte d'un inconnu, à 13h41 le vendredi. Entre les deux, du vide et les mots « seventeen hours ».",
 "de": "Zwei iPhone-Bildschirme vor einem unscharfen Sonnenuntergang. Links der Strand von Luskentyre mit einer angespülten Flasche im Sand, donnerstags um 20:41 Uhr. Rechts der offene Brief einer fremden Person, freitags um 13:41 Uhr. Dazwischen leerer Raum und die Worte «seventeen hours».",
 "pt-BR": "Duas telas de iPhone sobre um pôr do sol desfocado. À esquerda, a praia de Luskentyre com uma garrafa encalhada na areia, às 20h41 de uma quinta-feira. À direita, a carta aberta de um desconhecido, às 13h41 da sexta. Entre elas, espaço vazio e as palavras «seventeen hours».",
 "ja": "ぼかした夕焼けを背にした二つの iPhone の画面。左は木曜日の20時41分、砂に打ち上げられた瓶のあるラスケンタイアの浜。右は金曜日の13時41分、見知らぬ誰かからの開いた手紙。その間には余白と「seventeen hours」の文字。"},

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

"Bottlegram is a messaging app for strangers. You write a letter, seal it in a bottle and give it to the current. Six to thirty-six hours later it washes up on another castaway’s beach, somewhere in the world. Then it is their turn to wait. Free on iPhone.": {
 "it": "Bottlegram è un'app di messaggi fra sconosciuti. Scrivi una lettera, la chiudi in una bottiglia e la affidi alla corrente. Da sei a trentasei ore dopo approda sulla spiaggia di un altro naufrago, da qualche parte nel mondo. E poi tocca a lui aspettare. Gratis su iPhone.",
 "es": "Bottlegram es una app de mensajes entre desconocidos. Escribes una carta, la cierras en una botella y la entregas a la corriente. Entre seis y treinta y seis horas después llega a la playa de otro náufrago, en algún lugar del mundo. Y entonces le toca esperar a él. Gratis en iPhone.",
 "fr": "Bottlegram est une application de messages entre inconnus. Vous écrivez une lettre, vous la scellez dans une bouteille et vous la confiez au courant. Six à trente-six heures plus tard, elle échoue sur la plage d'un autre naufragé, quelque part dans le monde. Et c'est à lui d'attendre. Gratuit sur iPhone.",
 "de": "Bottlegram ist eine Nachrichten-App für Fremde. Sie schreiben einen Brief, verschließen ihn in einer Flasche und übergeben ihn der Strömung. Sechs bis sechsunddreißig Stunden später wird er an den Strand eines anderen Gestrandeten gespült, irgendwo auf der Welt. Und dann ist das Warten an ihm. Kostenlos für iPhone.",
 "pt-BR": "Bottlegram é um app de mensagens entre desconhecidos. Você escreve uma carta, fecha numa garrafa e entrega à correnteza. De seis a trinta e seis horas depois ela chega à praia de outro náufrago, em algum lugar do mundo. E então é a vez dele esperar. Grátis no iPhone.",
 "ja": "Bottlegram は見知らぬ人どうしのメッセージアプリです。手紙を書き、瓶に封じ、潮に託します。六時間から三十六時間後、世界のどこかで別の漂流者の浜に流れ着きます。そして今度はその人が待つ番です。iPhone で無料。"},

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

"I love walking on beaches, and I have done since I was a boy. Since I was a boy I have been looking for the same thing in the sand: a bottle with a letter inside, written years earlier by someone I would never meet, telling me something true about their life.": {
 "it": "Amo camminare sulle spiagge, e lo faccio da quando ero bambino. E da quando ero bambino cerco nella sabbia sempre la stessa cosa: una bottiglia con dentro una lettera, scritta anni prima da qualcuno che non incontrerò mai, che mi racconta qualcosa di vero della sua vita.",
 "es": "Me encanta caminar por las playas, y lo hago desde niño. Y desde niño busco en la arena siempre lo mismo: una botella con una carta dentro, escrita años antes por alguien a quien nunca conoceré, que me cuenta algo verdadero de su vida.",
 "fr": "J'aime marcher sur les plages, et je le fais depuis l'enfance. Et depuis l'enfance je cherche dans le sable toujours la même chose : une bouteille avec une lettre dedans, écrite des années plus tôt par quelqu'un que je ne rencontrerai jamais, et qui me raconte quelque chose de vrai sur sa vie.",
 "de": "Ich liebe es, an Stränden zu gehen, und tue es, seit ich ein Junge war. Und seit ich ein Junge war, suche ich im Sand immer dasselbe: eine Flasche mit einem Brief darin, Jahre zuvor geschrieben von jemandem, dem ich nie begegnen werde, und der mir etwas Wahres aus seinem Leben erzählt.",
 "pt-BR": "Amo caminhar pelas praias, e faço isso desde menino. E desde menino procuro na areia sempre a mesma coisa: uma garrafa com uma carta dentro, escrita anos antes por alguém que nunca vou encontrar, contando algo verdadeiro da sua vida.",
 "ja": "浜を歩くのが好きで、子どもの頃からずっと歩いています。そして子どもの頃からずっと、砂の中に同じものを探しています。中に手紙の入った瓶。何年も前に、二度と会うことのない誰かが書いた、その人の人生の本当のことが記された手紙です。"},

"I have never found one.": {
 "it": "Non l'ho mai trovata.",
 "es": "Nunca la he encontrado.",
 "fr": "Je n'en ai jamais trouvé.",
 "de": "Gefunden habe ich nie eine.",
 "pt-BR": "Nunca encontrei nenhuma.",
 "ja": "一度も見つかりませんでした。"},

"So I built it. Two hundred and fifty beaches drawn by hand, and a tide that carries a bottle along the real sea route between two coasts, taking the time that much water would take.": {
 "it": "Così me la sono costruita. Duecentocinquanta spiagge disegnate a mano, e una marea che porta una bottiglia lungo la rotta di mare vera fra due coste, prendendosi il tempo che ci vorrebbe per tutta quell'acqua.",
 "es": "Así que me la construí. Doscientas cincuenta playas dibujadas a mano, y una marea que lleva una botella por la ruta marina real entre dos costas, tomándose el tiempo que haría falta para toda esa agua.",
 "fr": "Alors je l'ai construite. Deux cent cinquante plages dessinées à la main, et une marée qui porte une bouteille le long de la vraie route maritime entre deux côtes, en prenant le temps qu'il faudrait pour toute cette eau.",
 "de": "Also habe ich sie gebaut. Zweihundertfünfzig von Hand gezeichnete Strände und eine Tide, die eine Flasche entlang der echten Seeroute zwischen zwei Küsten trägt und sich dafür die Zeit nimmt, die all dieses Wasser brauchen würde.",
 "pt-BR": "Então eu a construí. Duzentas e cinquenta praias desenhadas à mão, e uma maré que leva uma garrafa pela rota marítima real entre duas costas, levando o tempo que toda aquela água levaria.",
 "ja": "だから自分で作りました。手で描いた二百五十の浜と、二つの海岸のあいだの実際の航路に沿って瓶を運ぶ潮。それだけの海を渡るのにかかるはずの時間を、そのままかけて。"},

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

"You write to nobody in particular": {
 "it": "Scrivi a nessuno in particolare",
 "es": "Escribes a nadie en particular",
 "fr": "Vous écrivez à personne en particulier",
 "de": "Sie schreiben an niemanden bestimmten",
 "pt-BR": "Você escreve para ninguém em particular",
 "ja": "宛先のない手紙を書く"},

"Every day the sea leaves you three bottles. You put a letter in one and hand it to the current. There is no address on it, and the sea chooses who receives it.": {
 "it": "Ogni giorno il mare ti lascia tre bottiglie. Ci metti dentro una lettera e la affidi alla corrente. Sopra non c'è un indirizzo, e chi la riceve lo sceglie il mare.",
 "es": "Cada día el mar te deja tres botellas. Metes dentro una carta y la entregas a la corriente. No lleva dirección, y quién la recibe lo elige el mar.",
 "fr": "Chaque jour la mer vous laisse trois bouteilles. Vous glissez une lettre dans l'une d'elles et vous la confiez au courant. Il n'y a pas d'adresse dessus, et c'est la mer qui choisit qui la reçoit.",
 "de": "Jeden Tag lässt Ihnen das Meer drei Flaschen. Sie legen einen Brief hinein und geben ihn der Strömung. Eine Adresse steht nicht darauf, und wer ihn bekommt, entscheidet das Meer.",
 "pt-BR": "Todo dia o mar deixa três garrafas para você. Você põe uma carta dentro e a entrega à correnteza. Não há endereço nela, e quem a recebe é o mar que escolhe.",
 "ja": "海は毎日、三本の瓶をあなたに残します。その一本に手紙を入れ、潮に託します。宛名はなく、誰の手に渡るかは海が決めます。"},

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

"They can answer, and often they do": {
 "it": "Può rispondere, e spesso lo fa",
 "es": "Puede responder, y a menudo lo hace",
 "fr": "Il peut répondre, et souvent il le fait",
 "de": "Sie können antworten, und oft tun sie es",
 "pt-BR": "Pode responder, e muitas vezes responde",
 "ja": "返事が来ることもある"},

"Whoever finds your letter can write back, and the sea takes its own time to deliver the answer. A correspondence alternates: you write, they answer, you write again. Everything you choose to keep goes into a journal that stays on your beach.": {
 "it": "Chi trova la tua lettera può risponderti, e il mare si prende il suo tempo per consegnarti la risposta. Una corrispondenza si alterna: scrivi tu, risponde lui, scrivi di nuovo. Tutto quello che decidi di tenere finisce in un diario che resta sulla tua spiaggia.",
 "es": "Quien encuentre tu carta puede responderte, y el mar se toma su tiempo para entregarte la respuesta. Una correspondencia se alterna: escribes tú, responde él, vuelves a escribir. Todo lo que decides guardar va a un diario que se queda en tu playa.",
 "fr": "Celui qui trouve votre lettre peut vous répondre, et la mer prend son temps pour vous livrer la réponse. Une correspondance alterne : vous écrivez, il répond, vous écrivez de nouveau. Tout ce que vous choisissez de garder va dans un journal qui reste sur votre plage.",
 "de": "Wer Ihren Brief findet, kann zurückschreiben, und das Meer lässt sich Zeit, Ihnen die Antwort zu bringen. Ein Briefwechsel wechselt sich ab: Sie schreiben, die andere Person antwortet, Sie schreiben wieder. Alles, was Sie behalten wollen, kommt in ein Tagebuch, das an Ihrem Strand bleibt.",
 "pt-BR": "Quem encontrar sua carta pode responder, e o mar leva o tempo dele para entregar a resposta. Uma correspondência se alterna: você escreve, a pessoa responde, você escreve de novo. Tudo o que você decidir guardar vai para um diário que fica na sua praia.",
 "ja": "手紙を見つけた人は返事を書くことができ、それを届けるのに海はまた時間をかけます。文通は交互に進みます。あなたが書き、相手が答え、またあなたが書く。残したいと思ったものはすべて、あなたの浜にとどまる日誌に収められます。"},

"And then there are the spirits": {
 "it": "E poi ci sono gli spiriti",
 "es": "Y luego están los espíritus",
 "fr": "Et puis il y a les esprits",
 "de": "Und dann sind da die Geister",
 "pt-BR": "E então há os espíritos",
 "ja": "そして、海の魂たち"},

"Twelve souls live in this sea. They are not castaways: they have been here far longer, each with a life of their own to tell, and every so often one of them picks up a bottle and writes to you. No two of them tell the same story. If a spirit writes to you, you were lucky. Their letters always carry their mark, an artificial intelligence gives them their words, and the": {
 "it": "In questo mare vivono dodici anime. Non sono naufraghi: stanno qui da molto più tempo, ognuna con una vita sua da raccontare, e ogni tanto una di loro prende una bottiglia e scrive a te. Non ce ne sono due che raccontino la stessa storia. Se ti scrive uno spirito, sei stato fortunato. Le loro lettere portano sempre il loro segno, le parole gliele dà un'intelligenza artificiale, e la",
 "es": "En este mar viven doce almas. No son náufragos: llevan aquí mucho más tiempo, cada una con una vida propia que contar, y de vez en cuando una de ellas coge una botella y te escribe. No hay dos que cuenten la misma historia. Si te escribe un espíritu, has tenido suerte. Sus cartas llevan siempre su marca, las palabras se las da una inteligencia artificial, y la",
 "fr": "Douze âmes vivent dans cette mer. Ce ne sont pas des naufragés : elles sont ici depuis bien plus longtemps, chacune avec sa propre vie à raconter, et de temps en temps l'une d'elles prend une bouteille et vous écrit. Il n'y en a pas deux qui racontent la même histoire. Si un esprit vous écrit, vous avez eu de la chance. Leurs lettres portent toujours leur marque, une intelligence artificielle leur donne leurs mots, et la",
 "de": "In diesem Meer leben zwölf Seelen. Sie sind keine Gestrandeten: Sie sind weit länger hier, jede mit einem eigenen Leben zu erzählen, und hin und wieder nimmt eine von ihnen eine Flasche und schreibt Ihnen. Keine zwei erzählen dieselbe Geschichte. Wenn ein Geist Ihnen schreibt, hatten Sie Glück. Ihre Briefe tragen immer ihr Zeichen, eine künstliche Intelligenz gibt ihnen ihre Worte, und die",
 "pt-BR": "Neste mar vivem doze almas. Não são náufragos: estão aqui há muito mais tempo, cada uma com uma vida própria para contar, e de vez em quando uma delas pega uma garrafa e escreve para você. Não há duas que contem a mesma história. Se um espírito escrever para você, você teve sorte. As cartas deles trazem sempre a sua marca, as palavras vêm de uma inteligência artificial, e a",
 "ja": "この海には十二の魂が暮らしています。彼らは漂流者ではありません。ずっと前からここにいて、それぞれに語るべき生涯を持ち、ときおりそのうちの一人が瓶を手に取り、あなたに手紙を書きます。同じ物語を語る者は二人といません。魂から手紙が届いたなら、あなたは幸運でした。その手紙には必ず彼らの印があり、言葉は人工知能が与えています。あなたが書き返した言葉に何が起きるかは、"},

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

"Coming soon": {
 "it": "Prossimamente",
 "es": "Próximamente",
 "fr": "Bientôt",
 "de": "Demnächst",
 "pt-BR": "Em breve",
 "ja": "近日公開"},

"Francesco Gola, seascape photographer, Italy": {
 "it": "Francesco Gola, fotografo di paesaggio marino, Italia",
 "es": "Francesco Gola, fotógrafo de paisaje marino, Italia",
 "fr": "Francesco Gola, photographe de paysages marins, Italie",
 "de": "Francesco Gola, Seelandschaftsfotograf, Italien",
 "pt-BR": "Francesco Gola, fotógrafo de paisagem marinha, Itália",
 "ja": "フランチェスコ・ゴーラ（海景写真家、イタリア）"},

"Free · optional in-app purchases, €0.99 – €4.99": {
 "it": "Gratis · acquisti in-app facoltativi, 0,99 € – 4,99 €",
 "es": "Gratis · compras dentro de la app opcionales, 0,99 € – 4,99 €",
 "fr": "Gratuit · achats intégrés facultatifs, 0,99 € – 4,99 €",
 "de": "Kostenlos · optionale In-App-Käufe, 0,99 € – 4,99 €",
 "pt-BR": "Grátis · compras no app opcionais, € 0,99 – € 4,99",
 "ja": "無料 · 任意のアプリ内課金 0.99 € – 4.99 €"},

"English, Italian, German, Spanish, French, Japanese, Brazilian Portuguese": {
 "it": "Inglese, italiano, tedesco, spagnolo, francese, giapponese, portoghese brasiliano",
 "es": "Inglés, italiano, alemán, español, francés, japonés, portugués de Brasil",
 "fr": "Anglais, italien, allemand, espagnol, français, japonais, portugais brésilien",
 "de": "Englisch, Italienisch, Deutsch, Spanisch, Französisch, Japanisch, brasilianisches Portugiesisch",
 "pt-BR": "Inglês, italiano, alemão, espanhol, francês, japonês, português do Brasil",
 "ja": "英語、イタリア語、ドイツ語、スペイン語、フランス語、日本語、ブラジルポルトガル語"},

"beaches drawn by hand, each one different at dawn, at midday, at dusk and at night": {
 "it": "spiagge disegnate a mano, ognuna diversa all'alba, a mezzogiorno, al tramonto e di notte",
 "es": "playas dibujadas a mano, cada una distinta al alba, al mediodía, al atardecer y de noche",
 "fr": "plages dessinées à la main, chacune différente à l'aube, à midi, au crépuscule et la nuit",
 "de": "von Hand gezeichnete Strände, jeder anders im Morgengrauen, mittags, in der Dämmerung und nachts",
 "pt-BR": "praias desenhadas à mão, cada uma diferente ao amanhecer, ao meio-dia, ao entardecer e à noite",
 "ja": "手描きの浜。夜明け、正午、夕暮れ、夜でそれぞれ違う表情になる"},

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

"Images and video": {
 "it": "Immagini e video",
 "es": "Imágenes y vídeo",
 "fr": "Images et vidéo",
 "de": "Bilder und Video",
 "pt-BR": "Imagens e vídeo",
 "ja": "画像と動画"},

"Everything here may be reproduced freely in coverage of Bottlegram, in print or online, with or without credit.": {
 "it": "Tutto quello che c'è qui si può riprodurre liberamente parlando di Bottlegram, su carta o online, con o senza credito.",
 "es": "Todo lo que hay aquí puede reproducirse libremente al hablar de Bottlegram, en papel o en línea, con o sin crédito.",
 "fr": "Tout ce qui se trouve ici peut être reproduit librement dans un article sur Bottlegram, sur papier ou en ligne, avec ou sans crédit.",
 "de": "Alles hier darf in der Berichterstattung über Bottlegram frei verwendet werden, gedruckt oder online, mit oder ohne Quellenangabe.",
 "pt-BR": "Tudo o que está aqui pode ser reproduzido livremente ao falar do Bottlegram, no papel ou online, com ou sem crédito.",
 "ja": "ここにあるものはすべて、Bottlegram を紹介する記事で自由に使えます。紙でもオンラインでも、クレジットの有無を問いません。"},

"A beach at the end of the world: a dark shore under stars.": {
 "it": "Una spiaggia alla fine del mondo: una riva scura sotto le stelle.",
 "es": "Una playa en el fin del mundo: una orilla oscura bajo las estrellas.",
 "fr": "Une plage au bout du monde : un rivage sombre sous les étoiles.",
 "de": "Ein Strand am Ende der Welt: ein dunkles Ufer unter Sternen.",
 "pt-BR": "Uma praia no fim do mundo: uma orla escura sob as estrelas.",
 "ja": "世界の果ての浜。星の下の暗い岸辺。"},

"Every tide brings a stranger: a beach at sunset with bottles on the sand.": {
 "it": "Ogni marea porta uno sconosciuto: una spiaggia al tramonto con bottiglie sulla sabbia.",
 "es": "Cada marea trae a un desconocido: una playa al atardecer con botellas en la arena.",
 "fr": "Chaque marée amène un inconnu : une plage au coucher du soleil avec des bouteilles sur le sable.",
 "de": "Jede Tide bringt eine fremde Person: ein Strand bei Sonnenuntergang mit Flaschen im Sand.",
 "pt-BR": "Cada maré traz um desconhecido: uma praia ao pôr do sol com garrafas na areia.",
 "ja": "潮が満ちるたび見知らぬ誰かが来る。夕暮れの浜、砂の上の瓶。"},

"Nobody here knows your name: a bright daytime beach.": {
 "it": "Qui nessuno sa il tuo nome: una spiaggia luminosa di giorno.",
 "es": "Aquí nadie sabe tu nombre: una playa luminosa de día.",
 "fr": "Ici personne ne connaît votre nom : une plage lumineuse en plein jour.",
 "de": "Hier kennt niemand Ihren Namen: ein heller Strand bei Tag.",
 "pt-BR": "Aqui ninguém sabe seu nome: uma praia luminosa de dia.",
 "ja": "ここでは誰もあなたの名を知らない。明るい昼の浜。"},

"The nautical chart, with a bottle drifting between two coasts.": {
 "it": "La carta nautica, con una bottiglia che va da una costa all'altra.",
 "es": "La carta náutica, con una botella que va de una costa a otra.",
 "fr": "La carte marine, avec une bouteille qui dérive d'une côte à l'autre.",
 "de": "Die Seekarte, mit einer Flasche, die zwischen zwei Küsten treibt.",
 "pt-BR": "A carta náutica, com uma garrafa indo de uma costa a outra.",
 "ja": "海図。二つの海岸のあいだを漂う瓶。"},

"An open correspondence: a letter written to a stranger and the stranger's reply.": {
 "it": "Una corrispondenza aperta: una lettera scritta a uno sconosciuto e la sua risposta.",
 "es": "Una correspondencia abierta: una carta escrita a un desconocido y su respuesta.",
 "fr": "Une correspondance ouverte : une lettre écrite à un inconnu et sa réponse.",
 "de": "Ein offener Briefwechsel: ein Brief an eine fremde Person und deren Antwort.",
 "pt-BR": "Uma correspondência aberta: uma carta escrita a um desconhecido e a resposta dele.",
 "ja": "開かれた文通。見知らぬ人へ書いた手紙と、その返事。"},

"The journal, keeping every letter that reached this beach.": {
 "it": "Il diario, che conserva ogni lettera arrivata su questa spiaggia.",
 "es": "El diario, que guarda cada carta que llegó a esta playa.",
 "fr": "Le journal, qui garde chaque lettre arrivée sur cette plage.",
 "de": "Das Tagebuch, das jeden Brief bewahrt, der diesen Strand erreicht hat.",
 "pt-BR": "O diário, que guarda cada carta que chegou a esta praia.",
 "ja": "この浜に届いたすべての手紙を残す日誌。"},

"A bottle just thrown, drifting on a night sea.": {
 "it": "Una bottiglia appena lanciata, alla deriva su un mare notturno.",
 "es": "Una botella recién lanzada, a la deriva en un mar nocturno.",
 "fr": "Une bouteille tout juste jetée, à la dérive sur une mer nocturne.",
 "de": "Eine gerade geworfene Flasche, treibend auf nächtlichem Meer.",
 "pt-BR": "Uma garrafa recém-lançada, à deriva num mar noturno.",
 "ja": "投げたばかりの瓶が、夜の海を漂う。"},

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

"Bottlegram is not on the App Store yet. Write to this address and you get a TestFlight build, along with a beach of your own and enough bottles to see what comes back:": {
 "it": "Bottlegram non è ancora sull'App Store. Scrivi a questo indirizzo e ricevi una build TestFlight, con una spiaggia tua e bottiglie a sufficienza per vedere cosa torna indietro:",
 "es": "Bottlegram todavía no está en la App Store. Escribe a esta dirección y recibirás una build de TestFlight, con una playa propia y botellas suficientes para ver qué vuelve:",
 "fr": "Bottlegram n'est pas encore sur l'App Store. Écrivez à cette adresse et vous recevrez une version TestFlight, avec une plage à vous et assez de bouteilles pour voir ce qui revient :",
 "de": "Bottlegram ist noch nicht im App Store. Schreiben Sie an diese Adresse und Sie erhalten einen TestFlight-Build, dazu einen eigenen Strand und genug Flaschen, um zu sehen, was zurückkommt:",
 "pt-BR": "O Bottlegram ainda não está na App Store. Escreva para este endereço e você recebe uma build do TestFlight, com uma praia sua e garrafas suficientes para ver o que volta:",
 "ja": "Bottlegram はまだ App Store にありません。このアドレスに連絡いただければ TestFlight のビルドをお送りします。あなた専用の浜と、何が返ってくるかを確かめるのに十分な数の瓶つきで。"},

"The same address reaches Francesco directly for an interview, a question, or a detail this page does not cover.": {
 "it": "Lo stesso indirizzo arriva direttamente a Francesco per un'intervista, una domanda, o un dettaglio che questa pagina non copre.",
 "es": "La misma dirección llega directamente a Francesco para una entrevista, una pregunta o un detalle que esta página no cubre.",
 "fr": "La même adresse joint directement Francesco pour une interview, une question, ou un détail que cette page ne couvre pas.",
 "de": "Dieselbe Adresse erreicht Francesco direkt, für ein Interview, eine Frage oder ein Detail, das diese Seite nicht abdeckt.",
 "pt-BR": "O mesmo endereço chega diretamente ao Francesco para uma entrevista, uma pergunta ou um detalhe que esta página não cobre.",
 "ja": "同じアドレスはフランチェスコ本人に直接届きます。取材のご依頼、ご質問、このページにない詳細などはこちらへ。"},

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

"Twelve souls live in this sea. They are not castaways: they have been here far longer, each with a life of their own to tell, and every so often one of them picks up a bottle and writes to you. No two of them tell the same story. If a spirit writes to you, you were lucky. Their letters always carry their mark, and an artificial intelligence gives them their words.": {
 "it": "In questo mare vivono dodici anime. Non sono naufraghi: stanno qui da molto più tempo, ognuna con una vita sua da raccontare, e ogni tanto una di loro prende una bottiglia e scrive a te. Non ce ne sono due che raccontino la stessa storia. Se ti scrive uno spirito, sei stato fortunato. Le loro lettere portano sempre il loro segno, e le parole gliele dà un'intelligenza artificiale.",
 "es": "En este mar viven doce almas. No son náufragos: llevan aquí mucho más tiempo, cada una con una vida propia que contar, y de vez en cuando una de ellas coge una botella y te escribe. No hay dos que cuenten la misma historia. Si te escribe un espíritu, has tenido suerte. Sus cartas llevan siempre su marca, y las palabras se las da una inteligencia artificial.",
 "fr": "Douze âmes vivent dans cette mer. Ce ne sont pas des naufragés : elles sont ici depuis bien plus longtemps, chacune avec sa propre vie à raconter, et de temps en temps l'une d'elles prend une bouteille et vous écrit. Il n'y en a pas deux qui racontent la même histoire. Si un esprit vous écrit, vous avez eu de la chance. Leurs lettres portent toujours leur marque, et une intelligence artificielle leur donne leurs mots.",
 "de": "In diesem Meer leben zwölf Seelen. Sie sind keine Gestrandeten: Sie sind weit länger hier, jede mit einem eigenen Leben zu erzählen, und hin und wieder nimmt eine von ihnen eine Flasche und schreibt Ihnen. Keine zwei erzählen dieselbe Geschichte. Wenn ein Geist Ihnen schreibt, hatten Sie Glück. Ihre Briefe tragen immer ihr Zeichen, und eine künstliche Intelligenz gibt ihnen ihre Worte.",
 "pt-BR": "Neste mar vivem doze almas. Não são náufragos: estão aqui há muito mais tempo, cada uma com uma vida própria para contar, e de vez em quando uma delas pega uma garrafa e escreve para você. Não há duas que contem a mesma história. Se um espírito escrever para você, você teve sorte. As cartas deles trazem sempre a sua marca, e as palavras vêm de uma inteligência artificial.",
 "ja": "この海には十二の魂が暮らしています。彼らは漂流者ではありません。ずっと前からここにいて、それぞれに語るべき生涯を持ち、ときおりそのうちの一人が瓶を手に取り、あなたに手紙を書きます。同じ物語を語る者は二人といません。魂から手紙が届いたなら、あなたは幸運でした。その手紙には必ず彼らの印があり、言葉は人工知能が与えています。"},

"Somewhere a phone is buzzing and someone is waiting for an answer. Not here.": {
 "it": "Da qualche parte un telefono sta vibrando e qualcuno aspetta una risposta. Qui no.",
 "es": "En algún sitio un teléfono está vibrando y alguien espera una respuesta. Aquí no.",
 "fr": "Quelque part un téléphone vibre et quelqu'un attend une réponse. Ici, non.",
 "de": "Irgendwo vibriert ein Telefon und jemand wartet auf eine Antwort. Hier nicht.",
 "pt-BR": "Em algum lugar um telefone está vibrando e alguém espera uma resposta. Aqui não.",
 "ja": "どこかで電話が震え、誰かが返事を待っています。ここでは違います。"},

"Here your letter is at sea, and the sea can take more than a day to deliver a message. Nothing to check, nothing owed to anyone, nobody typing. It ends up on a beach you have never seen, and a stranger decides whether to write back.": {
 "it": "Qui la tua lettera è in mare, e il mare ci può mettere più di un giorno per consegnare un messaggio. Niente da controllare, niente che devi a nessuno, nessuno che sta scrivendo. Finisce su una spiaggia che non hai mai visto, e uno sconosciuto decide se risponderti.",
 "es": "Aquí tu carta está en el mar, y el mar puede tardar más de un día en entregar un mensaje. Nada que comprobar, nada que le debas a nadie, nadie escribiendo. Acaba en una playa que nunca has visto, y un desconocido decide si te responde.",
 "fr": "Ici votre lettre est en mer, et la mer peut mettre plus d'une journée à livrer un message. Rien à vérifier, rien que vous deviez à personne, personne en train d'écrire. Elle finit sur une plage que vous n'avez jamais vue, et un inconnu décide s'il vous répond.",
 "de": "Hier ist Ihr Brief auf See, und das Meer kann länger als einen Tag brauchen, um eine Nachricht zuzustellen. Nichts nachzusehen, niemandem etwas schuldig, niemand tippt. Er landet an einem Strand, den Sie nie gesehen haben, und eine fremde Person entscheidet, ob sie zurückschreibt.",
 "pt-BR": "Aqui sua carta está no mar, e o mar pode levar mais de um dia para entregar uma mensagem. Nada para conferir, nada devido a ninguém, ninguém digitando. Ela vai parar numa praia que você nunca viu, e um desconhecido decide se responde.",
 "ja": "ここでは、あなたの手紙は海の上にあり、海はひとつのメッセージを届けるのに一日以上かけることもあります。確認するものはなく、誰に対する義務もなく、入力中の人もいません。手紙は見たこともない浜に流れ着き、見知らぬ誰かが返事を書くかどうかを決めます。"},

"A friend of mine said it better: in a world that runs at two thousand miles an hour and expects us to answer at the same speed, this feels like the best possible reply.": {
 "it": "Un mio amico l'ha detta meglio: in un mondo che va a duemila all'ora e pretende che rispondiamo alla stessa velocità, questa mi sembra la migliore delle risposte.",
 "es": "Un amigo mío lo dijo mejor: en un mundo que va a dos mil por hora y pretende que respondamos a la misma velocidad, esta me parece la mejor de las respuestas.",
 "fr": "Un ami me l'a dit mieux : dans un monde qui file à deux mille à l'heure et qui exige qu'on réponde à la même vitesse, cela me semble la meilleure des réponses.",
 "de": "Ein Freund hat es besser gesagt: In einer Welt, die zweitausend Sachen fährt und erwartet, dass wir genauso schnell antworten, scheint mir das die beste aller Antworten.",
 "pt-BR": "Um amigo meu disse melhor: num mundo que corre a dois mil por hora e exige que a gente responda na mesma velocidade, essa me parece a melhor das respostas.",
 "ja": "友人が、もっとうまく言ってくれました。時速二千キロで走り、同じ速さで返事をすることを求めてくる世界にあって、これは考えうる最良の返事に思える、と。"},

"What Bottlegram is, in one line": {
 "it": "Cos'è Bottlegram in una riga",
 "es": "Qué es Bottlegram, en una línea",
 "fr": "Ce qu'est Bottlegram, en une ligne",
 "de": "Was Bottlegram ist, in einer Zeile",
 "pt-BR": "O que é o Bottlegram, em uma linha",
 "ja": "Bottlegram とは何か、一行で"},

"A slow messaging app where letters travel by sea, and the current decides who reads them and when.": {
 "it": "Un'app di messaggi lenti dove le lettere viaggiano via mare, ed è la corrente a decidere chi le legge e dopo quanto.",
 "es": "Una app de mensajes lentos donde las cartas viajan por mar y la corriente decide quién las lee y cuándo.",
 "fr": "Une application de messages lents où les lettres voyagent par la mer, et où le courant décide qui les lira et quand.",
 "de": "Eine App für langsame Nachrichten, in der Briefe über das Meer reisen und die Strömung entscheidet, wer sie liest und wann.",
 "pt-BR": "Um app de mensagens lentas onde as cartas viajam pelo mar e a correnteza decide quem as lê e quando.",
 "ja": "手紙が海を渡り、誰がいつ読むかは潮が決める、ゆっくりとしたメッセージアプリ。"},

"Press kit for Bottlegram: a slow messaging app where letters travel by sea, and the current decides who reads them and when. Screenshots, video, fact sheet.": {
 "it": "Press kit di Bottlegram: un'app di messaggi lenti dove le lettere viaggiano via mare, ed è la corrente a decidere chi le legge e dopo quanto. Schermate, video, scheda.",
 "es": "Press kit de Bottlegram: una app de mensajes lentos donde las cartas viajan por mar y la corriente decide quién las lee y cuándo. Capturas, vídeo, ficha.",
 "fr": "Dossier de presse de Bottlegram : une application de messages lents où les lettres voyagent par la mer, et où le courant décide qui les lira et quand. Captures, vidéo, fiche.",
 "de": "Pressemappe zu Bottlegram: eine App für langsame Nachrichten, in der Briefe über das Meer reisen und die Strömung entscheidet, wer sie liest und wann. Screenshots, Video, Steckbrief.",
 "pt-BR": "Kit de imprensa do Bottlegram: um app de mensagens lentas onde as cartas viajam pelo mar e a correnteza decide quem as lê e quando. Capturas, vídeo, ficha.",
 "ja": "Bottlegram のプレスキット。手紙が海を渡り、誰がいつ読むかは潮が決める、ゆっくりとしたメッセージアプリ。スクリーンショット、動画、ファクトシート。"},

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

"Not the first time. You hand the bottle to the current and the current picks the beach. But once someone has written back, that correspondence is yours: you go on writing to them for as long as you both keep answering.": {
 "it": "La prima volta no. La bottiglia la affidi alla corrente, e la spiaggia la sceglie lei. Ma quando qualcuno ti ha risposto, quel carteggio è tuo: continui a scrivere a quella persona finché tutti e due rispondete.",
 "es": "La primera vez no. Le entregas la botella a la corriente, y la playa la elige ella. Pero cuando alguien te ha contestado, esa correspondencia es tuya: le sigues escribiendo mientras ambos sigan respondiendo.",
 "fr": "Pas la première fois. Tu confies la bouteille au courant, et c'est lui qui choisit la plage. Mais dès que quelqu'un t'a répondu, cette correspondance est à toi : tu continues à lui écrire tant que vous vous répondez tous les deux.",
 "de": "Beim ersten Mal nicht. Du gibst die Flasche der Strömung, und die Strömung sucht den Strand aus. Aber sobald jemand geantwortet hat, gehört dieser Briefwechsel dir: Du schreibst dieser Person weiter, solange ihr beide antwortet.",
 "pt-BR": "Na primeira vez, não. Você entrega a garrafa à corrente, e é ela que escolhe a praia. Mas quando alguém responde, aquela correspondência é sua: você continua escrevendo para essa pessoa enquanto os dois continuarem respondendo.",
 "ja": "最初の一通は選べません。瓶は海流に託し、どの浜に着くかは海流が決めます。けれど誰かが返事をくれたら、その文通はあなたのものです。二人が返しつづけるかぎり、その相手に書きつづけられます。"},

"And if nobody answers?": {
 "it": "E se non risponde nessuno?", "es": "¿Y si no responde nadie?",
 "fr": "Et si personne ne répond ?", "de": "Und wenn niemand antwortet?",
 "pt-BR": "E se ninguém responder?", "ja": "誰も返事をくれなかったら。"},

"Some bottles are never answered. The sea gives you three more the next day, and by then somebody else's may already be on your sand. A letter that comes back is worth something here precisely because it might not have.": {
 "it": "Certe bottiglie non ricevono risposta. Il giorno dopo il mare te ne dà altre tre, e intanto sulla tua sabbia può esserci già quella di qualcun altro. Qui una lettera che torna vale qualcosa proprio perché poteva non tornare.",
 "es": "Algunas botellas nunca reciben respuesta. Al día siguiente el mar te da otras tres, y para entonces en tu arena puede haber ya la de otra persona. Aquí una carta que vuelve vale algo precisamente porque podía no volver.",
 "fr": "Certaines bouteilles ne reçoivent jamais de réponse. Le lendemain la mer t'en donne trois autres, et d'ici là celle de quelqu'un d'autre est peut-être déjà sur ton sable. Ici, une lettre qui revient vaut quelque chose justement parce qu'elle aurait pu ne pas revenir.",
 "de": "Manche Flaschen bekommen nie eine Antwort. Am nächsten Tag gibt dir das Meer drei neue, und bis dahin liegt vielleicht schon die von jemand anderem in deinem Sand. Ein Brief, der zurückkommt, ist hier genau deshalb etwas wert, weil er auch hätte ausbleiben können.",
 "pt-BR": "Algumas garrafas nunca são respondidas. No dia seguinte o mar te dá outras três, e até lá a de outra pessoa já pode estar na sua areia. Aqui uma carta que volta vale alguma coisa justamente porque podia não voltar.",
 "ja": "返事の来ない瓶もあります。翌日には海がまた三本くれますし、そのころには誰かの瓶があなたの砂に届いているかもしれません。ここでは、返ってきた手紙は、返らないこともありえたからこそ値打ちがあります。"},

"Who reads what I write?": {
 "it": "Chi legge quello che scrivo?", "es": "¿Quién lee lo que escribo?",
 "fr": "Qui lit ce que j'écris ?", "de": "Wer liest, was ich schreibe?",
 "pt-BR": "Quem lê o que eu escrevo?", "ja": "書いたものは誰が読みますか。"},

"One castaway, on one beach, and nobody else: there is no feed, no profile, nothing to scroll and nothing to look up afterwards. There is one exception: when a letter is reported, a person reads that letter, and only that one, to decide whether the sea keeps its writer.": {
 "it": "Un naufrago, su una spiaggia, e nessun altro: non c'è un feed, non c'è un profilo, non c'è niente da scorrere e niente da cercare dopo. C'è un'eccezione sola: quando una lettera viene segnalata, una persona legge quella lettera, e soltanto quella, per decidere se il mare tiene chi l'ha scritta.",
 "es": "Un náufrago, en una playa, y nadie más: no hay feed, no hay perfil, no hay nada que deslizar ni nada que buscar después. Hay una sola excepción: cuando una carta se denuncia, una persona lee esa carta, y solo esa, para decidir si el mar se queda con quien la escribió.",
 "fr": "Un naufragé, sur une plage, et personne d'autre : pas de fil, pas de profil, rien à faire défiler et rien à retrouver ensuite. Il y a une seule exception : quand une lettre est signalée, une personne lit cette lettre, et elle seule, pour décider si la mer garde celui qui l'a écrite.",
 "de": "Ein Schiffbrüchiger, an einem Strand, und sonst niemand: kein Feed, kein Profil, nichts zum Scrollen und nichts, das man später nachschlagen könnte. Es gibt eine einzige Ausnahme: Wird ein Brief gemeldet, liest ein Mensch diesen Brief, und nur diesen, um zu entscheiden, ob das Meer seinen Verfasser behält.",
 "pt-BR": "Um náufrago, em uma praia, e mais ninguém: não há feed, não há perfil, não há nada para rolar nem nada para procurar depois. Há uma única exceção: quando uma carta é denunciada, uma pessoa lê aquela carta, e só aquela, para decidir se o mar fica com quem a escreveu.",
 "ja": "一つの浜にいる一人の漂着者、それだけです。フィードもプロフィールもなく、スクロールするものも、あとから調べられるものもありません。例外は一つだけ。手紙が通報されたとき、人がその手紙だけを読み、書いた人を海が置いておくかどうかを決めます。"},

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

"Yes, free. There is a Wreck Emporium on your beach with a few things in it, and they are mostly a way to help with what this costs: the work on the app, the servers that keep the sea running. Nothing in there is needed to write a letter, or to receive one.": {
 "it": "Sì, è gratis. Sulla tua spiaggia c'è l'Emporio del Relitto con dentro qualche cosa, e servono soprattutto ad aiutare con quello che tutto questo costa: il lavoro sull'app, i server che tengono in piedi il mare. Niente di quello che c'è là dentro serve per scrivere una lettera, o per riceverne una.",
 "es": "Sí, es gratis. En tu playa está el Emporio del Naufragio con unas cuantas cosas dentro, y sirven sobre todo para ayudar con lo que todo esto cuesta: el trabajo en la app, los servidores que mantienen el mar en pie. Nada de lo que hay ahí hace falta para escribir una carta, ni para recibirla.",
 "fr": "Oui, c'est gratuit. Sur ta plage il y a l'Emporium de l'Épave, avec quelques objets dedans, et ils servent surtout à aider avec ce que tout cela coûte : le travail sur l'app, les serveurs qui tiennent la mer debout. Rien de ce qui s'y trouve n'est nécessaire pour écrire une lettre, ni pour en recevoir une.",
 "de": "Ja, kostenlos. An deinem Strand steht das Kontor des Wracks mit ein paar Dingen darin, und die sind vor allem eine Art zu helfen, was das hier kostet: die Arbeit an der App, die Server, die das Meer am Laufen halten. Nichts davon braucht man, um einen Brief zu schreiben oder einen zu bekommen.",
 "pt-BR": "Sim, é grátis. Na sua praia fica o Empório do Naufrágio com algumas coisas dentro, e elas servem sobretudo para ajudar com o que tudo isso custa: o trabalho no app, os servidores que mantêm o mar de pé. Nada do que há ali é preciso para escrever uma carta, nem para receber uma.",
 "ja": "はい、無料です。あなたの浜には難破商館があり、いくつか品物が置いてあります。それらは主に、これにかかるもの、つまりアプリの制作と、海を動かしつづけるサーバーを支えるためのものです。手紙を書くのにも、受け取るのにも、あの中のものは要りません。"},

"Coastlines from Natural Earth (public domain). Sounds from freesound.org (CC0). No map service, no tracking, no cookies: this page does not know who you are, exactly like the sea.": {
 "it": "Coste da Natural Earth (pubblico dominio). Suoni da freesound.org (CC0). Nessun servizio di mappe, nessun tracciamento, nessun cookie: questa pagina non sa chi sei, esattamente come il mare.",
 "es": "Costas de Natural Earth (dominio público). Sonidos de freesound.org (CC0). Sin servicio de mapas, sin rastreo, sin cookies: esta página no sabe quién eres, igual que el mar.",
 "fr": "Côtes issues de Natural Earth (domaine public). Sons de freesound.org (CC0). Aucun service cartographique, aucun traçage, aucun cookie : cette page ne sait pas qui tu es, exactement comme la mer.",
 "de": "Küstenlinien von Natural Earth (gemeinfrei). Klänge von freesound.org (CC0). Kein Kartendienst, kein Tracking, keine Cookies: Diese Seite weiß nicht, wer du bist — genau wie das Meer.",
 "pt-BR": "Costas do Natural Earth (domínio público). Sons do freesound.org (CC0). Sem serviço de mapas, sem rastreamento, sem cookies: esta página não sabe quem você é, exatamente como o mar.",
 "ja": "海岸線は Natural Earth（パブリックドメイン）。音は freesound.org（CC0）。地図サービスも、追跡も、Cookie もない。このページはあなたが誰かを知らない——海とまったく同じように。"},
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
             "6–36", "8.9 MB",
             # I nomi delle spiagge dell'approdo che ruota: endonimi, come
             # nell'app. I LUOGHI invece si traducono (voci qui sopra).
             "Cala Goloritzé", "Reynisfjara", "Anse Source d'Argent",
             "Haukland Beach", "Praia da Ursa"]

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
