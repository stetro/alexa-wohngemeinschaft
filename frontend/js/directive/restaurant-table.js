

angular.module('restaurant')
    .directive('restaurantTable', function(){
        return {
            restrict: 'E',
            replace: true,
            templateUrl:'template/restaurant-table.html',
            scope: {
                tableNumber: '=',
                guestCount: '='
            },
            link: function($scope){
                $scope.orders = [{
                    count:5,
                    name:'Currywurst'
                }];
            }
        };
    });