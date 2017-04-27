angular.module('restaurant')
    .service('Order', function($http){

        return{
            getOrders : function(){
                return $http.get('/api/orders');
            }
        };
    });