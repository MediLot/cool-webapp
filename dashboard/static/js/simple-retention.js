'use strict';

var chart = echarts.init(document.getElementById('line'));
var chart2 = echarts.init(document.getElementById('heat'));

function detect( events, measure, time, cohortField){
    $.ajax({
        type: "POST",
        data: { 
        	mode: "simple-cohort", 
        	csrfmiddlewaretoken: CSRF_TOKEN, 
        	events: JSON.stringify(events), 
        	measure: measure, 
        	time: time, 
        	cohortField: cohortField, 
        	datasource:  datasource,
        	ageField: ageField
        },
        url: "/api/v1",
        success: function(response) {
            // console.log(response);
            var responseData = JSON.parse(response);
            var option = {
		        tooltip: {
		            trigger: 'axis',

		            formatter: function (info) {
		            	var result = "";
		            	info.sort(function compare(a, b) {
		            		return b.data[1] - a.data[1];
						});
			        	for(var i in info){
			        		var value = info[i].data[1];
			            	if(Math.abs(value) > 1000000000)
			                	value = (value/1000000000).toFixed(2)+"B";
			                else if(Math.abs(value) > 1000000)
			                	value = (value/1000000).toFixed(2)+"M";
			                else if(Math.abs(value) > 1000)
			                	value = (value/1000).toFixed(2)+"K";
			                else
			                	value = value;
			        		result += "<div>" + info[i].seriesName+": "+ value + "</div>";
			        	}
			        	return result;
		            }
		        },
		        legend: {
		            x: 'center',
		            y: 'bottom',
		            data:['# of users']
		        },
		        toolbox:{
		            show:true,
		            x : 'left',
		            y : 'top',
		            feature: {
		                restore:{
		                    title: 'Restore'
		                },
		                saveAsImage:{
		                    title: 'Save'
		                },
		                dataView: {
		                    title: 'Dataview',
		                    lang: ['DataView', 'Close', 'Refresh']
		                },
		                dataZoom: {
		                    yAxisIndex: 'none',
		                    title:
		                    {
		                        zoom: 'Zoom',
		                        back: 'Back'
		                    }
		                },
		                magicType: {
		                    type: ['bar', 'line'],
		                    title:
		                    {
		                        'bar' : 'Change To Bar Chart',
		                        'line' : 'Change To Line Chart'
		                    }
		                }        }
		        },
		        grid: {
                        left: 'left',
                        bottom: '25%',
                        containLabel: true
                    },
		        xAxis: {
		            type: 'value'
		        },
		        yAxis: {
		            type: 'value'
		        },
		        series: [{
		            type: 'line',
		            smooth: true
		        }] 
		    };
		    var option2 = {
                tooltip: {
			        position: 'top',
			        formatter: function (info) {
			        	var value = info.data[2];
			        	return value;
		            }
			    },
			    animation: false,
			    grid: {
                    left: 'left',
                    bottom: '25%',
                    containLabel: true
                },
			    xAxis: {
			        type: 'category',
			        //data: x,
			        splitArea: {
			            show: true
			        }
			    },
			    yAxis: {
			        type: 'category',
			        splitArea: {
			            show: true
			        }
			    },
			    visualMap: {
			        min: 0,
			        max: 10000,
			        calculable: true,
			        orient: 'horizontal',
			        left: 'center',
			        bottom: '15%',
			        inRange: {
		                  color: ['lightgray', 'gold', 'tomato']
		              }
			        
			    },
			    series: [{
			        name: 'Usage',
			        type: 'heatmap',
			        label: {
			            normal: {
			            	textStyle:{
			        			color:"black",
                                fontSize: 10
			        		},
			                show: true,
			                formatter: function (info) {
                                for(var i in info){
                                    var value = info.value[2];
                                    // console.log(value);
                                    if(Math.abs(value) > 1000000000)
                                        value = (value/1000000000).toFixed(0)+"B";
                                    else if(Math.abs(value) > 1000000)
                                        value = (value/1000000).toFixed(0)+"M";
                                    else if(Math.abs(value) > 1000)
                                        value = (value/1000).toFixed(0)+"K";
                                    else
                                        value = value;
                                };
                                return value;
                            }
			            }
			        },
			        itemStyle: {
			        	normal:{
			        		
			        	},
			            emphasis: {
			                shadowBlur: 10,
			                shadowColor: 'rgba(0, 0, 0, 0.5)'
			            }
			        }
			    }]
			};

            var max = 0;
            for(var i in responseData['data']['heatmap']){
                if(responseData['data']['heatmap'][i][0] > max)
                    max = responseData['data']['heatmap'][i][0];
            };

            if(max > 15)
                max = 30;
            else if(max > 7)
                max = 15;
            else
                max = 7;

            var xAxisArray = [];
            for(var k = 0; k < max + 1; k++){
                xAxisArray.push(k);
            }

            var cols = responseData['data']['columes'].reverse()
            option['series'] = responseData['data']['values'];
            option['legend']['data'] = cols;
            option['xAxis']['max'] = max;
            option2['xAxis']['data'] = xAxisArray;
    		option2['series'][0]['data'] = responseData['data']['heatmap'];
            // console.log(responseData['data']['heatmap']);
    		option2['yAxis']['data'] = cols;
    		option2.visualMap.max = 100;
    		option2.visualMap.min = 0;
    		// console.log(responseData['data']['values']);
    		$("#line").css("height", "450px");
			$("#heat").css("height", "750px");
			chart.resize();
    		chart.setOption(option);
    		chart2.resize();
    		chart2.setOption(option2);
    		$('html, body').animate({
		        scrollTop: $("#line").offset().top
		    }, 500);
        },
    });
}

function updateChart() {
    var children = $("#sortable1").children("li");
    var events = [];
    for(var i = 0; i < children.length; i++) events.push(children[i].innerHTML);
	// console.log(events);
	var cohortField = $('input[name=cohortField]:checked').val();
	var time = $('input[name=time]:checked').val();
	var measure = $('input[name=measure]:checked').val();


    detect(events, measure, time, cohortField);
}
function changeFunc1() {
	$('input[name=cohortField]').parent().css("background-color", "lightgray");
	$('input[name=cohortField]:checked').parent().css("background-color", "rgba(155, 227, 177, 0.65)");
}

function changeFunc2() {
	$('input[name=time]').parent().css("background-color", "lightgray");
	$('input[name=time]:checked').parent().css("background-color", "rgba(155, 227, 177, 0.65)");
}

function changeFunc3() {
	$('input[name=measure]').parent().css("background-color", "lightgray");
	$('input[name=measure]:checked').parent().css("background-color", "rgba(155, 227, 177, 0.65)");
}

changeFunc1();
changeFunc2();
changeFunc3();

$(document).ready(function() {

    // Enable drag-n-drop behaviour on the sortable lists.
	$( "#sortable0" ).sortable({
        items: "li",
	}).disableSelection();
	$( ".connectedSortable" ).sortable({
        items: "li",
        update: function(event, ui) { 
            var sortables = $('.connectedSortable');
            for(var i = 0; i < sortables.length; i++) {
                if($(sortables[i]).children("li").length > 0) {
                    $(sortables[i]).children(".list-placeholder").hide();
                } else {
                    $(sortables[i]).children(".list-placeholder").show();
                }
            }
        },
		connectWith: ".connectedSortable"
	});
});

$(window).on('resize', function() {
    chart.resize();
    chart2.resize();
});
