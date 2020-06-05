'use strict';

angular.module( 'app', [ 'ui.router' ] )

.config( [
         '$stateProvider'
        ,'$urlRouterProvider'
    ,function(
         $stateProvider
        ,$urlRouterProvider
    ){
        [1,2,3].map( function(i){
            var step = 'step' + i
            $stateProvider.state({
                name: step
                ,url: '/'
                ,component: step
                ,params: {
                    step: null
                }
            });
        });
        $stateProvider.state({
            name: 'step2Error'
            ,url: '/upload/error/'
            ,component: 'step2Error'
                ,params: {
                    step: null
                }
        });
        $urlRouterProvider.otherwise( '/' );
}])


.value( 'fieldTypes', [
    {
         name:     'User ID'
        ,type:     'UserKey'
        ,dataType: 'String'
        ,label:     gettext('User ID')
    }
    ,{
         name:     'Event'
        ,type:     'Action'
        ,dataType: 'String'
        ,label:     gettext('Event')
    }
    ,{
         name:     'Event Related'
        ,type:     'Segment'
        ,dataType: 'String'
        ,label:     gettext('Event Related')
    }
    ,{
         name:     'Time'
        ,type:     'ActionTime'
        ,dataType: 'Int32'
        ,label:    gettext('Time')
    }
    ,{
         name:     'Value'
        ,type:     'Metric'
        ,dataType: 'Int32'
        ,label:    gettext('Value')
        ,default:  true
    }
])


.factory( 'fileReaderService', [
        '$q'
    ,function(
        $q
    ){
    return {
        data:     null
       ,header:   null
       ,filename: null
       ,fileObj:  null

       ,loadFile: function( fileObj ){
            this.filename   = fileObj.name;
            this.fileObj    = fileObj;
            var that        = this;
            var deferred    = $q.defer();
            var reader      = new FileReader()
            reader.onload   = function( event ){
                var data    = event.target.result.split('\n');
                that.header = data[0].split(',');
                that.data   = data.slice(0);
                deferred.resolve( that );
                return that;
            }
            reader.readAsText( fileObj );
            return deferred.promise;
        }
    }
}])


.factory( 'uploadValidation', [
    function(){
        var obj = {
            reset: function(){
                 this.sortedId   = 'OK'
                ,this.sortedTime = 'OK'
                ,this.timeFormat = 'OK'
                ,this.baseTime   = 'OK'
                ,this.error      = true
            }
            ,ok: function(){
                 this.sortedId   = null
                ,this.sortedTime = null
                ,this.timeFormat = null
                ,this.baseTime   = null
                ,this.error      = false
            }
        };
        obj.reset();
        return  obj;
    }
])


.factory( 'chkData', [
         'uploadValidation'
        ,'fileReaderService'
    ,function(
         uploadValidation
        ,fileReaderService
    ){
        function getColumnName( data, fieldType ){
            return data.find( function( field ){
                return field.fieldType.name == fieldType;
            });
        }

        return function( fields ){
            uploadValidation.reset();
            var error  = false;
            var data   = fileReaderService.data;
            var header = fileReaderService.header;

            var columnUserId = getColumnName( fields, 'User ID').name;
            var columnTime   = getColumnName( fields, 'Time').name;
            var idxId        = header.indexOf( columnUserId );
            var idxTime      = header.indexOf( columnTime );
            var columns      = data[1].split(',')
            var prevId       = columns [idxId];
            var prevTime     = columns [idxTime];
            var baseTime     = (new Date( '2016-01-01' )).valueOf();
            for ( var i=1, len=data.length; i<len; i++ ){
                var columns = data[i].split(',');
                var time = columns [idxTime];
                var date = new Date ( time );
            }

            if ( !error ){
                uploadValidation.ok();
            }
            return uploadValidation;
        }
    }
])


.component( 'step1', {
    templateUrl: '../../static/components/razer/uploadData/step1.html'
    ,controller: [
             '$q'
            ,'$state'
            ,'$timeout'
            ,'fileReaderService'
        ,function(
             $q
            ,$state
            ,$timeout
            ,fileReaderService
        ){
            var that = this;
            this.$onInit = function(){
                $('#fileElem')[0].addEventListener( 'change', this.fileChanged, false )
            };

            this.next = function( data){
                fileReaderService.loadFile( $('#fileElem')[0].files[0] ).then( function( data ){
                    $state.go( 'step2', { step: 2 } );
                });
            }

            this.fileChanged = function( e ){
                $timeout( function(){
                    that.filename = e.target.value;
                }, 0, true );
            }
        }
    ]
})


.component( 'step2', {
    templateUrl: STATIC_ROOT + 'components/razer/uploadData/step2.html'
    ,controller: [
             '$state'
            ,'$stateParams'
            ,'$timeout'
            ,'fieldTypes'
            ,'fileReaderService'
            ,'chkData'
        ,function(
             $state
            ,$stateParams
            ,$timeout
            ,fieldTypes
            ,fileReaderService
            ,chkData
        ){
            this.$onInit = function(){
                var that = this;
                if ( $stateParams.step != 2 ){
                    return $state.go( 'step1' );
                }
                this.fieldTypes = fieldTypes;
                this.defaultFieldType= fieldTypes.find( function( fieldType ){
                    return fieldType.default;
                });
                this.fields = fileReaderService.header.map( function( field ){
                    return { name: field, fieldType: that.defaultFieldType };
                });

                $timeout( function(){
                    $('[data-toggle="tooltip"]').tooltip();
                }, 0, false );
            };
            this.nextDisabled = function(){
                var fieldTypes = this.fields.map( function( field ){
                    return field.fieldType.name;
                });
                var required = [ 'Event', 'Time', 'User ID' ];
                this.missing = required.filter( function( field ){
                    var found = fieldTypes.find( function( val ){
                        return val == field;
                     })
                     return !found
                });
                this.message = (this.missing.length)? this.missing.join(', ') + ' field(s) are required': '';
                return this.missing.length;
            };
            this.next = function(){
                var uploadValidation = chkData( this.fields );
                if ( uploadValidation.error ) {
                    $state.go( 'step2Error', { step: 'error' } );
                } else {
                    fileReaderService.fields = this.fields;
                    $state.go( 'step3', { step: 3 } );
                }
            };
        }
    ]
})


.component( 'step2Error', {
    templateUrl: STATIC_ROOT + 'components/razer/uploadData/step2-error.html'
    ,controller: [
             '$state'
            ,'$stateParams'
            ,'uploadValidation'
        ,function(
             $state
            ,$stateParams
            ,uploadValidation
        ){
            this.$onInit = function(){
                if ( $stateParams.step != 'error' ){
                    return $state.go( 'step1' );
                }
                this.uploadValidation = uploadValidation;
            }
        }
    ]
})


.component( 'step3', {
    templateUrl: STATIC_ROOT + 'components/razer/uploadData/step3.html'
    ,controller: [
             '$state'
            ,'$stateParams'
            ,'$timeout'
            ,'fileReaderService'
        ,function(
             $state
            ,$stateParams
            ,$timeout
            ,fileReaderService
        ){
            this.$onInit = function(){
                if ( $stateParams.step != 3 ){
                    return $state.go( 'step1' );
                }
                this.fields = fileReaderService.fields;
                fileReaderService.metrics = [{}];
                this.metrics = fileReaderService.metrics;
                $timeout( function(){
                    $('[data-toggle="tooltip"]').tooltip();
                }, 0, false );
            };
            this.addMetric = function(){
                this.metrics.push({});
            }
            this.upload = function(){
                this.data = JSON.stringify({
                    fields:   fileReaderService.fields
                    ,metrics: fileReaderService.metrics
                });
                $timeout( function(){
                    $('#uploadForm').submit();
                }, 0, true );
            };
        }
    ]
})
