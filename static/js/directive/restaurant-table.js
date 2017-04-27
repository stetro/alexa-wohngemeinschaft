

angular.module('restaurant')
    .directive('restaurantTable', function(){
        return {
            restrict: 'E',
            replace: true,
            templateUrl:'template/restaurant-table.html',
            scope: {
                tableNumber: '=',
                guestCount: '=',
                orders:'='
            },
            link: function($scope){
            }
        };
    });