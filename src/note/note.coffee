###
note.coffee
Copyright (C) 2015 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
app.config(['$stateProvider', '$urlRouterProvider',
($stateProvider, $urlRouterProvider)->
  $urlRouterProvider.otherwise("/book")
  $stateProvider
    .state('book',
      url: '/book'
      templateUrl: 'partials/note/books.html?1.html'
      controller: 'BooksCtrl'
    )
])

