###
sectionViewCtrl.coffee
Copyright (C) 2015 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###

SectionViewCtrl = ($scope, $log, $http, $stateParams)->
  $scope.id = $stateParams.sid

SectionViewCtrl.$inject = [
  '$scope'
  '$log'
  '$http'
  '$stateParams'
]
