angular.module('restaurant')
    .controller('KitchenController', function ($scope, Order, $interval) {

        $scope.interval = $interval(function () {
            console.log('request...')

            Order.getOrders().then(function (orders) {
                Object
                    .keys(orders.data)
                    .map(function (key) {
                        $scope.table = key;
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