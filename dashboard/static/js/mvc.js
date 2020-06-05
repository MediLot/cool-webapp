$(document).ready(function() {
    var data = [[82,87,84,72,78],[66,59,22,45,43,37],[43,14,40,41,89,3,83,8],[27,42,28,7,30],[21,58,28,15,49],[3,13,9,16],[59,52,63,67,61,61,58,49,62,61],[90,28,29,6,7,6,7],[1.3,1.1,1.9,2.2,2.4,2.3,2.4,3.3,2.2,2.9],[73,85,41],[22,19,31,12,17,15,16,35,18,21],[24,61,33,48,30,68]];

    var legend = [["16-24","25-34","35-44","45-54","55+"],["Photos","Alarm","Calendar","Games","Music","News"],["Apparel","Appliances","Insurance","Cinema","Flights","Groceries","Hotels","TV sets"],["Advice","Compare","Inspire","Prepare","Other"],["Hobby","Inspire","Learn","Products","Relax"],["Colleague","Family","Friends","Partner"],["BR","CN","FR","DE","JP","RU","SG","KR","UK","US"],["Home","Work","Commuting","In a store","Bar","Park","Elsewhere"],["AR","BR","CN","FR","DE","JP","RU","SG","KR","US"],["Computer","Smartphone","Tablet"],["AU","BR","CN","FR","DE","JP","RU","SG","UK","US"],["Apparel","Appliances","Insurance","Cinema","Groceries","TV sets"]];

    function convert_to_bar_button(chart) {
        return {
            show: true,
            title: 'Change to Bar Chart',
            icon: 'http://www.iconarchive.com/download/i84572/custom-icon-design/flatastic-4/Pie-chart.ico',
            onclick: function() {
                var oldOption = chart.getOption();
                var newOption = jQuery.extend(true, {}, oldOption);

                newOption.toolbox[0].feature.myConvert.title = 'Change to Pie';
                newOption.toolbox[0].feature.myConvert.onclick = function() {
                    chart.clear();
                    chart.setOption(oldOption);
                };

                var series_data = newOption.series[0].data;
                var bar_category = series_data.map(function(x) {
                    return x.name
                });
                var bar_value = series_data.map(function(x) {
                    return {
                        value: x.value,
                        itemStyle: x.itemStyle
                    };
                });

                newOption.grid = {
                    left: 'left',
                    containLabel: true
                };
                newOption.xAxis = {
                    type: 'category',
                    data: bar_category,
                    axisLabel: {
                        interval: 0,
                    },
                };
                newOption.yAxis = {
                    type: 'value',
                };
                newOption.series = [{
                    type: 'bar',
                    data: bar_value,
                }];
                chart.clear();
                chart.setOption(newOption);
            }
        }
    }

    var colors = ['#f5c671','#FFF0BA','#f7a390','#CFD6DE','#ADC1D6','#7297BA']

    String.prototype.hashCode = function() {
        var hash = 0, i, chr;
        var string = this.substr(3, 7) + this.substr(0, 2) + this.slice(-2);
        if (string.length === 0) return hash;
        for (i = 0; i < string.length; i++) {
            chr   = string.charCodeAt(i);
            hash  = ((hash << 5) - hash) + chr;
            hash |= 37; // Convert to 32bit integer
        }
        return hash<0?hash%6+5:hash%6;
    };

    var c1g = echarts.init(document.getElementById('c1g'));
    var c1f = echarts.init(document.getElementById('c1f'));
    var c2g = echarts.init(document.getElementById('c2g'));
    var c2f = echarts.init(document.getElementById('c2f'));
    var c3g = echarts.init(document.getElementById('c3g'));
    var c3f = echarts.init(document.getElementById('c3f'));
    var c4g = echarts.init(document.getElementById('c4g'));
    var c4f = echarts.init(document.getElementById('c4f'));
    var c5g = echarts.init(document.getElementById('c5g'));
    var c5f = echarts.init(document.getElementById('c5f'));

    var continent_option = {
        tooltip: {
            trigger: 'item',
            formatter: function(d){
                var names = d.data.name.split(",");
                var result = "";
                for(var i in names){
                    result += "<p>"+names[i]+"</p>";
                }
                result += '<hr><b>' + d.value+'%</b>';
                return '<div>'+result+'</div>'
            }
        },
        legend: {
            orient: 'horizontal',
            x : 'center',
            y : 'bottom',
            formatter:function(i){
                if(i.length > 20){
                    return i.substr(0,15)+'...';
                }else{
                    return i;
                }

            },
            textStyle:{
                    fontSize: 10,
                }
        },
        toolbox: {
            show: true,
            // x: 'left',
            // y: 'bottom',
            feature: {

                // myConvert: convert_to_bar_button(c1g),
                restore: {
                    title: 'Restore'
                },
                dataView: {
                    title: 'DataView',
                    lang: ['DataView', 'Close', 'Refresh']
                },

                saveAsImage: {
                    title: 'Save'
                }
            }
        },
        series: [{
            name: 'Footprint',
            type: 'pie',
            radius : ['10%','50%'],
            // radius : '60%' ,
            center: ['50%', '40%'],
            // data: continent_data,
            roseType : 'radius',

            label: {
                normal: {
                    textStyle: {
                        fontSize: 12,
                        color: '#235894'
                    }
                },
                emphasis: {
                    show: true,
                    textStyle: {
                        fontSize: '24',
                        fontWeight: 'bold'
                    }
                }

            },
            labelLine: {
                normal: {
                    lineStyle: {
                        color: '#235894'
                    }
                }
            },
        }],

        itemStyle: {
            normal: {
                borderWidth: 4,
                borderColor: '#FFF'
            },
            emphasis: {
                shadowBlur: 15,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
        }
    };

    var bar_option = {
        tooltip: {
            trigger: 'axis',
            formatter: function(d){
                var names = d[1].data.name.split(",");
                var result = "";
                for(var i in names){
                    result += "<p>"+names[i]+"</p>";
                }
                result += '<hr><b>' + d[1].value+'%</b>';
                return '<div>'+result+'</div>'
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '0%',
            containLabel: true
        },
        toolbox: {
            show: true,
            x: 'left',
            y: 'top',
            feature: {
                restore: {
                    title: 'Restore'
                },
                saveAsImage: {
                    title: 'Save'
                },
                dataView: {
                    title: 'Dataview',
                    lang: ['DataView', 'Close', 'Refresh']
                },
                dataZoom: {
                    yAxisIndex: 'none',
                    title: {
                        zoom: 'Zoom',
                        back: 'Back'
                    }
                },
                magicType: {
                    type: ['line', 'bar'],
                    title: {
                        'line': 'Change To Line Chart',
                        'bar': 'Change To Bar Chart'
                    }
                }
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: true,
            data: [],
            axisLabel:{
                textStyle:{
                    fontSize: 10,
                }
            }
        },
        yAxis: {
            type: 'value',
        },
        series: [
            { // For shadow
                type: 'bar',
                itemStyle: {
                    normal: {color: 'rgba(0,0,0,0.05)'}
                },
                barGap:'-100%',
                barCategoryGap:'40%',
                data: [],
                animation: false
            },
            {
                type: 'bar',
                itemStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(
                            0, 0, 0, 1,
                            [
                                {offset: 0, color: '#83bff6'},
                                {offset: 0.5, color: '#188df0'},
                                {offset: 1, color: '#188df0'}
                            ]
                        )
                    }
                },
                data: []
            }
        ],
    };

    var getOption = function(index){
        var obj = jQuery.extend(true, {}, continent_option);
        obj.legend.data = legend[index];
        obj.series[0].data = data[index].map(function(x, i){
            return {
                'name': legend[index][i],
                'value': x,
                'itemStyle':{
                    'normal': {
                        'color': colors[legend[index][i].hashCode()],

                    },
                }
            }
        });
        return obj;
    }

    var getBarOption = function(index){
        var obj = jQuery.extend(true, {}, bar_option);
        obj.xAxis.data = legend[index];
        var y = 100;
        if(index == 8){
            y = 4;
            obj.tooltip.formatter = function(d){
                var names = d[1].data.name.split(",");
                var result = "";
                for(var i in names){
                    result += "<p>"+names[i]+"</p>";
                }
                result += '<hr><b>' + d[1].value+' devices</b>';
                return '<div>'+result+'</div>'
            }
        }

        obj.series[0].data = data[index].map(function(x, i){
            return {
                'name': legend[index][i],
                'value': y
            }
        });
        obj.series[1].data = data[index].map(function(x, i){
            return {
                'name': legend[index][i],
                'value': x,
                'itemStyle':{
                    'normal': {
                        'color': colors[legend[index][i].hashCode()],

                    },
                }
            }
        });
        return obj;
    }

    c1g.setOption(getBarOption(0));
    c1f.setOption(getOption(1));
    c2g.setOption(getOption(2));
    c2f.setOption(getBarOption(3));
    c3g.setOption(getOption(4));
    c3f.setOption(getBarOption(5));
    c4g.setOption(getBarOption(6));
    c4f.setOption(getBarOption(7));
    c5g.setOption(getBarOption(8));
    c5f.setOption(getOption(9));

    var c61 = echarts.init(document.getElementById('c61'));
    var c63 = echarts.init(document.getElementById('c63'));

    c61.setOption(getBarOption(10))
    c63.setOption(getOption(11))


    $(window).on('resize', function() {
        try {
            c1g.resize();
            c1f.resize();
            c2g.resize();
            c2f.resize();
            c3g.resize();
            c3f.resize();
            c4g.resize();
            c4f.resize();
            c5g.resize();
            c5f.resize();
            c61.resize();
            c63.resize();
        }
        catch(err) {}
    });

    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
        c1g.resize();
        c1f.resize();
        c2g.resize();
        c2f.resize();
        c3g.resize();
        c3f.resize();
        c4g.resize();
        c4f.resize();
        c5g.resize();
        c5f.resize();
        c61.resize();
        c63.resize();
    });
});
