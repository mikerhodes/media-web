$(document).bind("mobileinit", function(){
        $.extend(  $.mobile , {
                defaultPageTransition: 'slide'
            });
    });

$(document).bind('ready', function() {
        $('a.bg-ajax').bind('click', function(e){
                e.preventDefault();
                var that = $(this);
                var href = that.attr('data-goto');

                $.getJSON(href, function(data) {
                        var msg = data.msg;
                        var messages_el = that.siblings('.messages')
                        
                        messages_el.slideDown().text(msg);

                        var m = function() {
                            messages_el.slideUp();
                        };

                        setTimeout(m,3000);
                    });
            });
    });
