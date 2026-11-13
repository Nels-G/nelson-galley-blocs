<?php
/**
 * Composants et modèles d'articles (onglet « Compositions » de l'éditeur).
 * Le contenu de chaque composition est dans patterns/<nom>.html.
 *
 * @package NelsonGalleyBlocs
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function ngb_patterns() {
	$c = 'ng-composants';
	$m = 'ng-modeles';
	return array(
		'en-bref'             => array( 'En bref', $c, "Encadré des 3 points clés, en tête d'article." ),
		'afrique'             => array( 'Et en Afrique francophone ?', $c, "Encadré sombre pour votre analyse terrain." ),
		'note-expert'         => array( "Note d'expert", $c, 'Conseil tiré de votre expérience.' ),
		'erreur-solution'     => array( 'Erreur fréquente → Solution', $c, 'Le bug, puis sa correction, avec code.' ),
		'etapes'              => array( 'Étapes numérotées', $c, 'Une méthode pas à pas.' ),
		'chiffres-cles'       => array( 'Chiffres clés', $c, '3 chiffres mis en valeur.' ),
		'pour-contre'         => array( 'Avantages / Limites', $c, 'Deux colonnes : coches et croix.' ),
		'avant-apres'         => array( 'Avant / Après', $c, 'Deux images comparées.' ),
		'comparatif'          => array( 'Tableau comparatif', $c, 'Comparer des options critère par critère.' ),
		'frise'               => array( 'Frise chronologique', $c, 'Les étapes dans le temps.' ),
		'citation'            => array( 'Citation forte', $c, 'Une phrase qui marque.' ),
		'faq'                 => array( 'FAQ', $c, 'Questions dépliables.' ),
		'appel-action'        => array( "Appel à l'action", $c, 'Carte sombre avec boutons.' ),
		'capture-app'         => array( 'Capture dans un navigateur', $c, 'Image présentée dans une fenêtre de navigateur.' ),
		'capture-mobile'      => array( "Capture d'écran mobile", $c, 'Image dans un cadre de téléphone, avec explication.' ),
		'encart'              => array( 'Encart publicitaire', $c, "Remplacez 0 par l'identifiant de l'encart (plugin Encarts)." ),
		'modele-guide'        => array( 'Modèle : Guide pratique', $m, 'Article complet prêt à remplir.' ),
		'modele-tuto'         => array( 'Modèle : Tuto Ingénierie & Pratique', $m, 'Bug, explication, correction, méthode.' ),
		'modele-decryptage'   => array( 'Modèle : Décryptage actu', $m, "L'annonce, ce que ça change, votre avis." ),
		'modele-etude-de-cas' => array( 'Modèle : Étude de cas', $m, 'Contexte, défi, solution, résultats.' ),
	);
}

add_action( 'init', function () {
	register_block_pattern_category( 'ng-composants', array( 'label' => 'Nelson Galley — Composants' ) );
	register_block_pattern_category( 'ng-modeles', array( 'label' => "Nelson Galley — Modèles d'articles" ) );

	foreach ( ngb_patterns() as $slug => list( $title, $category, $description ) ) {
		$file = NGB_DIR . "patterns/$slug.html";
		if ( ! file_exists( $file ) ) {
			continue;
		}
		$args = array(
			'title'       => $title,
			'description' => $description,
			'categories'  => array( $category ),
			'content'     => file_get_contents( $file ),
		);
		if ( 'ng-modeles' === $category ) {
			// Proposés aussi à la création d'un nouvel article.
			$args['blockTypes'] = array( 'core/post-content' );
			$args['postTypes']  = array( 'post' );
		}
		register_block_pattern( 'nelson-galley/' . $slug, $args );
	}
} );
