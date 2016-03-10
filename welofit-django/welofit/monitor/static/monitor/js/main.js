$(document).ready(function(){
    var graficos = "#progress, #dieta-now, #rutina-now";
    var progress = c3.generate({
        bindto: '#progress',
        data: {
            x: 'x',
            xFormat: '%d-%m-%Y',
            columns: [
                ['x', '17-01-2016', '24-01-2016', '31-01-2016', '07-02-2016', '14-02-2016', '21-02-2016'],  
                ['Peso', 100, 96, 94, 90, 88, 85],
                ['Grasa', 35, 34, 34, 32, 30, 29]
            ]
        },
        color: {
            pattern: ['#400026', '#f09', '#7F004C']
        },
        axis: {
            x: {
                type: 'timeseries',
                tick: {
                    format: '%d-%m'
                }
            }
        }
    });
    
    var diet = c3.generate({
        bindto: '#dieta-now',
        data: {
            columns: [
                ['Carbohidratos', 44],
                ['Proteinas', 28],
                ['Grasas', 28],
            ],
            type : 'pie',    
        },
        color: {
            pattern: ['#400026', '#f09', '#7F004C']
        }       
    });
    
    var routine = c3.generate({
        bindto: '#rutina-now',
        data: {
            columns: [
                ['Aeróbico', 70, 50, 40],
                ['Musculación', 30, 50, 60],
            ],
            type : 'bar', 
            groups: [
                ['Aeróbico', 'Musculación']
            ]
        },
        color: {
            pattern: ['#400026', '#f09', '#7F004C']
        }       
    });    
    
    
    $('#simple-menu').sidr({
        displace: true,
        onOpen: function () {
            $("#page-wrapper").css("width","85%");
            $(graficos).css("width","85%");  
        },
        onOpenEnd: function () {
            progress.flush();
            diet.flush(); 
            routine.flush();
        },
        onClose: function () {
            $("#page-wrapper").css("width","100%");
            $(graficos).css("width","100%");
        },
        onCloseEnd: function () {
            progress.flush(); 
            diet.flush();
            routine.flush();
        }   
    });
    if ($(window).width() >= 850){
        $('#simple-menu').trigger('click');
    };
    
    $('#tabs-container').responsiveTabs({
        startCollapsed: 'tabs'
    }); 
    $('.toggle-sidr').click(function(){
        if($(this).hasClass("fa-angle-double-right")){
            $(this).removeClass("fa-angle-double-right");
            $(this).addClass("fa-angle-double-left");
            return;
        }
        if($(this).hasClass("fa-angle-double-left")){
            $(this).removeClass("fa-angle-double-left")
            $(this).addClass("fa-angle-double-right") 
        }
    });
    $('.r-tabs-anchor').click(function(){
        progress.flush(); 
        diet.flush();
        routine.flush();
    });
});   
