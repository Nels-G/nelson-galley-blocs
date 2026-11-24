# Nelson Galley — Blocs éditoriaux

Plugin WordPress qui transforme l'éditeur de blocs en outil de mise en page éditoriale : **26 styles de blocs**, **16 composants** et **4 modèles d'articles** à la charte Nelson Galley, sans constructeur de pages lourd.

On écrit vite, avec les blocs natifs de WordPress, et chaque bloc peut devenir un encadré, une liste d'étapes, un terminal, un comparatif ou une capture dans un cadre de navigateur, en un clic.

![WordPress 6.4+](https://img.shields.io/badge/WordPress-6.4%2B-21759b) ![PHP 7.4+](https://img.shields.io/badge/PHP-7.4%2B-777bb4) ![Licence GPL-2.0+](https://img.shields.io/badge/licence-GPL--2.0%2B-10b981)

## Pourquoi ce plugin

| Approche | Liberté | Vitesse de rédaction | Poids des pages | Identité visuelle |
| --- | --- | --- | --- | --- |
| Constructeur de pages (Elementor…) | Totale | Lente | Lourd | Varie d'un article à l'autre |
| Éditeur WordPress seul | Moyenne | Rapide | Léger | Générique |
| **Éditeur + Blocs éditoriaux** | Composants dédiés + réglages par bloc | Rapide | Léger | Constante et reconnaissable |

## Contenu

### Styles de blocs

Dans l'éditeur, sélectionnez un bloc, puis choisissez un style dans le panneau de droite (**Styles**).

| Bloc | Styles |
| --- | --- |
| Groupe | En bref · Afrique francophone · Note d'expert · Erreur fréquente · Solution · Carte · Carte sombre · Chiffre clé |
| Paragraphe | Chapô · Surtitre (pastille) · Surligné |
| Titre | Trait vert · Surtitre (pastille) |
| Citation | Citation forte |
| Liste | Étapes numérotées · Coches · Croix · Frise chronologique |
| Tableau | Comparatif |
| Détails | Question FAQ (dépliable) |
| Code | Terminal (avec bouton « Copier ») |
| Image | Cadre arrondi · Fenêtre de navigateur · Écran de téléphone |
| Séparateur | Dégradé vert |
| Colonnes | Colonnes en cartes |

Tous les blocs de code reçoivent aussi un bouton **Copier** sur le site.

### Composants

Bouton **+** › onglet **Compositions** › **Nelson Galley — Composants** :

En bref · Et en Afrique francophone ? · Note d'expert · Erreur fréquente → Solution · Étapes numérotées · Chiffres clés · Avantages / Limites · Avant / Après · Tableau comparatif · Frise chronologique · Citation forte · FAQ · Appel à l'action · Capture dans un navigateur · Capture d'écran mobile · Encart publicitaire.

### Modèles d'articles

**Nelson Galley — Modèles d'articles** (proposés aussi à la création d'un nouvel article) :

- **Guide pratique** : chapô, en bref, étapes, note d'expert, erreurs à éviter, Afrique francophone, FAQ, appel à l'action.
- **Tuto Ingénierie & Pratique** : symptôme, explication, erreur → solution, méthode de débogage, FAQ.
- **Décryptage actu** : l'annonce, chiffres clés, avantages / limites, Afrique francophone, avis.
- **Étude de cas** : chiffres clés, contexte, défi, solution avec captures, résultats avant / après.

### Palette

12 couleurs et 2 dégradés à la charte (préfixés « NG ») dans le sélecteur de couleurs de chaque bloc. Les réglages natifs de l'éditeur (bordures, arrondis, espacements, couleurs) restent disponibles sur tous les blocs.

## Installation

1. Téléchargez `nelson-galley-blocs.zip` depuis la [dernière release](https://github.com/Nels-G/nelson-galley-blocs/releases/latest) (pas les fichiers « Source code »).
2. **Extensions › Ajouter › Téléverser une extension**, puis **Activer**.

## Compatibilité et personnalisation

Les styles reprennent les couleurs du thème quand les variables `--ng-*` et `--cs-*` existent (thème Revision personnalisé Nelson Galley), et le mode sombre du thème. Sur un autre thème, ils utilisent un vert émeraude par défaut. Pour changer l'accent :

```css
:where([class*="is-style-ng-"]) {
  --ngb-accent: #10b981;
  --ngb-soft: rgba(16, 185, 129, 0.10);
}
```

Le composant « Encart publicitaire » utilise le code court du plugin [Nelson Galley — Encarts](https://github.com/Nels-G/nelson-galley-encarts).

## Développement

Les compositions sont générées par un script, pour garantir un balisage de blocs exact (sinon l'éditeur signale un « bloc invalide ») :

```bash
python tools/build-patterns.py   # régénère patterns/*.html
```

Pour ajouter un composant : ajoutez-le dans `tools/build-patterns.py`, régénérez, puis déclarez son titre dans `includes/patterns.php`. Pour un nouveau style de bloc : `includes/styles.php` + CSS dans `assets/css/blocs.css`.

```text
nelson-galley-blocs.php    En-tête, constantes, chargement
includes/styles.php        Styles de blocs (register_block_style)
includes/patterns.php      Catégories et compositions
includes/palette.php       Couleurs et dégradés de l'éditeur
includes/assets.php        CSS (site + éditeur) et script « Copier »
includes/updater.php       Mises à jour depuis les releases GitHub
assets/css/blocs.css       Rendu de tous les styles
assets/js/copy-code.js     Bouton « Copier » des blocs de code
patterns/*.html            Compositions (générées)
tools/build-patterns.py    Générateur des compositions
```

## Publier une mise à jour

1. Augmentez la version **à deux endroits** de `nelson-galley-blocs.php` : l'en-tête `Version:` et `NGB_VERSION`.
2. Ajoutez une entrée dans [CHANGELOG.md](CHANGELOG.md).
3. Commitez, puis poussez une étiquette :

```bash
git commit -am "Version 1.1.0"
git tag v1.1.0
git push origin main --tags
```

L'action GitHub construit `nelson-galley-blocs.zip` et publie la release ; WordPress propose ensuite la mise à jour dans **Tableau de bord › Mises à jour**.

## Licence

[GPL-2.0-or-later](LICENSE). Développé par [Nelson Galley](https://www.nelsongalley.online/), développeur web et designer UX/UI à Lomé, Togo.


https://drive.google.com/file/d/192lZ0-4DIIuGshj20vKrU8xsRtZfia9d/view?usp=drivesdk
