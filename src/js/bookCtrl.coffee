###
chapter.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
BookCtrl = ($scope, $modal, $http)->
  $scope.isEdit = false
  $scope.$watch('isEdit', (n, o)->
    console.info n
  )

BookCtrl.$inject = ['$scope', '$modal', '$http']
ChapterCtrl = ($scope, $modal, $http)->
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
    USER_IDS.push(userId)
    for id in USER_IDS
      for a in $scope.anns[id]
        if a.style == 'a'
          $("<li class='b1 ann user#{USER_IDS.indexOf(userId)}' id='a#{a.id}' data='#{JSON.stringify(a)}'>#{ a.context }</li>").appendTo('#anns')
        else
          underline(
            $("#s#{a.row}_#{a.start}"),
            $("#s#{a.row}_#{a.end}"),
            ["ul_#{a.style}", "user#{USER_IDS.indexOf(userId)}"]
          )
    sortAnns()
    showLine()
  $scope.readAnn = (userId)->
    # 读取注解
    if userId in USER_IDS
      css = "user#{USER_IDS.indexOf(userId)}"
      $(".jumbotron span").removeClass(css)
      $('.' + css).remove()
      $('.' + css + 'L').remove()
      JU.removeArray(USER_IDS, userId)
      showLine()
    else
      #TODO 显示用户批注的数量需要控制，收费点
      $scope.getAnn(userId, $scope.showAnn)
  $scope.add = ->
    # 增加注解
    $scope.menuOpen = false
    s = selectData()
    m = $modal.open
      backdrop: true
      keyboard: true
      backdropClick: true
      templateUrl: '/annotation'
      controller: 'AnnotationCtrl'
    m.result.then((res)->
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
          $("<li class='ann userMe' id='a#{data.data.id}' data='#{JSON.stringify(data.data)}'>#{ data.data.context }</li>").appendTo('#anns')
          createAnnotation(
            $("#s#{s.row}_#{s.start}"),
            $("#s#{s.row}_#{s.end}"),
            $("#a#{data.data.id}"),
            'userMe'
          )
          sortAnns()
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

ChapterCtrl.$inject = ['$scope', '$modal', '$http']
