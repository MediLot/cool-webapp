const MAX_STAGES = 8;
var lastSortableIndex = 4;

// Called when user clicks "Submit" button.
// Calls API with the user input to get the funnel chart data and uses the data to update the eCharts funnel.
function updateChart() {

    var requestData = [];
    for(var i = 1; i <= lastSortableIndex; i++) {
        var listItems = $("#sortable" + i).find("li");
        var events = listItems.map(function(d,i) {
            var currEventNode = $(this);
            var name = currEventNode.children(".event-title").html();
            var minTrigger = currEventNode.find(".minTrigger.number-of-times-input").val();
            var maxTrigger = currEventNode.find(".maxTrigger.number-of-times-input").val();
            return {
                name: name,
                minTrigger: minTrigger ? +minTrigger : 1,
                maxTrigger: maxTrigger ? +maxTrigger : -1,
            }
        }).get();
        //var events = [];
        //for(var j = 0; j < children.length; j++) events.push({ 
            //name: children[j].innerHTML,
            //minTrigger: 1,
            //maxTrigger: -1
        //});
        // console.log(events);
        requestData.push(events);
    }
    console.log(requestData);

    $.ajax({
        type: "POST",
        data: { mode: "simple-funnel", csrfmiddlewaretoken: CSRF_TOKEN, data: JSON.stringify(requestData), datasource: datasource },
        url: "/api/v1",
        success: function(response) {
            var responseData = JSON.parse(response);
            chartData = responseData.data.result.map(function(d,i) {
                return {value: d, name:gettext('Stage ') + (++i)};
            });
            option.series[0].data = chartData;

            var funnelHeight = 100 + 90 * lastSortableIndex;
            $("#funnel-container, #echarts-funnel").css("height", funnelHeight + "px");
            //$(chart).css("height", funnelHeight + "px");

            myChart.resize();
            myChart.setOption(option);
        },
    });

}

function addSortable() {
    lastSortableIndex++;
    $(".list-delete-btn").remove();
    var sortable = '<div class="list-separator"> <i class="fa fa-arrow-down" aria-hidden="true"></i> </div> <ul id="sortable' + lastSortableIndex + '" class="connectedSortable"> <div class="list-label">' + gettext("Stage ") + lastSortableIndex + '</div> <div class="list-placeholder">' + gettext("(Any Event)") + '</div> <div id="sortables-remove-btn" class="list-delete-btn" onClick="removeSortable()"> <i class="fa fa-minus-circle" aria-hidden="true"></i> </div> </ul>';
    $("#sortables-container").append(sortable);

    // Enforce max number of stages.
    if(lastSortableIndex >= MAX_STAGES) {
        $("#sortables-add-btn").hide();
    }

    prepareSortables();
}

function removeSortable() {
    lastSortableIndex--;
    $("#sortables-container >  *:nth-last-child(-n+2)").children("li").appendTo("#sortable0");
    $("#sortables-container >  *:nth-last-child(-n+2)").remove();
    var removeBtn = '<div id="sortables-remove-btn" class="list-delete-btn" onClick="removeSortable()"> <i class="fa fa-minus-circle" aria-hidden="true"></i> </div>';
    // console.log(lastSortableIndex);
    if(lastSortableIndex > 1) {
        $("#sortables-container >  *:nth-last-child(1)").append(removeBtn);
    }
}

var myChart, chart, option;
var chartData = [
    {value:30, name:gettext('Event') + ' 3'},
    {value:10, name:gettext('Event') + ' 4'},
    {value:5, name:gettext('Event') + ' 5'},
    {value:50, name:gettext('Event') + ' 2'},
    {value:80, name:gettext('Event') + ' 1'}
];
function prepareSortables() {
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
}

$(document).ready(function() {

    // Enable drag-n-drop behaviour on the sortable lists.
    prepareSortables();

	chart = document.getElementById('echarts-funnel');
	myChart = echarts.init(chart);
	option = {
		color : [
			'rgba(255, 69, 0, 0.5)',
			'rgba(255, 150, 0, 0.5)',
			'rgba(255, 200, 0, 0.5)',
			'rgba(155, 200, 50, 0.5)',
			'rgba(55, 200, 100, 0.5)'
		],
		title : {
			text: '',
			// subtext: '纯属虚构'
		},
		tooltip : {
			trigger: 'item',
			formatter: "{b} : {c} "
		},
		toolbox: {
			show : true,
			feature : {
				//mark : {show: true},
				//dataView : {show: true, readOnly: false},
				//restore : {show: true},
				//saveAsImage : {show: true}
			}
		},
		legend: {
			data : [gettext('Stage') + ' 1',gettext('Stage') + ' 2',gettext('Stage') + ' 3',gettext('Stage') + ' 4',gettext('Stage') + ' 5',gettext('Stage') + ' 6',gettext('Stage') + ' 7',gettext('Stage') + ' 8']
		},
		calculable : true,
		series : [
			//{
				//name:'预期',
				//type:'funnel',
				//x: '10%',
				//width: '80%',
				//itemStyle: {
					//normal: {
						//label: {
							////formatter: '{b}预期'
						//},
						//labelLine: {
							//show : false
						//}
					//},
					//emphasis: {
						//label: {
							//position:'inside',
							////formatter: '{b}预期 : {c}%'
						//}
					//}
				//},
				//data:[
					//{value:60, name:'Event 3'},
					//{value:40, name:'Event 4'},
					//{value:20, name:'Event 5'},
					//{value:80, name:'Event 2'},
					//{value:100, name:'Event 1'}
				//]
			//},
			{
				name:'Funnel',
				type:'funnel',
                x: '10%',
                y: '15%',
                width: '90%',
                height: '70%',
				//maxSize: '100%',
				itemStyle: {
					normal: {
						borderColor: '#fff',
						borderWidth: 2,
						label: {
							position: 'inside',
							formatter: '{c}',
							textStyle: {
								color: '#333'
							}
						}
					},
					emphasis: {
						label: {
							position:'inside',
							//formatter: '{b}实际 : {c}%'
						}
					}
				},
				data:chartData
			}
		]
    };
    //$(chart).css("height", "1000px");
    $("#funnel-container, #echarts-funnel").css("height", "450px");
    myChart.resize();
    myChart.setOption(option);

    // toggle visibility of simple filters
    $(".event-filter-button").on("mouseup", function(d) {
        if($(this).siblings(".event-settings").is(":visible")) {
            $(this).siblings(".event-settings").hide();
        } else {
            $(this).siblings(".event-settings").show();
        }
    });

    // highlight filter icon when there is text in textboxes
    $(".number-of-times-input").on('input', function(d) {
        var inputs = $.makeArray($(this).siblings('.number-of-times-input').addBack());
        if(inputs.every(function(d) { return $(d).val() === ""; })) {
            $(this).parent().parent().siblings(".event-filter-button").css("color", "rgba(0,0,0,0.3)");
        } else {
            $(this).parent().parent().siblings(".event-filter-button").css("color", "rgba(0,0,0,0.9)");
        }
    });

    $(".event-clear-button").on('click', function(d) {
        $(this).siblings('.event-text-fields').children('input').val("");
        $(this).parent().siblings(".event-filter-button").css("color", "rgba(0,0,0,0.3)");
    });
});
$(window).on('resize', function() {
    myChart.resize();
});

