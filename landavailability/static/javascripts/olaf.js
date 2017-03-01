$(function(){
    /**
    Only enable geolocation if the browser supports it, and attach a handler
    when the user clicks.
    **/
    if ($('.geolocation_span').size() > 0 && navigator.geolocation) {
        $('.geolocation_span').show();
        $('#getLocation').click(function(){
            $('.geolocation_span').blur();
            $(document).click();
            navigator.geolocation.getCurrentPosition(setPosition);
            return false;
        });
    }

    function setPosition(position) {
        /* Turn this into a loation, rather than a latlng */
        $('#location').val("Current Location");
        $('#latitude').val(position.coords.latitude);
        $('#longitude').val(position.coords.longitude);
    }
});


