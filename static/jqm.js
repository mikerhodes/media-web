$(document).bind("mobileinit", function(){
        $.extend(  $.mobile , {
                defaultPageTransition: 'slide'
            });
    });

$(document).bind('pageinit', function() {
        $('a.bg-ajax').bind('click', function(e){
                e.preventDefault();
                var that = $(this);
                var href = that.attr('data-goto');

                $.getJSON(href, function(data) {
                        var msg = data.msg;
                        var messages_el = that.siblings('.messages')
                        
                        messages_el.slideDown().text(msg);
                        var original_text = $(".ui-btn-text", that).text();
                        $(".ui-btn-text", that).text("Done!");

                        var m = function() {
                            messages_el.slideUp();
                            $(".ui-btn-text", that).text(original_text);
                        };

                        setTimeout(m,3000);
                    });
            });
    });
