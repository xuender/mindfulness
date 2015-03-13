###
manager.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
app.config(['$stateProvider', '$urlRouterProvider',
($stateProvider, $urlRouterProvider)->
  $urlRouterProvider.otherwise("/count")
  $stateProvider
    .state('count',
      url: '/count'
      templateUrl: 'partials/cs/count.html'
      controller: 'CountCtrl'
    ).state('users',
      url: '/users'
      templateUrl: 'partials/cs/users.html'
      controller: 'UsersCtrl'
    ).state('session',
      url: '/session'
      templateUrl: 'partials/cs/session.html'
      controller: 'SessionCtrl'
    ).state('post',
      url: '/post'
      templateUrl: 'partials/cs/posts.html'
      controller: 'PostsCtrl'
    )
])

