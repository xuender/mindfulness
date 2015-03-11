###
bookCtrl.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
BookCtrl = ($scope, $modalInstance, $log, book, del)->
  # 书籍编辑
  $scope.b = book
  $scope.showDel = del
  $log.debug $scope.b
  $scope.del = ->
    $modalInstance.close($scope.b.id)
  $scope.ok = ->
    $modalInstance.close($scope.b)
  $scope.cancel = ->
    $modalInstance.dismiss('cancel')

BookCtrl.$inject = [
  '$scope'
  '$modalInstance'
  '$log'
  'book'
  'del'
]
