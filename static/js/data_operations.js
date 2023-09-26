<script>
    $(document).ready(function () {
        // Abrir o modal de adição/editação
        $('.btn-primary').click(function () {
            $('#addDataModal').modal('show');
        });

        // Manipular envio de formulário para edição
        $('#formEditarAdicionarDados').on('submit', function (e) {
            e.preventDefault();
            var $form = $(this);
            var url = $form.data('url');

            $.ajax({
                type: 'POST',
                url: url,
                data: $form.serialize(),
                success: function (data) {
                    if (data.success) {
                        $('#addDataModal').modal('hide');
                        // Atualizar a tabela ou fazer outras ações após a edição
                    } else {
                        // Exibir erros ou lidar com erros de validação
                    }
                }
            });
        });
    });
</script>