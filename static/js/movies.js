/**
 * Created by Евгений on 07.03.15.
 */

function do_movie() {
    var id = this.name;
    $('#'+id).html(' Отправка... ').attr('disabled',true);
    v = this.value;
    $.ajax({
        url: document.documentURI,
        type: "POST",
        dataType: "json",
        data: {
            type : v,
            movie_id: id,
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
        },
        success: function(json) {
            if (json.success == 'False')
            {
                alert("error!"+json.errors);
            }
            else if (json.success == 'True')
            {
                if (v == 1) {
                    $("#remove_" + id).attr('disabled',true)
                        .css({'background-color':'rgba(218, 76, 76, 0.55)'})
                       .html("Удалено!");
                    $("#show_future_" + id).attr('disabled',true);
                }
                else if (v ==2 )
                    $("#remove_" + id).attr('disabled',true);
                    $("#show_future_" + id).attr('disabled',true)
                        .css({'background-color':'#F0C486'})
                       .html("Добавили!");
            }
        },
        error: function(xhr, errmsg, err) {
            alert(xhr.status + ": " + xhr.responseText);
        }
    });
    return false;
}

function prepareDocument() {
    //load_products();
    $(".btn-do").click(do_movie);
    $('.add_form').submit(add_cart_from_catalog);
}

$(document).ready(prepareDocument);