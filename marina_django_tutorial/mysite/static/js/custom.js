$(document).ready(function(){
     states = {
        'AL':'Alabama','AK':'Alaska','AZ':'Arizona','AR':'Arkansas','CA':'California',
        'CO':'Colorado','CT':'Connecticut','DE':'Delaware','FL':'FLorida','GA':'Georgia',
        'HI':'Hawaii','ID':'Idaho','IL':'Illinois','IN':'Indiana','IA':'Iowa','KS':'Kansas',
        'KY':'Kentucky','LA':'Louisiana','ME':'Maine','MD':'Maryland',
        'MA':'Massachusetts','MI':'Michigan','MN':'Minnesota','MS':'Mississippi','MO':'Missouri',
        'MT':'Montana','NE':'Nebraska','NV':'Nevada','NH':'New Hampshire','NJ':'New Jersey','NM':'New Mexico','NY':'New York',
        'NC':'North Carolina','ND':'North Dakota','OH':'Ohio','OK':'Oklahoma','OR':'Oregon',
        'PA':'Pennsylvania','RI':'Rhode Island','SC':'South Carolina','SD':'South Dakota',
        'TN':'Tennessee','TX':'Texas','UT':'Utah', 'VT':'Vermont','VA':'Virginia','WA':'Washington',
        'WV':'West Virginia','WI':'Wisconsin','WY':'Wyoming'
    }

    // $('.alert').toggle();

    populateMenu();

    $('#post-form').on('submit', function(event){
        event.preventDefault();
        // submit_zipcode();
    });

    $('#test_button').on('click',function(event){
        event.preventDefault();
        // send_zipcode_to_the_back();
        get_market_data_by_zipcode();
    });

    /// markets USDA data //calback
    function get_market_data_by_zipcode(){
        $.ajax({
            type: 'GET',
            url: 'http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=' + $("#zipcode").val(),
            success: function(json){
                console.log(json.results);
                var market_data = json.results;
                var markets = [];
                for (var i = 0; i< market_data.length; i++){
                    var market = market_data[i];
                    var id = market.id;
                    var marketplace = market.marketname;
                    var distance = marketplace.substr(0,marketplace.indexOf(' '));
                    var address = marketplace.substr(marketplace.indexOf(' ')+1);
                    $('.markets').append("<tr><td>"+distance+"</td><td>"+address+"</td></tr>");
                }
            },
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    function submit_zipcode()
    {
        get_state_by_zipcode(function(result){
            $.ajax({
                type: 'GET',
                url: '/polls/search',
                data: {statecode: result},
                success: function(json){
                    $("#results").prepend("<li>"+json.result+"</li>");
                },
                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            })
        });
    }

    function get_state_by_zipcode(callback){
        $.ajax({
            type: 'GET',
            url: 'http://ZiptasticAPI.com/' + $("#zipcode").val(),
            success: function(json){
                $("#zipcode").val('');
                var results = $.parseJSON(json);
                res = results.state;
                callback(states[res]);
            },
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    // function send_zipcode_to_the_back(){
    //     get_market_data_by_zipcode(function(result){
    //         $.ajax({
    //         type: 'GET',
    //         url: '/polls/getResults',
    //             data: {statecode: result},
    //             success: function(json){
    //                 $("#results").prepend("<li>"+json.result+"</li>");
    //             },
    //             error : function(xhr,errmsg,err) {
    //                 console.log(xhr.status + ": " + xhr.responseText);
    //             }
    //         })
    //     })
    // }



    // function get_market_data_by_id_from_zipcode(){

    // }






});

populateMenu = function(){
    for(i = 0; i < states.length; i++){
        $('.selectpicker').append('<option>'+states[i]+'</option>');
    }
}

