###
chapter.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
AnnotationCtrl = ($scope, $modalInstance)->
  $scope.ann = ''
  $scope.close = ->
    $modalInstance.close('close')
  $scope.save =(ann) ->
    $modalInstance.close(ann)
AnnotationCtrl.$inject = ['$scope', '$modalInstance']

ToolbarCtrl = ($scope, $http)->
  $scope.isEdit = false
  $scope.isStar = IS_STAR
  $scope.disabled = false
  $scope.starCount = STAR_COUNT
  $scope.stared = (b, id)->
    # 设置星标
    $scope.disabled = true
    if b
      url = "/book/#{id}/star"
    else
      url = "/book/#{id}/unstar"
    $http.post(url, '',
      headers:
        'X-CSRFToken': CSRF
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
