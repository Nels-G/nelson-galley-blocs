/* Nelson Galley — Blocs éditoriaux : bouton « Copier » sur les blocs de code. */
(function () {
	if (!navigator.clipboard) return;
	document.querySelectorAll('pre.wp-block-code').forEach(function (pre) {
		var code = pre.querySelector('code');
		if (!code || pre.querySelector('.ngb-copy')) return;
		var btn = document.createElement('button');
		btn.type = 'button';
		btn.className = 'ngb-copy';
		btn.textContent = 'Copier';
		btn.setAttribute('aria-label', 'Copier le code');
		btn.addEventListener('click', function () {
			navigator.clipboard.writeText(code.innerText).then(function () {
				btn.textContent = 'Copié ✓';
				btn.classList.add('is-copied');
				setTimeout(function () {
					btn.textContent = 'Copier';
					btn.classList.remove('is-copied');
				}, 2000);
			});
		});
		pre.appendChild(btn);
	});
})();
