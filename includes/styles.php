<?php
/**
 * Styles de blocs : un clic dans l'éditeur (panneau « Styles ») transforme un bloc natif
 * en composant à la charte. Classe générée : is-style-ng-<nom>.
 *
 * @package NelsonGalleyBlocs
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function ngb_block_styles() {
	return array(
		'core/group'     => array(
			'ng-bref'      => 'En bref',
			'ng-afrique'   => 'Afrique francophone',
			'ng-expert'    => "Note d'expert",
			'ng-attention' => 'Erreur fréquente',
			'ng-solution'  => 'Solution',
			'ng-carte'     => 'Carte',
			'ng-sombre'    => 'Carte sombre',
			'ng-chiffre'   => 'Chiffre clé',
		),
		'core/paragraph' => array(
			'ng-chapo'    => 'Chapô',
			'ng-surtitre' => 'Surtitre (pastille)',
			'ng-surligne' => 'Surligné',
		),
		'core/heading'   => array(
			'ng-accent'   => 'Trait vert',
			'ng-surtitre' => 'Surtitre (pastille)',
		),
		'core/quote'     => array(
			'ng-citation' => 'Citation forte',
		),
		'core/list'      => array(
			'ng-etapes' => 'Étapes numérotées',
			'ng-coches' => 'Coches (avantages)',
			'ng-croix'  => 'Croix (inconvénients)',
			'ng-frise'  => 'Frise chronologique',
		),
		'core/table'     => array(
			'ng-comparatif' => 'Comparatif',
		),
		'core/details'   => array(
			'ng-faq' => 'Question FAQ',
		),
		'core/code'      => array(
			'ng-terminal' => 'Terminal',
		),
		'core/image'     => array(
			'ng-cadre'     => 'Cadre arrondi',
			'ng-navigateur' => 'Fenêtre de navigateur',
			'ng-telephone' => 'Écran de téléphone',
		),
		'core/separator' => array(
			'ng-degrade' => 'Dégradé vert',
		),
		'core/columns'   => array(
			'ng-cartes' => 'Colonnes en cartes',
		),
	);
}

add_action( 'init', function () {
	foreach ( ngb_block_styles() as $block => $styles ) {
		foreach ( $styles as $name => $label ) {
			register_block_style( $block, array( 'name' => $name, 'label' => $label ) );
		}
	}
} );
