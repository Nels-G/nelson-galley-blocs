<?php
/**
 * Plugin Name:       Nelson Galley — Blocs éditoriaux
 * Plugin URI:        https://github.com/Nels-G/nelson-galley-blocs
 * Description:       Styles de blocs, composants et modèles d'articles à la charte Nelson Galley pour l'éditeur WordPress : encadrés, étapes, code façon terminal, chiffres clés, comparatifs, FAQ, appels à l'action, cadres navigateur et téléphone…
 * Version:           1.0.0
 * Requires at least: 6.4
 * Requires PHP:      7.4
 * Author:            Nelson Galley
 * Author URI:        https://www.nelsongalley.online/
 * License:           GPL-2.0-or-later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain:       nelson-galley-blocs
 * Update URI:        https://github.com/Nels-G/nelson-galley-blocs
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'NGB_VERSION', '1.0.0' );
define( 'NGB_FILE', __FILE__ );
define( 'NGB_DIR', plugin_dir_path( __FILE__ ) );
define( 'NGB_URL', plugin_dir_url( __FILE__ ) );
define( 'NGB_SLUG', 'nelson-galley-blocs' );
define( 'NGB_GITHUB_REPO', 'Nels-G/nelson-galley-blocs' );

require_once NGB_DIR . 'includes/styles.php';
require_once NGB_DIR . 'includes/patterns.php';
require_once NGB_DIR . 'includes/palette.php';
require_once NGB_DIR . 'includes/assets.php';
require_once NGB_DIR . 'includes/updater.php';
