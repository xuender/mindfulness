###
chapter.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###

AnnotationCtrl = ($scope, $modalInstance)->
  $scope.close = ->
    $modalInstance.close('close')
AnnotationCtrl.$inject = ['$scope', '$modalInstance']

ToolbarCtrl = ($scope)->
  $scope.isStar = IS_STAR
  $scope.$watch('isStar', (n, o)->
    if n
      $scope.starLabel = '取消关注'
    else
      $scope.starLabel = '关注'
  )
ToolbarCtrl.$inject = ['$scope']

BookCtrl = ($scope, $modal)->
  $scope.as = [
    {
      id: 1
      row: 1
      start: 3
      end: 3
      context: '规则'
    }
    {
      id: 2
      row: 1
      start: 4
      end: 5
      context: '孔子'
    }
  ]
  $scope.add = ->
    m = $modal.open
      backdrop: true
      keyboard: true
      backdropClick: true
      templateUrl: '/annotation'
      controller: 'AnnotationCtrl'
    m.result.then(->
      console.info('ok')
    ,->
      console.info('close')
    )
BookCtrl.$inject = ['$scope', '$modal']
