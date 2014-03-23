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

BookCtrl = ($scope, $modal, $http)->
  $scope.add = ->
    $scope.menuOpen = false
    s = selectData()
    console.info(s)
    m = $modal.open
      backdrop: true
      keyboard: true
      backdropClick: true
      templateUrl: '/annotation'
      controller: 'AnnotationCtrl'
    m.result.then((res)->
      console.info(res)
      style = 'a'
      if 'close' == res
        return
      url = "/book/#{BOOK}/#{CHAPTER}/annotate"
      $http.post(url,
        {
          row: s.row
          start: s.start
          end: s.end
          style: style
          context: res
        },
        {
        headers:
          'X-CSRFToken': CSRF
        }
      ).success((data, status, headers, config)->
        if data.ok
          underline($("#s#{s.row}_#{s.start}"), $("#s#{s.row}_#{s.end}"), 'ul_' + style)
          window.getSelection().removeAllRanges()
        else
          alert(data.msg)
      ).error((data, status, headers, config)->
        console.error data
      )
    ,->
      console.info('close')
    )
  # 弹出菜单位置
  $scope.menuStyle = {
  }
  # 弹出菜单是否打开
  $scope.menuOpen = false
  $scope.popup = ->
    # 弹出菜单
    s = selectData()
    if s and s.ok
      $scope.menuStyle = {
        top: s.y
        left: s.x
      }
      $scope.menuOpen = true
    else
      $scope.menuOpen = false
  $scope.emphasis = ->
    $scope.line('l')
  $scope.incisive = ->
    $scope.line('d')
  $scope.line = (style)->
    # 重点
    s = selectData()
    url = "/book/#{BOOK}/#{CHAPTER}/annotate"
    $http.post(url,
      {
        row: s.row
        start: s.start
        end: s.end
        style: style
      },
      {
      headers:
        'X-CSRFToken': CSRF
      }
    ).success((data, status, headers, config)->
      if data.ok
        underline($("#s#{s.row}_#{s.start}"), $("#s#{s.row}_#{s.end}"), 'ul_' + style)
        window.getSelection().removeAllRanges()
      else
        alert(data.msg)
    ).error((data, status, headers, config)->
      console.error data
    )
    $scope.menuOpen = false

BookCtrl.$inject = ['$scope', '$modal', '$http']
