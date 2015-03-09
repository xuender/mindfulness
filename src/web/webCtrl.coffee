###
web.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
WebCtrl = ($scope, $log, $http, $modal, lss, $q)->
  ### 网页制器 ###
  lss.bind($scope, "isLogin", false)
  $scope.selectBoolean = ->
    # 布尔列表
    def = $q.defer()
    ret = [
      {id:true, title:'是'}
      {id:false, title:'否'}
    ]
    def.resolve(ret)
    def
  $scope.post = (t)->
    ### 提交 ###
    $modal.open(
      templateUrl: 'partials/post.html?v=8.html'
      controller: PostCtrl
      backdrop: 'static'
      size: 'lg'
      resolve:
        type: ->
          t
    )
  $scope.showLog = ->
    ### 显示日志 ###
    $modal.open(
      templateUrl: 'partials/logger.html?3.html'
      controller: LoggerCtrl
      backdrop: 'static'
      size: 'lg'
      resolve:
        oid: ->
          false
    )
  $scope.password = ->
    # 更改密码
    i = $modal.open(
      templateUrl: 'partials/password.html?1.html'
      controller: PasswordCtrl
      backdrop: 'static'
      keyboard: false
      size: 'sm'
    )
  $scope.showLogin = (m='l')->
    ### 显示登录窗口 ###
    i = $modal.open(
      templateUrl: 'partials/login.html?3.html'
      controller: LoginCtrl
      backdrop: 'static'
      keyboard: false
      size: 'sm'
      resolve:
        m: ->
          m
        cid: ->
          if $scope.user and 'cid' in $scope.user
            return $scope.user.cid
          CID
    )
    i.result.then((user)->
      $scope.isLogin = true
      $scope.user = user
    ,->
      $log.info '取消'
    )
  $scope.alerts = []
  $scope.alert = (msg)->
    # 提示信息
    $scope.alerts.push(
      msg: msg
      type: 'success'
    )
  $scope.closeAlert = (index)->
    # 关闭
    $scope.alerts.splice(index, 1)
  $scope.confirm = (msg, oFunc, cFunc=null)->
    # 询问
    i = $modal.open(
      templateUrl: '/partials/confirm.html?v=2'
      controller: 'ConfirmCtrl'
      backdrop: 'static'
      keyboard: true
      size: 'sm'
      resolve:
        msg: ->
          msg
    )
    i.result.then((ok)->
      $log.debug '增加'
      $log.info ok
      oFunc()
    ,->
      if cFunc != null
        cFunc()
    )
  if 'false' == $scope.isLogin
    $scope.isLogin = false
  if $scope.isLogin
    $http.get('/login').success((data)->
      $log.debug(data)
      $scope.isLogin = data.ok
      if data.ok
        $scope.user = data.data
        $log.debug('user id:%s', data.data.Id)
    )

WebCtrl.$inject = [
  '$scope'
  '$log'
  '$http'
  '$modal'
  'localStorageService'
  '$q'
]

