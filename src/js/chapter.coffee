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

BookCtrl = ($scope, $modal, $http)->
  $scope.showUserIds = []
  $scope.anns = {}
  $scope.getAnn = (userId, callback)->
    #获取用户注解
    if userId of $scope.anns
      callback(userId)
    else
      url = "/user/#{userId}/#{BOOK}/#{CHAPTER}"
      $http.post(url, '',
        headers:
          'X-CSRFToken': CSRF
      ).success((data, status, headers, config)->
        if data.ok
          $scope.anns[userId] = data.data
          callback(userId)
        else
          alert(data.msg)
      ).error((data, status, headers, config)->
        console.error data
      )
  $scope.showAnn = (userId)->
    # 显示注解
    $scope.showUserIds.push(userId)
    for id in $scope.showUserIds
      for a in $scope.anns[id]
        if a.style == 'a'
          $("<li class='b1 ann user#{$scope.showUserIds.indexOf(userId)}' id='a#{a.id}' data='#{JSON.stringify(a)}'>#{ a.context }</li>").appendTo('#anns')
          createAnnotation(
            $("#s#{a.row}_#{a.start}"),
            $("#s#{a.row}_#{a.end}"),
            $("#a#{a.id}"),
            "user#{$scope.showUserIds.indexOf(userId)}"
          )
        else
          underline(
            $("#s#{a.row}_#{a.start}"),
            $("#s#{a.row}_#{a.end}"),
            ["ul_#{a.style}", "user#{$scope.showUserIds.indexOf(userId)}"]
          )
  $scope.readAnn = (userId)->
    # 读取注解
    if userId in $scope.showUserIds
      css = "user#{$scope.showUserIds.indexOf(userId)}"
      $(".jumbotron span").removeClass(css)
      $('.' + css).remove()
      $('.' + css + 'L').remove()
      JU.removeArray($scope.showUserIds, userId)
    else
      #TODO 显示用户批注的数量需要控制，收费点
      $scope.getAnn(userId, $scope.showAnn)
  $scope.add = ->
    # 增加注解
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
          console.info data
          $("<li class='ann' id='a#{data.data.id}' data='#{JSON.stringify(data.data)}'>#{ data.data.context }</li>").appendTo('#anns')
          createAnnotation(
            $("#s#{s.row}_#{s.start}"),
            $("#s#{s.row}_#{s.end}"),
            $("#a#{data.data.id}"),
            'userMe'
          )
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
    # 重点
    $scope.line('l')
  $scope.incisive = ->
    # 精辟
    $scope.line('d')
  $scope.line = (style)->
    # 画线
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
        underline(
          $("#s#{s.row}_#{s.start}"),
          $("#s#{s.row}_#{s.end}"),
          ['ul_' + style, 'userMe']
        )
        window.getSelection().removeAllRanges()
      else
        alert(data.msg)
    ).error((data, status, headers, config)->
      console.error data
    )
    $scope.menuOpen = false

BookCtrl.$inject = ['$scope', '$modal', '$http']
