###
bookCtrl.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
BooksCtrl = ($scope, $http, $log, $modal, ngTableParams, $filter, $q)->
  $scope.$parent.name = 'book'
  $log.debug 'xxx'
  $scope.status=
    new: '新建'
    publish: '发布'
  $scope.selectStatus = ->
    # 状态列表
    def = $q.defer()
    ret = []
    for k of $scope.status
      $log.debug k
      ret.push(
        id:k
        title: $scope.status[k]
      )
    def.resolve(ret)
    def
  $scope.new = ->
    $modal.open(
      templateUrl: 'partials/note/book.html?8.html'
      controller: BookCtrl
      backdrop: 'static'
      size: 'lg'
      resolve:
        book: ->
          publish: false
        del: ->
          false
        status: ->
          $scope.status
    ).result.then((b)->
      $http.post('/note/book', b).success((data)->
        if data.ok
          $scope.tableParams.reload()
        else
          alert(data.err)
      )
    ,->
      $log.info '取消'
    )
  $scope.update = (book)->
    $modal.open(
      templateUrl: 'partials/note/book.html?8.html'
      controller: BookCtrl
      backdrop: 'static'
      size: 'lg'
      resolve:
        book: ->
          book
        del: ->
          true
        status: ->
          $scope.status
    ).result.then((b)->
      $log.debug b
      if angular.isString(b)
        $http.delete('/note/book/' + b).success((data)->
          if data.ok
            $scope.tableParams.reload()
          else
            alert(data.err)
        )
      else
        $http.put('/note/book', b).success((data)->
          if data.ok
            $scope.tableParams.reload()
          else
            alert(data.err)
        )
    ,->
      $log.info '取消'
    )
  $scope.tableParams = new ngTableParams(
    page: 1
    count: 10
    sorting:
      ca: 'desc'
  ,
    getData: ($defer, params)->
      # 过滤
      $http.post('/note/books',
        Page: params.page()
        Count: params.count()
        Sorting: params.orderBy()
        Filter: params.filter()
      ).success((data)->
        $log.debug data
        params.total(data.count)
        $defer.resolve(data.data)
      )
  )
BooksCtrl.$inject = [
  '$scope'
  '$http'
  '$log'
  '$modal'
  'ngTableParams'
  '$filter'
  '$q'
]
