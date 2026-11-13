<?php
/**
 * Chargement des styles (site + éditeur) et du script « Copier le code ».
 *
 * @package NelsonGalleyBlocs
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

// enqueue_block_assets : chargé sur le site ET dans l'éditeur, pour un aperçu fidèle.
add_action( 'enqueue_block_assets', function () {
	wp_enqueue_style( 'nelson-galley-blocs', NGB_URL . 'assets/css/blocs.css', array(), NGB_VERSION );
} );

add_action( 'wp_enqueue_scripts', function () {
	if ( is_singular() ) {
		wp_enqueue_script( 'nelson-galley-blocs-code', NGB_URL . 'assets/js/copy-code.js', array(), NGB_VERSION, array( 'in_footer' => true, 'strategy' => 'defer' ) );
	}
} );
