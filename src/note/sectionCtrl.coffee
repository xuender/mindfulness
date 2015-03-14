###
sectionCtrl.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
SectionCtrl = ($scope, $modalInstance, $log, section, del, books)->
  # 章节编辑
  $scope.s = section
  $scope.showDel = del
  $scope.books = books
  $scope.del = ->
    $modalInstance.close($scope.s.id)
  $scope.ok = ->
    $modalInstance.close($scope.s)
  $scope.cancel = ->
    $modalInstance.dismiss('cancel')

SectionCtrl.$inject = [
  '$scope'
  '$modalInstance'
  '$log'
  'section'
  'del'
  'books'
]
