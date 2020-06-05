'use strict';
angular.module( 'app', [] )

.factory( 'caLoyalCreateQuery', [ function(){

    return function( modelData, dataSource ){
        var query = {
            "dataSource" : dataSource,
            "birthSequence" : {
                "birthEvents" : [{
                    "minTrigger": null,
                    "maxTrigger": null,
                    "eventSelection": [{
                        "fieldValue": {
                            "type" : "AbsoluteValue",
                            "values" : null,
                            "baseField" : null,
                            "baseEvent" : -1
                        },
                        "cubeField" : "ACTION",
                        "filterType" : "Set"
                    }],
                    "timeWindow" : {
                        "length" : null,
                        "slice" : "false",
                        "unit" : "DAY"
                    }
                }]
            },
            "outputCohort" : "loyal"
        };
        var birthEvent = query.birthSequence.birthEvents[0];
        birthEvent.minTrigger = modelData.userFrequency;
        birthEvent.maxTrigger = 1000;
        var event = modelData.userEvent.split('::');
        birthEvent.eventSelection[0].fieldValue.values = [ event[0] ];
        birthEvent.timeWindow.length = modelData.userDays;
        return query;
    }
}])


.factory( 'caQuery', [ function(){

    function Event(){
        var query = {
            "minTrigger" : 1,
            "maxTrigger" : null,
            "eventSelection" : [{
                "fieldValue" : {
                    "type" : "AbsoluteValue",
                    "values" : null,
                    "baseField" : null,
                    "baseEvent" : -1
                },
                "cubeField" : "ACTION",
                "filterType" : "Set"
            }],
            "cohortFields" : [{
                "field" : null,
                "numLevel" : 10,
                "minLevel" : 0,
                "logScale" : "false",
                "scale" : 20
            }]
        };
        return query;
    }


    function Query( modelData, dataSource, appKey ){
        var query = {
            "dataSource" : dataSource,
            "appKey" : appKey || "fd1ec667-75a4-415d-a250-8fbb71be7cab",
            "birthSequence" : {
                "birthEvents" : [],
            },
            "ageField" : {
                "field" : null,
                "ageInterval" : 1,
                "range" : null
            },
            "measure" : null
        };
        query.ageField.field = 'DATE';
        query.ageField.range = [ '1|' + modelData.days ];
        query.measure        = modelData.metric;
        return query;
    }

    function addEvent( query, event, modelData, prevEvent ){
        var newEvent = new Event();

        newEvent.minTrigger = modelData.frequency;
        newEvent.maxTrigger = modelData.frequency;
        if ( modelData.frequencyType == 'least' ){
            newEvent.maxTrigger = -1;
        }
        else if ( modelData.frequencyType == 'most' ){
            newEvent.minTrigger = -1;
        }

        if ( event.type != 'event' ){
            newEvent.minTrigger = prevEvent.minTrigger * event.comparisonValue;
            newEvent.maxTrigger = prevEvent.maxTrigger * event.comparisonValue;
        }

        if ( event.event == 'any' ){
            newEvent.eventSelection[0].fieldValue.values = [ event.anyEventGroupOption ];
            newEvent.eventSelection[0].cubeField = [ event.anyEventGroup ];
        } else {
            var eventData = event.event.split('::');
            newEvent.eventSelection[0].fieldValue.values = [ eventData[0] ];
            newEvent.eventSelection[0].cubeField = eventData[1];
        }

        newEvent.cohortFields[0].field = modelData.group;

        query.birthSequence.birthEvents.push( newEvent );
        return query;
    }

    return function( data, dataSource, appKey ){
        var query = new Query( data, dataSource, appKey );
        var prevEvent = null;
        data.events.map( function( event ){
            query = addEvent( query, event, data, prevEvent );
            var events = query.birthSequence.birthEvents;;
            prevEvent = events [events.length-1];
        });
        return query;
    }

}])


.component( 'cohortAnalysis', {
    templateUrl: STATIC_ROOT + 'components/razer/cohortAnalysis/index.html'
    ,bindings: {
        form: '<'
    }
    ,controller: [
            '$timeout'
            ,'caQuery'
            ,'caLoyalCreateQuery'
        ,function(
            $timeout
            ,caQuery
            ,caLoyalCreateQuery
        ){
            this.$onInit = function(){

                function getData( inputData, valueKey, selectKey, selectValue ){
                    var data = [];
                    inputData.map( function( item ){
                        if ( item[ selectKey ] == selectValue ) {
                            var val = item[ valueKey ];
                            data.push([ val, val]);
                        }
                    });
                    return data;
                }

                function getActions( fields ){
                    return fields.filter( function( field ){
                        return field.fieldType == 'Action';
                    })
                }

                function getEvents( fields, dimensions ){
                    var actions = getActions( fields );
                    var events  = [];
                    actions.map( function( action ){
                        var data = dimensions [action.name].map( function( event ){
                            return event + '::' + action.name;
                        });
                        events = events.concat( data );
                    });
                    events = events.map( function( event ){
                        var data = event.split('::');
                        return [ event, data[0] ];
                    });
                    return events;
                }

                function getMetrics( data ){
                    return data.measures.map( function( metric ){
                        return [ metric.name, metric.name ];
                    });
                }

                function testData( prefix, no ) {
                    var data = [];
                    for ( var i=1; i<=no; i++ ){
                        var item = prefix + i;
                        data.push( [ item, item ] );
                    }
                    return data;
                }

                this.debug = false;
                this.model = {
                    events: [{type:'event'}]
                }
                this.userTypes = [
                     [ 'general',    'General Users'    ]
                    ,[ 'loyal',      'Loyal Users'      ]
                    ,[ 'endangered', 'Endangered Users' ]
                ]
                this.comparisonTypes = [
                     [ 'more', 'more' ]
                    ,[ 'less', 'less' ]
                ]
                this.frequencyTypes = [
                     [ 'least',  'at least'   ]
                    ,[ 'most',   'at most'    ]
                    ,[ 'equals', 'equals to'  ]
                ]
                var fields                = djangoData['table.yaml'].fields;
                this.groups               = getData( fields, 'name', 'fieldType', 'Segment' );
                this.metrics              = getMetrics( djangoData['cube.yaml'] );
                this.dimensions           = djangoData['dimensions'];
                this.events               = getEvents( fields, this.dimensions );
                this.anyEvents            = this.events.slice().concat( [[ 'any', 'ANY event' ]] );
            }

            this.getEvents = function( idx ){
                if ( idx > 1 ) {
                    return this.events;
                }
                else if ( this.model.events.length > 1 ){
                    return this.events;
                }
                else {
                    return this.anyEvents;
                }
            }

            this.addEvent = function(type){
                this.model.events.push({type:type});
            };

            this.anyEventGroupChanged = function( data ){
                if (!this.dimensions[ data ]) { return [] }
                this.anyEventGroupOptions = this.dimensions[ data ]
                    .map( function( option ){
                        return [ option, option ];
                    });
            };

            this.removeEvent = function(idx){
                this.model.events.splice( idx, 1 );
                if ( this.model.events.length == 1 ) {
                    this.model.events[0].type='event';
                }
            };

            this.updateChart = function(){
                if ( this.form.$invalid ) return;
                var query = caQuery( this.model, djangoData.datasource);
                var loyalCreateQuery = null;
                if ( this.model.userType == 'loyal' ){
                    var loyalCreateQuery = caLoyalCreateQuery( this.model , djangoData.datasource);
                }

                this.queries = [ query, loyalCreateQuery ];
                $timeout( function(){
                    advancedCADetect( query, loyalCreateQuery );
                }, 0, false );
            }
        }
    ]
})


.component( 'caDataRow', {
    templateUrl: STATIC_ROOT + 'components/razer/cohortAnalysis/ca-data-row.html'
    ,bindings: {
        rowLabel: '@'
    }
    ,transclude: true
})


.component( 'caInputNumber', {
    templateUrl: STATIC_ROOT + 'components/razer/cohortAnalysis/ca-input-number.html'
    ,bindings: {
         name:      '@'
        ,model:     '='
        ,classes:   '@'
        ,min:       '@'
        ,step:      '@'
    }
})


.component( 'caInputSelect', {
    templateUrl: STATIC_ROOT + 'components/razer/cohortAnalysis/ca-input-select.html'
    ,transclude: true
    ,bindings: {
         name:        '@'
        ,model:       '='
        ,options:     '<'
        ,blankOption: '@'
        ,classes:     '@'
        ,onChange:    '&'
    }
    ,controller: [ function(){
        this.$onInit = function(){
            if ( this.blankOption = '' ) {
                this.model = this.options[0][0];
            }
        };
    }]
})
