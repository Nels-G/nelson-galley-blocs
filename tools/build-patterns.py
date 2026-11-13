"""
Génère les fichiers patterns/*.html (composants et modèles d'articles).
Le balisage des blocs doit correspondre exactement à celui de l'éditeur :
on le produit avec des fonctions plutôt qu'à la main.

Usage : python -I tools/build-patterns.py
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "patterns"


def attrs(d):
    return (" " + json.dumps(d, ensure_ascii=False, separators=(",", ":"))) if d else ""


def p(text, style=None, placeholder=None):
    a = {}
    if style:
        a["className"] = f"is-style-{style}"
    if placeholder:
        a["placeholder"] = placeholder
    cls = f' class="is-style-{style}"' if style else ""
    return f"<!-- wp:paragraph{attrs(a)} -->\n<p{cls}>{text}</p>\n<!-- /wp:paragraph -->"


def h(text, level=2, style=None):
    a = {}
    if level != 2:
        a["level"] = level
    if style:
        a["className"] = f"is-style-{style}"
    cls = "wp-block-heading" + (f" is-style-{style}" if style else "")
    return f'<!-- wp:heading{attrs(a)} -->\n<h{level} class="{cls}">{text}</h{level}>\n<!-- /wp:heading -->'


def lst(items, style=None, ordered=False):
    a = {}
    if ordered:
        a["ordered"] = True
    if style:
        a["className"] = f"is-style-{style}"
    tag = "ol" if ordered else "ul"
    cls = "wp-block-list" + (f" is-style-{style}" if style else "")
    inner = "\n\n".join(f"<!-- wp:list-item -->\n<li>{i}</li>\n<!-- /wp:list-item -->" for i in items)
    return f'<!-- wp:list{attrs(a)} -->\n<{tag} class="{cls}">{inner}</{tag}>\n<!-- /wp:list -->'


def group(inner, style=None, extra_class=None):
    classes = " ".join(c for c in [f"is-style-{style}" if style else None, extra_class] if c)
    a = {}
    if classes:
        a["className"] = classes
    a["layout"] = {"type": "constrained"}
    cls = "wp-block-group" + (f" {classes}" if classes else "")
    return f'<!-- wp:group{attrs(a)} -->\n<div class="{cls}">' + "\n\n".join(inner) + "</div>\n<!-- /wp:group -->"


def columns(cols, style=None):
    a = {"className": f"is-style-{style}"} if style else {}
    cls = "wp-block-columns" + (f" is-style-{style}" if style else "")
    inner = "\n\n".join(
        "<!-- wp:column -->\n<div class=\"wp-block-column\">" + "\n\n".join(c) + "</div>\n<!-- /wp:column -->" for c in cols
    )
    return f'<!-- wp:columns{attrs(a)} -->\n<div class="{cls}">{inner}</div>\n<!-- /wp:columns -->'


def quote(text, cite):
    return (
        '<!-- wp:quote {"className":"is-style-ng-citation"} -->\n<blockquote class="wp-block-quote is-style-ng-citation">'
        + p(text) + f"<cite>{cite}</cite></blockquote>\n<!-- /wp:quote -->"
    )


def table(head, rows, style="ng-comparatif"):
    th = "".join(f"<th>{c}</th>" for c in head)
    tb = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return (
        f'<!-- wp:table {{"className":"is-style-{style}"}} -->\n<figure class="wp-block-table is-style-{style}"><table>'
        f"<thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></figure>\n<!-- /wp:table -->"
    )


def details(q, a):
    return (
        '<!-- wp:details {"className":"is-style-ng-faq"} -->\n<details class="wp-block-details is-style-ng-faq">'
        f"<summary>{q}</summary>" + p(a) + "</details>\n<!-- /wp:details -->"
    )


def code(text, style="ng-terminal"):
    return f'<!-- wp:code {{"className":"is-style-{style}"}} -->\n<pre class="wp-block-code is-style-{style}"><code>{text}</code></pre>\n<!-- /wp:code -->'


def image(style):
    return f'<!-- wp:image {{"className":"is-style-{style}"}} -->\n<figure class="wp-block-image is-style-{style}"><img alt=""/></figure>\n<!-- /wp:image -->'


def buttons(*btns):
    inner = []
    for label, url, outline in btns:
        if outline:
            inner.append(
                f'<!-- wp:button {{"className":"is-style-outline"}} -->\n<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{url}">{label}</a></div>\n<!-- /wp:button -->'
            )
        else:
            inner.append(
                f'<!-- wp:button -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{url}">{label}</a></div>\n<!-- /wp:button -->'
            )
    return '<!-- wp:buttons -->\n<div class="wp-block-buttons">' + "\n\n".join(inner) + "</div>\n<!-- /wp:buttons -->"


def separator():
    return '<!-- wp:separator {"className":"is-style-ng-degrade"} -->\n<hr class="wp-block-separator has-alpha-channel-opacity is-style-ng-degrade"/>\n<!-- /wp:separator -->'


def shortcode(sc):
    return f"<!-- wp:shortcode -->\n{sc}\n<!-- /wp:shortcode -->"


# ---------------------------------------------------------------- Composants
C = {}
C["en-bref"] = group([p("<strong>En bref</strong>"), lst(["Premier point clé de l'article.", "Deuxième point clé.", "Troisième point clé."], "ng-coches")], "ng-bref")
C["afrique"] = group([h("Et en Afrique francophone ?", 3), p("Votre analyse terrain : ce que cela change concrètement pour les entreprises, les développeurs et les utilisateurs de la région.")], "ng-afrique")
C["note-expert"] = group([p("<strong>Note d'expert</strong>"), p("Un conseil tiré de votre expérience, que l'on ne trouve pas dans la documentation.")], "ng-expert")
C["erreur-solution"] = "\n\n".join([
    group([p("<strong>Erreur fréquente</strong>"), p("Décrivez le symptôme : le message d'erreur, ce que l'étudiant observe."), code("// Le code qui pose problème")], "ng-attention"),
    group([p("<strong>Solution</strong>"), p("Expliquez la correction et pourquoi elle fonctionne."), code("// Le code corrigé")], "ng-solution"),
])
C["etapes"] = "\n\n".join([h("Pas à pas", 3, "ng-accent"), lst([
    "<strong>Première étape.</strong> Ce qu'il faut faire, et pourquoi.",
    "<strong>Deuxième étape.</strong> Ce qu'il faut faire, et pourquoi.",
    "<strong>Troisième étape.</strong> Ce qu'il faut faire, et pourquoi.",
], "ng-etapes", ordered=True)])
C["chiffres-cles"] = columns([
    [group([p("00 %", "ng-surligne"), p("Ce que mesure ce chiffre, et sa source.")], "ng-chiffre")],
    [group([p("00", "ng-surligne"), p("Ce que mesure ce chiffre, et sa source.")], "ng-chiffre")],
    [group([p("00 k", "ng-surligne"), p("Ce que mesure ce chiffre, et sa source.")], "ng-chiffre")],
])
C["pour-contre"] = columns([
    [h("Avantages", 3), lst(["Premier avantage", "Deuxième avantage", "Troisième avantage"], "ng-coches")],
    [h("Limites", 3), lst(["Première limite", "Deuxième limite", "Troisième limite"], "ng-croix")],
], "ng-cartes")
C["avant-apres"] = columns([
    [p("Avant", "ng-surtitre"), image("ng-cadre"), p("Ce qui n'allait pas.")],
    [p("Après", "ng-surtitre"), image("ng-cadre"), p("Ce qui a changé, et le résultat obtenu.")],
], "ng-cartes")
C["comparatif"] = table(["Critère", "Option A", "Option B"], [["Prix", "…", "…"], ["Facilité", "…", "…"], ["Pour qui ?", "…", "…"]])
C["frise"] = "\n\n".join([h("Les grandes étapes", 3, "ng-accent"), lst([
    "<strong>2024</strong> — Ce qui s'est passé.",
    "<strong>2025</strong> — Ce qui s'est passé.",
    "<strong>2026</strong> — Ce qui s'est passé.",
], "ng-frise")])
C["citation"] = quote("Une phrase forte qui résume votre conviction.", "Nelson Galley")
C["faq"] = "\n\n".join([h("Questions fréquentes"), details("Première question que se posent vos lecteurs ?", "Réponse courte et directe."),
    details("Deuxième question ?", "Réponse courte et directe."), details("Troisième question ?", "Réponse courte et directe.")])
C["appel-action"] = group([p("Travaillons ensemble", "ng-surtitre"), h("Vous avez un projet web ou mobile ?", 3),
    p("Une phrase qui donne envie de passer à l'action."), buttons(("Parlons-en", "/contacts/", False), ("Voir mon portfolio", "https://www.nelsongalley.online/", True))], "ng-sombre")
C["capture-app"] = "\n\n".join([image("ng-navigateur"), p("Légende : ce que montre la capture.")])
C["capture-mobile"] = columns([[image("ng-telephone")], [p("Application mobile", "ng-surtitre"), h("Nom de l'écran", 3), p("Expliquez ce que l'utilisateur voit et pourquoi l'écran est conçu ainsi.")]])
C["encart"] = shortcode('[encart id="0"]')

# ---------------------------------------------------------------- Modèles d'articles
T = {}
T["modele-guide"] = "\n\n".join([
    p("Chapô : en deux ou trois phrases, la promesse de l'article et la réponse principale.", "ng-chapo"), C["en-bref"],
    h("Pourquoi c'est important"), p("Le problème que rencontre votre lecteur."),
    h("Les étapes à suivre"), C["etapes"], C["note-expert"],
    h("Les erreurs à éviter"), lst(["Erreur 1", "Erreur 2", "Erreur 3"], "ng-croix"),
    C["afrique"], C["faq"], C["appel-action"],
])
T["modele-tuto"] = "\n\n".join([
    p("Chapô : le bug ou le besoin, et ce que le lecteur saura faire à la fin.", "ng-chapo"), C["en-bref"],
    h("Le symptôme"), p("Ce que l'étudiant observe."), code("Message d'erreur exact"),
    h("Pourquoi ça arrive"), p("L'explication du mécanisme, simplement."),
    h("La correction"), C["erreur-solution"],
    h("Ma méthode de débogage"), C["etapes"],
    C["faq"], C["appel-action"],
])
T["modele-decryptage"] = "\n\n".join([
    p("Chapô : l'annonce en une phrase, et pourquoi elle compte pour vos lecteurs.", "ng-chapo"), C["en-bref"],
    h("Ce qui a été annoncé"), p("Les faits, avec les sources."), C["chiffres-cles"],
    h("Ce que ça change"), C["pour-contre"],
    C["afrique"], C["citation"], h("Mon avis"), p("Votre analyse et votre recommandation."),
    C["faq"], C["appel-action"],
])
T["modele-etude-de-cas"] = "\n\n".join([
    p("Chapô : le client, le problème, le résultat obtenu.", "ng-chapo"), C["chiffres-cles"],
    h("Le contexte"), p("Le client, son activité, ses contraintes."),
    h("Le défi"), C["note-expert"],
    h("La solution"), C["capture-app"], C["etapes"],
    h("Les résultats"), C["avant-apres"], C["citation"],
    C["afrique"], C["appel-action"],
])

OUT.mkdir(exist_ok=True)
for name, html in {**C, **T}.items():
    (OUT / f"{name}.html").write_text(html + "\n", encoding="utf-8", newline="\n")
print(f"{len(C)} composants, {len(T)} modèles générés dans {OUT}")
