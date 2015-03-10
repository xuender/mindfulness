###
note.coffee
Copyright (C) 2015 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
app.config(['$routeProvider', ($routeProvider)->
  $routeProvider.
    when('/book',
      templateUrl: 'partials/note/book.html'
      controller: 'BookCtrl'
    ).otherwise({
      redirectTo: '/book'
    })
])

