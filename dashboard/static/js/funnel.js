'use strict';

var eventFilterHtml = '<div class="form-group row"> <label class="control-label col-md-1 col-sm-1 col-xs-12">Their</label> <div class="select-multi-stage col-md-10 col-sm-10 col-xs-12"> <div class="col-md-5 col-sm-5 col-xs-11 width"> <select class="form-control select2-single data-table-yaml"> </select> </div> <label class="control-label float-left">is</label> <div class="col-md-6 col-sm-6 col-xs-12"> <select class="form-control second-stage"> </select> </div> <div class="col-sm-6 col-sm-6 col-xs-12 datetimepicker" style="display: none;"><div class="input-group date date1"><input type="text" class="form-control" /><span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span></div><div class="input-group date date2"><input type="text" class="form-control" /><span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span></div></div><div class="col-sm-6 col-sm-6 col-xs-12 intRange" style="display: none;"><div class="col-md-5 col-sm-5 col-xs-5"><input type="text" class="form-control event-min " placeholder="1"></div><div style="float:left; line-height:33px;">-</div><div class="col-md-5 col-sm-5 col-xs-5"><input type="text" class="form-control event-max " placeholder="100"></div></div></div> <i class="fa fa-plus-circle eventFilter-add" style="padding-right:7px;" aria-hidden="true"></i> <i class="fa fa-minus-circle eventFilter-remove" style="display:none;padding-right:7px;" aria-hidden="true"></i> </div>';
var cohortEventHtml = '<div class="event-container"><div class="form-group"><label class="col-sm-offset-2 control-label birthEvent-label">Event </label><i class="fa fa-minus-circle event-remove" style="display:none;padding-left:7px" aria-hidden="true"></i></div><div class="form-group"><div class="row"><label class="control-label col-md-3 col-sm-3 col-xs-12">Event:</label><div class="col-md-9 multi-eventFilters eventSelection"><div class="form-group row"><label class="control-label col-md-1 col-sm-1 col-xs-12">Their</label><div class="select-multi-stage col-md-10 col-sm-10 col-xs-12"><div class="col-md-5 col-sm-5 col-xs-11 width"><select class="form-control select2-single data-table-yaml"></select></div><label class="control-label float-left">is</label><div class="col-md-6 col-sm-6 col-xs-12 width"><select class="form-control second-stage"> </select></div><div class="col-sm-6 col-sm-6 col-xs-12 datetimepicker" style="display:none"><div class="input-group date date1"><input type="text" class="form-control" /><span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span></div><div class="input-group date date2"><input type="text" class="form-control" /><span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span></div></div><div class="col-sm-6 col-sm-6 col-xs-12 intRange" style="display:none"><div class="col-md-5 col-sm-5 col-xs-5"><input type="text" class="form-control event-min" placeholder="1"></div><div style="float:left;line-height:33px">-</div><div class="col-md-5 col-sm-5 col-xs-5"><input type="text" class="form-control event-max" placeholder="100"></div></div></div><i class="fa fa-plus-circle eventFilter-add" style="padding-right:7px" aria-hidden="true"></i><i class="fa fa-minus-circle eventFilter-remove" style="display:none;padding-right:7px" aria-hidden="true"></i></div></div></div><div class="form-group"><label class="control-label col-md-3 col-sm-3 col-xs-12" for="min">Frequency:</label><div class="col-md-1 col-sm-1 col-xs-5"><input type="text" name="min" required="required" class="form-control col-md-2 col-xs-2 min" placeholder="1"></div><div style="float:left;line-height:33px">-</div><div class="col-md-1 col-sm-1 col-xs-5"><input type="text" name="max" required="required" class="form-control col-md-2 col-xs-2 max" placeholder="∞"></div><div style="float:left;line-height:33px">time(s)</div></div></div></div>';
var cohortUserHtml = '<div class="event-container"> <div class="form-group"> <label class="col-sm-offset-2 control-label birthEvent-label">Event </label> <i class="fa fa-minus-circle event-remove" style="display:none;padding-left:7px;" aria-hidden="true"></i> </div><div class="form-group"> <div class="row"> <label class="control-label col-md-3 col-sm-3 col-xs-12">Event:</label> <div class="col-md-9 multi-eventFilters userSelection" > <div class="form-group row"> <label class="control-label col-md-1 col-sm-1 col-xs-12">Their</label> <div class="select-multi-stage col-md-10 col-sm-10 col-xs-12"> <div class="col-md-5 col-sm-5 col-xs-11 width"> <select class="form-control select2-single data-table-yaml"> </select> </div><label class="control-label float-left">is</label> <div class="col-md-6 col-sm-6 col-xs-12 width"> <select class="form-control second-stage"> </select> </div><div class="col-sm-6 col-sm-6 col-xs-12 datetimepicker" style="display: none;"><div class="input-group date date1"><input type="text" class="form-control" /><span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span></div><div class="input-group date date2"><input type="text" class="form-control" /><span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span></div></div><div class="col-sm-6 col-sm-6 col-xs-12 intRange" style="display: none;"><div class="col-md-5 col-sm-5 col-xs-5"><input type="text" class="form-control event-min " placeholder="1"></div><div style="float:left; line-height:33px;">-</div><div class="col-md-5 col-sm-5 col-xs-5"><input type="text" class="form-control event-max " placeholder="100"></div></div></div><i class="fa fa-plus-circle eventFilter-add" style="padding-right:7px;" aria-hidden="true"></i> <i class="fa fa-minus-circle eventFilter-remove" style="display:none;padding-right:7px;" aria-hidden="true"></i> </div></div></div><div class="form-group"> <label class="control-label col-md-3 col-sm-3 col-xs-12" for="last-name">Frequency:</label> <div class="col-md-1 col-sm-1 col-xs-5"> <input type="text" required="required" class="form-control col-md-2 col-xs-2 min" placeholder="1"> </div><div style="float:left; line-height:33px;">-</div><div class="col-md-1 col-sm-1 col-xs-5"> <input type="text" required="required" class="form-control col-md-2 col-xs-2 max" placeholder="∞"> </div><div style="float:left; line-height:33px;">time(s)</div></div><div class="form-group"> <label class="control-label col-md-3 col-sm-3 col-xs-12" for="last-name">In the </label> <div style="width: 80px; float:left; line-height:33px;"> <select class="form-control select2-single range-select first"> <option>first</option> <option>any</option> </select> </div><div class="col-md-1 col-sm-1 col-xs-5"> <input type="text" required="required" class="form-control col-md-2 col-xs-2 day" placeholder="7" > </div><div style="float:left; line-height:33px; font-weight: 800;">day(s)</div></div></div></div>';
var globalFilterHtml = '<div class="global-filter select-multi-stage row pad-bottom"> <div class="col-md-3 col-sm-3 col-xs-6"> <select class="form-control select2-single data-table-yaml"> </select> </div> <div class="col-md-6 col-sm-6 col-xs-6"> <select class="form-control select2-single second-stage"> </select> </div><div class="col-sm-6 col-sm-6 col-xs-6 datetimepicker" style="display: none;"><div class="input-group date date1"><input type="text" class="form-control" /><span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span></div><div class="input-group date date2"><input type="text" class="form-control" /><span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span></div></div><div class="col-sm-6 col-sm-6 col-xs-6 intRange" style="display: none;"><div class="col-md-5 col-sm-5 col-xs-5"><input type="text" class="form-control event-min " placeholder="1"></div><div style="float:left; line-height:33px;">-</div><div class="col-md-5 col-sm-5 col-xs-5"><input type="text" class="form-control event-max " placeholder="100"></div></div> <i class="fa fa-plus-circle globalFilter-add" style="padding-right:7px;" aria-hidden="true"></i> <i class="fa fa-minus-circle globalFilter-remove" style="padding-right:7px;" aria-hidden="true"></i> </div>';
var stageHtml = '<div class="stage-group"><div class="form-group form-section-label"><label class="control-label section-title col-md-3 col-sm-3 col-xs-12">Stage Selection<i class="fa fa-plus-circle stage-add" style="padding-right:7px" aria-hidden="true"></i><i class="fa fa-minus-circle stage-remove" style="display:none;padding-right:7px" aria-hidden="true"></i></label></div><div class="events-container"><div class="event-container"><div class="form-group"><label class="col-sm-offset-2 control-label birthEvent-label">Event </label><i class="fa fa-minus-circle event-remove" style="display:none;padding-left:7px" aria-hidden="true"></i></div><div class="form-group"><div class="row"><label class="control-label col-md-3 col-sm-3 col-xs-12">Event:</label><div class="col-md-9 multi-eventFilters eventSelection"><div class="form-group row"><label class="control-label col-md-1 col-sm-1 col-xs-12">Their</label><div class="select-multi-stage col-md-10 col-sm-10 col-xs-12"><div class="col-md-5 col-sm-5 col-xs-11 width"><select class="form-control select2-single data-table-yaml"></select></div><label class="control-label float-left">is</label><div class="col-md-6 col-sm-6 col-xs-12 width"><select class="form-control second-stage"> </select></div><div class="col-sm-6 col-sm-6 col-xs-12 datetimepicker" style="display:none"><div class="input-group date date1"><input type="text" class="form-control" /><span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span></div><div class="input-group date date2"><input type="text" class="form-control" /><span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span></div></div><div class="col-sm-6 col-sm-6 col-xs-12 intRange" style="display:none"><div class="col-md-5 col-sm-5 col-xs-5"><input type="text" class="form-control event-min" placeholder="1"></div><div style="float:left;line-height:33px">-</div><div class="col-md-5 col-sm-5 col-xs-5"><input type="text" class="form-control event-max" placeholder="100"></div></div></div><i class="fa fa-plus-circle eventFilter-add" style="padding-right:7px" aria-hidden="true"></i><i class="fa fa-minus-circle eventFilter-remove" style="display:none;padding-right:7px" aria-hidden="true"></i></div></div></div><div class="form-group"><label class="control-label col-md-3 col-sm-3 col-xs-12" for="min">Frequency:</label><div class="col-md-1 col-sm-1 col-xs-5"><input type="text" name="min" required="required" class="form-control col-md-2 col-xs-2 min" placeholder="1"></div><div style="float:left;line-height:33px">-</div><div class="col-md-1 col-sm-1 col-xs-5"><input type="text" name="max" required="required" class="form-control col-md-2 col-xs-2 max" placeholder="∞"></div><div style="float:left;line-height:33px">time(s)</div></div></div></div></div><div class="form-group add-event-btn"><div class="col-md-6 col-sm-6 col-xs-12 col-md-offset-2"><button type=button class="btn btn-primary add-btn"><i class="fa fa-plus-circle" style="padding-right:7px" aria-hidden="true"></i>Add Event</button></div></div></div>';

var funnelTemplate = '{"ordered": "true"}';
var eventSelectionTemplate = '{"eventSelection":[{"fieldValue":{"type":"AbsoluteValue","values":["LAUNCH"],"baseField":null,"baseEvent":-1},"cubeField":"ACTION","filterType":"Set"}]}';
var eventTemplate = '{"fieldValue":{"type":"AbsoluteValue","values":["LAUNCH"],"baseField":null,"baseEvent":-1},"cubeField":"ACTION","filterType":"Set"}';
var loyalTemplate = '{"birthSequence":{"birthEvents":[]},"outputCohort":"loyal"}';
var loyalSelectionTemplate = '{"eventSelection":[],"timeWindow":{"length":7,"slice":"false","unit":"DAY"}}';

$(document).ready(function() {
    $(".range-select").select2({
        //placeholder: 'Select some events',
        minimumResultsForSearch: 999,
    }).on('change', function() {
        //console.log($(this).val());
        if($(this).val() === "events") {
            $(".range-others").show();
        } else {
            $(".range-others").hide();
        }
    });
    $(".select2-multiple-remote").select2({
        multiple: true,
        placeholder: 'Select some events',
        data: djangoData.events
    });

    initCubeYamlSelect2($(".select2-single.data-cube-yaml"));
    initTableYamlSelect2($(".select2-single.data-table-yaml"));
    initSpecialTableYamlSelect2($(".select2-single2.data-table-yaml"));
    $("#line").hide();
    $("#heat").hide();
    $("#loading").hide();
});


function initCubeYamlSelect2(jqObj) {
    jqObj.append('<option></option>'); // for select2 placeholder
    jqObj.select2({
        minimumResultsForSearch: 5,
        placeholder: 'Select an option',
        data: djangoData['cube.yaml']['measures'].map(function(d,i) {
            return { id: String(d.name), text: d.name};
        })
    });
}

function initTableYamlSelect2(jqObj) {
    jqObj.append('<option></option>'); // for select2 placeholder
    jqObj.parents(".select-multi-stage").find(".second-stage").select2({
        placeholder: 'Select an option',
        disabled: true
    });
    jqObj.select2({
        minimumResultsForSearch: 5,
        placeholder: 'Select an option',
        data: djangoData['table.yaml']['fields'].map(function(d,i) {
            return { id: String(i), text: d.name };
        })
    }).on('change', function(d) {
        var idx = $(this).val();
        var obj = djangoData['table.yaml']['fields'][idx];
        // console.log(obj);
        if(obj.dataType === 'String'){
        	var datetimepicker = $(this).parents(".select-multi-stage").find(".datetimepicker");
        	$(datetimepicker).hide();
        	var intRange = $(this).parents(".select-multi-stage").find(".intRange");
        	$(intRange).hide();
        	var secondStage = $(this).parents(".select-multi-stage").find(".second-stage");
        	secondStage.show();
	        secondStage.select2('destroy').empty().select2({
	            multiple: true,
	            ajax: {
	                url: '/dim/v1/?col=' + obj.name,
	                dataType: 'json',
	                data: function(params) {
	                    // console.log("params", params);
	                    return {
	                        term: params.term || '',
	                        page: params.page || 1
	                    }
	                },
	                processResults: function(resp) {
	                    // console.log("server response: " ,resp);
	                    resp.results = resp.results.map(function(d,i) {
	                        return { id: d, text: d };
	                    });
	                    resp.pagination.more = (resp.pagination.more === "true");
	                    return resp;
	                },
	                delay: 500
	            },
	            cache: true,
	            disabled: false
	        });
        }else if(obj.fieldType === 'ActionTime'){
        	var secondStage = $(this).parents(".select-multi-stage").find(".second-stage");
        	secondStage.select2('destroy').empty().select2({
		        placeholder: 'Select an option',
		        disabled: true
		    });
        	var secondStageContainer = $(this).parents(".select-multi-stage").find(".select2-container--disabled");
        	$(secondStage).hide();
        	$(secondStageContainer).hide();
        	var intRange = $(this).parents(".select-multi-stage").find(".intRange");
        	$(intRange).hide();
        	var datetimepicker = $(this).parents(".select-multi-stage").find(".datetimepicker");
        	$(datetimepicker).show();
        	
        	$.get( '/dim/v1/?col=' + obj.name, function( data ) {
        		var result = JSON.parse(data).results[0].split("|");
        		var start = result[0] + " 00:00:00";
        		var end = result[1] + " 23:59:59";
				$($(datetimepicker).find(".input-group.date1")).datetimepicker({
					format: 'YYYY/MM/DD HH:mm:ss',
					minDate: start,
    				maxDate: end,
    				defaultDate: start
				});
        		$($(datetimepicker).find(".input-group.date2")).datetimepicker({
        			format: 'YYYY/MM/DD HH:mm:ss',
        			minDate: start,
    				maxDate: end,
    				defaultDate: end
        		});
        		$($(datetimepicker).find(".input-group.date1")).on("dp.change", function (e) {
		            $($(datetimepicker).find(".input-group.date2")).data("DateTimePicker").minDate(e.date);
		        });
		        $($(datetimepicker).find(".input-group.date2")).on("dp.change", function (e) {
		            $($(datetimepicker).find(".input-group.date1")).data("DateTimePicker").maxDate(e.date);
		        });
			});
        }else{
        	var secondStage = $(this).parents(".select-multi-stage").find(".second-stage");
        	secondStage.select2('destroy').empty().select2({
		        placeholder: 'Select an option',
		        disabled: true
		    });
        	var secondStageContainer = $(this).parents(".select-multi-stage").find(".select2-container--disabled");
        	$(secondStage).hide();
        	$(secondStageContainer).hide();
        	var datetimepicker = $(this).parents(".select-multi-stage").find(".datetimepicker");
        	$(datetimepicker).hide();
        	var intRange = $(this).parents(".select-multi-stage").find(".intRange");
        	$(intRange).show();
        }
        
    });
}

function initSpecialTableYamlSelect2(jqObj) {
    jqObj.append('<option></option>'); // for select2 placeholder
    jqObj.parents(".select-multi-stage").find(".second-stage").select2({
        placeholder: 'Select an option',
        disabled: true
    });
    var data = [];
    for(var i in djangoData['table.yaml']['fields']){
    	var obj = djangoData['table.yaml']['fields'][i];
    	if(obj.dataType === 'String'){
    		data.push({ id: String(i), text: obj.name });
    	}
    }
    jqObj.select2({
        minimumResultsForSearch: 5,
        placeholder: 'Select an option',
        data: data
    }).on('change', function(d) {
        var idx = $(this).val();
        var obj = djangoData['table.yaml']['fields'][idx];
        // console.log(obj);
    	var secondStage = $(this).parents(".select-multi-stage").find(".second-stage");
    	secondStage.show();
        secondStage.select2('destroy').empty().select2({
            multiple: true,
            ajax: {
                url: '/dim/v1/?col=' + obj.name,
                dataType: 'json',
                data: function(params) {
                    // console.log("params", params);
                    return {
                        term: params.term || '',
                        page: params.page || 1
                    }
                },
                processResults: function(resp) {
                    // console.log("server response: " ,resp);
                    resp.results = resp.results.map(function(d,i) {
                        return { id: d, text: d };
                    });
                    resp.pagination.more = (resp.pagination.more === "true");
                    return resp;
                },
                delay: 500
            },
            cache: true,
            disabled: false
        });
        
    });
}

$(document.body).on('click', '.globalFilter-add.fa-plus-circle', function(d) {
    var filterContainer = $("#global-filters-container");
    var added = $(globalFilterHtml);
    filterContainer.append(added);
    initTableYamlSelect2(added.find(".data-table-yaml"));
    $(".globalFilter-empty-btn").hide();
});

$(document.body).on('click', '.globalFilter-remove.fa-minus-circle', function(d) {
    var globalFiltersContainer = $("#global-filters-container");
    $(this).parents(".global-filter").remove();
    if(globalFiltersContainer.children(".global-filter").size() < 1) {
        $(".globalFilter-empty-btn").show();
    } else {
        $(".globalFilter-empty-btn").hide();
    }

});

// Add event.
function handleNewUserEvent() {
    var added = $(cohortUserHtml);
    $("#users-events-container").append(added);
    initTableYamlSelect2(added.find(".data-table-yaml"));
    added.find(".select2-multiple-remote").select2({
        multiple: true,
        placeholder: 'Select some events',
        data: djangoData.events
    });
    var eventsContainer = $("#users-events-container");
    eventsContainer.find('.event-remove.fa-minus-circle').show();
}

$(document.body).on('click', '.add-btn', function(d) {
    var added = $(cohortEventHtml);
    var eventsContainer = $(this).parents(".form-group").prev('.events-container');
    eventsContainer.append(added);
    initTableYamlSelect2(added.find(".data-table-yaml"));
    added.find(".select2-multiple-remote").select2({
        multiple: true,
        placeholder: 'Select some events',
        data: djangoData.events
    });

    
    eventsContainer.find('.event-remove.fa-minus-circle').show();
});

// Remove event.
$(document.body).on('click', '.event-remove.fa-minus-circle', function(d) {
    var eventContainer = $(this).parents(".event-container");
    var eventsContainer = $(this).parents(".events-container");
    eventContainer.remove();
    if(eventsContainer.children(".event-container").size() <= 1) {
        eventsContainer.find('.event-remove.fa-minus-circle').hide();
    }
});

// Add eventFilter.
$(document.body).on('click', '.eventFilter-add.fa-plus-circle', function(d) {
    var container = $(this).parents(".multi-eventFilters");
    var added = $(eventFilterHtml);
    container.append(added);
    initTableYamlSelect2(added.find(".data-table-yaml"));

    // If going from 1 to 2, show del btn
    container.find(".eventFilter-remove").show();
});

$(document.body).on('click', '.stage-remove.fa-minus-circle', function(d) {
    var stageContainer = $(this).parents(".stage-group");
    var stagesContainer = $(this).parents(".stages");
    stageContainer.remove();
    if(stagesContainer.children(".stage-group").size() <= 1) {
        stagesContainer.find('.stage-remove.fa-minus-circle').hide();
    }
});

// Add eventFilter.
$(document.body).on('click', '.stage-add.fa-plus-circle', function(d) {
    var container = $(this).parents(".stages");
    var added = $(stageHtml);
    // console.log(added);
    container.append(added);
    initTableYamlSelect2(added.find(".data-table-yaml"));

    // If going from 1 to 2, show del btn
    container.find(".stage-remove").show();
});

// Remove eventFilter.
$(document.body).on('click', '.eventFilter-remove.fa-minus-circle', function(d) {
    var container = $(this).parents(".multi-eventFilters");
    $(this).parent().remove();

    // If only 1 left, hide del btn
    if(container.children().size() < 2) {
        container.find(".eventFilter-remove").hide();
    }
});

// Show/Hide Advanced options.
//$(".advanced-checkbox").on('change', function(d) {
$(document.body).on('click', '.advanced-checkbox', function(d) {
    var advancedForm = $(this).parents('.form-group').siblings(".advanced-container");
    if($(this).is(':checked')) {
        advancedForm.show();
    } else {
        advancedForm.hide();
    }
});
// Show/Hide Filter Users.
$("#filter-users-checkbox").on('change', function(d) {
    if($(this).is(':checked')) {
        $("#users-events-container").show();
        $(".users-add-event-btn").show();

    } else {
        $("#users-events-container").hide();
        $(".users-add-event-btn").hide();
    }
});

function buildLoyal(){
	var query = JSON.parse(loyalTemplate);
	query['dataSource'] = djangoData['datasource'];

	var eventSelectSize = $(".event-container .userSelection").size();
	var eventSelects = [];
	for(var h = 0; h < eventSelectSize; h++){
		var eventDiv = $($($(".event-container .userSelection")[h]).parent('div').parent('div')[0]);
		var eventSize = $($(".event-container .userSelection")[h]).find(".row").size();
		var events = [];
		for(var i = 0; i < eventSize; i++){
			// console.log($("#eventSelection .row")[i]);
			var event = JSON.parse(eventTemplate);
			var index = $($($(".event-container .userSelection")[h]).find(".row .data-table-yaml")[i]).val();
			
			var obj = djangoData["table.yaml"]['fields'][index];
			event['cubeField'] = obj.name;
			if(obj.dataType === 'String'){
				event['fieldValue']['values'] = $($($(".event-container .userSelection")[h]).find(".row .second-stage")[i]).val();
				events.push(event);
			}else if(obj.fieldType === 'ActionTime'){
				var v1 = $($($(".event-container .userSelection")[h]).find(".row .date1")[i]).find('input').val();
				var v2 = $($($(".event-container .userSelection")[h]).find(".row .date2")[i]).find('input').val();
				var range = v1 + "|" + v2;
				var value = [];
				value.push(range);
				event['fieldValue']['values'] = value;
			}else{
				var v1 = parseInt($($($(".event-container .userSelection")[h]).find(".row .event-min")[i]).val());
				var v2 = parseInt($($($(".event-container .userSelection")[h]).find(".row .event-max")[i]).val());
				v1 = Number.isInteger(v1)?v1:0;
				v2 = Number.isInteger(v2)?v2:100;
				if(v2 < v1){
					v2 = v1+1;
				}
				var range = v1 + "|" + v2;
				var value = [];
				value.push(range);
				event['fieldValue']['values'] = value;
			}
			events.push(event);
			
		}
		var eventSelect = JSON.parse(loyalSelectionTemplate);

		var min = parseInt($(eventDiv.find('.min')[0]).val());
		var max = parseInt($(eventDiv.find('.max')[0]).val());
		eventSelect['minTrigger'] = Number.isInteger(min)?min:1;
		eventSelect['maxTrigger'] = Number.isInteger(max)?max:-1;
		
		eventSelect['eventSelection'] = events;
		var day = parseInt(eventDiv.find('.day').val());
		eventSelect['timeWindow']['length'] = Number.isInteger(day)?day:7;
		eventSelect['timeWindow']['slice'] = (eventDiv.find('.first').val()==='any');
		eventSelects.push(eventSelect);
	}

	query['birthSequence']['birthEvents'] = eventSelects;

	return query;
}

function buildQuery(){
	var query = JSON.parse(funnelTemplate);
	query['dataSource'] = djangoData['datasource'];
	var measure = $('#measure').val();
	query['measure'] = measure;
    var stageSize = $(".stage-group").size();
    var stages = [];
    for(var g = 0; g < stageSize; g++){
    	var eventSelectSize = $($(".stage-group")[g]).find(".event-container .eventSelection").size();
    	var eventSelects = [];
    	for(var h = 0; h < eventSelectSize; h++){
    		var eventDiv = $($($($(".stage-group")[g]).find(".event-container .eventSelection")[h]).parent('div').parent('div')[0]);
    		var eventSize = $($($(".stage-group")[g]).find(".event-container .eventSelection")[h]).find(".row").size();
    		var events = [];
    		for(var i = 0; i < eventSize; i++){
    			// console.log($("#eventSelection .row")[i]);
    			var event = JSON.parse(eventTemplate);
    			var index = $($($($(".stage-group")[g]).find(".event-container .eventSelection")[h]).find(".row .data-table-yaml")[i]).val();

    			var obj = djangoData["table.yaml"]['fields'][index];
    			event['cubeField'] = obj.name;
    			if(obj.dataType === 'String'){
    				event['fieldValue']['values'] = $($($(".event-container .eventSelection")[h]).find(".row .second-stage")[i]).val();
    			}else if(obj.fieldType === 'ActionTime'){
    				var v1 = $($($($(".stage-group")[g]).find(".event-container .eventSelection")[h]).find(".row .date1")[i]).find('input').val();
    				var v2 = $($($($(".stage-group")[g]).find(".event-container .eventSelection")[h]).find(".row .date2")[i]).find('input').val();
    				var range = v1 + "|" + v2;
    				var value = [];
    				value.push(range);
    				event['fieldValue']['values'] = value;
    			}else{
    				var v1 = parseInt($($($($(".stage-group")[g]).find(".event-container .eventSelection")[h]).find(".row .event-min")[i]).val());
    				var v2 = parseInt($($($($(".stage-group")[g]).find(".event-container .eventSelection")[h]).find(".row .event-max")[i]).val());
    				v1 = Number.isInteger(v1)?v1:0;
    				v2 = Number.isInteger(v2)?v2:100;
    				if(v2 < v1){
    					v2 = v1+1;
    				}
    				var range = v1 + "|" + v2;
    				var value = [];
    				value.push(range);
    				event['fieldValue']['values'] = value;
    			}
    			events.push(event);
    		}
    		var eventSelect = JSON.parse(eventSelectionTemplate);
    		eventSelect['eventSelection'] = events;
    		var min = parseInt($(eventDiv.find('.min')[0]).val());
    		var max = parseInt($(eventDiv.find('.max')[0]).val());
    		eventSelect['minTrigger'] = Number.isInteger(min)?min:1;
    		eventSelect['maxTrigger'] = Number.isInteger(max)?max:-1;
    		eventSelects.push(eventSelect);
    	}
    	var stage = {};
        stage['birthEvents'] = eventSelects;
        stages.push(stage);
    }
	query['stages'] = stages;

	return query;
}

$('#query-form')[0].onsubmit = function(){
	var selects = $(".select2-single.data-table-yaml");
	for(var i = 0; i < selects.size(); i++){
		if($(selects[i]).is(":visible")){
			if($(selects[i]).val() === "" ){
				alert("Please select an option.");
				$(selects[i]).focus();
				return false;
			}
		}
	}
	var selects = $(".second-stage");
	for(var i = 0; i < selects.size(); i++){
		if($(selects[i]).is(":visible")){
			if($(selects[i]).val() === null){
				alert("Please select at least one value.");
				$(selects[i]).focus();
				return false;
			}
		}
	}

	
	if($('#filter-users-checkbox').is(":checked")){
		var loyalCreate = buildLoyal();
		// console.log(loyalCreate);
		var query = buildQuery();
		query['inputCohort'] = 'loyal';
		// console.log(query);
		loyalQuery(query, loyalCreate);
	}else{
		var query = buildQuery();
		// console.log(query);
		singleQuery(query);
	}
    
    return false;
}

function singleQuery(query){
    $("#funnel").hide();
    $("#loading").show();
	$.ajax({
		type: "POST",
		data: { mode: "funnel", csrfmiddlewaretoken: CSRF_TOKEN, data: JSON.stringify(query) },
		url: "/api/v1",
		success: function(response) {
			var responseData = JSON.parse(response);
			if(responseData.message == "OK"){
				var option = {
					tooltip: {
						trigger: 'axis',
                        formatter: '{c}',
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
							}		}
					},
					grid: {
					  left: 'left',
					  containLabel: true
					},
					xAxis: {
						type: 'category',
                        data: ['Stage'],
					},
					yAxis: {
						type: 'value'
                        
					},
					series: [{
						type: 'bar',
						smooth: true,
                        barMaxWidth: '120px',
                        data: []
					}]
				};
                var cols = []
                var stageSize = $(".stage-group").size();
                for(var g = 0; g < stageSize; g++){
                    cols.push("Stage "+(g+1));
                }

				option['series'][0]['data'] = responseData['data']['result'].map(function(d,i) {
                    return { name: "Stage " + String(i+1), value: ["Stage " + String(i+1), d]};
                });
				option['xAxis']['data'] = cols;
				var chart = echarts.init(document.getElementById('funnel'));
				$("#funnel").css("height", "450px");
                $("#loading").hide();
                $("#funnel").show();
				chart.resize();
				chart.setOption(option);
				$('html, body').animate({
					scrollTop: $("#funnel").offset().top
				}, 500);

				$(window).on('resize', function() {
					chart.resize();
				});			
			}else{
                $("#loading").hide();
				alert(responseData.message);
			}
		},
		error: function(response) {
            $("#loading").hide();
			alert("Invalid Query");
		}
	});
}

function loyalQuery(query1, query2){
    $("#funnel").hide();
    $("#loading").show();
	$.ajax({
		type: "POST",
		data: { mode: "loyal-funnel", csrfmiddlewaretoken: CSRF_TOKEN, data1: JSON.stringify(query1), data2: JSON.stringify(query2) },
		url: "/api/v1",
		success: function(response) {
            var responseData = JSON.parse(response);
            if(responseData.message == "OK"){
                var option = {
                    tooltip: {
                        trigger: 'axis',
                        formatter: '{c}',
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
                            }       }
                    },
                    grid: {
                      left: 'left',
                      containLabel: true
                    },
                    xAxis: {
                        type: 'category',
                        data: ['Stage'],
                    },
                    yAxis: {
                        type: 'value'
                        
                    },
                    series: [{
                        type: 'bar',
                        smooth: true,
                        barMaxWidth: '120px',
                        data: []
                    }]
                };
                var cols = []
                var stageSize = $(".stage-group").size();
                for(var g = 0; g < stageSize; g++){
                    cols.push("Stage "+(g+1));
                }

                option['series'][0]['data'] = responseData['data']['result'].map(function(d,i) {
                    return { name: "Stage " + String(i+1), value: ["Stage " + String(i+1), d]};
                });
                option['xAxis']['data'] = cols;
                var chart = echarts.init(document.getElementById('funnel'));
                $("#funnel").css("height", "450px");
                $("#loading").hide();
                $("#funnel").show();
                chart.resize();
                chart.setOption(option);
                $('html, body').animate({
                    scrollTop: $("#funnel").offset().top
                }, 500);

                $(window).on('resize', function() {
                    chart.resize();
                });      
            }else{
                $("#loading").hide();
                alert(responseData.message);
            }
		},
		error: function(response) {
            $("#loading").hide();
			alert("Invalid Query");
		}
	});
}


