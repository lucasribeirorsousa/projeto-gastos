function loadView() {
    const hash = window.location.hash.substr(1);

    const views = {
        'despesas_por_mes': 'despesas_por_mes.html',
        'despesas_por_categoria': 'despesas_por_categoria.html',
        'fontes_de_dinheiro': 'fontes_de_dinheiro.html',
    };

    const viewPath = views[hash];

    if (viewPath) {
        fetch(viewPath)
            .then(response => response.text())
            .then(data => {
                document.getElementById('app').innerHTML = data;
            })
            .catch(error => {
                console.error(error);
            });
    }
}

window.addEventListener('hashchange', loadView);

loadView();