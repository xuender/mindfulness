###
chapter.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###

AnnotationCtrl = ($scope, $modalInstance)->
  $scope.close = ->
    $modalInstance.close('close')
AnnotationCtrl.$inject = ['$scope', '$modalInstance']

ToolbarCtrl = ($scope, $http)->
  $scope.isStar = IS_STAR
  $scope.disabled = false
  $scope.starCount = STAR_COUNT
  $scope.stared = (b, id)->
    # 设置星标
    $scope.disabled = true
    if b
      url = "/star/#{id}"
    else
      url = "/unstar/#{id}"
    $http(
      method: 'POST'
      headers:
        'X-CSRFToken': CSRF
      url: url
    ).success((data, status, headers, config)->
      $scope.isStar = b
      $scope.disabled = false
      $scope.starCount = data
    ).error((data, status, headers, config)->
      if b
        alert('关注失败，请检查网络')
      else
        alert('取消关注失败，请检查网络')
      $scope.disabled = false
    )
ToolbarCtrl.$inject = ['$scope', '$http']

BookCtrl = ($scope, $modal)->
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
