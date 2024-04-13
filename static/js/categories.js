$(document).ready(function() {
            $("#new").click(function() {
                showProducts("is_new");
            });

            $("#popular").click(function() {
                showProducts('is_popular');
            });

            $("#drinks").click(function() {
                showProducts("is_drink");
            });

            $("#combo").click(function() {
                showProducts("combo");
            });

            $("#burgers").click(function() {
                showProducts("is_burger");
            });

            $("#snacks").click(function() {
                showProducts("is_snack");
            });

            $("#cafe").click(function() {
                showProducts("is_cafe");
            });

            $("#breakfast").click(function() {
                showProducts("is_breakfast");
            });

            $("#kids-combo").click(function() {
                showProducts("kids_combo");
            });

            $("#desserts").click(function() {
                showProducts("is_dessert");
            });

            $("#other").click(function() {
                showProducts("is_other");
            });

            function showProducts(filter) {
                $.ajax({
                    type: 'GET',
                    url: '/get_products',
                    data: JSON.parse(JSON.stringify(filter)),
                    success: function(data) {
                        console.log(data)
                        // Сохраняем полученные данные в скрытом элементе
                        $('#hidden-data').val(JSON.stringify(data));
                        $('#test').html(JSON.parse($('#hidden-data').val())['products'][0]['title']);
                    }
                });
            }
        });