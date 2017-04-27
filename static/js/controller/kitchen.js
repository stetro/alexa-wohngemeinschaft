

angular.module('restaurant')
    .controller('KitchenController', function($scope, Order, $interval){

        $scope.interval = $interval(function(){
            console.log('request...')

            Order.getOrders().then(function(a){
                
            });
        }, 1000);

        
    });

