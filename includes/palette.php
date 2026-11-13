<?php
/**
 * Palette Nelson Galley dans le sélecteur de couleurs de l'éditeur
 * (ajoutée à la palette par défaut, sans toucher à celle du thème).
 *
 * @package NelsonGalleyBlocs
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function ngb_palette() {
	return array(
		array( 'slug' => 'ng-emeraude', 'name' => 'NG Émeraude', 'color' => '#10b981' ),
		array( 'slug' => 'ng-emeraude-fonce', 'name' => 'NG Émeraude foncé', 'color' => '#059669' ),
		array( 'slug' => 'ng-vert-profond', 'name' => 'NG Vert profond', 'color' => '#065f46' ),
		array( 'slug' => 'ng-menthe', 'name' => 'NG Menthe', 'color' => '#d1fae5' ),
		array( 'slug' => 'ng-menthe-pale', 'name' => 'NG Menthe pâle', 'color' => '#f0fdf4' ),
		array( 'slug' => 'ng-nuit', 'name' => 'NG Bleu nuit', 'color' => '#0f172a' ),
		array( 'slug' => 'ng-ardoise', 'name' => 'NG Ardoise', 'color' => '#1e293b' ),
		array( 'slug' => 'ng-encre', 'name' => 'NG Encre', 'color' => '#111827' ),
		array( 'slug' => 'ng-gris', 'name' => 'NG Gris', 'color' => '#6b7280' ),
		array( 'slug' => 'ng-bordure', 'name' => 'NG Bordure', 'color' => '#e5e7eb' ),
		array( 'slug' => 'ng-ambre', 'name' => 'NG Ambre', 'color' => '#f59e0b' ),
		array( 'slug' => 'ng-rouge', 'name' => 'NG Rouge', 'color' => '#ef4444' ),
	);
}

add_filter( 'wp_theme_json_data_default', function ( $theme_json ) {
	$data    = $theme_json->get_data();
	$current = $data['settings']['color']['palette']['default'] ?? array();
	return $theme_json->update_with( array(
		'version'  => 2,
		'settings' => array(
			'color' => array(
				'palette'   => array_merge( ngb_palette(), $current ),
				'gradients' => array_merge(
					array(
						array( 'slug' => 'ng-nuit-emeraude', 'name' => 'NG Nuit → émeraude', 'gradient' => 'linear-gradient(135deg, #0f172a 0%, #065f46 100%)' ),
						array( 'slug' => 'ng-menthe', 'name' => 'NG Menthe', 'gradient' => 'linear-gradient(135deg, #f0fdf4 0%, #d1fae5 100%)' ),
					),
					$data['settings']['color']['gradients']['default'] ?? array()
				),
			),
		),
	) );
} );
