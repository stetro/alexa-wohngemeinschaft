

angular.module('restaurant')
    .controller('TableController', function($scope, Order, $interval){
        $scope.interval = $interval(function(){

            Order.getOrders().then(function (orders) {
                Object
                    .keys(orders.data)
                    .map(function (key) {
                        $scope.orders = orders.data[key].map(function (order) {
                            return {
                                name: 'Menü ' + order,
                                count: '1x'
                            }
                        });
                    });
            });
        }, 1000);
    });

